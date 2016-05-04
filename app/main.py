#!/usr/bin/env python

# Start Up Python Script

# print "Python Time Baby"

# Lets get the arguments from the command line to pass in the information we need
import sys

# print "\n".join(sys.argv)

# Our Option Types Defined Here
# --url shows the
if len(sys.argv) == 1:
    print "Rancher Deployment Script\n"
    print "This script will assist you in updating your rancher environment."
    print "All the following command line arguments are required to update rancher\n"
    print "Usage: --url <http://example.com> --key <key> --secret <secret_key> --env [dev|staging|prod]"
    print "    --url \t url to connect to your rancher server"
    print "    --key \t api key to connect to your rancher host"
    print "    --secret \t secret key to connect to your rancher host"
    print "    --env \t environment you wish to update"
    sys.exit(0);
else:
    print "Starting Deployment Business"


# # Lets print the current working directory
# import os
# print os.getcwd()
#
# # Lets try to read in a YML File into Python :)
# import yaml
#
# with open("templates/common.stage.yml", 'r') as stream:
#     try:
#         # print(yaml.load(stream))
#         yamlFile = yaml.load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)
#
# print "New Test"
# print yamlFile["web"]["environment"][0]
