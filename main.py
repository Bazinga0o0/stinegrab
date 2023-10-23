import time
from selenium import webdriver

url = 'https://stine.uni-hamburg.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000265,-Astartseite'

# Starten Sie den Chrome-Browser
from selenium.webdriver.common.by import By
while True:
    driver = webdriver.Chrome()

    # Öffnen Sie die Website im Browser
    driver.get(url)

    # Rufen Sie den HTML-Code der Website ab
    html_code = driver.page_source

    # Schließen Sie den Browser
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[6]/div[2]/div/a[1]')
    button.click()
    time.sleep(1)

    us = driver.find_element(By.ID, 'Username')
    us.send_keys('hier username eingeben')
    pw = driver.find_element(By.ID, 'Password')
    pw.send_keys('hier pwd eingeben')
    button= driver.find_element(By.NAME, 'button')
    try:
        button.click()
    except:
        print("Login fehlgeschlagen, wahrscheinlich falsche Daten eingegeben")
        break
    time.sleep(1)
    try:
        button = driver.find_element(By.ID, 'link000270')
    except:
        print("Login fehlgeschlagen, wahrscheinlich falsche Daten eingegeben")
        break
    button.click()
    time.sleep(1)
    button = driver.find_element(By.ID, 'link000309')
    button.click()
    time.sleep(1)
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/ul/li[2]/a')
    button.click()
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/ul/li[2]/a')
    button.click()
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/table/tbody/tr[8]/td[4]/a')
    button.click()
    time.sleep(1)
    data = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/form/table/tbody/tr[9]/td[3]').text
    time.sleep(1)                         
    print(data)
    if data == '130 | 130':
        print('Keine neuen Plätze')
    else:
        print('Neue Plätze')
    driver.close()
    time.sleep(20)
