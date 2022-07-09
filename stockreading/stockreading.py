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
kospi_dict['삼성전자우'] = '005935'
kospi_dict['kodex2차전지'] = '305720'


nasdaq_dict = dict()
nasdaq_dict['존슨앤존슨'] = 'JNJ'
nasdaq_dict['코카콜라'] = 'KO'
nasdaq_dict['애플'] = 'AAPL'


#데이터 프레임에서 행선택 하기 위해서 str형식으로 변환
today_str = today.strftime('%Y-%m-%d')

result_str = ''
result_str += '='*10 + '코스피' + '='*10

for key, val in zip(kospi_dict.keys(), kospi_dict.values()):
    open_price = fdr.DataReader(val, today).loc[today_str, 'Open']
    result_str += f'\n\n {key} \n 시작가격 :  {int(open_price)}원'

result_str += '\n' + '='*10 + '나스닥' + '='*10
for key, val in zip(nasdaq_dict.keys(), nasdaq_dict.values()):
    open_price = fdr.DataReader(val, today).loc[today_str, 'Open']
    result_str += f'\n\n {key} \n 시작가격 :  {float(open_price)}달러'

print(result_str)