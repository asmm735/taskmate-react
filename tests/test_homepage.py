from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1400,900')
options.binary_location = '/usr/bin/chromium'

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('http://127.0.0.1:3000')
    body_text = driver.find_element(By.TAG_NAME, 'body').text
    assert 'Taskmate' in driver.title or 'Taskmate' in body_text, 'Taskmate text not found'
    assert 'Todo' in body_text, 'Todo section not found on page'
    print('Selenium UI smoke test passed.')
finally:
    driver.quit()
