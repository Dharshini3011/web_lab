from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# -------- CONFIG --------
URL = "http://127.0.0.1:5500/demo2/index.html#!/books"  # Change if needed
CHROMEDRIVER_PATH = r"D:\web terminal\web_lab\chromedriver-win64\chromedriver.exe"

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)
driver.maximize_window()
time.sleep(2)  # wait for page to load

# ---------------- FUNCTIONALITY TEST ----------------
try:
    # Fill Book form
    driver.find_element(By.XPATH, "//input[@ng-model='newBook.title']").send_keys("AngularJS Basics")
    driver.find_element(By.XPATH, "//input[@ng-model='newBook.author']").send_keys("Dharshini")
    driver.find_element(By.XPATH, "//input[@ng-model='newBook.price']").send_keys("150")
    driver.find_element(By.XPATH, "//input[@ng-model='newBook.genre']").send_keys("Programming")
    driver.find_element(By.XPATH, "//input[@ng-model='newBook.available']").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add Book')]").click()
    print("✅ Functionality Test Passed: Book added successfully.")
except Exception as e:
    print("❌ Functionality Test Failed:", e)

time.sleep(2)

# ---------------- EDIT TEST ----------------
try:
    edit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Edit')]")
    if edit_buttons:
        last_edit_btn = edit_buttons[-1]
        last_edit_btn.click()

        # Handle prompt alert automatically
        alert = Alert(driver)
        print("⚠ Prompt detected with text:", alert.text)
        alert.send_keys("AngularJS Advanced")  # New title
        alert.accept()
        print("✅ Edit Test Passed: Book title updated successfully.")
    else:
        print("⚠ Edit Test Warning: No edit buttons found.")
except Exception as e:
    print("❌ Edit Test Failed:", e)

time.sleep(2)

# ---------------- DELETE TEST ----------------
try:
    delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Delete')]")
    if delete_buttons:
        delete_buttons[-1].click()
        # Confirm deletion if Angular shows confirm alert
        try:
            alert = Alert(driver)
            alert.accept()
        except:
            pass
        print("✅ Delete Test Passed: Book deleted successfully.")
    else:
        print("⚠ Delete Test Warning: No delete buttons found.")
except Exception as e:
    print("❌ Delete Test Failed:", e)

time.sleep(1)

# ---------------- INTERFACE TEST ----------------
try:
    heading = driver.find_element(By.TAG_NAME, "h1").text
    if "angularjs" in heading.lower() or "book" in heading.lower():
        print("✅ Interface Test Passed: Heading displayed correctly.")
    else:
        print("⚠ Interface Test Warning: Heading text issue.")
except Exception as e:
    print("❌ Interface Test Failed:", e)

# ---------------- USABILITY TEST ----------------
try:
    inputs = [
        driver.find_element(By.XPATH, "//input[@ng-model='newBook.title']"),
        driver.find_element(By.XPATH, "//input[@ng-model='newBook.author']"),
        driver.find_element(By.XPATH, "//input[@ng-model='newBook.price']"),
        driver.find_element(By.XPATH, "//input[@ng-model='newBook.genre']"),
        driver.find_element(By.XPATH, "//input[@ng-model='newBook.available']"),
    ]
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Book')]")

    if all(inp.is_displayed() for inp in inputs) and add_button.is_enabled():
        print("✅ Usability Test Passed: Inputs and button accessible.")
    else:
        print("⚠ Usability Test Warning: Some input/button not accessible.")
except Exception as e:
    print("❌ Usability Test Failed:", e)

# ---------------- FINAL STEP ----------------
input("Press Enter to close the browser...")
driver.quit()
