#import all dependencies
from selenium import webdriver
import bs4 as bs
from bs4 import BeautifulSoup
import pandas as pd
import keyboard
hex_color_code = input("Input Hex Color Code Without #:")

#open firefox browser
browser = webdriver.Firefox()
browser.get("https://www.color-hex.com/color/" + hex_color_code)
if KeyboardInterrupt:
    browser.close()
