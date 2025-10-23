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
    page.get_by_label("Topbar Menu").get_by_text("User Management").click()
    page.get_by_text("Job").click()
    page.get_by_text("Organization").click()
    page.get_by_text("Qualifications").click()
    page.get_by_role("listitem").filter(has_text="Nationalities").click()
    page.get_by_role("link", name="Corporate Branding").click()
    page.locator("#app").click()
    page.get_by_text("Configuration").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
