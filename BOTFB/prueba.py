from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from tkinter import *
import glob
import os

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(10)
