from selenium.webdriver.common.by import By


class HomePage:
    lnk_signup_xpath="//span[@class='_1Mikcj']"
    lnk_login_xpath="//a[@class='wsejfv']"
    txt_username_xpath="//input[@class='r4vIwl BV+Dqf']"
    btn_reuestotp_xpath="//button[normalize-space()='Request OTP']"


    def __init__(self, driver):
        self.driver = driver

    def click_signup(self):
        self.driver.find_element(By.XPATH,self.lnk_signup_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()