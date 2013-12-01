#!/usr/local/bin/python3.3
# encoding: utf-8
'''
openpt.app -- OpenPT main script

OpenPT is a easy to use open source poker tracker.

@author:     Marcus Bitzl

@license:    Apache License
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from openpt.sites import start_import
from openpt.gui import start_gui

__all__ = []
__version__ = 0.1
__date__ = '2013-11-29'
__updated__ = '2013-11-29'

DEBUG = 1
TESTRUN = 0


def get_or_create_config():
    '''If a config exists, read it. If none exists, create a default one before.'''
    pass


def prepare_database():
    '''Check if there the database exists. If not, create one.'''


def create_session():
    '''Creates a new session. If there is no database create one.'''
    pass


def main(argv=None):  # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by Marcus Bitzl on %s.
  Copyright 2013 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)

        # Process arguments
        args = parser.parse_args()

        verbose = args.verbose

        if verbose > 0:
            print("Verbose mode on")

        config = get_or_create_config()
        prepare_database()
        session = create_session()
        start_import(config, session)
        start_gui(config, session)

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    sys.exit(main())
