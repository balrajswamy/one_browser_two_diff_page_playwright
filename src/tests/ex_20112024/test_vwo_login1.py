from playwright.sync_api import sync_playwright, expect
from pytest_playwright.pytest_playwright import browser, context
import pytest


@pytest.mark.smoke
def test_login_vwo_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://app.vwo.com/#/login")
        page.wait_for_timeout(300)
        print("\n--title=>", page.title())

        try:
            expect(page).to_have_title("Login - VWO")

        except:
            assert page.title() == "Login - VWO", "Page title does not match!"

        context.close()
        browser.close()