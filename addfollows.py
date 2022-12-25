from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
    web.get("https://www.instagram.com/" + account)
    time.sleep(5)
    web.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]"
                               "/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
    i = 1
    window = web.find_element(By.XPATH, "//div[@class='_aano']")

    time.sleep(5)
    while True:
        if i == 15:
            break
        web.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                           window)
        time.sleep(5)
        i += 1
    time.sleep(5)

    follower = web.find_elements(By.XPATH,
                                 "//div[@class='_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
    print("--------")
    print("total de busqueda:", len(follower))
    print("--------")

    time.sleep(5)
    for child in follower:
        print(child.get_attribute("outerHTML"))
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")

        if "Seguir" == button_name.text or "Follow" == button_name.text:
            web.execute_script("arguments[0].click();", button_name)
            print(user_name.text + "Seguido")
            time.sleep(15)
        else:
            print("Ya lo sigues")
            time.sleep(1)


src = ["sktech_786", "soytechnove", "tech4dev", "developers_community_._",
           "the_smart_dev", "art0xdev", "dev_steph", "developers_society", "midu.dev"]

login("user", "password")
time.sleep(5)
for account in src:
    followers(account)
