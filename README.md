# 🐞 MantisBT Bug Automation with Selenium

Automated the bug creation, assignment, and status update workflow in the MantisBT bug tracking system using Selenium WebDriver, Pytest, and Allure Reporting.

---

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Allure Report](https://img.shields.io/badge/Allure-ED2B88?style=for-the-badge&logo=allure&logoColor=white)


## 🚀 Project Features

- ✅ Login to MantisBT
- ✅ Navigate to "Report Issue"
- ✅ Fill and submit bug form
- ✅ Assign bug to an administrator
- ✅ Change bug status to "resolved"
- ✅ Capture and validate bug ID

---

## 🛠️ Tech Stack

- **Language:** python
- **Automation Tool:** Selenium WebDriver
- **Test Runner:** Pytest
- **Reporting:** Allure
- **Browser:** Chrome
- **Test Framework:** Page Object Model (POM)

---

## 📸 Allure Test Report Screenshot

![allure_report](https://github.com/user-attachments/assets/466ef382-e71e-441a-a479-19d1bec9f890)


---

## 🧪 Run the Tests

### 1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Run the test and generate report data
pytest tests/test_create_bug.py --alluredir=allure-results

3️⃣ Generate the Allure report
allure generate allure-results --clean -o allure-report

4️⃣ Open the report manually
Go to the allure-report folder and open index.html in your browser.

📁 Project Structure

mantisbt-automation/
│
├── drivers/               # WebDriver executables
├── pages/                 # Page Object files
├── tests/                 # Pytest test cases
├── utils/                 # Utility functions (if any)
├── allure-results/        # Raw results for Allure (auto-created)
├── allure-report/         # Generated HTML report (auto-created)
├── report.png             # Screenshot of Allure report
├── requirements.txt       # Python dependencies
├── conftest.py            # Pytest fixtures
└── README.md              # Project documentation


🙋‍♀️ Author
KavyaSri Singam
