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

def safeServiceLoad(compose_file, service):
    if service in compose_file:
        return True
    else:
        print "ERROR: Service does not exist in compose file"
        raise Exception('Service was not found inside your rancher compose file. \nMISSING SERVICE: ' + service)

def optionExistsInService(service_array, option):
    if option in service_array:
        return True
    else:
        return False

def createOptionInService(service_array, service, option, option_type):
    if option_type is dict:
        default_value = {}
    if option_type is list:
        default_value = []
    if option_type is str:
        default_value = ""
    service_array[service].update({option: default_value})

def addOptionToService(docker_config, service, option, config_options):
    option_type = type(config_options)
    if option_type is dict:
        for key in config_options:
            docker_config[service][option][key] = config_options[key]
    elif option_type is list:
        for value in config_options:
            docker_config[service][option].append(value)
    elif option_type is str:
        docker_config[service][option] = config_options

def addConfigToDockerCompose(docker_config, add_config):
    for service in add_config:
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
    docker_config['web']['image'] = image_name
