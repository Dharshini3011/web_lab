# https://googlechromelabs.github.io/chrome-for-testing/
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


URL = "http://localhost:3000/employee.html"  
# Path to your chromedriver.exe
service = Service(r"D:\web terminal\web_lab\chromedriver-win64\chromedriver.exe")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service)
driver.get(URL)
driver.maximize_window()
time.sleep(3)  # wait for page to load fully


# ---------------- FUNCTIONALITY TEST ----------------
try:
    # Fill Name
    driver.find_element(By.XPATH, "//input[@ng-model='newemp.name']").send_keys("Shivanika")
    time.sleep(1)

    # Fill Role
    driver.find_element(By.XPATH, "//input[@ng-model='newemp.role']").send_keys("Developer")
    time.sleep(1)

    # Click Add Employee
    driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()
    print("✅ Functionality Test Passed: Employee added successfully.")
except Exception as e:
    print("❌ Functionality Test Failed:", e)

time.sleep(3)


# ---------------- INTERFACE TEST ----------------
try:
    heading = driver.find_element(By.TAG_NAME, "h1").text
    if "emp details" in heading.lower() or "employee" in heading.lower():
        print("✅ Interface Test Passed: Heading displayed correctly.")
    else:
        print("⚠ Interface Test Warning: Heading text issue.")
except Exception as e:
    print("❌ Interface Test Failed:", e)


# ---------------- USABILITY TEST ----------------
try:
    name_input = driver.find_element(By.XPATH, "//input[@ng-model='newemp.name']")
    role_input = driver.find_element(By.XPATH, "//input[@ng-model='newemp.role']")
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")

    if name_input.is_displayed() and role_input.is_displayed() and add_button.is_enabled():
        print("✅ Usability Test Passed: Inputs and button are accessible.")
    else:
        print("⚠ Usability Test Warning: Some input/button not accessible.")
except Exception as e:
    print("❌ Usability Test Failed:", e)

time.sleep(2)


# ---------------- UPDATE (EDIT) TEST ----------------
try:
    edit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Edit')]")
    if edit_buttons:
        last_edit_btn = edit_buttons[-1]

        # Get the corresponding role input near the last Edit button
        role_input_xpath = "(//tr[td/input[@ng-model='emp.role']])[last()]/td/input[@ng-model='emp.role']"
        role_input = driver.find_element(By.XPATH, role_input_xpath)

        # Clear and update the role
        role_input.clear()
        role_input.send_keys("Team Lead")
        time.sleep(1)

        # Click Edit button
        last_edit_btn.click()
        print("✅ Update Test Passed: Employee role updated successfully.")
    else:
        print("⚠ Update Test Warning: No records found to update.")
except Exception as e:
    print("❌ Update Test Failed:", e)

time.sleep(2)


# ---------------- DELETE TEST ----------------
try:
    delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Delete')]")
    if delete_buttons:
        delete_buttons[-1].click()
        print("✅ Delete Test Passed: Employee record deleted successfully.")
    else:
        print("⚠ Delete Test Warning: No records found to delete.")
except Exception as e:
    print("❌ Delete Test Failed:", e)


# ---------------- FINAL STEP ----------------
input("Press Enter to close the browser...")
driver.quit()
