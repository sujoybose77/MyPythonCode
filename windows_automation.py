#Python path is C:\Users\sujoy\AppData\Local\Programs\Python\Python37\python.exe
#This python installation path is added in environment PATH variable using control panel
#pip path is C:\Users\sujoy\AppData\Local\Programs\Python\Python37\Scripts\pip.exe

import time
import datetime
print (str(datetime.datetime.now()) + " - Start of automation")


#------------------------ Browser automation WITHOUT Selenium ------------------------------------------
import webbrowser
url='https://us.hotstar.com/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open_new(url)

#------------------------ Desktop automation -----------------------------------------------------------
#Refer to https://automatetheboringstuff.com/chapter18/ for more details
#pyautogui installed using following command:
#C:\Users\sujoy\AppData\Local\Programs\Python\Python37\Scripts\pip.exe install pyautogui
import pyautogui

#Every PyAutoGUI function call will wait one second after performing its action. Non-PyAutoGUI instructions will not have this pause.
#pyautogui.PAUSE = 1
#pyautogui.FAILSAFE = True

#Get the size of current window
width, height = pyautogui.size()
print ("Width of current winow is : " + str(width))
print ("Height of current window is : " + str(height))

#Moving the cursor
#for i in range(5):
#    pyautogui.moveTo(100, 100, duration=0.25)
#    pyautogui.moveTo(200, 100, duration=0.25)
#    pyautogui.moveTo(200, 200, duration=0.25)
#    pyautogui.moveTo(100, 200, duration=0.25)

#Moves the mouse cursor relative to its current position.
#for i in range(5):
#    pyautogui.moveRel(100, 0, duration=0.25)
#    pyautogui.moveRel(0, 100, duration=0.25)
#    pyautogui.moveRel(-100, 0, duration=0.25)
#    pyautogui.moveRel(0, -100, duration=0.25)

#Get cursor position. This function returns a tuple of the mouse cursor's x and y positions at the time of the function call
x,y=pyautogui.position()
print ("Current cursor position is: " + str(x) + "," + str(y))

#time.sleep(5)
#pyautogui.click(900,500)

#------------------------ Browser automation WITH Selenium ---------------------------------------------
#To install Selenium:
#C:\Users\sujoy\AppData\Local\Programs\Python\Python37\Scripts\pip.exe install -U selenium
#Download chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
#And save chrome driver in C:\Sujoy\Take_backup\My_Python\Windows_and_browser_automation

from selenium import webdriver
#Mention chromedriver path below
dr = webdriver.Chrome('C:\Sujoy\Take_backup\My_Python\Windows_and_browser_automation\chromedriver.exe')
dr.maximize_window()
for i in range(1,100):
    #Clearning browser history
    dr.get('chrome://settings/clearBrowserData')
    time.sleep(2) # Let the user actually see something!
    pyautogui.click(1250,900)   #Clicking 'Clear Data' button. !! Position may vary !!
    time.sleep(4) # Let the user actually see something!
    dr.get('https://us.hotstar.com/');
    time.sleep(3) # Let the user actually see something!
    pyautogui.click(900,500)
    time.sleep(20)
#    pyautogui.click(1550,980)   #Clicking full screen button.
    current_window_title=dr.title
    print (current_window_title)
    #pyautogui.hotkey('ctrl', 'h')
    time.sleep(2)
#    pyautogui.click(1800,1100)   #Clicking settings.
    time.sleep(2) 
#    pyautogui.click(1825,900)   #Clicking auto
    time.sleep(2) 
#    pyautogui.click(1825,950)   #Clicking HD
    time.sleep(250) 
dr.close()
dr.quit()


print (str(datetime.datetime.now()) + " - End of automation")

