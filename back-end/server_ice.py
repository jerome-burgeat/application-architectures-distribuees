# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.8
#
# <auto-generated>
#
# Generated from file `server.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module ApplicationArchitecturesDistribuees
_M_ApplicationArchitecturesDistribuees = Ice.openModule('ApplicationArchitecturesDistribuees')
__name__ = 'ApplicationArchitecturesDistribuees'

_M_ApplicationArchitecturesDistribuees._t_Server = IcePy.defineValue('::ApplicationArchitecturesDistribuees::Server', Ice.Value, -1, (), False, True, None, ())

if 'ServerPrx' not in _M_ApplicationArchitecturesDistribuees.__dict__:
    _M_ApplicationArchitecturesDistribuees.ServerPrx = Ice.createTempClass()
    class ServerPrx(Ice.ObjectPrx):

        def helloWorld(self, helloWorld, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_helloWorld.invoke(self, ((helloWorld, ), context))

        def helloWorldAsync(self, helloWorld, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_helloWorld.invokeAsync(self, ((helloWorld, ), context))

        def begin_helloWorld(self, helloWorld, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_helloWorld.begin(self, ((helloWorld, ), _response, _ex, _sent, context))

        def end_helloWorld(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_helloWorld.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.ServerPrx.ice_checkedCast(proxy, '::ApplicationArchitecturesDistribuees::Server', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ApplicationArchitecturesDistribuees.ServerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ApplicationArchitecturesDistribuees::Server'
    _M_ApplicationArchitecturesDistribuees._t_ServerPrx = IcePy.defineProxy('::ApplicationArchitecturesDistribuees::Server', ServerPrx)

    _M_ApplicationArchitecturesDistribuees.ServerPrx = ServerPrx
    del ServerPrx

    _M_ApplicationArchitecturesDistribuees.Server = Ice.createTempClass()
    class Server(Ice.Object):

        def ice_ids(self, current=None):
            return ('::ApplicationArchitecturesDistribuees::Server', '::Ice::Object')

        def ice_id(self, current=None):
            return '::ApplicationArchitecturesDistribuees::Server'

        @staticmethod
        def ice_staticId():
            return '::ApplicationArchitecturesDistribuees::Server'

        def helloWorld(self, helloWorld, current=None):
            raise NotImplementedError("servant method 'helloWorld' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ApplicationArchitecturesDistribuees._t_ServerDisp)

        __repr__ = __str__

    _M_ApplicationArchitecturesDistribuees._t_ServerDisp = IcePy.defineClass('::ApplicationArchitecturesDistribuees::Server', Server, (), None, ())
    Server._ice_type = _M_ApplicationArchitecturesDistribuees._t_ServerDisp

    Server._op_helloWorld = IcePy.Operation('helloWorld', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_ApplicationArchitecturesDistribuees.Server = Server
    del Server

# End of module ApplicationArchitecturesDistribuees
