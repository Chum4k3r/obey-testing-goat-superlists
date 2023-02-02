# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def _check_for_row_in_list_table(browser: webdriver.Firefox, row_text: str):
    table = browser.find_element(by=By.ID, value='id_list_table')
    rows = table.find_elements(by=By.TAG_NAME, value='tr')
    assert row_text in [row.text for row in rows], f"Task {row_text} is not in the list."


def test_can_start_a_list_and_retrieve_it_later(browser: webdriver.Firefox) -> None:

    # Lionel heard of a new todo list website
    # and accessed it via his browser.
    browser.get('http://localhost:8000')

    # The new todo list website has a cool title that he notices.
    assert 'From Do To Done' in browser.title, f"Browser title is {browser.title}"
    header_text = browser.find_element(by=By.TAG_NAME, value='h1').text
    assert 'Your To-Do tasks' in header_text, f"Header text is {header_text}"

    # He is invited to enter a new task right away
    inputbox = browser.find_element(by=By.ID, value='id_new_item')
    assert inputbox.get_attribute('placeholder') == 'Enter a new task'

    # He enters "Check my email box" into a text box
    inputbox.send_keys('Check my email box')

    # And presses enter
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1.)

    # Then, the list updates and shows his task as '1: Check my email box'
    _check_for_row_in_list_table(browser, '1: Check my email box')

    # There is still a text box inviting him to enter a new task
    # Lionel then types "Remove spam emails" and hits enter again
    inputbox = browser.find_element(by=By.ID, value='id_new_item')
    inputbox.send_keys('Remove spam emails')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1.)

    # The page updates again and shows both his tasks.
    _check_for_row_in_list_table(browser, '1: Check my email box')
    _check_for_row_in_list_table(browser, '2: Remove spam emails')

    # Lionel wonders if the task will be there if he exits then come back again
    # The website generated a unique URL for him

    # He visits the URL and is satisfied to see that his tasks are still there.

    assert False, "TEST UNDER DEVELOPMENT: Finish building the test!"
