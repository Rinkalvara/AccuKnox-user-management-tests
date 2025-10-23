import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("listitem").filter(has_text="Configuration").locator("i").click()
    page.get_by_role("menuitem", name="Email Configuration").click()
    page.get_by_label("Topbar Menu").get_by_text("Configuration").click()
    page.get_by_role("menuitem", name="Email Subscriptions").click()
    page.get_by_label("Topbar Menu").get_by_text("Configuration").click()
    page.get_by_role("menuitem", name="Localization").click()
    page.get_by_role("listitem").filter(has_text="Configuration").click()
    page.get_by_role("menuitem", name="Language Packages").click()
    page.get_by_role("listitem").filter(has_text="Configuration").locator("i").click()
    page.get_by_role("menuitem", name="Modules").click()
    page.get_by_role("listitem").filter(has_text="Configuration").locator("i").click()
    page.get_by_role("menuitem", name="Social Media Authentication").click()
    page.get_by_role("listitem").filter(has_text="Configuration").locator("i").click()
    page.get_by_role("menuitem", name="Register OAuth Client").click()
    page.get_by_role("listitem").filter(has_text="Configuration").click()
    page.get_by_role("menuitem", name="LDAP Configuration").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
