from selenium import webdriver

import time
import os

executable_path_input = "Input Location of Chromedrive"
FirstName_input = "Input First Name"
LastName_input = "Input Last Name"
Email_input = "Input Email"
SchoolName_input = "Input School Name"

driver = webdriver.Chrome(executable_path=executable_path_input)
driver.get("https://healthscreening.schools.nyc/?type=G")

RadioButtonGuest = driver.find_element_by_xpath('//*[@id="guest_identity_form"]/div[2]/div[1]/div')
RadioButtonGuest.click()

first = driver.find_element_by_xpath('//*[@id="guest_first_name"]')
first.send_keys(FirstName_input)

last = driver.find_element_by_xpath('//*[@id="guest_last_name"]')
last.send_keys(LastName_input)

email = driver.find_element_by_xpath('//*[@id="guest_email"]')
email.send_keys(Email_input)

RadioButtonOther = driver.find_element_by_xpath('//*[@id="other_label"]')
RadioButtonOther.click()

school = driver.find_element_by_xpath('//*[@id="guest_location"]')
school.send_keys(SchoolName_input)

RadioButtonFillOut = driver.find_element_by_xpath('//*[@id="btnDailyScreeningSubmit"]/button')
RadioButtonFillOut.click()

time.sleep(.5)

RadioButtonAge = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[2]/div/div[3]/label')
RadioButtonAge.click()

time.sleep(.5)

RadioButtonSymptoms = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[4]/div[1]/div/div[2]/label')
RadioButtonSymptoms.click()

time.sleep(.5)

RadioButtonTest = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[4]/div[2]/div/div[2]/label')
RadioButtonTest.click()

time.sleep(.5)

RadioButtonContact = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[4]/div[3]/div/div[2]/label')
RadioButtonContact.click()

time.sleep(.5)

RadioButtonSubmit = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[5]/div[1]/button')
RadioButtonSubmit.click()
