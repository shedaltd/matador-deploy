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
CATTLE_URL = 'http://localhost:8080/v1/'
CATTLE_ACCESS_KEY = '9F68C78100A2CAA209EC'
CATTLE_SECRET_KEY = 'pEkMsBYjcZNxhY4rzYuEfdLLj7mDBZ8EPYwbtgVZ'


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

# import imp
# cattle = imp.load_source('cattle', './app/libs/cattle-0.5.4/cattle.py')

import cattle

client = cattle.Client(
    url = CATTLE_URL,
    access_key = CATTLE_ACCESS_KEY,
    secret_key = CATTLE_SECRET_KEY
)

# print dir(client)


# rancher_data = {}
# rancher_data['description'] = "This is a great"
# rancher_data['dockerCompose'] = './templates/default-docker-compose.yml'
# rancher_data['rancherCompose'] = './templates/rancher-compose.yml'
# rancher_data['startOnCreate'] = True
# rancher_data['name'] = "Test Env"
# rancher_data['id'] = '0a23n1l451'

print "Getting Environments"

req_dict = {}
req_dict['id'] = '0a23n1l451'
req_dict['type'] = 'schema'
req_dict['links'] = {}
req_dict['links']['self'] = 'https://base/v1/schemas/folder'

client.create_environment(req_dict)


print "Got Here"
