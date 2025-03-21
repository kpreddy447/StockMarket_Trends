import schedule
import time
import logging
from fetch_data import fetch_data
from transform_data import transform_data
from upload_data import upload_to_s3
from datetime import datetime
import pandas as pd
from saveToCsv import save_to_csv
# from config import SYMBOLS

# Set up logging to append to the file instead of overwriting
logging.basicConfig(filename='log/stocks_log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s', filemode='a')

# Example log message
logging.info("Log setup successful!")

# Fetching and uploading data for each company
def fetch_and_upload():
    api_url = "https://www.alphavantage.co/query"
    api_key = "GET KEY"

    symbols = ["AAPL", "IBM"]  # List of companies

    # Create an empty DataFrame to accumulate data for all companies
    combined_df = pd.DataFrame()

    # Loop through all companies to fetch, transform and accumulate data
    for i in symbols:
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": i,
            "interval": "5min",
            "apikey": api_key
        }

        bucket_name = "Your_bucket_name"
        
        # Generate a unique file name with timestamp
        file_name = f"stock_price_combined_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

        # Fetch, transform, and upload the data
        try:
            # Step 1: Fetch data from the API with retries
            data = fetch_data(api_url, params)
            time_series = data['Time Series (5min)']

            # Step 2: Transform the data
            transformed_data = transform_data(time_series, i)

            # Append the transformed data to the combined DataFrame
            combined_df = pd.concat([combined_df, transformed_data], ignore_index=True)

            print(f"Data for {i}:")
            print(pd.DataFrame(transformed_data))

            # Step 3: Add a delay between API requests to avoid hitting rate limits
            time.sleep(12)  # Wait for 12 seconds (adjust according to API rate limits)

        except Exception as e:
            print(f"An error occurred while processing {i}: {e}")

    # After all data is collected, save the combined DataFrame to CSV
    if not combined_df.empty:
        file_content = save_to_csv(combined_df)

        # Step 4: Upload to S3
        upload_to_s3(bucket_name, file_content, file_name)
    else:
        print("No data was collected.")
# Schedule the task every 12 hours
schedule.every(12).hours.do(fetch_and_upload)

fetch_and_upload()
# Keep the scheduler running
if __name__ == "__main__":
     logging.info("Starting the scheduler...")
     while True:
         schedule.run_pending()
         time.sleep(1)  # Sleep for 1 second before checking again
