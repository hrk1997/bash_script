#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#**************     THIS CODE WILL PRINT ACCORDING TO THE NAME AND THE LINK IN PATTERN    ***********************************
#           
#            *  _price : will be having an extra space
#            *  bash stock_watch_add.sh >> /home/hrk/Desktop/my_code/bash_script/stock_watch.py
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#!/bin/bash
read name
read link

echo "$name = BeautifulSoup(requests.get('$link').text, 'lxml')"
echo "$name _price = $name.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text"
echo "print('$name     :: ' + $name _price)"
print('                            ')
print('                            ')

# nifty50 = BeautifulSoup(requests.get('https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI&.tsrc=fin-srch').text, 'lxml')
# nifty50_price = nifty50.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text

# print('SBI_CARD     :: ' + sbi_price)
# print('                            ')
