from rest_framework import serializers
from django.contrib.auth.models import User
from management.models import *

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
    hashScheme = serializers.CharField(max_length=255)
    enterpriseMode = serializers.BooleanField(default=False)
    hardQuota = serializers.CharField(max_length=255)
    softQuota = serializers.CharField(max_length=255)
    aclsUsage = serializers.CharField(max_length=255)
    searchEnabled = serializers.BooleanField(default=False)
    indexingEnabled = serializers.BooleanField(default=False)
    customMetadataIndexingEnabled = serializers.BooleanField(default=False)
    replicationEnabled = serializers.BooleanField(default=False)
    readFromReplica = serializers.BooleanField(default=False)
    serviceRemoteSystemRequests = serializers.BooleanField(default=False)