#! /usr/bin/env python

import ConfigParser
import os

credentials = "~/.artiste-creds"

configs = ConfigParser.ConfigParser()
configs.read([credentials, os.path.expanduser(credentials)])

conf = {}
conf['token'] = configs.get('discogs', 'token')
conf['agent'] = configs.get('discogs', 'agent')

def get_configs():
    return conf
