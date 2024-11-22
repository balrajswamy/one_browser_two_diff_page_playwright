import pytest
import allure
from playwright.sync_api import sync_playwright, expect, Page
from pytest_playwright.pytest_playwright import browser, context


def test_login_two_browsers():
    browser = sync_playwright().start().chromium.launch(headless=False,slow_mo=2000)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://app.vwo.com")
    breakpoint()

    expect(page1).to_have_title("Login - VWO")
    page1.wait_for_timeout(300)
    page2.goto("https://www.bing.com")
    breakpoint()

    page2.wait_for_timeout(600)
    expect(page2).to_have_title("Bing")

    context2.close()
    context1.close()
    browser.close()

