import FinanceDataReader as fdr
from datetime import date
import datetime
today = date.today()

weekend = ''

if today.weekday() == 5:
    today -= datetime.timedelta(days=1)
    weekend = '토요일'
elif today.weekday() == 6:
    today -= datetime.timedelta(days=2)
    weekend = '일요일'

warning = f'오늘은 {weekend}이므로 금요일 기준으로 제공합니다.'

print(today)
kospi_dict = dict()
kospi_dict['SKhynic'] = '000660'
kospi_dict['Samsung_normal'] = '005930'

for key, val in zip(kospi_dict.keys(), kospi_dict.values()):
    print(f'{key} \n'
          f'시작가격 :  \n {fdr.DataReader(val, today)}')

#
# SKhynix = fdr.DataReader('000660', today)
# print(SKhynix[['Open', 'High', 'Low']])
#
# Samsung_normal = fdr.DataReader('005930', today)
# print(Samsung_normal)
#
# Samsung_first = fdr.DataReader('005935', today)
#

