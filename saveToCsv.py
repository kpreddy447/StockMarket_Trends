from io import StringIO
import logging


# Set up logging to append to the file instead of overwriting
logging.basicConfig(filename='log/stocks_log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s', filemode='a')

# Step 3: Save the Data to a CSV file in memory (using StringIO)
def save_to_csv(df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    # Example log message
    logging.info("Saving to csv file!")
    return csv_buffer.getvalue()