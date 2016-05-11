
class TenantCreation(object):
    def __init__(self,name,systemVisibleDescription,hardQuota,softQuota,namespaceQuota, created=None):
        self.name=name
        self.systemVisibleDescription=systemVisibleDescription
        self.hardQuota=hardQuota
        self.softQuota=softQuota
        self.namespaceQuota=namespaceQuota
        '''
        self.complianceConfigurationEnabled=complianceConfigurationEnabled
        self.versioningConfigurationEnabled=versioningConfigurationEnabled
        self.searchConfigurationEnabled=searchConfigurationEnabled
        self.replicationConfigurationEnabled=replicationConfigurationEnabled
        self.servicePlanSelectionEnabled=servicePlanSelectionEnabled
        self.servicePlan=servicePlan
        '''

