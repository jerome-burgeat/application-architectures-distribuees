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

if '_t_byteList' not in _M_ApplicationArchitecturesDistribuees.__dict__:
    _M_ApplicationArchitecturesDistribuees._t_byteList = IcePy.defineSequence('::ApplicationArchitecturesDistribuees::byteList', (), IcePy._t_byte)

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

        def getNewIndex(self, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_getNewIndex.invoke(self, ((), context))

        def getNewIndexAsync(self, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_getNewIndex.invokeAsync(self, ((), context))

        def begin_getNewIndex(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_getNewIndex.begin(self, ((), _response, _ex, _sent, context))

        def end_getNewIndex(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_getNewIndex.end(self, _r)

        def uploadPart(self, id, part, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadPart.invoke(self, ((id, part), context))

        def uploadPartAsync(self, id, part, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadPart.invokeAsync(self, ((id, part), context))

        def begin_uploadPart(self, id, part, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadPart.begin(self, ((id, part), _response, _ex, _sent, context))

        def end_uploadPart(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadPart.end(self, _r)

        def uploadFileAndInsertMusic(self, id, filename, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadFileAndInsertMusic.invoke(self, ((id, filename), context))

        def uploadFileAndInsertMusicAsync(self, id, filename, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadFileAndInsertMusic.invokeAsync(self, ((id, filename), context))

        def begin_uploadFileAndInsertMusic(self, id, filename, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadFileAndInsertMusic.begin(self, ((id, filename), _response, _ex, _sent, context))

        def end_uploadFileAndInsertMusic(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_uploadFileAndInsertMusic.end(self, _r)

        def deleteMusic(self, titleMusic, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_deleteMusic.invoke(self, ((titleMusic, ), context))

        def deleteMusicAsync(self, titleMusic, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_deleteMusic.invokeAsync(self, ((titleMusic, ), context))

        def begin_deleteMusic(self, titleMusic, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_deleteMusic.begin(self, ((titleMusic, ), _response, _ex, _sent, context))

        def end_deleteMusic(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_deleteMusic.end(self, _r)

        def searchMusic(self, titleMusic, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_searchMusic.invoke(self, ((titleMusic, ), context))

        def searchMusicAsync(self, titleMusic, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_searchMusic.invokeAsync(self, ((titleMusic, ), context))

        def begin_searchMusic(self, titleMusic, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_searchMusic.begin(self, ((titleMusic, ), _response, _ex, _sent, context))

        def end_searchMusic(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_searchMusic.end(self, _r)

        def updateMusicChangeTitle(self, titleCurrent, newTitle, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_updateMusicChangeTitle.invoke(self, ((titleCurrent, newTitle), context))

        def updateMusicChangeTitleAsync(self, titleCurrent, newTitle, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_updateMusicChangeTitle.invokeAsync(self, ((titleCurrent, newTitle), context))

        def begin_updateMusicChangeTitle(self, titleCurrent, newTitle, _response=None, _ex=None, _sent=None, context=None):
            return _M_ApplicationArchitecturesDistribuees.Server._op_updateMusicChangeTitle.begin(self, ((titleCurrent, newTitle), _response, _ex, _sent, context))

        def end_updateMusicChangeTitle(self, _r):
            return _M_ApplicationArchitecturesDistribuees.Server._op_updateMusicChangeTitle.end(self, _r)

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

        def getNewIndex(self, current=None):
            raise NotImplementedError("servant method 'getNewIndex' not implemented")

        def uploadPart(self, id, part, current=None):
            raise NotImplementedError("servant method 'uploadPart' not implemented")

        def uploadFileAndInsertMusic(self, id, filename, current=None):
            raise NotImplementedError("servant method 'uploadFileAndInsertMusic' not implemented")

        def deleteMusic(self, titleMusic, current=None):
            raise NotImplementedError("servant method 'deleteMusic' not implemented")

        def searchMusic(self, titleMusic, current=None):
            raise NotImplementedError("servant method 'searchMusic' not implemented")

        def updateMusicChangeTitle(self, titleCurrent, newTitle, current=None):
            raise NotImplementedError("servant method 'updateMusicChangeTitle' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ApplicationArchitecturesDistribuees._t_ServerDisp)

        __repr__ = __str__

    _M_ApplicationArchitecturesDistribuees._t_ServerDisp = IcePy.defineClass('::ApplicationArchitecturesDistribuees::Server', Server, (), None, ())
    Server._ice_type = _M_ApplicationArchitecturesDistribuees._t_ServerDisp

    Server._op_helloWorld = IcePy.Operation('helloWorld', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Server._op_getNewIndex = IcePy.Operation('getNewIndex', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Server._op_uploadPart = IcePy.Operation('uploadPart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), _M_ApplicationArchitecturesDistribuees._t_byteList, False, 0)), (), ((), IcePy._t_bool, False, 0), ())
    Server._op_uploadFileAndInsertMusic = IcePy.Operation('uploadFileAndInsertMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_bool, False, 0), ())
    Server._op_deleteMusic = IcePy.Operation('deleteMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Server._op_searchMusic = IcePy.Operation('searchMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Server._op_updateMusicChangeTitle = IcePy.Operation('updateMusicChangeTitle', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())

    _M_ApplicationArchitecturesDistribuees.Server = Server
    del Server

# End of module ApplicationArchitecturesDistribuees
