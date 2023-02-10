from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Create an instance of the web browser driver
driver = webdriver.Chrome(ChromeDriverManager().install())


# Open the conversion website
driver.get("https://www.calculator.net/conversion-calculator.html")

# Select the Length tab
driver.find_element_by_link_text("Length").click()

# Select the "From" unit in the "calFrom" table
from_unit = driver.find_element_by_xpath('//table[@name="calFrom"]//option[text()="Centimeters"]')
from_unit.click()

# Select the "To" unit in the "calTo" table
to_unit = driver.find_element_by_xpath('//table[@name="calTo"]//option[text()="Inches"]')
to_unit.click()

# Enter the value to convert in the input field
input_field = driver.find_element_by_xpath('//table[@name="fromVal"]//input')
input_field.send_keys("10")
input_field.send_keys(Keys.RETURN)

# Wait for the conversion to complete
time.sleep(1)

# Get the result of the conversion
output = driver.find_element_by_xpath('//table[@name="toVal"]//input').get_attribute("value")

# Compare the result with the expected value
expected_output = "3.93700787401575"
assert output == expected_output, f"Expected {expected_output}, but got {output}"

# Repeat the same steps for another test case
input_field.clear()
input_field.send_keys("20")
input_field.send_keys(Keys.RETURN)

time.sleep(1)

output = driver.find_element_by_xpath('//table[@name="toVal"]//input').get_attribute("value")

expected_output = "7.8740157480315"
assert output == expected_output, f"Expected {expected_output}, but got {output}"

# Close the web browser
driver.close()
