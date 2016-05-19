# ------------------------------------------------------------------------------
# RANCHER_COMPOSE Module
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This module uses a local copy of rancher compose to push to the remote
# Rancher server using the url and keys passed into the CLI
#
import sys
from subprocess import call
import logging

logger = logging.getLogger('Rancher Deployment')

base_command = []
module = {'ENV_EXISTS': False}

def setRancherVars(RANCHER_URL, RANCHER_ACCESS_KEY, RANCHER_SECRET_KEY, PROJECT_NAME):
    RANCHER_URL = RANCHER_URL
    RANCHER_ACCESS_KEY = RANCHER_ACCESS_KEY
    RANCHER_SECRET_KEY = RANCHER_SECRET_KEY
    base_command.extend(["rancher-compose", "--url", RANCHER_URL, "--access-key", RANCHER_ACCESS_KEY, "--secret-key", RANCHER_SECRET_KEY, "-f", "./build/docker-compose.yml", "-p", PROJECT_NAME, "-r", "./build/rancher-compose.yml"])

def checkForExistingEnvironment(cattle_client, PROJECT_NAME):
    logger.debug("DEBUG: Searching Environments For PROJECT_NAME: %s", PROJECT_NAME)
    client_envs = cattle_client.list_environment()
    logger.debug("DEBUG: Total Environments Retrieved from Rancher: %s", len(client_envs.data))
    for environment in client_envs.data:
        logger.debug("DEBUG: Comparing Env: %s", environment.name)
        if environment.name == PROJECT_NAME:
            logger.debug("DEBUG: ENVIRONMENT MATCH FOUND")
            module['ENV_EXISTS'] = True;

def pushToRancher():
    up_command = list(base_command)
    up_command.extend(["up", "-d"])
    # Here if the environment exists, we want to add the update flags to the end of our base command
    if module['ENV_EXISTS']:
        up_command.extend(["--force-upgrade","--confirm-upgrade", "--pull"]);
    logger.debug("DEBUG: Running Rancher Compose:")
    logger.debug("DEBUG: Command: %s", up_command)
    try:
        call(up_command)
    except OSError as e:
        logger.error("ERROR: Command rancher-compose could not be found.")
        logger.error("ERROR: Please ensure you have rancher-compose installed. This is a dependancy for matador-deploy")
        logger.info("INFO: See the documentation at https://github.com/seedtech/matador-deploy on how to install rancher-compose")
        logger.info("INFO: Alternatively, go directly to the rancher-compose repo at https://github.com/rancher/rancher-compose")
        sys.exit(1)
