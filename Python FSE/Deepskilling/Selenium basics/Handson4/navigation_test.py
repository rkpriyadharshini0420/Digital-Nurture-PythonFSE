from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/")
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
assert 'simple-form-demo' in driver.current_url
driver.back()

driver.execute_script('window.open("https://www.google.com");')
driver.switch_to.window(driver.window_handles[1])
print("Google Tab Title:", driver.title)

driver.switch_to.window(driver.window_handles[0])
driver.save_screenshot('playground_screenshot.png')


driver.set_window_size(1280, 800)
print("Window size set to:", driver.get_window_size())

driver.quit()