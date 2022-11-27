from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)
nav.get("https://accounts.google.com/ServiceLogin/identifier")

#LOGIN com verificação
#nav.find_element(By.XPATH, '//*[@id="identifierId"]')
#nav.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
while len(nav.find_elements(By.XPATH, '//*[@id="identifierId"]')) < 1:
    print("Procurando input de email")
    time.sleep(1)
    if len(nav.find_elements(By.XPATH, '//*[@id="identifierId"]')) > 1:
        break
nav.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('')

while len(nav.find_elements(By.XPATH, '//*[@id="identifierNext"]/div/button/span')) < 1:
    print("Procurando botão")
    time.sleep(1)
    if len(nav.find_elements(By.XPATH, '//*[@id="identifierNext"]/div/button/span')) > 1:
        break
nav.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
print("Email ok")
time.sleep(5)
#-----------------------------#
#SENHA
#nav.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('')
#nav.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
while len(nav.find_elements(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')) < 1:
    print("Procurando input da senha")
    time.sleep(1)
    if len(nav.find_elements(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')) > 1:
        break
nav.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('')
nav.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
print("Login realizado com sucesso")
#-----------------------------#

#ACESSAR A CAIXA DE EMAIL
while len(nav.find_elements(By.ID, ':3')) < 1:
    print("Tentando acessar caixa de email")
    nav.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(10)
    if len(nav.find_elements(By.ID, ':3')) > 1:
        break

#nav.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
#nav.find_element(By.XPATH, '//*[@id=":jz"]').send_keys('Assunto teste')
while len(nav.find_elements(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')) < 1:
    print("Aguarde...")
    time.sleep(1)
    if len(nav.find_elements(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')) > 1:
        break
nav.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()

while len(nav.find_elements(By.XPATH, '//*[@id=":8u"]')) < 1:
    print("Aguarde...")
    time.sleep(1)
    if len(nav.find_elements(By.XPATH, '//*[@id=":8u"]')) > 1:
        break
nav.find_element(By.XPATH, '//*[@id=":8u"]').send_keys('Assunto teste')

