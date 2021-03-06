"""
    Created by tareq on ২৯/৫/১৯
"""
import uuid
from collections import OrderedDict

from django.apps import apps
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, OneToOneField
from rest_framework.fields import DecimalField
from rest_framework.relations import PrimaryKeyRelatedField

get_model = apps.get_model
from django.db.models.manager import Manager
from rest_framework import serializers

from rest_framework.fields import empty

__author__ = "Tareq"


class DomainEntitySerializer(serializers.ModelSerializer):
    serializer_related_field = PrimaryKeyRelatedField

    def __init__(self, *args, fields=None, context=None, **kwargs):
        super().__init__(*args, context=context, **kwargs)

        if bool(context):
            if context["request"].GET.get("accept_disabled_objects", False):
                setattr(self, 'accept_disabled_objects', True)
            if hasattr(context['request'], 'query_params'):
                fields = context['request'].query_params.get('fields', None)
                if bool(fields):
                    if isinstance(fields, tuple) or isinstance(fields, list):
                        pass
                    else:
                        fields = (fields,)

                    allowed = set(fields)
                    existing = set(self.fields.keys())
                    for field_name in existing - allowed:
                        self.fields.pop(field_name)

    def run_validation(self, data=empty):
        if data != empty:
            fields = self._writable_fields
            decimal_fields = [field for field in fields if type(field) == DecimalField]
            for field in decimal_fields:
                if field.field_name in data:
                    primitive_value = data.get(field.field_name)
                    data[field.field_name] = str(round(float(primitive_value), field.decimal_places))
            primary_key_related_fields = [field for field in fields if type(field) == PrimaryKeyRelatedField]
        return super(DomainEntitySerializer, self).run_validation(data)

    def update(self, instance, validated_data):
        with transaction.atomic():
            m2m_fields = [
                (f, f.model if f.model != self.Meta.model else None)
                for f in self.Meta.model._meta.get_fields()
                if (f.one_to_many and f.name in validated_data.keys()) or
                   (f.many_to_many and not f.auto_created)
            ]
            m2m_dict = dict()
            for m in m2m_fields:
                m2m_dict[m[0].name] = validated_data.pop(m[0].name, [])

            attributes = self.Meta.model._meta.fields

            for attr in attributes:
                if attr.name in validated_data and isinstance(validated_data[attr.name], dict):
                    _obj = getattr(instance, attr.name)

                    # Trying to find out the related serializer instance from current serializer fields
                    # Otherwise finding it from model's get_serializer. Which will be deprecated slowly.
                    field_name = attr.name
                    _serializer = self._fields.get(field_name)
                    if not _serializer:
                        _serializer = attr.related_model.get_serializer()(context=self.context)

                    if not _serializer.context:
                        _serializer.context = self.context

                    if _obj is None:
                        if callable(getattr(_serializer, 'create', None)):
                            validated_data[attr.name] = _serializer.create(validated_data[attr.name])
                    else:
                        if callable(getattr(_serializer, 'update', None)):
                            validated_data[attr.name] = _serializer.update(_obj, validated_data[attr.name])

            for attr in attributes:
                if attr.name in validated_data.keys():
                    if isinstance(attr, ForeignKey) or isinstance(attr, OneToOneField):
                        # _obj = getattr(instance, attr.name)
                        value = validated_data.pop(attr.name, None)
                        if isinstance(value, Model) and value.pk is None:
                            value.save()
                        setattr(instance, attr.name,
                                attr.model.objects.get(pk=value) if isinstance(value, int) else value)

            for m in m2m_fields:
                if m[0].name in m2m_dict.keys() and len(m2m_dict[m[0].name]) > 0:
                    _field = getattr(instance, m[0].name)
                    _values = m2m_dict[m[0].name]
                    if m[0].name in instance.__class__.get_dependent_field_list():
                        if isinstance(_values, User):
                            _values.delete()
                        elif isinstance(_values, Model):
                            temp = _values
                            setattr(instance, m[0].name, None)
                            instance.save()
                            temp.delete()
                        elif isinstance(_values, Manager):
                            items = list(_values.all())
                            _values.clear()
                            for item in items:
                                item.delete(force_delete=True)
                        else:
                            pass

                    if m[0].name in [x for x in instance.__class__.get_dependent_field_list() if
                                     isinstance(getattr(instance, x), Manager)]:
                        _field.clear()
                    for v in _values:
                        if isinstance(v, (dict, OrderedDict)):

                            # Trying to find out the related serializer instance from current serializer fields
                            # Otherwise finding it from model's get_serializer. Which will be deprecated slowly.
                            field_name = m[0].name
                            _serializer = None
                            _serializer_parent_instance = self._fields.get(field_name)
                            if _serializer_parent_instance:
                                _serializer = getattr(_serializer_parent_instance, 'child', None)
                            if not _serializer:
                                _serializer = m[0].related_model.get_serializer()(context=self.context)

                            if isinstance(v, int):
                                v = m[0].related_model.objects.get(pk=v)
                            else:
                                try:
                                    # Try to get the object
                                    _instance = None
                                    if 'id' in v.keys():
                                        _instance = m[0].related_model.objects.get(pk=v['id'])
                                    elif 'pk' in v.keys():
                                        _instance = m[0].related_model.objects.get(pk=v['pk'])
                                    elif 'tsync_id' in v.keys():
                                        _instance = m[0].related_model.objects.get(tsync_id=v['tsync_id'])
                                    if _instance:
                                        v = _serializer.update(instance=_instance, validated_data=v)
                                    else:
                                        if m[0].one_to_many:
                                            v[_field.field.name] = instance
                                        v = _serializer.create(v)
                                except:
                                    if m[0].one_to_many:
                                        v[_field.field.name] = instance
                                    v = _serializer.create(v)

                        v.save()
                        _field.add(v)
            return super().update(instance, validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        with transaction.atomic():
            tsync_id = validated_data.get('tsync_id', uuid.uuid4())
            responseObj = self.Meta.model.objects.filter(tsync_id=tsync_id)
            if responseObj.exists():
                return responseObj.first()
            m2m_fields = [
                (f, f.model if f.model != self.Meta.model else None)
                for f in self.Meta.model._meta.get_fields()
                if (f.one_to_many and f.name in validated_data.keys()) or
                   (f.many_to_many and not f.auto_created)
            ]
            m2m_dict = dict()
            for m in m2m_fields:
                m2m_dict[m[0].name] = validated_data.pop(m[0].name, [])

            attributes = self.Meta.model._meta.fields

            for attr in attributes:
                if attr.name in validated_data and isinstance(validated_data[attr.name], dict):
                    # Trying to find out the related serializer instance from current serializer fields
                    # Otherwise finding it from model's get_serializer. Which will be deprecated slowly.
                    field_name = attr.name
                    _serializer = self._fields.get(field_name)
                    if not _serializer:
                        _serializer = attr.related_model.get_serializer()(context=self.context)
                    if callable(getattr(_serializer, 'create', None)):
                        validated_data[attr.name] = _serializer.create(validated_data[attr.name])

            pk = validated_data.pop('id', None)
            if pk:
                obj = self.Meta.model.objects.get(pk=pk)
            else:
                obj = self.Meta.model.objects.create(**validated_data)

            for attr in attributes:
                if isinstance(attr, ForeignKey) or isinstance(attr, OneToOneField):
                    value = validated_data.pop(attr.name, None)
                    if isinstance(value, Model) and value.pk is None:
                        value.save()
                    setattr(obj, attr.name,
                            attr.model.objects.get(pk=value) if isinstance(value, int) else value)
                else:
                    pass
            obj.save()

            for m in m2m_fields:
                _field = getattr(obj, m[0].name)
                _values = m2m_dict[m[0].name]
                for v in _values:
                    if isinstance(v, (dict, OrderedDict)):

                        # Trying to find out the related serializer instance from current serializer fields
                        # Otherwise finding it from model's get_serializer. Which will be deprecated slowly.
                        field_name = m[0].name
                        _serializer = None
                        _serializer_parent_instance = self._fields.get(field_name)
                        if _serializer_parent_instance:
                            _serializer = getattr(_serializer_parent_instance, 'child', None)
                        if not _serializer:
                            _serializer = m[0].related_model.get_serializer()(context=self.context)

                        if m[0].one_to_many:
                            v[_field.field.name] = obj
                        v = _serializer.create(v)

                    v.save()
                    _field.add(v)

            return obj

    def create_or_update(self, validated_data, *args, **kwargs):
        with transaction.atomic():
            tsync_id = validated_data.get('tsync_id')
            instance = self.Meta.model.objects.filter(tsync_id=tsync_id).first()
            if instance:
                return self.update(instance, validated_data)
            else:
                return self.create(validated_data)

    def mutate(self, **kwargs):
        self.instance = self.instance.mutate_to()
        return self.instance

    @classmethod
    def required_location_fields(cls):
        return ["location"]

    class Meta:
        fields = [
            'id', 'name', 'tsync_id', 'date_created', 'last_updated'
        ]
