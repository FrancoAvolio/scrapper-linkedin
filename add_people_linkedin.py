from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
linkedin_user = os.getenv("LINKEDIN_EMAIL")
linkedin_url = os.getenv("LINKEDIN_URL")
chrome_driver_path = r'C:/Users/franc/Downloads/chromedriver-win64/chromedriver.exe'

# Configura las opciones del navegador Chrome
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" # Provide your Chrome binary path

# Set Chrome WebDriver executable path
options.add_argument("webdriver.chrome.driver=" + chrome_driver_path)

# Inicializa el controlador de Chrome con las opciones del navegador
driver = webdriver.Chrome(options=options)
driver.get("https://linkedin.com")

time.sleep(4)
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
time.sleep(3)
username.send_keys(linkedin_user)
time.sleep(3)
password.send_keys(linkedin_password)
time.sleep(3)
submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

n_pages = 10
base_url = linkedin_url
for n in range(n_pages + 1):
    if n == 0:
        url = base_url
    else:
        url = f"{base_url}&page={n}"
    
    driver.get(url)
    time.sleep(3)
    all_buttons = driver.find_elements(By.TAG_NAME, ("button"))
    connect_buttons = [btn for btn in all_buttons if btn.text.strip() == "Conectar"]
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
        send = driver.find_element(By.XPATH, "//button[@aria-label='Enviar sin nota']")
        driver.execute_script("arguments[0].click();", send)
        close = driver.find_element(By.XPATH, "//button[@aria-label='Descartar']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(3)








