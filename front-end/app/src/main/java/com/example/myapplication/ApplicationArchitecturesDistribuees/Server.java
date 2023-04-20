// **********************************************************************
//
// Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.7.1
//
// <auto-generated>
//
// Generated from file `server.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package ApplicationArchitecturesDistribuees;

public interface Server extends com.zeroc.Ice.Object
{
    void helloWorld(String helloWorld, com.zeroc.Ice.Current current);

    int getNewIndex(com.zeroc.Ice.Current current);

    boolean uploadPart(int id, byte[] part, com.zeroc.Ice.Current current);

    boolean uploadFileAndInsertMusic(int id, String filename, com.zeroc.Ice.Current current);

    void deleteMusic(String titleMusic, com.zeroc.Ice.Current current);

    void searchMusic(String titleMusic, com.zeroc.Ice.Current current);

    void updateMusicChangeTitle(String titleCurrent, String newTitle, com.zeroc.Ice.Current current);

    boolean playMusic(String filename, com.zeroc.Ice.Current current);

    boolean stopMusic(com.zeroc.Ice.Current current);

    boolean pauseMusic(com.zeroc.Ice.Current current);

    static final String[] _iceIds =
    {
        "::ApplicationArchitecturesDistribuees::Server",
        "::Ice::Object"
    };

    @Override
    default String[] ice_ids(com.zeroc.Ice.Current current)
    {
        return _iceIds;
    }

    @Override
    default String ice_id(com.zeroc.Ice.Current current)
    {
        return ice_staticId();
    }

    static String ice_staticId()
    {
        return "::ApplicationArchitecturesDistribuees::Server";
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_helloWorld(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_helloWorld;
        iceP_helloWorld = istr.readString();
        inS.endReadParams();
        obj.helloWorld(iceP_helloWorld, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_getNewIndex(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        inS.readEmptyParams();
        int ret = obj.getNewIndex(current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeInt(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_uploadPart(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        int iceP_id;
        byte[] iceP_part;
        iceP_id = istr.readInt();
        iceP_part = istr.readByteSeq();
        inS.endReadParams();
        boolean ret = obj.uploadPart(iceP_id, iceP_part, current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeBool(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_uploadFileAndInsertMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        int iceP_id;
        String iceP_filename;
        iceP_id = istr.readInt();
        iceP_filename = istr.readString();
        inS.endReadParams();
        boolean ret = obj.uploadFileAndInsertMusic(iceP_id, iceP_filename, current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeBool(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_deleteMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_titleMusic;
        iceP_titleMusic = istr.readString();
        inS.endReadParams();
        obj.deleteMusic(iceP_titleMusic, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_searchMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_titleMusic;
        iceP_titleMusic = istr.readString();
        inS.endReadParams();
        obj.searchMusic(iceP_titleMusic, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_updateMusicChangeTitle(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_titleCurrent;
        String iceP_newTitle;
        iceP_titleCurrent = istr.readString();
        iceP_newTitle = istr.readString();
        inS.endReadParams();
        obj.updateMusicChangeTitle(iceP_titleCurrent, iceP_newTitle, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_playMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_filename;
        iceP_filename = istr.readString();
        inS.endReadParams();
        boolean ret = obj.playMusic(iceP_filename, current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeBool(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_stopMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        inS.readEmptyParams();
        boolean ret = obj.stopMusic(current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeBool(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_pauseMusic(Server obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        inS.readEmptyParams();
        boolean ret = obj.pauseMusic(current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeBool(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    final static String[] _iceOps =
    {
        "deleteMusic",
        "getNewIndex",
        "helloWorld",
        "ice_id",
        "ice_ids",
        "ice_isA",
        "ice_ping",
        "pauseMusic",
        "playMusic",
        "searchMusic",
        "stopMusic",
        "updateMusicChangeTitle",
        "uploadFileAndInsertMusic",
        "uploadPart"
    };

    @Override
    default java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceDispatch(com.zeroc.IceInternal.Incoming in, com.zeroc.Ice.Current current)
        throws com.zeroc.Ice.UserException
    {
        int pos = java.util.Arrays.binarySearch(_iceOps, current.operation);
        if(pos < 0)
        {
            throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
        }

        switch(pos)
        {
            case 0:
            {
                return _iceD_deleteMusic(this, in, current);
            }
            case 1:
            {
                return _iceD_getNewIndex(this, in, current);
            }
            case 2:
            {
                return _iceD_helloWorld(this, in, current);
            }
            case 3:
            {
                return com.zeroc.Ice.Object._iceD_ice_id(this, in, current);
            }
            case 4:
            {
                return com.zeroc.Ice.Object._iceD_ice_ids(this, in, current);
            }
            case 5:
            {
                return com.zeroc.Ice.Object._iceD_ice_isA(this, in, current);
            }
            case 6:
            {
                return com.zeroc.Ice.Object._iceD_ice_ping(this, in, current);
            }
            case 7:
            {
                return _iceD_pauseMusic(this, in, current);
            }
            case 8:
            {
                return _iceD_playMusic(this, in, current);
            }
            case 9:
            {
                return _iceD_searchMusic(this, in, current);
            }
            case 10:
            {
                return _iceD_stopMusic(this, in, current);
            }
            case 11:
            {
                return _iceD_updateMusicChangeTitle(this, in, current);
            }
            case 12:
            {
                return _iceD_uploadFileAndInsertMusic(this, in, current);
            }
            case 13:
            {
                return _iceD_uploadPart(this, in, current);
            }
        }

        assert(false);
        throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
    }
}
