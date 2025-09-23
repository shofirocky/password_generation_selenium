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