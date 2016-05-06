#! /usr/bin/env python

import config
from mutagen.flac import FLAC


class Artiste(object):
    conf = config.get_configs()
    flac_file = None

    def __init__(self, path):
        self.flac_file = FLAC(path)

    def has_pic(self):
        return len(self.flac_file.pictures) > 0
