from selenium import webdriver
from time import sleep


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def openUrl(self, url):
        self.driver.get(url)

    def closeBrowser(self):
        self.driver.close()


class LoginPage(Page):
    def setLogin(self, login):
        loginField = self.driver.find_element_by_id('mailbox:login')
        loginField.clear()
        loginField.send_keys(login)

    def setPassword(self, password):
        passwordField = self.driver.find_element_by_id('mailbox:password')
        passwordField.clear()
        passwordField.send_keys(password)

    def clickSignIn(self):
        loginButton = self.driver.find_element_by_id('mailbox:submit')
        loginButton.click()

    def checkIfLoggedIn(self, address):
        return True if address + '@mail.ru' in self.driver.page_source else False


class NewLetter(Page):
    def openNewLetter(self):
        self.driver.get('https://e.mail.ru/compose/')

    def setAddressTo(self, addressTo):
        addressToField = self.driver.find_element_by_xpath('//textarea[@class="js-input compose__labels__input"]')
        addressToField.send_keys(addressTo)

    def setSubject(self, subject):
        subjectField = self.driver.find_element_by_xpath('//input[@class="b-input"]')
        subjectField.send_keys(subject)

    def setText(self, text):
        # нажимаем кнопку "Убрать оформление", если находим её
        try:
            disableTextEditorA = self.driver.find_element_by_xpath(
                '//a[@class="mceToolbarLink mceToolbarLinkEnabled mce_enableTextEditor"]')
            disableTextEditorA.click()
        except:
            pass

        emailTextField = self.driver.find_element_by_xpath('//textarea[@class="bsbb composeEditor"]')
        emailTextField.clear()
        emailTextField.send_keys(text)

    def clickSendButton(self):
        self.driver.find_element_by_xpath(
            '//div[@class="b-toolbar__btn b-toolbar__btn_ b-toolbar__btn_false js-shortcut"]').click()

    def checkSend(self):
        sleep(1)
        return 'Письмо отправлено' in self.driver.title
