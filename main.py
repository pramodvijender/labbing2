import time
import sys
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from threading import Thread
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoSuchWindowException

#driver = webdriver.firefox()

def geturl(thread_id):
      options=Options()
      # Set the path to the Chrome driver executable
      driver_path = './usr/local/bin/geckodriver'

# Create a new instance of the Chrome driver
# make this a headless Browser



# Open the website login page
      ff_options = webdriver.FirefoxOptions()
      ff_options.add_argument("--headless")
      ff_options.add_argument('--no-sandbox')
      ff_options.add_argument('--disable-dev-shm-usage')
      ff_options.add_argument('--enable-javascript')


      with open('./usernames') as myfile:
              for line in myfile.readlines():
                    driver = webdriver.Firefox(options=ff_options)
                    driver.get("https://lab.macquarie.com.au/personal")
                    time.sleep(5)
                    wait = WebDriverWait(driver, 2)

                  # Find the username and password input fields by their HTML attributes
                  #adding Wait Times until th fields are found
                    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
                    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
                    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'btn btn-lg btn-primary btn-block ladda-button')]")))

                  # Enter your username and password

                    username_field.send_keys(line)
                    print(line + "This is the username being sent")
                    print(thread_id)
                    time.sleep(2)
                    password_field.send_keys("R@ksat12")
                    response = password_field.send_keys(Keys.RETURN)
                    login_button.click()
                    print("Button Clicked")
                    time.sleep(10)
                    
                    try:
                        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div/iframe")))
                        results2 = driver.find_element(By.XPATH, "//*[@id='game-core-frame']").text
                        print("Arkose Challenge Kicked off" + results2)
                    except:                      
                        try:
                          print(thread_id, "There was no challenge for this thread ID, trying next")
                          driver.implicitly_wait(5)
                          WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[contains(@class, 'ng-star-inserted')]")))
                          print("Chootiya")
                          results1 = driver.find_element((By.XPATH, "//*[contains(@id='mq-mfa-validate-heading')]")).text                       
                          print(results1, "Noting to see here")
                        except:
                            try:
                              returntext = driver.find_element((By.XPATH,"//*[contains(@class, 'auth-heading')]")).text
                              if returntext == "Something went wrong":
                                print(returntext + " This was picked up by botman")
                              else:
                                print(returntext + " This was not picked up by botman")
                            except:
                                print("none of this work")
                  

# Wait for the login process to complete
def main():
    try:
        for i in range(1,5):
          print(f"[*] Starting thread {i} ...")
          t = Thread(target=geturl, args=[i], daemon=True)
          t.start()  

        while True:
             print("[*] Sleeping main thread") 
             time.sleep(10)
    except:
         print("error in python")


if __name__=="__main__":
     sys.exit(main())


