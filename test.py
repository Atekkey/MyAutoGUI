import pyautogui
import time

time.sleep(4)
pyautogui.moveRel(30, 30) #show start

# https://www.websudoku.com/
screenWidth, screenHeight = pyautogui.size()

spot = pyautogui.locateOnScreen('pngs/here_top2.png')
startX, startY = spot[0]/2, spot[1]/2 + 55
kMoveDist = 50

def fill1s():
    pyautogui.moveTo(startX, startY)
    for x in range(9):
        pyautogui.moveTo(startX, startY + kMoveDist * x)
        for y in range(8):
            pyautogui.click()
            pyautogui.typewrite("1")
            pyautogui.moveRel(kMoveDist,0)
        pyautogui.click()
        pyautogui.typewrite("1")
def find4s():
    return list(pyautogui.locateAllOnScreen('pngs/4.png'))
print("this many 4's: ", str(len(find4s())))

fill1s()


pyautogui.moveRel(-30, -30) #show end