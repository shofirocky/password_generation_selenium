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









