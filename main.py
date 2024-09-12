#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import google.generativeai as genai
import time
import requests
import PIL.Image
from playsound import playsound
import sys
import re

def resource_path(relative_path):
  base_path = os.path.abspath(".")

  return os.path.join(base_path, relative_path)

def find_available_dates(driver):
      
    Possible_holiday_elements = driver.find_elements(By.XPATH, "//td")  # Find all <td> elements
    available_dates = []
    for element in Possible_holiday_elements:
        title = element.get_attribute("title")
        if title not in ['Not Available', 'Holiday', 'Slots Full', 'Weekly Off', '']:
            available_dates.append(element.text)  # Add the available date to the list
  
    return available_dates

def navigate_and_find_dates(driver, passport):
  
  for _ in range(2):
    holiday_dates = find_available_dates(driver)
    
    if holiday_dates:
        
        date_element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, f"//td[text()='{holiday_dates[0]}']"))
)
        date_element.click()

        WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "valAppointmentType"))
                )
        #dropdown_element_type = driver.find_element(By.ID, "valAppointmentType")
        dropdown_element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID, 'valAppointmentType')))
        select_object_type = Select(dropdown_element)
        try:
          select_object_type.select_by_value  ('normal')
        except NoSuchElementException:
          print("balls")
          time.sleep(5)
          first_option = select_object_type.options[1]
          first_option.click()

        time.sleep(2)
        playsound(resource_path("sound.mp3"))  
        print("DATE AVAILABLE!")
        WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.NAME, "valApplicant[1][passport_number]"))
                )
        
        input_element = driver.find_element(By.NAME, "valApplicant[1][passport_number]")
        driver.execute_script("arguments[0].removeAttribute('readonly'); arguments[0].value = '';", input_element);

# Now you can edit the input field
        input_element.send_keys(passport)
        time.sleep(10000)
        sys.exit()

    for holiday in holiday_dates:
      holiday_date = holiday.get_attribute("data-date")
      holiday_title = holiday.get_attribute("title")
      print(f"Holiday: {holiday_title} on {holiday_date}")

    try:
      next_button = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, ".next"))
      )
      next_button.click()
    except:
      print("No next button found, assuming reached last month")
      break

def main(link, passport):
   
    print("📄 [INFO] Driver Script Running On Link:", link)
    driver_path = resource_path("chromedriver.exe")
    print("📄 [INFO] Attempting fetch chromedriver.exe from:", driver_path)
    if os.path.isfile(driver_path):
      service = Service(executable_path = driver_path)
      driver = webdriver.Chrome(service=service)
      print("📄 [INFO] Fetched chromedriver.exe from:", driver_path)
      playsound(resource_path("sound.mp3"))  
    else:
      print("❌ [ERROR] ChromeDriver Does Not Exist!")
      input("Press any key to exit...")
      exit()

    time.sleep(100)
    try:
      driver.get(link)
    except TimeoutException:
       driver.get(link)

    time.sleep(10)

    while(1):
        try:
            WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "valCenterLocationTypeId"))
                )
            dropdown_element_type = driver.find_element(By.ID, "valCenterLocationId")
            select_object_type = Select(dropdown_element_type)
            select_object_type.select_by_visible_text("Cebu (PHILIPPINES)")

            WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "valCenterLocationTypeId"))
                )
            dropdown_element_type = driver.find_element(By.ID, "valCenterLocationTypeId")
            select_object_type = Select(dropdown_element_type)
            select_object_type.select_by_visible_text("National Visa Others")


            WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "valAppointmentForMembers"))
                )
            dropdown_element_type = driver.find_element(By.ID, "valAppointmentForMembers")
            select_object_type = Select(dropdown_element_type)
            select_object_type.select_by_visible_text("Individual")



            WebDriverWait(driver, 60).until(
                            EC.presence_of_element_located((By.ID, "valAppointmentDate"))
                    )

            date_input = driver.find_element(By.ID, "valAppointmentDate")
            date_input.click()

            navigate_and_find_dates(driver, passport)
            driver.refresh()
        except TimeoutException:
            driver.refresh()


if __name__ == "__main__":
  link = sys.argv[1]
  #passport = sys.arg[2]
  passport = "ZB654321"
  main(link,passport)