import pandas as pd
import logging 

logging.info("Transforming the data!")
logging.basicConfig(filename='logfile/stocks_log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def transform_data(data, Comp_name):
    filtered_data = []
    for time, values in data.items():
        filtered_data.append({
            "Company": Comp_name,
            "timestamp": time,
            "open": values["1. open"],
            "high": values["2. high"],
            "low": values["3. low"],
            "close": values["4. close"],
            "volume": values["5. volume"]
        })
    
    df = pd.DataFrame(filtered_data)
    return df