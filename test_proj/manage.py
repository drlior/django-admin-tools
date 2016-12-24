#!/usr/bin/env python

import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)
from django.core.management import execute_from_command_line


os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

execute_from_command_line(sys.argv)
