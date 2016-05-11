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

from subprocess import call

base_command = []

def setRancherVars(RANCHER_URL, RANCHER_ACCESS_KEY, RANCHER_SECRET_KEY):
    RANCHER_URL = RANCHER_URL
    RANCHER_ACCESS_KEY = RANCHER_ACCESS_KEY
    RANCHER_SECRET_KEY = RANCHER_SECRET_KEY
    base_command.extend(["./rancher/rancher-compose", "--url", RANCHER_URL, "--access-key", RANCHER_ACCESS_KEY, "--secret-key", RANCHER_SECRET_KEY, "-f", "./build/docker-compose.yml", "-p", "ProjectName", "-r", "./build/rancher-compose.yml"])

def pushToRancher():
    up_command = list(base_command)
    up_command.extend(["up", "-d"])
    call(up_command)
