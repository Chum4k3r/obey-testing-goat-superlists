# -*- coding: utf-8 -*-

from pytest import fixture
from selenium import webdriver
from django.test import Client


@fixture(scope='function')
def browser() -> webdriver.Firefox:
    """Returns a Firefox webdriver instance."""
    options = webdriver.FirefoxOptions()
    options.binary = '/usr/bin/firefox'
    options.add_argument('--headless')
    _browser = webdriver.Firefox(options=options)
    yield _browser
    _browser.quit()


@fixture(scope='function')
def client() -> Client:
    _client = Client()
    return _client
