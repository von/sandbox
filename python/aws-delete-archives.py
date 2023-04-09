#!/usr/bin/env python3
"""Given an inventory, delete all archives in an AWS vault.
Presumably in preparation for deleting the vault.

Kudos: https://gist.github.com/Remiii/507f500b5c4e801e4ddc

Assumes you have the AWS CLI installed and configured. See:
https://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-delete-archive-cli.html
"""

import argparse
import json
import subprocess
import sys


def make_argparser():
    """Return arparse.ArgumentParser instance"""
    parser = argparse.ArgumentParser(
        description=__doc__,  # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # To have --help print defaults with trade-off it changes
        # formatting, use: ArgumentDefaultsHelpFormatter
    )
    # Only allow one of debug/quiet mode
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-d", "--debug",
                                 action='store_true', default=False,
                                 help="Turn on debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_true", default=False,
                                 help="run quietly")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("accountid", metavar="account-id", help="account id")
    parser.add_argument("vaultname", metavar="vault-name", help="vault name")
    parser.add_argument("inventoryfile", metavar="path",
                        help="path to inventory file")
    return parser


def main(argv=None):
    parser = make_argparser()
    args = parser.parse_args(argv if argv else sys.argv[1:])

    with open(args.inventoryfile) as f:
        json_string = f.read()

    parsed_json = json.loads(json_string)
    archive_list = parsed_json['ArchiveList']
    num_archives = len(archive_list)
    if not args.quiet:
        print("Total number of archives: " + str(num_archives))

    for index, archive in enumerate(archive_list):
        if not args.quiet:
            print("Deleting archive (" + str(index+1) + "/" +
                  str(num_archives) + "): " + archive['ArchiveId'])
        # Use '=' for archive-id as it may start with a "-" which will
        # confuse the aws-cli.
        command = "aws glacier delete-archive" + \
            " --archive-id='" + archive['ArchiveId'] + "'" + \
            " --vault-name " + args.vaultname + \
            " --account-id " + args.accountid
        if args.debug:
            print(command)
        cp = subprocess.run(command, shell=True, check=True)
        if cp.returncode != 0:
            return cp.returncode
    return(0)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
