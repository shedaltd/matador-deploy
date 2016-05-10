# ------------------------------------------------------------------------------
# RANCHER_CONNECT Module
# ------------------------------------------------------------------------------
# Rancher Deployment Script - SEED DIGITAL (C) 2016
#
# Author: Timon C Sotiropoulos
# Contact: timon@seeddigital.co
# Seed Digital: http://seeddigital.co/
# Rancher: http://rancher.com/
#
# This module leveridges the cattle.py library to connect to rancher and
# handles the updating of our rancher projects
#

import imp
cattle = imp.load_source('cattle', './app/libs/cattle.py')

client = cattle.Client()
