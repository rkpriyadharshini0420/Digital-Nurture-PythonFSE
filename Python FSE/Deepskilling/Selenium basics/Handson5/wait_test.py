from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

btn = driver.find_element(By.ID, "simple-btn-success")
btn.click()

wait = WebDriverWait(driver, 10)
alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
assert "successfully" in alert.text.lower()
print("Alert text verified!")

wait.until(EC.element_to_be_clickable((By.ID, "simple-btn-success"))).click()

fluent_wait = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])


driver.quit()