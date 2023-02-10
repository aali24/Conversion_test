from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


from webdriver_manager.chrome import ChromeDriverManager

def test_unit_conversion():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.calculator.net/conversion-calculator.html")

    # select the length conversion
    length_conversion = driver.find_element("xpath", '//a[contains(text(), "Length")]')
    length_conversion.click()

    # input the value to convert
    input_field = driver.find_element("xpath", '//*[@name="fromVal"]')
    input_field.send_keys("-10")

    # select the unit to convert from
    unit_from = driver.find_element("xpath", '//select[@name="calFrom"]')
    unit_from.send_keys("Centimeters")

    # select the unit to convert to
    unit_to = driver.find_element("xpath", '//select[@name="calTo"]')
    unit_to.send_keys("Inches")

    # perform the conversion
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # assert that the conversion was successful
    result = driver.find_element("xpath", '//input[@name="toVal"]')
    assert result.get_attribute("value") == "-3.937007874"

    # repeat the above steps for a different conversion
    input_field = driver.find_element("xpath", '//*[@name="fromVal"]')
    input_field.clear()
    input_field.send_keys("20E306")
    unit_from = driver.find_element("xpath", '//select[@name="calFrom"]')
    unit_from.send_keys("Centimeters")
    unit_to = driver.find_element("xpath", '//select[@name="calTo"]')
    unit_to.send_keys("Inches")
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)
    result = driver.find_element("xpath", '//input[@name="toVal"]')
    assert result.get_attribute("value") == "7.874015748E+306"

    # close the browser window
    driver.quit()

if __name__ == "__main__":
    test_unit_conversion()