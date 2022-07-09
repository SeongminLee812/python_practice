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

kospi_dict = dict()
kospi_dict['SK하이닉스'] = '000660'
kospi_dict['삼성전자'] = '005930'


#데이터 프레임에서 행선택 하기 위해서 str형식으로 변환
today_str = today.strftime('%Y-%m-%d')
print(today_str)

for key, val in zip(kospi_dict.keys(), kospi_dict.values()):
    open_price = fdr.DataReader(val, today).loc[today_str, 'Open']
    print(f'{key} \n'
          f'시작가격 :  {int(open_price)}원')

#
