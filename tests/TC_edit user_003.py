import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("button", name="").nth(1).click()
    page.locator("form i").first.click()
    page.get_by_role("option", name="Admin").click()
    page.locator("form i").nth(1).click()
    page.get_by_role("option", name="Disabled").click()
    page.get_by_role("textbox").nth(2).dblclick()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("bhahuss14")
    page.get_by_role("button", name="Cancel").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
