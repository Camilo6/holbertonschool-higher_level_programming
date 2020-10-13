#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest
from io import StringIO
import sys
import contextlib
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ testing pep8 style and __document__ """

    def test_pep8_model(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
