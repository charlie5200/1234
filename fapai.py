import requests
import streamlit as st
url = 'https://invoice.etax.nat.gov.tw/index.html'
# 取得網頁html
web = requests.get(url)    
# 設置編碼，避免中文亂碼
web.encoding='utf-8'       

pip install beautifulsoup4
from bs4 import BeautifulSoup
# 轉換成標籤樹
tree = BeautifulSoup(web.text, "html.parser")  
# 取出開獎月份
issue = tree.select(".carousel-item")[0].getText(); 
st.write(issue)
# 取出中獎號碼陣列
winlist = tree.select('.container-fluid')[0].select('.etw-tbiggest')  
#特別獎
nss = winlist[0].getText()  
#特獎
ns = winlist[1].getText() 
# 頭獎
n1 = [winlist[2].getText()[-8:], winlist[3].getText()[-8:], winlist[4].getText()[-8:]] 
st.write("特別獎:\n" + "　　"+nss + "\n")
st.write("特獎:\n"+"　　" + ns + "\n")
st.write("頭獎:")
for j in n1:
  st.write("　　"+j)
st.write("\n")
while True:
    try:
        # 對獎
        st.title(inputnum = input('輸入發票號碼：'))
        if inputnum == nss: print('中 1000 萬元！')
        if inputnum == ns: print('中 200 萬元！')
        for i in n1:
            if inputnum == i:
                st.write('中 20 萬元！')
                break
            if inputnum[-7:] == i[-7:]:
                st.write('中 4 萬元！')
                break
            if inputnum[-6:] == i[-6:]:
                st.write('中 1 萬元！')
                break
            if inputnum[-5:] == i[-5:]:
                st.write('中 4000 元！')
                break
            if inputnum[-4:] == i[-4:]:
                st.write('中 1000 元！')
                break
            if inputnum[-3:] == i[-3:]:
                st.write('中 200 元！')
                break
    except:
      st.write("再接再厲") 
      break
