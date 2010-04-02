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
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IRPCMonitorDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    rpcServer = schema.Text(title=_t(u'RPC Server'))
    rpcCommand = schema.Text(title=_t(u'RPC Command'))
    port = schema.Int(title=_t(u'Port'))
    protocol = schema.Choice(title=_t(u'Protocol'),
                             vocabulary="rpcMonitorProtocolVocabulary")
    
