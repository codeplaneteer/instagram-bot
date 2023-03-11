from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint

web = webdriver.Chrome()
web.get('https://www.instagram.com')
time.sleep(3)


def login(user, passe):
    time.sleep(3)
    inputuser = web.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(1) > div > label > input")
    inputuser.send_keys(user)
    inpupass = web.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
    inpupass.send_keys(passe)
    time.sleep(3)
    loginButton = web.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button").click()


def followers(account):
    web.get("https://www.instagram.com/" + account + "/followers/")
    time.sleep(10)
    i = 1
    window = web.find_element(By.XPATH, "//div[@class='_aano']")

    time.sleep(5)
    while True:
        if i == 50:
            break
        web.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                           window)
        time.sleep(1)
        i += 1
    time.sleep(5)

    follower = web.find_elements(By.XPATH,
                                 "//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")

    print("--------")
    print("Perfiles en la cadena antes de eliminar")
    print("--------")
    newFollows = follower
    index = 0
    for child in newFollows:
        user_name = child.find_element(
            By.CSS_SELECTOR, "div > div > div > a > span > div")
        print("Perfiles: " + user_name.text)

    print("---------------")
    print("---------------")
    print("---------------")
    print("---------------")

    for child in follower:
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")
        index += 1
        if "Seguido" == button_name.text or "Following" == button_name.text or "Requested" == button_name.text or button_name.text == "Followed":
            del newFollows[index-1]
            print("Perfil eliminado de la lista:" + user_name.text)

    
    print("--------")
    print("Perfiles en la cadena luego de eliminar")
    print("--------")
    for child in newFollows:
        user_name = child.find_element(
            By.CSS_SELECTOR, "div > div > div > a > span > div")
        print("Perfiles: " + user_name.text)

        
    print("--------")
    print("total de busqueda:", len(newFollows))
    print("--------")
# > div > div > span > a > span > div
    time.sleep(5)

    for child in newFollows:
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")

        if "Seguido" == button_name.text or "Following" == button_name.text or "Requested" == button_name.text or button_name.text == "Followed":
            print("Ya lo sigues")

        else:
            time.sleep(randint(100, 150))
            web.execute_script("arguments[0].click();", button_name)
            print(user_name.text + "->Seguido")
            time.sleep(randint(40, 50))


# src = ["jalasoft", "intellisysdcorp"]
src = ["tania_lucely"]


time.sleep(10)
for account in src:
    followers(account)
