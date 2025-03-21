 **Stock Market Data Fetcher**  

This project fetches real-time stock market data from the Alpha Vantage API, processes it, and uploads it to an AWS S3 bucket for further analysis. The script runs automatically every 12 hours and logs execution details.  

---

## **Table of Contents**  

- [Prerequisites](#prerequisites)  
- [Getting API Key from Alpha Vantage](#getting-api-key-from-alpha-vantage)  
- [Setting Up AWS S3](#setting-up-aws-s3)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Running the Script](#running-the-script)  
- [Automating the Process](#automating-the-process)  
- [Integrating with Power BI or Tableau](#integrating-with-power-bi-or-tableau)  

---

## **Prerequisites**  

1. **Python 3.8+** installed  
2. **AWS account** with an S3 bucket created  
3. **Alpha Vantage API key**  
4. **Git** installed for version control  
5. **Virtual environment (optional, but recommended)**  

---

## **Getting API Key from Alpha Vantage**  

1. Go to [Alpha Vantage](https://www.alphavantage.co/support/#api-key)  
2. Sign up for a free account  
3. Copy the API key from the dashboard  

---

## **Setting Up AWS S3**  

1. **Create an S3 bucket:**  
   - Log in to [AWS Console](https://aws.amazon.com/console/)  
   - Go to **S3** → Click **Create bucket**  
   - Give it a name (e.g., `stocksmarketdata`)  
   - Enable **public access block** (recommended)  
   - Click **Create bucket**  

2. **Set up AWS credentials:**  
   - Install the AWS CLI:  
     ```bash
     pip install awscli
     ```
   - Configure AWS credentials:  
     ```bash
     aws configure
     ```
     - Enter your **AWS Access Key ID**  
     - Enter your **AWS Secret Access Key**  
     - Set region (e.g., `us-east-1`)  
     - Default output format: **None**  

---

## **Project Structure**  

```
stockmarket/
│── data/                    # Stores extracted data (if needed locally)
│── logs/                    # Log files
├── main.py                  # Main script
├── fetch_data.py            # API call functions
├── transform_data.py        # Data transformation logic
├── upload_s3.py             # AWS S3 upload logic
├── scheduler.py             # Scheduling automation
│── requirements.txt         # Python dependencies
│── .gitignore               # Ignore unnecessary files
│── README.md                # Documentation
```

---

## **Installation**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/stockmarket-data.git
   cd stockmarket-data
   ```

2. **Set up a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Configuration**  

Update **`src/main.py`** with your API key and S3 bucket name:  

```python
API_KEY = "your_alpha_vantage_api_key"
BUCKET_NAME = "your_s3_bucket_name"
```

---

## **Running the Script**  

To fetch and upload stock data manually, run:  

```bash
python src/main.py
```

---

## **Automating the Process**  

We use **Python `schedule`** to run this script every 12 hours.  

Modify `scheduler.py`:  

```python
import schedule
import time
from main import fetch_and_upload

schedule.every(12).hours.do(fetch_and_upload)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
```

### **Run the Scheduler**  

```bash
python src/scheduler.py
```

**Stopping the Scheduler**  
Use `CTRL + C` to stop it.

For **Windows**, use **Task Scheduler** to run the script every 12 hours.

---

## **Integrating with Power BI or Tableau**  

### **Connecting S3 to Power BI**  
1. Open **Power BI Desktop**  
2. Go to **Get Data** → Select **Amazon S3**  
3. Enter your S3 bucket details  
4. Import and visualize the stock data  
