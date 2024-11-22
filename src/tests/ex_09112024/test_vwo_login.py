import pytest
import allure
from playwright.sync_api import Page, expect,sync_playwright
from pytest_playwright.pytest_playwright import browser


def test_vwo_login():

    #step-1
    browser = sync_playwright().start().chromium.launch(headless=False)

    page = browser.new_page()

    #step-2
    page.goto("https://app.vwo.com/")
    breakpoint()
    #step-3 for validation/assertions
    expect(page).to_have_title("Login - VWO")

    page.wait_for_timeout(300)
    print(f"\n\n=====waiting browser to close till 6 secs!=====\n")
    browser.close()

