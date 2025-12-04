from selenium import webdriver
from selenium.webdriver.common.by import By
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver
def alert(text):
    alert = driver.switch_to.alert
    assert alert.text == text
    alert.accept()
def empty_usename(setup_teardown):
    driver = setup_teardown
    driver.get("http://localhost:5000/")
    driver.find_element(By.NAME, "username").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("passwordd")
    driver.find_element(By.NAME, "age").send_keys("25")
    driver.find_element(By.NAME, "submit").click()  
    assert "Username cannot be empty" in alert.text
def empty_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://localhost:5000/")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("")
    driver.find_element(By.NAME, "age").send_keys("25")
    driver.find_element(By.NAME, "submit").click()  
    assert "Password cannot be empty" in alert.text
def password_length(setup_teardown):
    driver = setup_teardown
    driver.get("http://localhost:5000/")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("pass")
    driver.find_element(By.NAME, "age").send_keys("25")
    driver.find_element(By.NAME, "submit").click()  
    assert "Password must be at least 6 characters long" in alert.text



    