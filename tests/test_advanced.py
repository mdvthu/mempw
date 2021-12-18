#!/usr/bin/env python3

import unittest

from .context import mempw  # noqa: F401


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    def test_thoughts(self):
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()
