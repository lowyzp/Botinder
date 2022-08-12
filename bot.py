from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TinderBot:
    
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=C:Users\\Luiz\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("profile-directory=Profile 2")
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.driver.get('https://tinder.com')
        sleep(5)

    def waitForLogin(self):
        print("Reach swipe page and press enter when you're ready.")
        input()

    def like(self):
        global likeBtn
        try:
            likeBtn = self.driver.find_element(by='xpath', value='//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')[1]
        except:
            try:
                likeBtn = self.driver.find_element(by='xpath', value='//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            except:
                pass
        finally:
            sleep(1)
            likeBtn.click()
            # try:
            #     sleep(3)
            #     if self.driver.find_element_by_xpath("//label[text()='Say something nice!']") is not None:
            #         sleep(3)
            #         fechar_janela_match = self.driver.find_element_by_xpath(
            #             "//button[@title='Back to Tinder']")
            #         sleep(3)
            #         fechar_janela_match.click()
            #         sleep(3)
            # except:
            #     pass

bot = TinderBot()
bot.waitForLogin()

while True:
    bot.like()
