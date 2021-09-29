from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path='Input Location of Chromedriver')
driver.get("https://healthscreening.schools.nyc/?type=G")


RadioButtonGuest = driver.find_element_by_xpath('//*[@id="guest_identity_form"]/div[2]/div[1]/div')
RadioButtonGuest.click()

FirstName = "Input First Name"
first = driver.find_element_by_xpath('//*[@id="guest_first_name"]')
first.send_keys(FirstName)

LastName = "Input Last Name"
last = driver.find_element_by_xpath('//*[@id="guest_last_name"]')
last.send_keys(LastName)

Email = "Input Email"
email = driver.find_element_by_xpath('//*[@id="guest_email"]')
email.send_keys(Email)

RadioButtonOther = driver.find_element_by_xpath('//*[@id="other_label"]')
RadioButtonOther.click()

SchoolName = "Input School Name"
school = driver.find_element_by_xpath('//*[@id="guest_location"]')
school.send_keys(SchoolName)

RadioButtonFillOut = driver.find_element_by_xpath('//*[@id="btnDailyScreeningSubmit"]/button')
RadioButtonFillOut.click()

time.sleep(.5)

RadioButtonSymptoms = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[1]/div/div[2]/label')
RadioButtonSymptoms.click()

time.sleep(.5)

RadioButtonResult = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[2]/div/div[2]/label')
RadioButtonResult.click()

time.sleep(.5)

RadioButtonVaccination = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[3]/div/div[2]/label')
RadioButtonVaccination.click()

time.sleep(.5)

RadioButtonContact = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[4]/div/div[2]/label')
RadioButtonContact.click()

time.sleep(.5)

RadioButtonSubmit = driver.find_element_by_xpath('//*[@id="questions_layout"]/div[5]/div[1]/button')
RadioButtonSubmit.click()
