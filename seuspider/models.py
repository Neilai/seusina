
from __future__ import unicode_literals

from django.db import models

class Sina(models.Model):
    likenum = models.BigIntegerField(blank=True, null=True)
    commentnum = models.BigIntegerField(blank=True, null=True)
    repeatnum = models.BigIntegerField(blank=True, null=True)
    datetime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sina'

class Sina1(models.Model):
    comment_name = models.CharField(max_length=64, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    likenum = models.BigIntegerField(blank=True, null=True)
    datetime = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sina1'


class Sina2(models.Model):
    repeatname = models.CharField(max_length=125, blank=True, null=True)
    repeatnum = models.BigIntegerField(blank=True, null=True)
    datetime = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sina2'


class Sina3(models.Model):
    username = models.CharField(max_length=125, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    follow = models.BigIntegerField(blank=True, null=True)
    fans = models.BigIntegerField(blank=True, null=True)
    webnum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sina3'


class Sina4(models.Model):
    fansparent = models.CharField(max_length=255, blank=True, null=True)
    fansname = models.CharField(max_length=255, blank=True, null=True)
    fanslevel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sina4'