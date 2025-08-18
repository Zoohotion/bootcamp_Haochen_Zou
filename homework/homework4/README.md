# Data Acquisition Project - AAPL Stock Data

## Project Overview

This project pulls historical stock data for AAPL from an API and web scraping, saving the data as CSV files for further analysis.

## Data Sources

| Source           | Type      | Description                      | URL/Endpoint                 |
| ---------------- | --------- | -------------------------------| ----------------------------|
| Alpha Vantage    | API       | Historical stock price data     | https://www.alphavantage.co/ |
| Yahoo Finance    | Backup API| Stock data via yfinance library | https://finance.yahoo.com/   |
| Example Webpage  | Scraping  | Simple table data from webpage  | [Example URL]                |

## Environment & Dependencies

- Python 3.11(whatever..)  
- Dependencies listed in `requirements.txt`  
- API keys stored in `.env` and loaded with `python-dotenv`

## Usage Instructions

1. Clone the repository  
2. Create `.env` file with your API key  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
