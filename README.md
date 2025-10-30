# 🧪 OrangeHRM Automation Testing (Playwright + Python)

This project automates the functional and UI testing of the **OrangeHRM web application** using **Playwright with Python**.  
It helps ensure that key modules like **Login**, **Admin**, and **User Management** work as expected.

---

## ⚙️ Project Setup Steps

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rinkalvara/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests

python -m venv venv
venv\Scripts\activate       # For Windows
# or
source venv/bin/activate    # For Mac/Linux

pip install -r requirements.txt

playwright install

pytest

pytest --html=reports/report.html

npx playwright show-report

npx playwright show-report

Playwright Version: 1.47.0

Rinkal Vara
GitHub Profile