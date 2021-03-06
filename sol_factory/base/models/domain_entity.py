"""
    Created by tareq on ১৭/৫/১৯
"""
import uuid

from django.db.models import Model, DateTimeField, CharField

__author__ = "Tareq"


class DomainEntity(Model):
    name = CharField(blank=True, null=True, max_length=127)
    tsync_id = CharField(max_length=64, blank=True)
    date_created = DateTimeField(auto_now_add=True)
    last_updated = DateTimeField(auto_now=True)

    class Meta:
        app_label = 'base'
        abstract = True

    def __str__(self):
        return self.name or "{}-{}".format(self.__class__.__name__, self.pk)

    @classmethod
    def get_dependent_field_list(cls):
        return []

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.tsync_id:
            self.tsync_id = uuid.uuid4()
        super(DomainEntity, self).save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
