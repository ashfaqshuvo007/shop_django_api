"""
    Created by tareq on 8/16/19
"""
import os
import random
import string
from datetime import datetime

from django.core.files import File
from django.db import transaction
from django.db.models import FileField, CharField, IntegerField
from django_drf_filepond.models import TemporaryUpload

from settings import BASE_URL
from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


def instance_directory_path(instance, filename):
    date = datetime.now()
    split_name = filename.rsplit('.', 1)
    split_name[0] = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))
    filename = '.'.join(split_name)
    return '{0}/{1}/{2}/{3}/{4}'.format(
        instance.pk, date.year, date.month, date.day, filename
    )


class FileObject(DomainEntity):
    title = CharField(max_length=512, default='_', null=True, blank=True)
    token = CharField(max_length=128, default=None, null=True, blank=True)
    file_name = CharField(max_length=512, default='_')
    extension = CharField(max_length=128, default='_')
    description = CharField(max_length=2048, default='_', null=True, blank=True)
    file = FileField(default=None, max_length=8000, upload_to=instance_directory_path, null=True)
    order = IntegerField(default=0)

    # This is the code to save "the temp file that was uploaded through File Pond" as permanent file
    def create_from_filepond(self, token=None, request=None, **kwargs):
        if not token or not request:
            return None
        try:
            with transaction.atomic():
                temp_upload = TemporaryUpload.objects.get(upload_id=token)
                instance = self
                instance.order = kwargs.get('order', 0)
                instance.save()
                instance.file.save(
                    temp_upload.upload_name,
                    File(open(temp_upload.file.path, mode='rb'))
                )
                file_name = os.path.basename(instance.file.name)
                instance.file_name = os.path.splitext(file_name)[0]
                instance.extension = os.path.splitext(file_name)[1]
                instance.token = None
                instance.save()
                temp_upload.delete()
                return instance
        except:
            return None

    def convert_pondfile_to_file(self, token=None, **kwargs):
        return self.create_from_filepond(token=token, **kwargs)

    @property
    def size(self):
        try:
            return self.file.size
        except:
            return -1

    @property
    def url(self):
        if self.file:
            return self.file.url
        return None

    @property
    def full_url(self):
        return f'{BASE_URL}/{self.url}'

    class Meta:
        app_label = 'base'
