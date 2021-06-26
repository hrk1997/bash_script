import requests
from bs4 import BeautifulSoup

sbi = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/SBICARD.NS?p=SBICARD.NS&.tsrc=fin-srch').text, 'lxml')
sbi_price = sbi.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

itc = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/ITC.NS?p=ITC.NS&.tsrc=fin-srch').text, 'lxml')
itc_price = itc.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

relaince = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/RELIANCE.NS?p=RELIANCE.NS&.tsrc=fin-srch').text, 'lxml')
relaince_price = relaince.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

tatamotors = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS&.tsrc=fin-srch').text, 'lxml')
tatamotors_price = tatamotors.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

wipro = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/WIPRO.NS?p=WIPRO.NS&.tsrc=fin-srch').text, 'lxml')
wipro_price = wipro.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

nifty50 = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI&.tsrc=fin-srch').text, 'lxml')
nifty50_price = nifty50.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

# ioc = BeautifulSoup(requests.get('').text, 'lxml')
# ioc_price = ioc.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

# ioc = BeautifulSoup(requests.get('').text, 'lxml')
# ioc_price = ioc.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

print('SBI_CARD     :: ' + sbi_price)
print('                            ')

print('ITC          :: ' + itc_price)
print('                            ')

print('WIPRO        :: ' + wipro_price)
print('                            ')

print('TATAMOTORS   :: ' + tatamotors_price)
print('                            ')

print('RELAINCE     :: ' + relaince_price)
print('                            ')

print('nifty50     :: ' + nifty50_price)
print('                            ')


# :::::::::::::::::::::::::::::::::::::  if you want to add a stock ::::::::::::::::::::::::::::::::

# CHANGE THE NAME IN THE CAP
# Get the yahoo-finace stock link

# NAME_OF_THE_STOCK = BeautifulSoup(requests.get('       LINK      ').text, 'lxml')
# STOCK_PRICE = .find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

#EXAMPLE
# sbi = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/SBICARD.NS?p=SBICARD.NS&.tsrc=fin-srch').text, 'lxml')
# sbi_price = sbi.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
