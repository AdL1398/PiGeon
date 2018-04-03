import sys
import time
import argparse
import traceback
import os
import subprocess


from pyndn import Interest
from pyndn import Data
from pyndn import Exclude
from pyndn import Name
from pyndn import Face
from pyndn import InterestFilter
from pyndn.security import KeyChain
from modules.tools.enumerate_publisher import EnumeratePublisher

# from NOMAD import enumerate_publisher
class trigger(object):
    def __init__(self):

        self.script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
        self.script_dir = os.path.split(self.script_path)[0] #i.e. /path/to/dir/
        self.prefix_DE = "/picasso/start_de/"
        self.prefix_pullService = "/picasso/pull_Service/"
        self.prefix_pushService = "/picasso/service_deployment_push/"

        # Default configuration of NDN
        self.outstanding = dict()
        self.isDone = False
        self.keyChain = KeyChain()
        self.face = Face("127.0.0.1")

        self.face.setCommandSigningInfo(self.keyChain, \
                                        self.keyChain.getDefaultCertificateName())

    def run(self):
        try:
            # send Interest message to retrieve data
            #self.sendNextInterest(self.prefix_serviceMigration)

            print 'Select Migration Method'
            print '   (a) push'
            print '   (b) pull'
            method = raw_input('Choose method to migrate service (type code, e.g., a): ')
            if method == 'a':
                print 'Migrate by PUSH'
                type_name = self.prefix_pushService
            elif method == 'b':
                print 'Migrate by PULL'
                type_name = self.prefix_pullService
            else:
                print 'Chosen type is not available'

            print 'Select Service '
            print '   (1) umobilestore'
            print '   (2) cloudrone'
            print '   (3) kebapp'
            service = raw_input('Choose service to be deployed (type number, e.g., 1): ')

            if service == '1':
                print 'Start migrating umobilestore'
                service_name = 'umobilestore'
            elif service == '2':
                print 'Start migrating cloudrone'
                service_name = 'cloudrone'
            elif service == '3':
                print 'Start migrating kebapp'
                service_name = 'kebapp'
            else:
                print 'Chosen service is not available'

            name_prefix = type_name + service_name + '.tar.gz'
            print 'name prefix: %s' % name_prefix
            self.sendInterest(Name(name_prefix))


        except RuntimeError as e:
            print "ERROR: %s" % e

    def sendInterest(self, name):
        interest = Interest(name)
        interestName = interest.getName()
        interest.setInterestLifetimeMilliseconds(4000)
        interest.setMustBeFresh(True)
        self.face.expressInterest(interest, None, None)  ## set None --> sent out only, don't wait for Data and Timeout
        print "Sent Interest for %s" % interestName

if __name__ == '__main__':

    try:

        trigger().run()

    except:
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)



