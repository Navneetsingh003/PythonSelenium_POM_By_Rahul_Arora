from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")

remote_url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(
    command_executor=remote_url, options=chrome_options
)
driver.get("http://www.google.com")
print(driver.title)
driver.quit()