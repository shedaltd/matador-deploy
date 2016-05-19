#!/usr/bin/env python
# ------------------------------------------------------------------------------
# LICENCE INFORMATION
# ------------------------------------------------------------------------------
# Matador Deploy - SEED DIGITAL (C) 2016
# Rancher Deployment Assitant Script
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
import cattle
import logging
from rainbow_logging_handler import RainbowLoggingHandler

def main():
    # setup `logging` module
    logger = logging.getLogger('Rancher Deployment')
    # logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(message)s")  # same as default

    # setup `RainbowLoggingHandler`
    handler = RainbowLoggingHandler(sys.stderr,
        color_funcName=('black', 'yellow', True),
        color_module=('yellow', None, False))

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # ###################################
    # Importing Args Modules
    # -----------------------------------
    from src import arguments

    # #####################################################
    # 1. Confirming Command Config and Required Arguments
    # -----------------------------------------------------
    # Check to see if arguments have been passed at all
    if arguments.noSystemArgsExist(sys.argv):
        arguments.printHelpDocumentationThenExit()

    # Check if we are printing out the version information
    if arguments.isVersionCommandEntered(sys.argv):
        arguments.printVersionInformationThenExit()

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
        logger.setLevel(logging.DEBUG)

    logger.info("INFO: Flag Configuration Set")
    logger.debug("DEBUG: Force Mode: %s", FORCE_MODE)
    logger.debug("DEBUG: Verbose Mode: %s", VERBOSE_MODE)
    logger.debug("DEBUG: Development Mode: %s\n", DEVELOPMENT_MODE)

    if not DEVELOPMENT_MODE:
        arguments.checkArgumentStructure(sys.argv)
        ENV_ARGUMENT = arguments.setEnvironment(sys.argv)
        RANCHER_URL = arguments.setRancherUrl(sys.argv)
        RANCHER_ACCESS_KEY = arguments.setRancherKey(sys.argv)
        RANCHER_SECRET_KEY = arguments.setRancherSecret(sys.argv)
    else:
        logger.info("INFO: Currently In Development Mode. Setting Default Parameters.")
        ENV_ARGUMENT = "staging"
        RANCHER_URL = 'http://localhost:8080/v1/'
        RANCHER_ACCESS_KEY = '9F68C78100A2CAA209EC'
        RANCHER_SECRET_KEY = 'pEkMsBYjcZNxhY4rzYuEfdLLj7mDBZ8EPYwbtgVZ'

    if not FORCE_MODE:
        print "Rancher Arguments Set"
        print "ENVIRONMENT: %s" % ENV_ARGUMENT
        logger.debug("DEBUG: RANCHER_URL: %s", RANCHER_URL)
        logger.debug("DEBUG: RANCHER_ACCESS_KEY: %s", RANCHER_ACCESS_KEY)
        logger.debug("DEBUG: RANCHER_SECRET_KEY: %s", RANCHER_SECRET_KEY)
        print "Would you like to continue?"
        var = raw_input("Please enter (Y|N): ")
        if var == "y" or var == "Y":
            print "User Confirmation Accepted. Performing Rancher Deployment"
            logger.debug("DEBUG: Please use the [-f] flag to force application execution and skip confirmation")
        elif var == "n" or var == "N":
            logger.error("ERROR: User stopped app execution.")
            logger.debug("DEBUG: Please use the [-f] flag to force application execution and skip confirmation")
            print sys.exit(0)
        else:
            logger.error("ERROR: Invalid User Input")
            logger.error("ERROR: Please use the [-f] flag to force application execution and skip confirmation")
            print sys.exit(0)
    else:
        logger.info("INFO: Force Mode Enabled. Skipping Flag Confirmation")


    print "Starting Matador Deploy..."
    # ##################################
    # Import Additional Custom Modules
    # ----------------------------------
    # NOTE: This is done here so that the global vars can be used in the inner modules
    from src import yml_reader
    from src import compose_builder
    from src import rancher_compose

    # ##################################
    # 2. Reading YAML Files Into Script
    # ----------------------------------
    rancher_compose_list = yml_reader.readRancherComposeTemplate()
    docker_compose_list = yml_reader.readDockerComposeTemplate()
    config_file = yml_reader.readConfigurationFile()
    global_config = yml_reader.getGlobalConfig()
    env_config = yml_reader.getEnvConfig(ENV_ARGUMENT)
    PROJECT_NAME = config_file['project_name'] + "-" + ENV_ARGUMENT

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
    yml_reader.createBuildDirectory()
    yml_reader.saveRancherComposeFile(rancher_compose_list)
    yml_reader.saveDockerComposeFile(docker_compose_list)

    # ###############################################
    # 6. Start updating this stuff to rancher baby
    # -----------------------------------------------
    cattle_client = cattle.Client(
        url=RANCHER_URL,
        access_key=RANCHER_ACCESS_KEY,
        secret_key=RANCHER_SECRET_KEY
    )
    rancher_compose.setRancherVars(RANCHER_URL, RANCHER_ACCESS_KEY, RANCHER_SECRET_KEY, PROJECT_NAME)
    rancher_compose.checkForExistingEnvironment(cattle_client, PROJECT_NAME)
    rancher_compose.pushToRancher()
main()
