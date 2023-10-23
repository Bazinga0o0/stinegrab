import time
from selenium import webdriver

url = 'https://stine.uni-hamburg.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000265,-Astartseite'
itanList = """001 575029
007 466741
013 278285
019 656513
025 278706
031 035552
037 694968
043 565434
049 100931
055 792677
002 935034
008 116895
014 539748
020 260572
026 916037
032 796379
038 190839
044 731641
050 184103
056 802574
003 926042
009 670491
015 152977
021 860503
027 492862
033 938911
039 209443
045 365650
051 001315
057 895382
004 461005
010 803380
016 780993
022 947790
028 884390
034 812915
040 203920
046 869803
052 191526
058 242107
005 099328
011 397851
017 766792
023 090108
029 833445
035 989551
041 937006
047 788771
053 211547
059 741453"""
# Starten Sie den Chrome-Browser

# Split the ITAN list into lines
itan_lines = itanList.split('\n')

# Search for the string "\n007" in each line
def findItan(itan):
    for line in itan_lines:
        if line.find(itan) != -1:
            if line[0:3]==itan:
                return line[4:]
    print('done')   
from selenium.webdriver.common.by import By
def checkverfügbar(anmelden : bool):
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
        us.send_keys('hier Benutzername einfügen')
        pw = driver.find_element(By.ID, 'Password')
        pw.send_keys('hier Passwort einfügen')
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
        while True:
            data = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/form/table/tbody/tr[9]/td[3]').text
            time.sleep(1)                         
            print(data)
            if data == '130 | 130':
                print('Keine neuen Plätze')
            else:
                print('Neue Plätze')
                if anmelden:
                    #time.sleep(10)
                    #table = driver.find_element(By.CSS_SELECTOR, "input.checkBox")
                    #table.click()
                    time.sleep(1)
                    button = driver.find_element(By.NAME, 'Next')
                    button.click()
                    time.sleep(1)
                    table = driver.find_element(By.CSS_SELECTOR, "input.checkBox")
                    table.click()
                    button = driver.find_element(By.NAME, 'Next')
                    button.click()
                    time.sleep(1)
                    tan = driver.find_element(By.CSS_SELECTOR, "input[name='tan_code']")
                    itanbeg = driver.find_element(By.CSS_SELECTOR, ".itan").text
                    tan.send_keys(findItan(itanbeg))
                    time.sleep(1)
                    button = driver.find_element(By.NAME, 'campusnet_submit')
                    #button.click()
                    
                    time.sleep(20)
            driver.refresh()
            time.sleep(20)
    print('done')
checkverfügbar(True)