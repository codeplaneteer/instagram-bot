from selenium import webdriver
import time
from random import randint

from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get("https://www.instagram.com")
time.sleep(5)


def login(user, passe):
    time.sleep(5)
    inputuser = web.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div"
        "[1]/div/label/input"
    )
    inputuser.send_keys(user)
    inpupass = web.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div["
                  "2]/form/div/div[2]/div/label/input")
    inpupass.send_keys(passe)
    time.sleep(3)
    loginButton = web.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/"
                  "main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()


def openmyfollowers(account_instagram):
    web.get("https://www.instagram.com/" + account_instagram)
    time.sleep(20)
 

    i = 1
    window = web.find_element(By.XPATH, "//div[@class='_aano']")

    while True:
        if i == 200:
            break
        web.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                           window)  
        i += 1
        time.sleep(1)

    time.sleep(5)


def deletemyfollowers():
    follows = web.find_elements(By.XPATH,
                                "//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")

    print("total de busqueda:", len(follows))
    print("--------")

    for child in follows:
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")
               
        print(user_name.text)
        print(button_name.text)
        print("------------")
        if "Siguiendo" == button_name.text or "Following" == button_name.text and user_name.text != "stefany_princess":
            web.execute_script("arguments[0].click();", button_name)
            time.sleep(randint(10,100))
            unfollow = web.find_element(By.XPATH, "//button[@class='_a9-- _a9-_']")
            web.execute_script("arguments[0].click();", unfollow)
            print(user_name.text + " Eliminado")
        time.sleep(randint(15,100))
            

login("StevHernandez28@gmail.com", "62750606")
time.sleep(5)
openmyfollowers("stev_hernandez28/following/")
time.sleep(15)
deletemyfollowers()
# PS C:\Users\Steven\Desktop\Projects\Instagram bot> & "c:/Users/Steven/Desktop/Projects/Instagram bot/.venv/Scripts/Activate.ps1"
# (.venv) PS C:\Users\Steven\Desktop\Projects\Instagram bot> & "c:/Users/Steven/Desktop/Projects/Instagram bot/.venv/Scripts/python.exe" "c:/Users/Steven/Desktop/Projects/Instagram bot/removefollows.py"