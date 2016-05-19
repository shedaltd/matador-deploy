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
import logging
from subprocess import call
from app import __version__

logger = logging.getLogger('Rancher Deployment')

def noSystemArgsExist(arguments):
    if len(arguments) == 1:
        print "ERROR: No Arguments Found. Please Read Documentation For Usage Instructions.\n"
    return len(arguments) == 1

def printHelpDocumentationThenExit():
    print "Matador-Deploy - Rancher Deployment Assitant Script\n"
    print "Author: SEED Digital\n"
    print "This script will assist you in updating your rancher environment."
    print "All the following command line arguments are required to update rancher\n"
    print "Version: v%s" % __version__
    call(["rancher-compose", "-v"])
    print ""
    print "Usage: [-flags] --url <http://example.com> --key <key> --secret <secret_key> --env [dev|staging|prod]"
    print "  --url \t url to connect to your rancher server"
    print "  --key \t username of api key to connect to rancher host"
    print "  --secret \t password of api key to connect to rancher host"
    print "  --env \t environment you wish to update"
    print ""
    print "  Flags [-hfvd]"
    print "  -h  \t Show the help documentation -- (will stop application from running unless force mode is also present)"
    print "  -f  \t Force Mode: force the application to run and supress all warnings"
    print "  -v  \t Verbose Mode: print additional messages are processes run"
    print "  -d  \t Development Mode: will bypass command line arguments and set default values for Rancher configuration"
    print ""
    print "  Version Information"
    print "  --version  \t Print out the current version of matador-deploy and the local installed version of rancher-compose"
    sys.exit(0)

def printVersionInformationThenExit():
    print "matador-deploy version v%s" % __version__
    call(["rancher-compose", "-v"])
    sys.exit(0)

def checkArgumentStructure(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;
    if len(arguments) < 9:
        logger.error("ERROR: Not enough arguments passed. Please use the [-h] flag for usage instructions.")
        sys.exit(0)
    if not arguments[args_init_index] == '--url':
        logger.error("ERROR: [--url] not present. Either the [--url] argument was not supplied or was not supplied in the correct order.")
        sys.exit(0)
    if not arguments[args_init_index + 2] == '--key':
        logger.error("ERROR: [--key] not present. Either the [--key] argument was not supplied or was not supplied in the correct order.")
        sys.exit(0)
    if not arguments[args_init_index + 4] == '--secret':
        logger.error("ERROR: [--secret] not present. Either the [--secret] argument was not supplied or was not supplied in the correct order.")
        sys.exit(0)
    if not arguments[args_init_index + 6] == '--env':
        logger.error("ERROR: [--env] not present. Either the [--env] argument was not supplied or was not supplied in the correct order.")
        sys.exit(0)

def doFlagsExist(arguments):
    return not arguments[1] == '--url'

def isVersionCommandEntered(arguments):
    return arguments[1] == '--version'

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

def setRancherUrl(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;
    return arguments[args_init_index + 1]

def setRancherKey(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;
    return arguments[args_init_index + 3]

def setRancherSecret(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;
    return arguments[args_init_index + 5]

def setEnvironment(arguments):
    args_init_index = 1;
    if not arguments[1] == '--url':
        args_init_index = 2;
    return arguments[args_init_index + 7]
