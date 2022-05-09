import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a service object
driver_path = "E:\MSM_Work\Selenium\driver\chromedriver.exe"
serv_obj = Service(driver_path)

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://twin-cities.umn.edu/academics-admissions/majors-programs")
driver.implicitly_wait(10)
# implicit, because if website loads before wait time then move on to next line of code

elements = driver.find_elements(By.CSS_SELECTOR, "a.program-title--link")
program_types = []
for element in elements:
    program_types.append(element.text)

print(len(program_types))
