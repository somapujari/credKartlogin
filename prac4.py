from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.binary_location = R'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get('https://automation.credence.in/login')

    driver.find_element(By.ID, 'email').send_keys('soma1@credence.com')
    driver.find_element(By.ID, 'password').send_keys('Test@123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    value = driver.find_element(By.XPATH, '//h2').text
    if value == "CredKart":
        assert True
    else:
        assert False
