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
    page.get_by_role("button", name=" Add").click()
    page.get_by_text("-- Select --").first.click()
    page.get_by_role("option", name="Admin").click()
    page.get_by_role("textbox", name="Type for hints...").click()
    page.get_by_role("textbox", name="Type for hints...").fill("ousse")
    page.get_by_text("Oussema akhil user").click()
    page.locator("form i").nth(1).click()
    page.get_by_role("option", name="Enabled").click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("akhil_1")
    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("Akhil@123")
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).fill("Akhil@123")
    page.get_by_role("button", name="Save").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
