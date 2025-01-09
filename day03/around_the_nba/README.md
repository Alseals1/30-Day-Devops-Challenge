# NBA Data Lake Setup

This project demonstrates how to build a simple data lake for NBA sports analytics using AWS services and Python. The setup fetches NBA data from an external API, stores it in an AWS S3 bucket, creates a Glue database and table for processing, and configures Athena for querying.

## **Features**

    -	Automatically create an S3 bucket to store raw NBA player data.
    -	Fetch NBA data from an external API.
    -	Upload data to S3 in line-delimited JSON format.
    -	Set up an AWS Glue database and table for the data.
    -	Configure AWS Athena for querying the data.

## **Next**

    Look for a UI to show the data to users

## To use this project, ensure you have:

1. Clone this repository.
2. Set up your environment variables in a `.env` file:
   - `REGION`: Your AWS region.
   - `BUCKET_NAME`: Name of your S3 bucket.
   - `GLUE_DATA`: Name of your Glue database.
   - `NBA_API_KEY`: Your NBA API key.
   - `NBA_ENDPOINT`: The NBA API endpoint.
3. Run the script:
   ```bash
   python3 nba_data_setup.py
   ```
