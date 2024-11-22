import pytest
from playwright.sync_api import sync_playwright
import allure


@allure.feature("VWO Login Page")
@allure.story("Validate Login Page Title")
@pytest.mark.playwright
def test_vwo_login_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the URL
        page.goto("https://app.vwo.com/")

        # Capture the title
        actual_title = page.title()

        # Validate the page title
        expected_title = "Login - VWO"
        with allure.step("Check if the page title is as expected"):
            assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"

        # Cleanup

        browser.close()
