# ------------------------------------------------------------------------------
# ARGUMENTS MODULE
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This module handles all the argument validation and printing out of
# help messages etc.
#

import sys

def noSystemArgsExist(arguments):
    print len(arguments) == 1
    return len(arguments) == 1

def printHelpDocumentationThenExit():
    print "Rancher Deployment Script\n"
    print "This script will assist you in updating your rancher environment."
    print "All the following command line arguments are required to update rancher\n"
    print "Usage: --url <http://example.com> --key <key> --secret <secret_key> --env [dev|staging|prod]"
    print "    --url \t url to connect to your rancher server"
    print "    --key \t username of api key to connect to rancher host"
    print "    --secret \t password of api key to connect to rancher host"
    print "    --env \t environment you wish to update"
    sys.exit(0);
