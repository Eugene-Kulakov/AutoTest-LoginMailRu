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
    newLetter.setSubject('Тест для quality-lab')
    newLetter.setText('\tПривет, Лаборатория качества!\nЯ хочу работать у вас')
    newLetter.clickSendButton()
    if newLetter.checkSend():
        print('Письмо отправлено')
    else:
        print('Что-то пошло не так, письмо не отправлено')
    print('Для выхода нажмите enter')
    input()


if __name__ == '__main__':
    main()
