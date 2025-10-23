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
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    page.get_by_role("row", name=" sruthy ESS sruthy krishna").locator("span i").click()
    page.get_by_role("row", name=" testbusters_ess_enabled ESS").locator("span i").click()
    page.get_by_role("button", name=" Delete Selected").click()
    page.get_by_role("button", name=" Yes, Delete").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
