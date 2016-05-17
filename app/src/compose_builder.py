# ------------------------------------------------------------------------------
# COMPOSE_BUILDER MODULE
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This module handles all the combining and altering methods of the yml
# files once they have been read into the application
#

import logging

logger = logging.getLogger('Rancher Deployment')

def safeServiceLoad(compose_file, service):
    logger.debug("DEBUG: Attempting to Load Service: %s", service)
    if service in compose_file:
        logger.debug("DEBUG: Succesfully Loaded Service: %s", service)
        return True
    else:
        logger.error("ERROR: Service Does Not Exists In Compose File. MISSING SERVICE: %s", service)
        raise Exception('Service was not found inside your rancher compose file. \nMISSING SERVICE: ' + service)

def optionExistsInService(service_array, option):
    logger.debug("DEBUG: Attempting to Load Option: %s", option)
    if option in service_array:
        logger.debug("DEBUG: Succesfully Found Option: %s", option)
        return True
    else:
        logger.debug("DEBUG: Failed to Find Option: %s", option)
        return False

def createOptionInService(service_array, service, option, option_type):
    logger.debug("DEBUG: Creating Option in Service: %s", option)
    logger.debug("DEBUG: Service Name: %s", service)
    logger.debug("DEBUG: Option Name: %s", option)
    if option_type is dict:
        logger.debug("DEBUG: Option Created of Type: dict")
        default_value = {}
    if option_type is list:
        logger.debug("DEBUG: Option Created of Type: list")
        default_value = []
    if option_type is str:
        logger.debug("DEBUG: Option Created of Type: str")
        default_value = ""
    service_array[service].update({option: default_value})

def addOptionToService(docker_config, service, option, config_options):
    logger.debug("DEBUG: Adding Option in Service from Config: %s", option)
    logger.debug("DEBUG: Service Name: %s", service)
    logger.debug("DEBUG: Option Name: %s", option)
    option_type = type(config_options)
    if option_type is dict:
        logger.debug("DEBUG: Adding Dictionary...")
        for key in config_options:
            logger.debug("DEBUG: Adding Key: %s", key)
            logger.debug("DEBUG: Adding Value: %s", config_options[key])
            docker_config[service][option][key] = config_options[key]
    elif option_type is list:
        logger.debug("DEBUG: Adding List Items...")
        for value in config_options:
            logger.debug("DEBUG: Adding Value: %s", value)
            docker_config[service][option].append(value)
    elif option_type is str:
        logger.debug("DEBUG: Adding String: %s", config_options)
        docker_config[service][option] = config_options

def addConfigToDockerCompose(docker_config, add_config):
    logger.debug("DEBUG: Adding Config To Docker Compose File")
    for service in add_config:
        logger.debug("DEBUG: Updaing Config In Service: %s", service)
        if safeServiceLoad(docker_config, service):
            for option in add_config[service]:
                if not optionExistsInService(docker_config[service], option):
                    createOptionInService(docker_config, service, option, type(add_config[service][option]))
                addOptionToService(docker_config, service, option, add_config[service][option])


def setImageForDockerConfig(docker_config, environment, image_base):
    if environment == 'dev':
        image_name = image_base + ':dev'
    elif environment == 'staging':
        image_name = image_base + ':staging'
    elif environment == 'prod':
        image_name = image_base + ':latest'
    logger.debug("DEBUG: Docker Image Name Set To: %s", image_name)
    docker_config['web']['image'] = image_name
