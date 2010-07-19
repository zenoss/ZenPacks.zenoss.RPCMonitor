###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################


import Products.ZenModel.RRDDataSource as RRDDataSource
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from AccessControl import ClassSecurityInfo, Permissions
from Products.ZenUtils.ZenTales import talesCompile, getEngine
from Products.ZenUtils.Utils import binPath

class RPCMonitorDataSource(ZenPackPersistence, RRDDataSource.RRDDataSource):
    
    RPC_MONITOR = 'RPCMonitor'
    ZENPACKID = 'ZenPacks.zenoss.RPCMonitor'

    sourcetypes = (RPC_MONITOR,)
    sourcetype = RPC_MONITOR

    eventClass = '/Status/RPC'
        
    rpcServer = '${dev/id}'
    rpcCommand = '${here/zRPCCommand}'
    port = 0
    protocol = 'UDP'
    protocolTypes = ['UDP', 'TCP']
    
    _properties = RRDDataSource.RRDDataSource._properties + (
        {'id':'rpcServer', 'type':'string', 'mode':'w'},
        {'id':'rpcCommand', 'type':'string', 'mode':'w'},
        {'id':'port', 'type':'int', 'mode':'w'},
        {'id':'protocol', 'type':'string', 'mode':'w'},
        )
        
    _relations = RRDDataSource.RRDDataSource._relations + (
        )


    factory_type_information = ( 
    { 
        'immediate_view' : 'editRPCMonitorDataSource',
        'actions'        :
        ( 
            { 'id'            : 'edit',
              'name'          : 'Data Source',
              'action'        : 'editRPCMonitorDataSource',
              'permissions'   : ( Permissions.view, ),
            },
        )
    },
    )

    security = ClassSecurityInfo()


    def __init__(self, id, title=None, buildRelations=True):
        RRDDataSource.RRDDataSource.__init__(self, id, title, buildRelations)


    def getDescription(self):
        if self.sourcetype == self.RPC_MONITOR:
            return self.rpcServer + self.rpcCommand
        return RRDDataSource.RRDDataSource.getDescription(self)


    def useZenCommand(self):
        return True


    def getCommand(self, context):
        # Check if a rpc service is registered and running using
        #     rpcinfo -H host -C rpc_command 
        #
        #     Usage: 
        #          check_rpc -H host -C rpc_command [-p port] [-c program_version] [-u|-t] [-v]
        #          check_rpc [-h | --help]
        #          check_rpc [-V | --version]
        #
        #          <host>          The server providing the rpc service
        #          <rpc_command>   The program na
        #          [-v]            Verbose 
        #          [-v -v]         Verbose - will print s

        parts = [binPath('check_rpc')]
        if self.rpcServer:
            parts.append('-H %s' % self.rpcServer)
        if self.rpcCommand:
            parts.append('-C %s' % self.rpcCommand)
        if self.port:
            parts.append('-p %d' % self.port)
        if self.protocol == 'TCP':
            parts.append('-t')
        else:
            parts.append('-u')

        cmd = ' '.join(parts)
        cmd = RRDDataSource.RRDDataSource.getCommand(self, context, cmd)
        return cmd


    def checkCommandPrefix(self, context, cmd):
        return cmd


    def addDataPoints(self):
        if not hasattr(self.datapoints, 'time'):
            self.manage_addRRDDataPoint('time')


    def zmanage_editProperties(self, REQUEST=None):
        '''validation, etc'''
        if REQUEST:
            # ensure default datapoint didn't go away
            self.addDataPoints()
            # and eventClass
            if not REQUEST.form.get('eventClass', None):
                REQUEST.form['eventClass'] = self.__class__.eventClass
        return RRDDataSource.RRDDataSource.zmanage_editProperties(self, REQUEST)


