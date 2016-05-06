#! /usr/bin/env python

import ConfigParser
import os

credentials = "~/.artiste"

configs = ConfigParser.ConfigParser()
configs.read([credentials, os.path.expanduser(credentials)])

conf = {}
conf['token'] = configs.get('ssh', 'token')

def get_configs():
    return conf
