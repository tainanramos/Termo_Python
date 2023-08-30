from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_webdriver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions() 
    #options.add_argument(r"user-data-dir=C:\Users\taina\AppData\Local\Google\Chrome\User Data\RPA")
    #drive = webdriver.Chrome(service=service, options=options)
    drive = webdriver.Chrome(service=service)
    drive.maximize_window()
    return drive