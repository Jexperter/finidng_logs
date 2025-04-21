import requests
import time

symbol = 'BTCUSDT'
url = f'https://fapi.binance.com/fapi/v1/openInterest?symbol={symbol}'

previous_oi = None  # Start with no previous value

while True:
    response = requests.get(url)
    data = response.json()
    
    current_oi = float(data['openInterest'])
    print(f"{data['symbol']} Open Interest: {current_oi}")
    
    if previous_oi is not None:
        difference = current_oi - previous_oi
        print(f"Difference: {difference}")
        
        if abs(difference) > 5:
            print("🚨 ALERT: Open Interest changed by more than 5!")
    
    previous_oi = current_oi  # Update for next comparison
    
    time.sleep(10)
