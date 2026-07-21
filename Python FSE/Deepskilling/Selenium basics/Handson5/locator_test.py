from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")


try:
    
    input_by_id = driver.find_element(By.ID, "user-message")
    input_by_name = driver.find_element(By.NAME, "message")
    input_by_class = driver.find_element(By.CLASS_NAME, "form-control")
    input_by_tag = driver.find_elements(By.TAG_NAME, "input")[1] # Usually the second input
    input_by_xpath_abs = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div[1]/input")
    input_by_xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")
    print("All 6 locator strategies found the element successfully!")
except Exception as e:
    print("Locator Error:", e)

css1 = driver.find_element(By.CSS_SELECTOR, "#user-message")
css2 = driver.find_element(By.CSS_SELECTOR, "[name='message']")
css3 = driver.find_element(By.CSS_SELECTOR, "div > input")


driver.quit()