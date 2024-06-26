# Import the necessary packages
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By

# Class Create
class LinearDemo(unittest.TestCase):

   def setUp(self):
       """Setup method to initiate the Chrome browser."""
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.implicitly_wait(2)

   def test_linear_flow_testing(self):
       # Navigate to desired web page and verify web page is displayed
       self.driver.get("https://jignect.tech/")
       # self.assertTrue("Software Testing Company" in self.driver.title)

       # Click on the contact us button
       contact_us_button = self.driver.find_element(By.XPATH, "//ul[@id='menu-main-menu']//a[text()='Contact Us']")
       contact_us_button.click()

       # Verify desired page is displayed
       contact_us_header = self.driver.find_element(By.CSS_SELECTOR, "div[class='contact-title'] h2").text
       self.assertEqual(contact_us_header, "Let's talk", "Contact Us page does not displayed")

       # Generate random string
       full_name = "".join(random.choice(string.ascii_letters) for _ in range(8))

       # Enter value in full name and company name, select checkbox and click on submit button
       self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Full name']").send_keys(full_name)
       self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Company']").send_keys("TechTonic")
       self.driver.find_element(By.CSS_SELECTOR, "span[id='checkboxOne']").click()
       self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

       # Verify the validation message for mandatory fields
       expected_validation_message = 'The field is required.'

       textarea_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR,
                                                                     "textarea[name*='textarea'] + span").text
       email_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "input[name*='email'] + span").text
       phone_number_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR,
                                                                         "input[placeholder='Phone number'] + span").text

       self.assertEqual(textarea_actual_validation_message, expected_validation_message,
                        "Textarea validation message does not match")
       self.assertEqual(email_actual_validation_message, expected_validation_message,
                        "Email validation message does not match")
       self.assertEqual(phone_number_actual_validation_message, expected_validation_message,
                        "Phone number validation message does not match")

   
   def tearDown(self):
       """Tear down method to close the browser."""
       self.driver.quit()


