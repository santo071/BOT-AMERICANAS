from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.americanas.com.br/produto/3680329351/ventilador-de-mesa-30cm-mondial-vsp-30-b-super-power-preto?pfm_carac=&pfm_index=NaN&pfm_page=especial&pfm_pos=maintop3&pfm_type=vit_spacey&offerId=6255c38187c00289c2d22cad&cor=Preto&voltagem=110V&condition=NEW")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/header/div[2]/button').click()

sleep(10)

driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div[1]/div[3]/a/span').click()


sleep(6)

driver.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/div[2]/div/div/div/div[2]/a/span').click()

slee
sleep(5)