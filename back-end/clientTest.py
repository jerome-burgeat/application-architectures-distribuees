import sys, Ice
import ApplicationArchitecturesDistribuees
 
with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("ApplicationArchitecturesDistribuees:default -p 10000")
    app = ApplicationArchitecturesDistribuees.ServerPrx.checkedCast(base)
    if not app:
        raise RuntimeError("Invalid proxy")
 
    app.helloWorld("Hello World!")

    # data = '{"title": "test1", "url2": "www.goggle2.com"}'
    # app.addMusic(data)

    # app.deleteMusic('test1')

    app.searchMusic('test')

    app.updateMusicChangeTitle('test', 'testUpdated')
