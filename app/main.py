#!/usr/bin/env python

# Start Up Python Script

# print "Python Time Baby"

# Lets get the arguments from the command line to pass in the information we need
import sys

# print "\n".join(sys.argv)

# ##############################################################################
# HELP OPTIONS AND HOW TO USE PYTHON APPLICATION
# ------------------------------------------------------------------------------

# Our Option Types Defined Here
# --url shows the
# if len(sys.argv) == 1:
#     print "Rancher Deployment Script\n"
#     print "This script will assist you in updating your rancher environment."
#     print "All the following command line arguments are required to update rancher\n"
#     print "Usage: --url <http://example.com> --key <key> --secret <secret_key> --env [dev|staging|prod]"
#     print "    --url \t url to connect to your rancher server"
#     print "    --key \t username of api key to connect to rancher host"
#     print "    --secret \t password of api key to connect to rancher host"
#     print "    --env \t environment you wish to update"
#     sys.exit(0);
# else: # This needs to be extended to start actually doing stuff with the arg variables, checking if they exist etc etc
#     print "Starting Deployment Business"


# Lets try to read in a YML File into Python :)
import yaml


# ##############################################################################
# READING YAML FILES FROM FILES
# ------------------------------------------------------------------------------

# Load in out base rancher template
with open("templates/rancher-compose.yml", 'r') as stream:
    try:
        rancher_compose_file = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Load in our configuration file
with open("templates/config.yml", 'r') as stream:
    try:
        # print(yaml.load(stream))
        config_file = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


# First get the global config, this needs to be added regardless
global_config = config_file["global"]

# Then get the specific environment config from the file by adding
ENV_ARGUMENT = "prod"
env_config = config_file[ENV_ARGUMENT]


# ##############################################################################
# COMBINING CONFIG AND RANCHER COMPOSE FILES
# ------------------------------------------------------------------------------

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

# NOTE: There must be a better way to do this
def createOptionInService(service_array, option, config_options):
    option_type = type(env_config[service][option])
    if option_type is dict:
        default_value = {}
    if option_type is list:
        default_value = []
    if option_type is str:
        default_value = ""
    service_array.update({option: default_value})

def addOptionToService(service, option, config_options):
    option_type = type(config_options)
    if option_type is dict:
        for key in config_options:
            rancher_compose_file[service][option][key] = config_options[key]
    elif option_type is list:
        for value in config_options:
            rancher_compose_file[service][option].append(value)
    elif option_type is str:
        rancher_compose_file[service][option] = config_options


# CONFIG FILE STRUCTURE
# service
    # option
        # value

# Loop through each of the services being altered in the env_config
for service in env_config:
    if safeServiceLoad(rancher_compose_file, service):
        for option in env_config[service]: # Next, loop through each of the additional options defined in the
            # Here we need to see if the option exists in the actual rancher config
            if not optionExistsInService(rancher_compose_file[service], option):
                createOptionInService(rancher_compose_file[service], option, env_config[service][option])
            # Then add the option to the service in the rancher config
            addOptionToService(service, option, env_config[service][option])


print "Saving File To Disk"

# Writing out the yaml object to a file
with open('result.yml', 'w') as new_yaml_file:
    try:
        new_yaml_file.write(yaml.dump(rancher_compose_file, default_flow_style=False))
    except yaml.YAMLError as exc:
        print(exc)
