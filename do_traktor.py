#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from traktor import run
from argparse import ArgumentParser


DEFAULT_SETTINGS_FILE_PATH = '/etc/traktor.yml'
DEFAULT_LIBRARY_FILE_PATH = '/var/lib/traktor/traktor.db'

parser = ArgumentParser()

parser.add_argument('-s', '--settings', help='Path to settings file')
parser.add_argument('-l', '--library', help='Path to library file')

args = parser.parse_args()

run(args.settings or DEFAULT_SETTINGS_FILE_PATH,
    args.library or DEFAULT_LIBRARY_FILE_PATH
)
