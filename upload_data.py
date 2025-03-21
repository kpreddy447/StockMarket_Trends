
import boto3
import logging

logging.basicConfig(filename='logfile/stocks_log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def upload_to_s3(bucket_name, file_content, file_name):
    s3 = boto3.client('s3')  # Set up your awscli
    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        logging.info(f'File {file_name} uploaded to S3 bucket {bucket_name}.')
    except Exception as e:
        logging.error(f"Failed to upload file to S3: {e}")
