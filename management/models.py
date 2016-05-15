# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    token_string = models.CharField(max_length=255)

class SystemTenants(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    space_url = models.URLField(blank=False)
    space_name = models.CharField(max_length=255)
    space_type = models.IntegerField(choices=[(1, 'namespace'), (2, 'tenant')])
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username+" "+self.space_url

    class Meta:
        verbose_name_plural = "System Tenants"

class UserSpaces(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    space_url = models.URLField(blank=False)
    space_name = models.CharField(max_length=255)
    space_type = models.IntegerField(choices=[(1, 'namespace'), (2, 'tenant')])
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username+" "+self.space_url

    class Meta:
        verbose_name_plural = "User Spaces"

class UserSubspaces(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    space_url = models.URLField(blank=False)
    space_name = models.CharField(max_length=255)
    space_type = models.IntegerField(choices=[(1, 'namespace'), (2, 'tenant')])
    created_date = models.DateTimeField(auto_now=True)
    parent_space = models.ForeignKey(UserSpaces)

    def __unicode__(self):
        return self.user.username+" "+self.space_url

    class Meta:
        verbose_name_plural = "User Subspaces"

class SpaceAuthorizations(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    space_type = models.IntegerField(choices=[(1, 'Space'), (2, 'Subspace')])
    space_name = models.CharField(max_length=255)
    is_authority_valid = models.BooleanField()

    def __unicode__(self):
        return self.user.username+" "+self.space_type

    class Meta:
        verbose_name_plural = "Space Authorizations"

