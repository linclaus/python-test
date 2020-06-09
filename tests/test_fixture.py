# -*- encoding: utf-8 -*-
from __future__ import print_function
import pytest


@pytest.fixture(scope='module')
def resource_a_setup(request):
    print('\nresources_a_setup()')

    def resource_a_teardown():
        print('\nresources_a_teardown()')

    request.addfinalizer(resource_a_teardown)


def test_1(resource_a_setup):
    print('test_1()')


def test_2():
    print('\ntest_2()')


def test_3(resource_a_setup):
    print('\ntest_3()')


import pytest


# test_fixture1.py


@pytest.fixture()
def test1():
    print('\n开始执行function')


@pytest.mark.usefixtures('test1')
def test_a():
    print('---用例a执行---')


@pytest.mark.usefixtures('test1')
class TestCase:

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')
