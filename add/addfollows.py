from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint

web = webdriver.Chrome()
web.get('https://www.instagram.com')
time.sleep(3)


def login(user, passe):
    time.sleep(3)
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


def followers(account):
    web.get("https://www.instagram.com/" + account + "/followers/")
    time.sleep(10)
    i = 1
    window = web.find_element(By.XPATH, "//div[@class='_aano']")

    time.sleep(5)
    while True:
        if i == 200:
            break
        web.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                           window)
        time.sleep(1)
        i += 1
    time.sleep(5)

    follower = web.find_elements(By.XPATH,
                                 "//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
    print("--------")
    print("total de busqueda:", len(follower))
    print("--------")
# > div > div > span > a > span > div
    time.sleep(5)
    for child in follower:
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")

        time.sleep(randint(100,150))
        if "Seguir" == button_name.text or "Follow" == button_name.text:
            web.execute_script("arguments[0].click();", button_name)
            print(user_name.text + "->Seguido")
            time.sleep(randint(40,50))
        else:
            print("Ya lo sigues")
            time.sleep(1)


src = ["soydalto"]

login("", "")

time.sleep(5)
for account in src:
    followers(account)
