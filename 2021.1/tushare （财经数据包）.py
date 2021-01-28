##tushare （财经数据包）
#import tushare as ts
#ts.get_today_all()
"""This script parse stock info"""
import tushare as ts
def get_all_price(code_list):
    '''process all stock'''
    df = ts.get_realtime_quotes(STOCK)
    print (df)

if __name__ == '__main__':
        STOCK = ['600219',
                 '000002',
                 '000623',
                 '000725',
                 '600036',
                 '601166',
                 '600298',
                 '600881',
                 '002582',
                 '600750',
                 '601088',
                 '000338',
                 '000895',
                 '000792',
                 '601006',
                 '600519',
                 '600839']
        get_all_price(STOCK)




