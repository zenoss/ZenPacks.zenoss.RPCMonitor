##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.zenoss.RPCMonitor.interfaces import IRPCMonitorDataSourceInfo
from ZenPacks.zenoss.RPCMonitor.datasources.RPCMonitorDataSource import RPCMonitorDataSource

def rpcMonitorProtocolVocabulary(context):
    return SimpleVocabulary.fromValues(RPCMonitorDataSource.protocolTypes)

class RPCMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(IRPCMonitorDataSourceInfo)
    cycletime = ProxyProperty('cycletime')
    rpcServer = ProxyProperty('rpcServer')
    rpcCommand = ProxyProperty('rpcCommand')
    port = ProxyProperty('port')
    protocol = ProxyProperty('protocol')
    
        
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
