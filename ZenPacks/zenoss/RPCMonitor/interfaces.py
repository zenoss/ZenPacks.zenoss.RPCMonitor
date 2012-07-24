##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IRPCMonitorDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    rpcServer = schema.TextLine(title=_t(u'RPC Server'))
    rpcCommand = schema.TextLine(title=_t(u'RPC Command'))
    port = schema.Int(title=_t(u'Port'))
    protocol = schema.Choice(title=_t(u'Protocol'),
                             vocabulary="rpcMonitorProtocolVocabulary")
