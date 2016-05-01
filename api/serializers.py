# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from management.models import *

#TODO: Tüm namespace ve tenant parametreleri burada örnek jsonlara göre işlenebilir olmalı.

class TenantCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    systemVisibleDescription = serializers.CharField(max_length=255)
    hardQuota = serializers.CharField(max_length=255)
    softQuota = serializers.CharField(max_length=255)
    namespaceQuota = serializers.CharField(max_length=255)
    complianceConfigurationEnabled = serializers.BooleanField(default=False)
    versioningConfigurationEnabled = serializers.BooleanField(default=False)
    searchConfigurationEnabled = serializers.BooleanField(default=False)
    replicationConfigurationEnabled = serializers.BooleanField(default=False)
    servicePlanSelectionEnabled = serializers.BooleanField(default=False)
    servicePlan = serializers.CharField(max_length=255,required=False)

class NamespaceCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    hardQuota = serializers.CharField(max_length=255)
    softQuota = serializers.CharField(max_length=255)

class FileDeleteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

class FolderSerializer(serializers.Serializer):
    namespace_id = serializers.IntegerField()
    folder_name = serializers.CharField(max_length=255)