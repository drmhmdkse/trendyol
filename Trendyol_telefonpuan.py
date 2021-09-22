#-*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.trendyol.com/cep-telefonu-x-c103498'



header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

response = requests.get(url,headers=header)



html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")




telefonlar_divi=soup.find("div", attrs={"class":"prdct-cntnr-wrppr"})


phone_names=[]
for i in range(20):
    

    names=telefonlar_divi.find_all("span",attrs={"class":"prdct-desc-cntnr-name hasRatings"})[i].text
    phone_names.append(names)

i=0
telefon_links=[]

for link in telefonlar_divi.find_all('a',  #### divin içindeki ilk 2o linki aldik
                          attrs={'href': re.compile("^/")}):
    
    # gercek url
    telefon_links.append("http://trendyol.com"+link.get('href')+"/yorumlar")
  
    
    
    
    i=i+1
    if(i==20): 
        
        break


############ her bir telefonun puanını  çekiyorum##################
telefon_puan=[]
olumlular=[]
olumsuzlar=[]
for i in range(20):
    
    url2 =str(telefon_links[i])
    response2 = requests.get(url2,headers=header)
    html_icerigi2 = response2.content
    soup = BeautifulSoup(html_icerigi2,"html.parser")    
    
    
    telefonlar_ort=soup.find("div", attrs={"class":"pr-rnr-sm-p"})
    olumsuz=soup.find("div", attrs={"class":"rating-filter-wrapper"})

    if telefonlar_ort is None:
        
        telefon_puan.append(4.4)#### bir tane yorumsuz olduğu için elle girdim
        olumsuzlar.append(0)
        olumlular.append(0)
        
    else:
        ekle=telefonlar_ort.find("span").text
        telefon_puan.append(float(ekle))
        ekle_olumsuz=int((olumsuz.find_all("span")[0].text).strip("()"))
        ekle_olumsuz2=int((olumsuz.find_all("span")[1].text).strip("()"))
        
        
        
        
        ekle_olumlu=int((olumsuz.find_all("span")[-1].text).strip("()"))
        ekle_olumlu2=int((olumsuz.find_all("span")[-2].text).strip("()"))
        oran=ekle_olumlu+ekle_olumlu2+ekle_olumsuz+ekle_olumsuz2
        olumlular.append((ekle_olumlu+ekle_olumlu2)*100/(ekle_olumlu+ekle_olumlu2+ekle_olumsuz+ekle_olumsuz2))
        olumsuzlar.append((ekle_olumsuz+ekle_olumsuz2)*100/(ekle_olumlu+ekle_olumlu2+ekle_olumsuz+ekle_olumsuz2))
        
 

    



birlestir={"tablet_marka":phone_names,"tablet_puan":telefon_puan,"olumlular":olumlular,"olumsuzlar":olumsuzlar}
df = pd.DataFrame(birlestir)


#################### exelle aktarma ############

#df.to_excel("eccxelim.xlsx", index = False)











