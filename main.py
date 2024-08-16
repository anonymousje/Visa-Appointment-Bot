from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os
import google.generativeai as genai
import time
import requests
import PIL.Image
from playsound import playsound
import sys

def find_available_dates(driver):
  
    #print("in-function")
    holiday_elements = holiday_elements = driver.find_elements(By.XPATH, "//td[@title='Available']")
  
    #print("out-function")

    return holiday_elements

def navigate_and_find_dates(driver):
  
  for _ in range(36):
    # Find available dates in the current month
    holiday_dates = find_available_dates(driver)
    
    # Process available dates (replace the comment with your logic)
    if holiday_dates:
        playsound.playsound("/home/anonymousje/Downloads/codes/selenium/alarm.mp3")  # Replace "your_sound_file.mp3" with the actual path to your sound file
        print("Sound played for holiday:", holiday)
        sys.exit()

    for holiday in holiday_dates:
      holiday_date = holiday.get_attribute("data-date")
      holiday_title = holiday.get_attribute("title")
      print(f"Holiday: {holiday_title} on {holiday_date}")

    # Click the "next" button (if available)
    try:
      next_button = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, ".next"))
      )
      next_button.click()
    except:
      print("No next button found, assuming reached last month")
      break  # Exit loop if no next button is found

service = Service(executable_path = "/home/anonymousje/Downloads/codes/selenium/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://blsitalypakistan.com/account/login")
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
)
username_input = driver.find_element(By.CLASS_NAME, "form-control")
username_input.send_keys("foadahmed0903@gmail.com")

password_input = driver.find_element(By.NAME, "login_password")
password_input.send_keys("ugfrx8iu")

tag_element = driver.find_element(By.ID, "Imageid")
src_value = tag_element.get_attribute("src")

response = requests.get(src_value)
image_path = "downloaded_image.jpg"  # Choose a suitable filename
with open(image_path, "wb") as f:
    f.write(response.content)

img = PIL.Image.open("downloaded_image.jpg")
#print(src_value)
os.environ["GEMINI_API_KEY"] = "AIzaSyBInq8zdbnYmpRhstpRDq0WbbQhFFf57y8"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(img)

#print(response.text)
#time.sleep(1000)

captcha_input = driver.find_element(By.ID, "captcha_code_reg")
captcha_input.send_keys(response.text)

submit_box = driver.find_element(By.NAME, "submitLogin")
submit_box.click()

if os.path.exists(image_path):
    os.remove(image_path)
    print("Image deleted successfully.")

time.sleep(5)

driver.get("https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment")


#close_button = driver.find_element(By.CLASS_NAME, "cl")
#close_button.click()

try:
  
  close_button = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "cl"))
  )
  close_button.click()
  print("Popup closed successfully!")
except:
  print("No popup found.")

dropdown_element_location = driver.find_element(By.ID, "valCenterLocationId")
select_object_location = Select(dropdown_element_location)
select_object_location.select_by_visible_text("Lahore (Pakistan)")

dropdown_element_type = driver.find_element(By.ID, "valCenterLocationTypeId")
select_object_type = Select(dropdown_element_type)
select_object_type.select_by_visible_text("National - Work")

dropdown_element_applicant = driver.find_element(By.ID, "valAppointmentForMembers")
select_object_applicant = Select(dropdown_element_applicant)
select_object_applicant.select_by_visible_text("Individual")



date_input = driver.find_element(By.ID, "valAppointmentDate")
date_input.click()

calendar = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".datepicker"))
  )




while(1):
    #print("Start process: ")

    navigate_and_find_dates(driver)
    #print("end process")
    #time.sleep(20)
    driver.refresh()
    date_input = driver.find_element(By.ID, "valAppointmentDate")
    date_input.click()

    calendar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".datepicker"))
    )


#driver.quit()

#holiday_dates = find_available_dates(driver)

#for holiday in holiday_dates:
#    holiday_date = holiday.get_attribute("data-date")
#    holiday_title = holiday.get_attribute("title")
#    print(f"Holiday: {holiday_title} on {holiday_date}")

