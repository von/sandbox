#!/usr/bin/env python
# encoding: utf-8
"""Demo mock

Kudos: http://www.toptal.com/python/an-introduction-to-mocking-in-python

For pre-3.3 python, you need to install mock:
    pip install mock
"""
import mock

from mymockdemo import rm

import unittest


class RmTestCase(unittest.TestCase):

    # This causes 'os' and 'os.path' respectively to be mocked
    # for the following method
    @mock.patch('mymockdemo.os.path')
    @mock.patch('mymockdemo.os')
    def test_rm(self, mock_os, mock_path):
        """Make sure rm() calls os.remove() as expected."""

        # Set up the mock return for isfile()
        mock_path.isfile.return_value = True

        # Do the test
        rm("any path")

        # And make sure it had the desired interactions with
        # the system calls.

        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

    @mock.patch('mymockdemo.os.path')
    @mock.patch('mymockdemo.os')
    def test_no_rm(self, mock_os, mock_path):
        """Make sure we don't try to remove nonexistent files"""

        # Set up the mock return for isfile()
        mock_path.isfile.return_value = False

        # Do the test
        rm("any path")

        # And make sure it had the desired interactions with
        # the system calls.

        # os.remove() should not have been called
        self.assertFalse(mock_os.remove.called,
                         "Failed to not remove the file if not present.")


if __name__ == '__main__':
        unittest.main()
