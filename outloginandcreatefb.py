import time, os
import sys
import random
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from pymongo import MongoClient
from string import digits

client = MongoClient(host="mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/outlookmail?retryWrites=true&w=majority",connect=False)
collection = client.get_database("outlookmail").get_collection("tempmail")
collection2 = client.get_database("outlookmail").get_collection("mailwithdata")
remove_digits = str.maketrans('', '', digits)

options = webdriver.ChromeOptions() 
# options.headless = True
options.add_argument('--disable-popup-blocking')
bot = uc.Chrome(options=options)
# bot.get('https://login.live.com/login.srf')
# firstname = (names.get_first_name(gender='male')).lower()
# lastname = (names.get_last_name()).lower()
# email = firstname+'_'+lastname+str(random.randrange(7598,100000))+'@outlook.com'
# print(email)

# print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

try:

    a = collection.find_one_and_delete({})
    print(a['email'])
    email = a['email']
    fullname = email.split('@')[0]

    try:
        try:
            lastname = fullname.split('_')[1]
            print('1')
            lastnamewithnodigits = lastname.translate(remove_digits)
            firstname = fullname.split('_')[0]
        except:
            pass

        try:
            lastname = fullname.split('.')[1]
            print('2')
            lastnamewithnodigits = lastname.translate(remove_digits)
            firstname = fullname.split('.')[0]
        except:
            # firstname  = fullname[:len(fullname)//2]
            # lastname = fullname[len(fullname)//2:]
            # lastnamewithnodigits = lastname.translate(remove_digits)
            print('3')
            pass
    except:
        firstname  = fullname[:len(fullname)//2]
        lastname = fullname[len(fullname)//2:]
        lastnamewithnodigits = lastname.translate(remove_digits)


    # print(fullname)
    print(firstname)
    print(lastnamewithnodigits)

    bot.get('https://login.live.com/login.srf')

    # bot.save_screenshot('1.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="loginfmt"]'))).send_keys('lilian.grante@outlook.com')

    # bot.save_screenshot('2.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

    

    time.sleep(2)

    # bot.save_screenshot('3.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="passwd"]'))).send_keys('Jatin@123')

    # bot.save_screenshot('4.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

    # bot.save_screenshot('5.png')

    try:
        WebDriverWait(bot,5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    except:
        pass

    try:

        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="button"]'))).click()

        # bot.save_screenshot('6.png')
    except:
        pass

    try:
        WebDriverWait(bot,5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    except:
        pass

    # try:
    #     WebDriverWait(bot,5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Skip for now')]"))).click()
    # except:
    #     pass
    
    # time.sleep(4)

    

    
    # time.sleep(5)

    # bot.save_screenshot('66.png')

    bot.get('https://outlook.live.com/mail/0/')

    try:
        WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Skip for now')]"))).click()
    except:
        pass


    try:
        WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Junk Email')]")))
    except:
        bot.get('https://outlook.live.com/mail/0/')
        time.sleep(2)
        pass

    # bot.save_screenshot('7.png')

    print("Outlook Done!!!!!!!!!!!!!")

    bot.execute_script("window.open('');")

    time.sleep(2)

    bot.switch_to.window(bot.window_handles[1])

    

    bot.get('https://en-gb.facebook.com/')

    time.sleep(5)

    # bot.save_screenshot('8.png')


    try:


        bot.find_element(By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy').click()

        # bot.save_screenshot('9.png')
    except:
        pass
    # WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy'))).click()


    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy'))).click()

    # bot.save_screenshot('10.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email__"]'))).send_keys('lilian.grante@outlook.com')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email_confirmation__"]'))).send_keys('lilian.grante@outlook.com')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="firstname"]'))).send_keys('lilian')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="lastname"]'))).send_keys('grante')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_passwd__"]'))).send_keys('Jatin@123')


    randdate = random.randint(3,20)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="day"]/option[{randdate}]'))).click()


    randmonth = random.randint(2,9)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="month"]/option[{randmonth}]'))).click()

    randyear = random.randint(28, 34)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="year"]/option[{randyear}]'))).click()

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value="2"]'))).click()

    # bot.save_screenshot('11.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="websubmit"]'))).click()

    # bot.save_screenshot('12.png')


    time.sleep(15)

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Complete these steps in the next 180 days to make sure that you can use this account.')]")))

        print('180 days Text Came. Account not created')

        data = {'email': email, 'fb': 'No', 'firstname': firstname, 'lastname': lastnamewithnodigits}

        collection2.insert_one(data)

        # time.sleep(10)

        bot.save_screenshot('13.png')

        bot.quit()

        sys.exit("Account Not Created 180 days Text Came")

         


        #if 180 days wala msg came then stop here
    except:
        pass

    #Going Outlook For OTP Code
    bot.switch_to.window(bot.window_handles[0])

    time.sleep(2)

    bot.get('https://outlook.live.com/mail/0/')

    # time.sleep(10)

    
    # bot.save_screenshot('133.png')

    elee = WebDriverWait(bot,100).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'is your Facebook confirmation code')]")))

    # bot.save_screenshot('14.png')

    ttext = elee.text

    facebookcode = ttext.replace('FB-',"").replace(" is your Facebook confirmation code","")
    
    print(facebookcode)

    time.sleep(1)

    bot.switch_to.window(bot.window_handles[1])

    time.sleep(2)

    ###############NOTEE##########
    #Put This code using send_keys

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="code_in_cliff"]'))).send_keys(facebookcode)

    # bot.save_screenshot('15.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="confirm"]'))).click()
            
    time.sleep(20)

    # bot.save_screenshot('16.png')

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Allow all cookies')]"))).click()

        # bot.save_screenshot('17.png')
    except:
        pass
        
    # Then Click Next
    bot.get('https://www.facebook.com/')

    print("Done Facebook!!!!!!.... Account Created")

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Group conversations')]"))).click()

    print('Confirmed FB Account Created')

    data = {'email': email, 'fb': 'Yes', 'firstname': firstname, 'lastname': lastnamewithnodigits}

    collection2.insert_one(data)
    

    # bot.save_screenshot('18.png')

    


        
    time.sleep(50000)
    bot.quit()
except Exception as e:
    data = {'email': email, 'fb': 'error', 'firstname': firstname, 'lastname': lastnamewithnodigits}

    collection2.insert_one(data)
    print(e)
    time.sleep(10000)

bot.quit()
print("Program Ended")

