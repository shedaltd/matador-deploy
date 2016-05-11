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
docker_compose_file = yml_reader.readDockerComposeFile()
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


rancher_data = {}
rancher_data['id'] = '1e42'
rancher_data['type'] = 'environment'
rancher_data['name'] = 'test-env'
rancher_data['links'] = {}
rancher_data['links']['self'] = 'http://localhost:8080/v1/environments/1e6'
rancher_data['links']['account'] = 'http://localhost:8080/v1/environments/1e6/account'
rancher_data['links']['services'] = 'http://localhost:8080/v1/environments/1e6/services'
rancher_data['links']['composeConfig'] = 'http://localhost:8080/v1/environments/1e6/composeconfi'
rancher_data['actions'] = {}
rancher_data['actions']['remove'] = 'http://localhost:8080/v1/environments/1e6/?action=remove'
rancher_data['actions']['error'] = 'http://localhost:8080/v1/environments/1e6/?action=error'
rancher_data['actions']['addoutputs'] = 'http://localhost:8080/v1/environments/1e6/?action=addoutputs'
rancher_data['actions']['activateservices'] = 'http://localhost:8080/v1/environments/1e6/?action=activateservices'
rancher_data['actions']['deactivateservices'] = 'http://localhost:8080/v1/environments/1e6/?action=deactivateservices'
rancher_data['actions']['exportconfig'] = 'http://localhost:8080/v1/environments/1e6/?action=exportconfi'

# {
#   "scale": 1,
#   "launchConfig": {
#     "imageUuid": "docker:mongo:3",
#     "labels": {
#       "io.rancher.service.hash": "adf1538e466f1a8cc3f6c1935ce9b75218f4166b"
#     },
#     "logConfig": {},
#     "networkMode": "managed",
#     "ports": [
#       "27017:27017/tcp"
#     ],
#     "startOnCreate": true,
#     "kind": "container",
#     "privileged": false,
#     "publishAllPorts": false,
#     "readOnly": false,
#     "stdinOpen": false,
#     "tty": false,
#     "version": "0",
#     "vcpu": 1
#   },
#   "name": "db",
#   "metadata": {
#     "io.rancher.service.hash": "d207d194d16104535c1df27c1c9ac5918b7cfa26"
#   },
#   "environmentId": 17,
#   "assignServiceIpAddress": false,
#   "startOnCreate": false
# }


# mongo_service = {}
# mongo_service['type'] = 'service'
# mongo_service['scale'] = '1'
# mongo_service['name'] = 'db'
# mongo_service['environmentId'] = environment['id']
# mongo_service['launchConfig'] = rancher_compose_file['db']


def createServiceObject(name, compose_config, env_id):
    service = {}
    service['type'] = 'service'
    service['scale'] = '1'
    service['environmentId'] = env_id
    service['name'] = compose_config['container_name'] if 'container_name' in compose_config else name
    service['launchConfig'] = compose_config
    service['launchConfig']['imageUuid'] = 'docker:' + compose_config['image']
    service['startOnCreate'] = True
    return service


environment = client.create_environment(rancher_data)
mongo_service = createServiceObject('db', rancher_compose_file['db'], environment['id'])

container = client.create_service(mongo_service)



# print dir(client)
# print environment['id']
# ranch = {}
# ranch['name'] = 'test-project'
# ranch['dockerCompose'] = docker_compose_file
# ranch['rancherCompose'] = rancher_compose_file
# ranch['startOnCreate'] = True
# response = client.create_environment(ranch)

print dir(client)

print "Got Here"
