from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_tab = page.locator("//a[@href='/web/index.php/admin/viewAdminModule']")
        self.add_button = page.locator("//button[text()='Add']")
        self.username_field = page.locator("input[name='username']")
        self.user_role_dropdown = page.locator("select[name='userRole']")
        self.status_dropdown = page.locator("select[name='status']")
        self.password_field = page.locator("input[name='password']")
        self.confirm_password_field = page.locator("input[name='confirmPassword']")
        self.save_button = page.locator("button[type='submit']")
        self.search_username = page.locator("input[name='searchSystemUser[userName]']")
        self.search_button = page.locator("button[text()='Search']")
        self.edit_button = page.locator("//button[contains(@class,'oxd-icon-button')]")
        self.delete_button = page.locator("//button[contains(@class,'oxd-button--danger')]")
        self.confirm_delete_button = page.locator("//button[text()='Yes, Delete']")

    def navigate_admin_tab(self):
        self.admin_tab.click()

    def add_user(self, username, password, role="Admin", status="Enabled"):
        self.add_button.click()
        self.username_field.fill(username)
        self.user_role_dropdown.select_option(label=role)
        self.status_dropdown.select_option(label=status)
        self.password_field.fill(password)
        self.confirm_password_field.fill(password)
        self.save_button.click()

    def search_user(self, username):
        self.search_username.fill(username)
        self.search_button.click()

    def edit_user(self, username, new_username):
        self.search_user(username)
        self.edit_button.click()
        self.username_field.fill(new_username)
        self.save_button.click()

    def delete_user(self, username):
        self.search_user(username)
        self.delete_button.click()
        self.confirm_delete_button.click()
