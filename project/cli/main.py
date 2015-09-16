import os
import sys

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import logging

from $PROJECT$ import set_logging
from $PROJECT$.constants import __VERSION__, __PROJECT__, __DESCRIPTION__
from $PROJECT$.utils import Utils

logger = logging.getLogger(__name__)


def cli_run(args):
    print("Running app %s in version %s.\n You said %s" % (__PROJECT__, __VERSION__, args.VERB))

class CLI():

    def __init__(self):
        self.parser = ArgumentParser(
            prog=__PROJECT__,
            description=__DESCRIPTION__,
            formatter_class=RawDescriptionHelpFormatter)

    def set_arguments(self):

        self.parser.add_argument(
            "-V",
            "--version",
            action='version',
            version='%s %s' % (__PROJECT__, __VERSION__),
            help="show the version and exit.")
        # TODO refactor program name and version to some globals

        self.parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            default=False,
            action="store_true",
            help="Verbose output mode.")

        self.parser.add_argument(
            "-q",
            "--quiet",
            dest="quiet",
            default=False,
            action="store_true",
            help="Quiet output mode.")

        self.parser.add_argument(
            "--dry-run",
            dest="dryrun",
            default=False,
            action="store_true",
            help=("Don't change any data, just print the steps."))

        subparsers = self.parser.add_subparsers()

        parser_verb = subparsers.add_parser("verb")
        parser_verb.add_argument(
            "--arg",
            dest="arg",
            help="Some argument..")

        parser_verb.add_argument(
            "VERB",
            help="Some VERB to do some stuff")

        parser_verb.set_defaults(func=cli_run)

    def run(self):
        self.set_arguments()
        args = self.parser.parse_args()
        if args.verbose:
            set_logging(level=logging.DEBUG)
        elif args.quiet:
            set_logging(level=logging.WARNING)
        else:
            set_logging(level=logging.INFO)

        try:
            args.func(args)
        except AttributeError:
            if hasattr(args, 'func'):
                raise
            else:
                self.parser.print_help()
        except Exception as ex:
            if args.verbose:
                raise
            else:
                logger.error("Exception caught: %s", repr(ex))
                logger.error(
                    "Run the command again with -v option to get more information.")

def main():
    cli = CLI()
    cli.run()

if __name__ == '__main__':
    main()
