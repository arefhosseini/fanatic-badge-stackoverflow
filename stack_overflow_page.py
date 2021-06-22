import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def login():
    print("Logging into stackoverflow.com")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.get("https://stackoverflow.com")

        driver.find_element_by_link_text("Log in").click()

        driver.find_element_by_id("email").send_keys(os.environ['STACK_OVERFLOW_EMAIL'])
        driver.find_element_by_id("password").send_keys(os.environ['STACK_OVERFLOW_PASSWORD'])
        driver.find_element_by_id("submit-button").submit()

        driver.find_element_by_class_name("my-profile").click()

        elem = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "grid--cell.ws-nowrap.fs-body3"))
        )
        assert os.environ['STACK_OVERFLOW_DISPLAY_NAME'] in elem.text
        print("Logged into stackoverflow.com and accessed profile page")

    except Exception as e:
        print("An error occurred while trying to access stackoverflow.com!", e)        
    finally:
        driver.close()


if __name__ == "__main__":
    login()
