import requests
from bs4 import BeautifulSoup

print('                            ')
banknifty = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/%5ENSEBANK?p=%5ENSEBANK&.tsrc=fin-srch').text, 'lxml')
banknifty_price = banknifty.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('banknifty     :: ' + banknifty_price)
print('                            ')
nifty50 = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI&.tsrc=fin-srch').text, 'lxml')
nifty50_price = nifty50.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('nifty50     :: ' + nifty50_price)
print('                            ')
sbi = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/SBIN.NS?p=SBIN.NS&.tsrc=fin-srch').text, 'lxml')
sbi_price = sbi.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('sbi     :: ' + sbi_price)
print('                            ')
reliance = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/RELIANCE.NS?p=RELIANCE.NS&.tsrc=fin-srch').text, 'lxml')
reliance_price = reliance.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('reliance     :: ' + reliance_price)
print('                            ')
jsw = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/JSWSTEEL.NS?p=JSWSTEEL.NS&.tsrc=fin-srch').text, 'lxml')
jsw_price = jsw.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('jsw     :: ' + jsw_price)
print('                            ')