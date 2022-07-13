import FinanceDataReader as fdr
from datetime import date
import datetime
today = date.today()
today_wd = today.weekday()

weekend = ''

if today_wd == 5:
    today -= datetime.timedelta(days=1)
    weekend = '토요일'
elif today_wd == 6:
    today -= datetime.timedelta(days=2)
    weekend = '일요일'

warning = f'오늘은 {weekend}이므로 금요일 기준으로 제공합니다.'

#코스피 딕셔너리
kospi_dict = dict()
kospi_dict['SK하이닉스'] = '000660'
kospi_dict['삼성전자'] = '005930'
kospi_dict['삼성전자우'] = '005935'
kospi_dict['kodex2차전지'] = '305720'

# 나스닥 딕셔너리
nasdaq_dict = dict()
nasdaq_dict['존슨앤존슨'] = 'JNJ'
nasdaq_dict['코카콜라'] = 'KO'
nasdaq_dict['애플'] = 'AAPL'


#데이터 프레임에서 행선택 하기 위해서 str형식으로 변환
today_str = today.strftime('%Y-%m-%d')

result_str = ''
result_str += '='*10 + '코스피' + '='*10

print(today - datetime.timedelta(1))

for key, val in zip(kospi_dict.keys(), kospi_dict.values()):
    #주말일 경우 금요일 마감 가격을 보여주기
    if today_wd >= 5:
        open_price = fdr.DataReader(val, today).loc[today_str, 'Close']
        result_str += f'\n\n {key} \n 마감가격 :  {int(open_price)}원'
    else:
        open_price = fdr.DataReader(val, today).loc[today_str, 'Open']
        result_str += f'\n\n {key} \n 시작가격 :  {int(open_price)}원'
        if fdr.DataReader(val, today).loc[today_str, 'Close']:
            today_close_price = fdr.DataReader(val, today).loc[today_str, 'Close']
            result_str += f'\n\n {key} \n 마감가격 :  {int(today_close_price)}원'

result_str += '\n' + '='*10 + '나스닥' + '='*10
for key, val in zip(nasdaq_dict.keys(), nasdaq_dict.values()):
    if today_wd >= 5:
        open_price = fdr.DataReader(val, today).loc[today_str, 'Close']
        result_str += f'\n\n {key} \n 마감가격 :  {float(open_price)}달러'
    else:
        yesterday = today - datetime.timedelta(1)
        yesterday_str = yesterday.strftime('%Y-%m-%d')
        open_price = fdr.DataReader(val, yesterday).loc[yesterday_str, 'Close']
        result_str += f'\n\n {key} \n 어제종가 :  {float(open_price)}달러'



print(result_str)