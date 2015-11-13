
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from random import randint
from config import config
import re

# Variables
referLink = 'http://refer.grubhub.com/micro/microsite6?channel=email&source=share12'
gmailLink = 'https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default'
smsLink = 'https://smsreceivefree.com/'
alphabetArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
password = 'GrubHubRSuckers12345'
newEmail = ''

#Open all browsers
emailWindow = webdriver.Firefox() # Get local session of firefox
emailWindow.get(gmailLink) # Load page
referWindow = webdriver.Firefox() # Get local session of firefox
referWindow.get(referLink) # Load page

def main():
    fillOutEmailForm()
    #waitForConfirmCode(emailWindow)
    refer = raw_input("Type ok when you have verified the email: ")
    if (refer == 'ok'):
        sendReferral()

def fillOutEmailForm():
    global newEmail

    firstNameBox = emailWindow.find_element_by_id("FirstName") # Find the first name box
    firstNameBox.send_keys("Joe")

    lastNameBox = emailWindow.find_element_by_id("LastName") # Find the last name box
    lastNameBox.send_keys("Smith")

    # Randomly generate new username
    for x in range(0, 25):
        newEmail += alphabetArray[randint(0,35)]

    emailBox = emailWindow.find_element_by_id("GmailAddress") # Find the email box
    emailBox.send_keys(newEmail)

    passwordBox = emailWindow.find_element_by_id("Passwd") # Find the password box
    passwordBox.send_keys(password)

    passwordAgainBox = emailWindow.find_element_by_id("PasswdAgain") # Find the password again box
    passwordAgainBox.send_keys(password)

    dropDowns = emailWindow.find_elements_by_class_name("jfk-select") # all dropdown menus
    dropDowns[0].send_keys('January') # birth month dropdown
    dropDowns[1].send_keys('Other') # gender dropdown

    BirthDayBox = emailWindow.find_element_by_id("BirthDay") # Find the birth day box
    BirthDayBox.send_keys('1')

    BirthYearBox = emailWindow.find_element_by_id("BirthYear") # Find the birth year box
    BirthYearBox.send_keys(1990)

    robotCheckbox = emailWindow.find_element_by_id("SkipCaptcha") # Find the verify checkbox
    robotCheckbox.click()

    termsCheckbox = emailWindow.find_element_by_id("TermsOfService") # Find the terms checkbox
    termsCheckbox.click()

    submitButton = emailWindow.find_element_by_id("submitbutton") # Find the submit button
    submitButton.click()
    time.sleep(.5)


# wait for confirmation code to be entered
def waitForConfirmCode():
    try:
        phoneNumberBox = emailWindow.find_element_by_id("signupidvinput") # Find the phone number box
        phoneNumberBox.click()
    except:
        time.sleep(1)
        print('waiting for confirmation code')
        waitForConfirmCode()

# send referral
def sendReferral():
    global newEmail
    newEmail = newEmail + '@gmail.com'
    try:
        container = referWindow.find_element_by_id("modal_container")
        fullClass = container.get_attribute("class")
        m = re.search("\d", fullClass)
        classNumber = fullClass[m.start():]
        print("referral page class number: " + classNumber)

        emailDiv = referWindow.find_element_by_class_name("email-input-section" + classNumber) # Find the email div
        emailDiv2 = emailDiv.find_element_by_class_name("input" + classNumber) # Find the email div
        emailBox = emailDiv2.find_elements_by_xpath(".//*") # Find the email box
        emailBox[1].send_keys(config['email'])

        tagBox = referWindow.find_element_by_class_name("new-tag-input" + classNumber) # Find the email box
        tagBox.send_keys(newEmail)

        submitButton = referWindow.find_element_by_class_name("submit-button" + classNumber) # Find the email box
        submitButton.click()
    except:
        print('failed to send referral')

# Run main method
if __name__ == "__main__":
    main()


