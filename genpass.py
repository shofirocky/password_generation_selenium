"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Chrome()
driver.get("https://genpass.lovable.app/")
time.sleep(2)

# locate the "Generate" button by its text and click it
#generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
#generate_button.click()
#password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
#print(len(password.text))

#print("Password generated! :", password.text)


# wait 10 seconds so you can see result
#time.sleep(5)

slider = driver.find_element(By.XPATH,"//span[@role='slider']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
print(len(password.text))


"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Chrome()
driver.get("https://genpass.lovable.app/")
time.sleep(5)

# locate the "Generate" button by its text and click it
#generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
#generate_button.click()
#password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
#print(len(password.text))

#print("Password generated! :", password.text)


# wait 10 seconds so you can see result
#time.sleep(5)
"""
slider = driver.find_element(By.XPATH,"//span[@role='slider']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(150, 0).release().perform()
generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
print(len(password.text))
print("Password generated! :", password.text)
"""

"""
#upercheck= driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-blue-600 p-4']/div[1]")
generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
print(password.text)

has_upper = any(ch.isupper() for ch in password.text)
has_lower = any(ch.islower() for ch in password.text)
has_digit = any(ch.isdigit() for ch in password.text)
if has_upper:
    print("matched:", password.text)

elif has_upper and has_digit:
    print ("2nd matched:", password.text)

elif has_lower and has_digit:
    print("3rd matched:", password.text)

else:
    print("not matched")




#if upercheck.is_selected():
    #upercheck.click()
time.sleep(2)

"""
"""
toggle= driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-blue-600 p-4']/div[1]")
status=toggle.get_attribute(data-status)
if "active" not in status:   # depends on site’s CSS class
    toggle.click()
    print("clicked")

"""
"""
toggle = driver.find_element(By.XPATH, "//button[@role='switch' and @aria-checked]")

state = toggle.get_attribute("aria-checked")  # "true" or "false"

if state == "false":   # If on
    toggle.click()
generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
time.sleep(2)
"""

"""
toggle1 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[1]")
toggle2 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[2]")
toggle3 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[3]")

state1 = toggle1.get_attribute("aria-checked")  # "true" or "false"
state2 = toggle2.get_attribute("aria-checked")
state3 = toggle3.get_attribute("aria-checked")

if state1 == "true":   # If on
    toggle1.click()
if state2 == "true":
    toggle2.click()
if state3 == "false":
    toggle3.click()

generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
time.sleep(2)

password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
has_upper = any(ch.isupper() for ch in password.text)
has_lower = any(ch.islower() for ch in password.text)
has_digit = any(ch.isdigit() for ch in password.text)
if has_upper:
    print("matched:", password.text)

elif has_upper and has_digit:
    print ("2nd matched:", password.text)

elif has_lower and has_digit:
    print("3rd matched:", password.text)

elif has_digit:
    print("Only digit:", password.text)

else:

    print("not matched")

time.sleep(2)
"""
#Print method (without assert)

toggle1 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[1]")
toggle2 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[2]")
toggle3 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[3]")

state1 = toggle1.get_attribute("aria-checked")  # "true" or "false"
state2 = toggle2.get_attribute("aria-checked")
state3 = toggle3.get_attribute("aria-checked")

if state1 == "true":   # If on
    toggle1.click()
if state2 == "true":
    toggle2.click()
if state3 == "false":
    toggle3.click()

generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
time.sleep(2)

password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
has_upper = any(ch.isupper() for ch in password.text)
has_lower = any(ch.islower() for ch in password.text)
has_digit = any(ch.isdigit() for ch in password.text)
if has_upper & has_lower & has_digit:
    print("perfect:", password.text)
elif has_upper & has_lower:
    print("normal:", password.text)
else:
    print("low quality:", password.text)

time.sleep(2)

"""



#With assert

toggle1 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[1]")
toggle2 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[2]")
toggle3 = driver.find_element(By.XPATH, "(//button[@role='switch' and @aria-checked])[3]")

state1 = toggle1.get_attribute("aria-checked")  # "true" or "false"
state2 = toggle2.get_attribute("aria-checked")
state3 = toggle3.get_attribute("aria-checked")

if state1 == "true":   # If on
    toggle1.click()
if state2 == "true":
    toggle2.click()
if state3 == "false":
    toggle3.click()

generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate')]")
generate_button.click()
time.sleep(2)

password = driver.find_element(By.XPATH, "//code[@class='font-mono text-xl text-white flex-1 overflow-x-auto']")
has_upper = any(ch.isupper() for ch in password.text)
has_lower = any(ch.islower() for ch in password.text)
has_digit = any(ch.isdigit() for ch in password.text)
if has_upper and has_lower and has_digit:
    assert True, f"✅ Perfect password: {password.text}"
elif has_upper and has_lower:
    assert True, f"⚠️ Normal password (missing digit): {password.text}"
else:
    assert False, f"❌ Low quality password: {password.text}"

time.sleep(2)

"""








