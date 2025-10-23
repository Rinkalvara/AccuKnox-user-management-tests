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
    page.get_by_role("row", name=" akhilppp ESS Akhil o").locator("span i").click()
    page.get_by_role("row", name=" Doki123 ESS Chandrika H").locator("span i").click()
    page.get_by_role("row", name=" Doki123 ESS Chandrika H").locator("span i").click()
    page.get_by_role("row", name=" Doki123 ESS Chandrika H").locator("span i").click()
    page.get_by_role("row", name=" emp_78259_330_1761235693059").locator("span i").click()
    page.get_by_role("row", name=" FMLName ESS Qwerty LName").locator("span i").click()
    page.get_by_role("row", name=" Halle_Romaguera-Collins ESS").locator("span i").click()
    page.get_by_role("row", name=" Jaylin.Rutherford-Hermann").locator("span i").click()
    page.get_by_role("row", name=" Jeanne60 ESS Scottie").locator("label").click()
    page.get_by_role("row", name=" kunkan ESS Sreelakshmi").locator("span i").click()
    page.get_by_role("row", name=" kunkan ESS Sreelakshmi").locator("span i").click()
    page.get_by_role("row", name=" laletyar ESS Laletya Vulchi").locator("span i").click()
    page.get_by_role("row", name=" kunkan ESS Sreelakshmi").locator("span i").click()
    page.get_by_role("row", name=" laletyas ESS Laletya Vulchi").locator("span i").click()
    page.get_by_role("row", name=" Leilani_Streich81 ESS Oran").locator("span i").click()
    page.get_by_role("row", name=" Mastan_111 Admin Peter").locator("span i").click()
    page.get_by_role("row", name=" Seth.Huel76 ESS Dalton").locator("span i").click()
    page.get_by_role("row", name=" sysuser_78259_330 ESS").locator("span i").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
