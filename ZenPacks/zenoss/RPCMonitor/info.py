###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
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
    


