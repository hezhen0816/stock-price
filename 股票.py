from tkinter.constants import Y
from typing import Text

import pandas as pd

import threading as thd
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote import command
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome = webdriver.Chrome()


#搜尋
def search(chrome):
    btn1.config(text='')
    btn2.config(text='')
    btn3.config(text='')
    btn4.config(text='')
    btn5.config(text='')

    chrome.get("https://www.google.com/finance/")
    Position = chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]')
    Position.send_keys(en.get())
    

    time.sleep(1)

    import bs4

    soup = bs4.BeautifulSoup(chrome.page_source, 'html.parser')
    titles = soup.find_all('div', {'role': 'option'})

    result = []

    for title in titles:
 
        post = title.find('div', {'class': 'CrPloe'})

        result.append((post.getText()))

    df = pd.DataFrame(result, columns=['股票列表'])

    for Stock_list in df:
        (btn1.config(text=(df.at[0, "股票列表"])))
        (btn2.config(text=(df.at[1, "股票列表"])))
        (btn3.config(text=(df.at[2, "股票列表"])))
        (btn4.config(text=(df.at[3, "股票列表"])))
        (btn5.config(text=(df.at[4, "股票列表"])))


def result1(chrome):
    Position=chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div[1]/div/div')
    Position.click()
def result2(chrome):
    Position=chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div')
    Position.click() 
def result3(chrome):
    Position=chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div[3]/div/div')
    Position.click()
def result4(chrome):
    Position=chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div[4]/div/div')
    Position.click()
def result5(chrome):
    Position=chrome.find_element_by_xpath('/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div[5]/div/div')
    Position.click()


def share_price():

    time.sleep(1)

    def fn():
        import bs4

        soup = bs4.BeautifulSoup(chrome.page_source, 'html.parser')
        titles = soup.find_all('div', {'class': 'kf1m0'})

        result = []

        for title in titles:
 
            post = title.find('div', {'class': 'YMlKec fxKbKc'})
            result.append((post.getText()))

        df = pd.DataFrame(result, columns=['股價'])

        lb1.config(text=(df.at[0, "股價"]))
        thd.Timer(1,fn).start()
    
    fn()

def statistical_data():
    Y

import time
import tkinter as tk



win = tk.Tk()
win.title('股票')
win.geometry('+400+200')
win.resizable(0,0)
win.config(background='#323232')
win.attributes("-topmost", True)


lb = tk.Label(background='#323232',foreground='white',text='股票名稱or代號',font=("",15))
lb.grid(row=0,column=0)


en = tk.Entry(font=("",15))
en.grid(row=1,column=0)


btn = tk.Button(text='搜尋',font=("",10),command=lambda:[search(chrome)])
btn.grid(row=2,column=0)


lb = tk.Label(background='#323232',foreground='white',text='搜尋列表',font=("",15))
lb.grid(row=3,column=0)


btn1 = tk.Button(text='',font=("",10),command=lambda:[result1(chrome),share_price()])
btn2 = tk.Button(text='',font=("",10),command=lambda:[result2(chrome),share_price()])
btn3 = tk.Button(text='',font=("",10),command=lambda:[result3(chrome),share_price()])
btn4 = tk.Button(text='',font=("",10),command=lambda:[result4(chrome),share_price()])
btn5 = tk.Button(text='',font=("",10),command=lambda:[result5(chrome),share_price()])
btn1.grid(row=4,column=0,)
btn2.grid(row=5,column=0,)
btn3.grid(row=6,column=0,)
btn4.grid(row=7,column=0,)
btn5.grid(row=8,column=0,)



lb = tk.Label(background='#323232',foreground='white',text='即時股價',font=("",15))
lb.grid(row=0,column=2)
lb1 = tk.Label(background='#323232',foreground='white',text='...',font=("",15))
lb1.grid(row=1,column=2)


lb = tk.Label(background='#323232',foreground='white',text='統計資料(十年)',font=("",15))
lb.grid(row=2,column=2)
lb = tk.Label(background='#323232',foreground='white',text='最低',font=("",15))
lb.grid(row=3,column=1)
lb = tk.Label(background='#323232',foreground='white',text='平均',font=("",15))
lb.grid(row=3,column=2)
lb = tk.Label(background='#323232',foreground='white',text='最高',font=("",15))
lb.grid(row=3,column=3)
lb = tk.Label(background='#323232',foreground='white',text='...',font=("",15))
lb.grid(row=4,column=1)
lb = tk.Label(background='#323232',foreground='white',text='...',font=("",15))
lb.grid(row=4,column=2)
lb = tk.Label(background='#323232',foreground='white',text='...',font=("",15))
lb.grid(row=4,column=3)


win.mainloop()