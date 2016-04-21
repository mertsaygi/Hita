#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    if not os.geteuid() == 0:
        sys.exit('Script must be run as root')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hita.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
