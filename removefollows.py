from selenium import webdriver
import time

from selenium.webdriver.common.by import By

web = webdriver.Chrome();
web.get("https://www.instagram.com")
time.sleep(5)


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


def openmyfollowers(account_instagram):
    web.get("https://www.instagram.com/" + account_instagram)
    time.sleep(15)
    followbtn = web.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/"
                                           "div[1]/div[2]/section/main/div/header/section/ul/li[3]/a")
    followbtn.click()

    time.sleep(1)

    i = 1
    window = web.find_element(By.XPATH, "//div[@class='_aano']")

    while True:
        if i == 30:
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
        print(child.get_attribute("outerHTML"))
        user_name = child.find_element(By.CSS_SELECTOR, "div > div > div > div > a > span > div")
        button_name = child.find_element(By.CSS_SELECTOR,
                                         "div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm > button")

        print(user_name.text)
        print(button_name.text)
        print("------------")
        if "Siguiendo" == button_name.text or "Following" == button_name.text:
            web.execute_script("arguments[0].click();", button_name)
            time.sleep(2)
            unfollow = web.find_element(By.XPATH, "//button[@class='_a9-- _a9-_']")
            web.execute_script("arguments[0].click();", unfollow)
            print(user_name.text + " Eliminado")
        time.sleep(15)


login("user","password")
time.sleep(5)
openmyfollowers("urlFollowers")
time.sleep(2)
deletemyfollowers()
