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

def readComposeFile():
    # Load in out base rancher template
    with open("templates/rancher-compose.yml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def readDockerComposeFile():
    # Load in out base rancher template
    with open("templates/default-docker-compose.yml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def readConfigurationFile():
    # Load in our configuration file
    with open("templates/config.yml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def getGlobalConfig():
    config_file = readConfigurationFile()
    return config_file["global"]

def getEnvConfig(environment):
    config_file = readConfigurationFile()
    return config_file[environment]

def saveRancherComposeFile(rancher_compose_file):
    # Writing out the yaml object to a file
    with open('result.yml', 'w') as new_yaml_file:
        try:
            new_yaml_file.write(yaml.dump(rancher_compose_file, default_flow_style=False))
        except yaml.YAMLError as exc:
            print(exc)
