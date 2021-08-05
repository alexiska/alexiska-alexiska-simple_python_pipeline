from my_awesome_module import bin_number_to_tens
import pytest

"""
To run:

0. Make sure pytest is installed, either globally or in a virtualenv, and that virtualenv is activated
1. cd into this folder
2. Run: python -m pytest test_my_awesome_module.py

"""

def test_this_will_always_crash():
    # Assert:
    assert False