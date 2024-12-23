## Python Code to Fetch and Analyze Cryptocurrency Data Every 5 Minutes

### How to Run the Code

#### Step 1: Install Dependencies
Make sure you have Python installed. Then, install the required libraries by running:

```bash
pip install -r requirements.txt
```

#### Step 2: Run the Script
Execute the Python script to start fetching and analyzing cryptocurrency data:

```bash
python pipeline.py
```

### Overview
This script fetches cryptocurrency data from the CoinGecko API every 5 minutes, analyzes the data, and updates it into an Excel file. Key metrics include:
- Top 5 cryptocurrencies by market capitalization.
- Average price of all cryptocurrencies.
- The cryptocurrency with the highest 24-hour price change.
- The cryptocurrency with the lowest 24-hour price change.
