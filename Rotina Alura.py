#!/usr/bin/env python
# coding: utf-8

# In[23]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


# In[24]:


options = webdriver.ChromeOptions() 
options.add_argument('--headless')
# no caso do caminho do chrome os diretorios não podem ter espaço no nome.
options.add_argument("C:/Users/zuh/AppData/Local/Google/Chrome/UserData/Profile5/Accounts")

#acessando Alura
driver.get("https://www.alura.com.br/")
#pwindow = navegador.current_window_handle
print('Conexão Estabelecida')

print('acessando plataforma')
driver.find_element("xpath",'/html/body/div[1]/div/header/div/nav/div[1]/a[1]').click()
sleep(1)


driver.find_element("xpath",'//*[@id="login-email"]').send_keys("seu email aqui")
sleep(1)


driver.find_element("xpath", '//*[@id="password"]').send_keys("sua senha aqui")
sleep(1)


driver.find_element("xpath",'//*[@id="form-default"]/button').click()
sleep(1)

driver.find_element("xpath",'/html/body/main/div[2]/div/div/div[1]/div[2]/div[2]/a').click()

encerrado = print('Carregado')
#encerrado ciclo1

#acessando Youtube
driver.execute_script("window.open('https://www.youtube.com/watch?v=iLDqFVlZiog')")
print('Conexão Estabelecida')


# In[ ]:




