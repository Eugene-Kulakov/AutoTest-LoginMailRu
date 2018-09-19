from selenium import webdriver
import secret # заполните данные для авторизации в файле secret.py
from POM import LoginPage, NewLetter


def main():
    driver = webdriver.Firefox()
    loginPage = LoginPage(driver)
    loginPage.openUrl('https://mail.ru')
    if not loginPage.checkIfLoggedIn(secret.username):
        loginPage.setLogin(secret.username)
        loginPage.setPassword(secret.password)
        loginPage.clickSignIn()
    newLetter = NewLetter(driver)
    newLetter.openNewLetter()
    newLetter.setAddressTo(secret.addressTo)
    newLetter.setSubject('Тест Python, Selenium, Page Object')
    newLetter.setText('\tТекст письма.\nЭто письмо отправлено автоматически, не отвечайте на него.')
    newLetter.clickSendButton()
    if newLetter.checkSend():
        print('Письмо отправлено')
    else:
        print('Что-то пошло не так, письмо не отправлено')
    print('Для выхода нажмите enter')
    input()


if __name__ == '__main__':
    main()
