# NBA Data Lake Setup

This project demonstrates how to build a simple data lake for NBA sports analytics using AWS services and Python. The setup fetches NBA data from an external API, stores it in an AWS S3 bucket, creates a Glue database and table for processing, and configures Athena for querying.

## **Features**

    •	Automatically create an S3 bucket to store raw NBA player data.
    •	Fetch NBA data from an external API.
    •	Upload data to S3 in line-delimited JSON format.
    •	Set up an AWS Glue database and table for the data.
    •	Configure AWS Athena for querying the data.

## **Future Features**

    •	Look for a UI to show the data to users

To use this project, ensure you have:

    1.	Python 3.7 or higher installed.
    2.	AWS credentials configured with appropriate permissions for S3, Glue, and Athena.
    3.	An .env file set up with the following variables:

    ```bash
        REGION=your-aws-region
        BUCKET_NAME=your-unique-s3-bucket-name
        GLUE_DATA=your-glue-database-name
        NBA_API_KEY=your-nba-api-key
        NBA_ENDPOINT=your-nba-api-endpoint
    ```
