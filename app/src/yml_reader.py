# ------------------------------------------------------------------------------
# YML_READER MODULE
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This module handles reading all the yml configuration files in from the
# file system.
#
import yaml
import logging

logger = logging.getLogger('Rancher Deployment')

def readRancherComposeTemplate():
    logger.debug("DEBUG: Attempting To Load Rancher Compose Template")
    # Load in out base rancher template
    with open("templates/rancher-compose-template.yml", 'r') as stream:
        try:
            logger.debug("DEBUG: Rancher Compose Template Successfully Loaded")
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            logger.error("ERROR: Failed To Load Rancher Compose Template")
            print(exc)

def readDockerComposeTemplate():
    logger.debug("DEBUG: Attempting to Load Docker Compose Template")
    # Load in out base rancher template
    with open("templates/docker-compose-template.yml", 'r') as stream:
        try:
            logger.debug("DEBUG: Docker Compose Template Successfully Loaded")
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            logger.error("ERROR: Failed To Load Docker Compose Template")
            print(exc)

def readConfigurationFile():
    logger.debug("DEBUG: Attempting to Load Configuration File")
    # Load in our configuration file
    with open("templates/config.yml", 'r') as stream:
        try:
            logger.debug("DEBUG: Configuration File Succesfully Loaded")
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            logger.error("ERROR: Failed To Load Configuration File")
            print(exc)

def getGlobalConfig():
    logger.debug("DEBUG: Extracting Global Configuration")
    config_file = readConfigurationFile()
    return config_file["global"]

def getEnvConfig(environment):
    logger.debug("DEBUG: Extracting Environment Configuration")
    logger.debug("DEBUG: Environment Extracting: %s", environment)
    config_file = readConfigurationFile()
    return config_file[environment]

def saveRancherComposeFile(rancher_compose_list):
    logger.debug("DEBUG: Attempting to Save New Rancher Compose File")
    # Writing out the yaml object to a file
    with open('./build/rancher-compose.yml', 'w') as new_yaml_file:
        try:
            logger.debug("DEBUG: Rancher Compose Template Successfully Saved")
            new_yaml_file.write(yaml.dump(rancher_compose_list, default_flow_style=False))
        except yaml.YAMLError as exc:
            logger.error("ERROR: Failed To Save Rancher Compose File")
            print(exc)

def saveDockerComposeFile(docker_compose_list):
    logger.debug("DEBUG: Attempting to Save New Docker Compose File")
    # Writing out the yaml object to a file
    with open('./build/docker-compose.yml', 'w') as new_yaml_file:
        try:
            logger.debug("DEBUG: Docker Compose Template Successfully Saved")
            new_yaml_file.write(yaml.dump(docker_compose_list, default_flow_style=False))
        except yaml.YAMLError as exc:
            logger.error("ERROR: Failed To Save Docker Compose File")
            print(exc)
