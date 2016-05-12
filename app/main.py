#!/usr/bin/env python
# ------------------------------------------------------------------------------
# LICENCE INFORMATION
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This application is a script for deploying applications to the
# Rancher platform. It takes a number of command linke arguments
# and will then use these variables to build a rancher compose
# file and then push the application to the rancher environment
# defined by the API Keys it is provided.
#

# ###################################
# Core Python Modules
# -----------------------------------
import sys
import imp
import logging
from rainbow_logging_handler import RainbowLoggingHandler

# setup `logging` module
logger = logging.getLogger('Rancher Deployment')
# logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] %(name)s %(funcName)s():%(lineno)d\t%(message)s")  # same as default

# setup `RainbowLoggingHandler`
handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'yellow', True))
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.error("MEssage about an error")
logger.info("Only shown in info mode")
logger.debug("Only shown in debug mode")

# ###################################
# Importing Args Modules
# -----------------------------------
arguments = imp.load_source('arguments', './app/src/arguments.py')



# #####################################################
# 1. Confirming Command Config and Required Arguments
# -----------------------------------------------------
# Check to see if arguments have been passed at all
if arguments.noSystemArgsExist(sys.argv):
    arguments.printHelpDocumentationThenExit()

# Check for the existance of flags
if arguments.doFlagsExist(sys.argv):
    flags = sys.argv[1]
    arguments.checkHelpFlag(flags)
    FORCE_MODE = arguments.setForceFlag(flags)
    VERBOSE_MODE = arguments.setVerboseFlag(flags)
    DEVELOPMENT_MODE = arguments.setDevelopmentFlag(flags)
else:
    FORCE_MODE = False
    VERBOSE_MODE = False
    DEVELOPMENT_MODE = False

if VERBOSE_MODE:
    print "Flag Configuration - "
    print "Force Mode: %s" % FORCE_MODE
    print "Verbose Mode: %s" % VERBOSE_MODE
    print "Development Mode: %s" % DEVELOPMENT_MODE

if not DEVELOPMENT_MODE:
    arguments.checkArgumentStructure(sys.argv)
    ENV_ARGUMENT = arguments.setEnvironment(sys.argv)
    RANCHER_URL = arguments.setRancherUrl(sys.argv)
    RANCHER_ACCESS_KEY = arguments.setRancherKey(sys.argv)
    RANCHER_SECRET_KEY = arguments.setRancherSecret(sys.argv)
else:
    print "Currently In Development Mode. Setting Default Parameters"
    ENV_ARGUMENT = "prod"
    RANCHER_URL = 'http://localhost:8080/v1/'
    RANCHER_ACCESS_KEY = '9F68C78100A2CAA209EC'
    RANCHER_SECRET_KEY = 'pEkMsBYjcZNxhY4rzYuEfdLLj7mDBZ8EPYwbtgVZ'

if VERBOSE_MODE:
    print ""


print "Stopping App Execution"
print sys.exit(0)

# ##################################
# Import Additional Custom Modules
# ----------------------------------
# NOTE: This is done here so that the global vars can be used in the inner modules
yml_reader = imp.load_source('yml_reader', './app/src/yml_reader.py')
compose_builder = imp.load_source('compose_builder', './app/src/compose_builder.py')
rancher_compose = imp.load_source('rancher_compose', './app/src/rancher_compose.py')


# ##################################
# 2. Reading YAML Files Into Script
# ----------------------------------
rancher_compose_list = yml_reader.readRancherComposeTemplate()
docker_compose_list = yml_reader.readDockerComposeTemplate()
config_file = yml_reader.readConfigurationFile()
global_config = yml_reader.getGlobalConfig()
env_config = yml_reader.getEnvConfig(ENV_ARGUMENT)


# ##################################################
# 3. Combine config into the rancher compose
# --------------------------------------------------
compose_builder.addConfigToDockerCompose(docker_compose_list, global_config)
compose_builder.addConfigToDockerCompose(docker_compose_list, env_config)

# ###############################################
# 4. Set the image for the deployment
# -----------------------------------------------
compose_builder.setImageForDockerConfig(docker_compose_list, ENV_ARGUMENT, config_file['image_base'])

# ###############################################
# 5. Save new yml out to a temp file
# -----------------------------------------------
yml_reader.saveRancherComposeFile(rancher_compose_list)
yml_reader.saveDockerComposeFile(docker_compose_list)

# ###############################################
# 6. Start updating this stuff to rancher baby
# -----------------------------------------------
rancher_compose.setRancherVars(RANCHER_URL, RANCHER_ACCESS_KEY, RANCHER_SECRET_KEY)
rancher_compose.pushToRancher()
