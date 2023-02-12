import pyautogui


if pyautogui.confirm('Do you want to continue?') == "OK":
    print(pyautogui.size())  # current screen resolution width and height
else:
    print ("Cancled")
# pyautogui.PAUSE = 2.5

# print(pyautogui.position())  # current mouse x and y


#print(pyautogui.KEYBOARD_KEYS)


# print(pyautogui.locateCenterOnScreen("/Users/Omid/Desktop/Portfolio/GitPortfolio/PythonScripts/PyAutoGui/j.png"))
# filesX = pyautogui.locateCenterOnScreen("/Users/Omid/Desktop/Portfolio/GitPortfolio/PythonScripts/PyAutoGui/j.png").x
# filesY = pyautogui.locateCenterOnScreen("/Users/Omid/Desktop/Portfolio/GitPortfolio/PythonScripts/PyAutoGui/j.png").y
# pyautogui.click(x=filesX, y=filesY)



