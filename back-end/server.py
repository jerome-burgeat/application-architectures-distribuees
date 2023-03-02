import sys, Ice
import ApplicationArchitecturesDistribuees
 
class Server(ApplicationArchitecturesDistribuees.Server):

    def helloWorld(self, helloWorld, current=None):
        print helloWorld
 
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ApplicationArchitecturesDistribuees", "default -p 10000")
    object = PrinterI()
    adapter.add(object, communicator.stringToIdentity("ApplicationArchitecturesDistribuees"))
    adapter.activate()
    communicator.waitForShutdown()