
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from random import randint

# Variables
referLink = 'http://refer.grubhub.com/micro/microsite6?channel=email&source=share12'
gmailLink = 'https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default'
alphabetArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
password = 'GrubHubRSuckers12345'


def main():
    browser = openNewWindow(gmailLink)
    fillOutEmailForm(browser)
    phoneConfirmation(browser)

def openNewWindow(url):
    try:
        browser = webdriver.Firefox() # Get local session of firefox
        browser.get(url) # Load page
        return browser
    except:
        print("failure to open new window")

def fillOutEmailForm(browser):
    newEmail = ''
    
    firstNameBox = browser.find_element_by_id("FirstName") # Find the first name box
    firstNameBox.send_keys("Joe")

    lastNameBox = browser.find_element_by_id("LastName") # Find the last name box
    lastNameBox.send_keys("Smith")

    # Randomly generate new username
    for x in range(0, 25):
        newEmail += alphabetArray[randint(0,35)]

    emailBox = browser.find_element_by_id("GmailAddress") # Find the email box
    emailBox.send_keys(newEmail)

    passwordBox = browser.find_element_by_id("Passwd") # Find the password box
    passwordBox.send_keys(password)

    passwordAgainBox = browser.find_element_by_id("PasswdAgain") # Find the password again box
    passwordAgainBox.send_keys(password)

    dropDowns = browser.find_elements_by_class_name("jfk-select") # all dropdown menus
    dropDowns[0].send_keys('January') # birth month dropdown
    dropDowns[1].send_keys('Other') # gender dropdown

    BirthDayBox = browser.find_element_by_id("BirthDay") # Find the birth day box
    BirthDayBox.send_keys('1')

    BirthYearBox = browser.find_element_by_id("BirthYear") # Find the birth year box
    BirthYearBox.send_keys(1990)

    robotCheckbox = browser.find_element_by_id("SkipCaptcha") # Find the verify checkbox
    robotCheckbox.click()

    termsCheckbox = browser.find_element_by_id("TermsOfService") # Find the terms checkbox
    termsCheckbox.click()

    submitButton = browser.find_element_by_id("submitbutton") # Find the submit button
    submitButton.click()
    time.sleep(.5)
   
# confirm new email through text 
def phoneConfirmation(browser):
    try:
        phoneNumber = input('Enter your phone number: ')
        phoneNumberBox = browser.find_element_by_id("signupidvinput") # Find the phone number box
        phoneNumberBox.send_keys(phoneNumber)
    except:
        print('Failed to confirm phone number')

# Run main method
if __name__ == "__main__":
    main()


