from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

"""
Selenium Components:
1. WebDriver: An API that allows code to communicate directly with the browser via a driver executable.
2. Selenium Grid: Allows running tests in parallel across different machines and browser combinations.
3. Selenium IDE: A browser extension for record-and-playback to quickly prototype test cases.
"""

options = Options()

options.add_argument('--headless') 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

driver.quit()