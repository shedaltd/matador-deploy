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

# ###################################
# Custom Python Modules
# -----------------------------------
arguments = imp.load_source('arguments', './app/src/arguments.py')
yml_reader = imp.load_source('yml_reader', './app/src/yml_reader.py')
compose_builder = imp.load_source('compose_builder', './app/src/compose_builder.py')


# #####################################################
# 1. Confirming Command Config and Required Arguments
# -----------------------------------------------------
# if arguments.noSystemArgsExist(sys.argv):
    # arguments.printHelpDocumentationThenExit()

#TODO: Add flag reading stuff in here

# Setup GLOBAL Env Vars passed in from command line
ENV_ARGUMENT = "prod"
RANCHER_SECRET_KEY = "dfasf"
RANCHER_API_THING = "dfasf"
RANCHER_URL = "dfasf"


# ##################################
# 2. Reading YAML Files Into Script
# ----------------------------------
rancher_compose_file = yml_reader.readComposeFile()
config_file = yml_reader.readConfigurationFile()
global_config = yml_reader.getGlobalConfig()
env_config = yml_reader.getEnvConfig(ENV_ARGUMENT)


# ##################################################
# 3. Combine config into the rancher compose
# --------------------------------------------------
compose_builder.addConfigToRancherCompose(rancher_compose_file, global_config)
compose_builder.addConfigToRancherCompose(rancher_compose_file, env_config)

# ###############################################
# 4. Set the image for the deployment
# -----------------------------------------------
compose_builder.setImageForRancherConfig(rancher_compose_file, ENV_ARGUMENT, config_file['image_base'])

# ###############################################
# 5. Save new yml out to a temp file
# -----------------------------------------------
yml_reader.saveRancherComposeFile(rancher_compose_file)

# ###############################################
# 6. Start updating this stuff to rancher baby
# -----------------------------------------------
