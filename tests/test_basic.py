#!/usr/bin/env python3

import unittest

from .context import mempw  # noqa: F401


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()
