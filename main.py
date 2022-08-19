from yahoo_fin import stock_info as yf
import requests
import secret as s

def create_order(symbol, qty):
    data = {
        'symbol': symbol,
        'notional': qty,
        'side': 'buy',
        'type': 'market',
        'time_in_force': 'day'
    }
    r = requests.post(s.ORDERS_URL, json=data, headers=s.HEADERS)
    print(r)

if __name__ == '__main__':
    losers_list = (yf.get_day_losers())

    for i in range(5):
        if(float(losers_list['% Change'][i]) < -20):
            create_order(losers_list['Symbol'][i], '1')

