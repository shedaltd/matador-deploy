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
    if len(arguments) == 1:
        print "ERROR: No Arguments Found. Please Read Documentation For Usage Instructions.\n"
    return len(arguments) == 1

def printHelpDocumentationThenExit():
    print "Rancher Deployment Script\n"
    print "This script will assist you in updating your rancher environment."
    print "All the following command line arguments are required to update rancher\n"
    print "Usage: [-flags] --url <http://example.com> --key <key> --secret <secret_key> --env [dev|staging|prod]"
    print "    --url \t url to connect to your rancher server"
    print "    --key \t username of api key to connect to rancher host"
    print "    --secret \t password of api key to connect to rancher host"
    print "    --env \t environment you wish to update"
    print ""
    print "    Flags [-hfvd]"
    print "    -h  \t Show the help documentation -- (will stop application from running unless force mode is also present)"
    print "    -f  \t Force Mode: force the application to run and supress all warnings"
    print "    -v  \t Verbose Mode: print additional messages are processes run"
    print "    -d  \t Development Mode: will bypass command line arguments and set default values for Rancher configuration"
    sys.exit(0);

def checkArgumentStructure(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;



def doFlagsExist(arguments):
    return not arguments[1] == '--url'

def checkHelpFlag(flags):
    if 'h' in flags:
        if not 'f' in flags:
            printHelpDocumentationThenExit()

def setForceFlag(flags):
    return 'f' in flags

def setVerboseFlag(flags):
    return 'v' in flags

def setDevelopmentFlag(flags):
    return 'd' in flags
