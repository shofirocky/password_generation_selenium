
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# % Function to test password generation based on toggle states %
def run_test_case(driver, mode):
    print(f"\n==============================")
    print(f"🔹 Running {mode}")
    print(f"==============================")

    # Locate toggles
    toggle1 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[1]")
    toggle2 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[2]")
    toggle3 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[3]")

    # % Get current states %
    state1 = toggle1.get_attribute("aria-checked")
    state2 = toggle2.get_attribute("aria-checked")
    state3 = toggle3.get_attribute("aria-checked")

    print(f"Initial states → Toggle1={state1}, Toggle2={state2}, Toggle3={state3}")

    # % Handle toggles per mode %
    if mode == "case1":
        if state1 == "false": toggle1.click()
        if state2 == "false": toggle2.click()
        if state3 == "true": toggle3.click()

    elif mode == "case2":
        if state1 == "true": toggle1.click()
        if state2 == "true": toggle2.click()
        if state3 == "false": toggle3.click()

    print(f"✅ Toggle setup done for {mode}")

    # % Click generate %
    generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
    generate_button.click()
    time.sleep(2)

    # % Get password %
    password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']").text
    print(f"Generated Password ({mode}): {password}")

    # Analyze password
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    # % Assertions for each mode %
    """
    if mode == "case1":
        if has_upper and has_lower and has_digit:
            print(f"✅ Case1: Perfect password → {password}")
        elif has_upper and has_lower:
            print(f"⚠️ Case1: Normal password (missing digit) → {password}")
        else:
            raise AssertionError(f"❌ Case1: Weak password → {password}")
    """
    if mode == "case1":
        if has_upper and has_lower:
            print(f"✅ Case1: Perfect password → {password}")
        elif has_upper and has_digit :
            raise AssertionError(f"❌ Case1: Not working → {password}")

    elif mode == "case2":
        if has_digit:
            print(f"✅ Case2: Strong password (upper + digit) → {password}")
        else:
            raise AssertionError(f"❌ Case2: Not working → {password}")

    time.sleep(1)


# % Main flow %
driver = webdriver.Chrome()
driver.get("https://genpass.lovable.app/")
driver.maximize_window()
time.sleep(2)

# % Run both test cases one by one %
run_test_case(driver, "case1")
time.sleep(2)
run_test_case(driver, "case2")

print("\n🎉 All test cases executed successfully!")
driver.quit()






