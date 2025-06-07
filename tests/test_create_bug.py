import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')  # <- important for CI
    options.add_argument('--no-sandbox')  # <- for Linux containers
    options.add_argument('--disable-dev-shm-usage')  # <- for memory usage
    options.add_argument('--disable-gpu')  # optional
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_create_and_assign_bug(driver):
    wait = WebDriverWait(driver, 15)

    # Step 1: Open MantisBT login page
    driver.get("http://localhost:8080/mantisbt/login_page.php")

    # Login username
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys("administrator")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Login password
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys("Admin@1234")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    wait.until(EC.title_contains("My View"))

    # Step 2: Go to Report Issue page
    driver.get("http://localhost:8080/mantisbt/bug_report_page.php")

    # Step 3: Fill in bug form
    category_select_elem = wait.until(EC.presence_of_element_located((By.NAME, "category_id")))
    Select(category_select_elem).select_by_visible_text("[All Projects] General")
    Select(driver.find_element(By.NAME, "reproducibility")).select_by_visible_text("always")
    Select(driver.find_element(By.NAME, "severity")).select_by_visible_text("minor")

    driver.find_element(By.NAME, "summary").send_keys("Automation bug summary test")
    driver.find_element(By.NAME, "description").send_keys("Steps to reproduce the bug described in detail.")

    # Step 4: Submit the bug
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit Issue']").click()

    # Step 5: Verify bug creation by checking URL and bug id
    wait.until(EC.url_contains("view.php?id="))
    bug_id = driver.current_url.split("id=")[-1]
    bug_id_formatted = bug_id.zfill(7)
    wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{bug_id_formatted}')]")))

    # Step 6: Assign to administrator
    driver.get(f"http://localhost:8080/mantisbt/view.php?id={bug_id}")
    assign_to_select = wait.until(EC.presence_of_element_located((By.NAME, "handler_id")))
    Select(assign_to_select).select_by_visible_text("administrator")
    driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value, 'Assign To')]").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'administrator')]")))

    # Step 7: Change status to resolved
    status_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "new_status")))
    Select(status_dropdown).select_by_visible_text("resolved")

    # Click the Close button on the same page after selecting resolved
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and contains(@value, 'Close')]")))
    close_button.click()

    # Wait until navigated to bug_change_status_page.php
    wait.until(EC.url_contains("bug_change_status_page.php"))

    # On bug_change_status_page.php, click Close Issue button
    close_issue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and contains(@value, 'Close Issue')]")))
    close_issue_button.click()

    # Verify redirected back to view page with updated status (optional)
    wait.until(EC.url_contains("view.php?id="))
    # Add assertion to verify "resolved" status if you want:
    # status_text = driver.find_element(By.CSS_SELECTOR, "td.status-category").text
    # assert "resolved" in status_text.lower()



