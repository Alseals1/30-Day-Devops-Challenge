import boto3
import os
import json
import time
from dotenv import load_dotenv
import requests

load_dotenv()

region = os.getenv("REGION")
bucketName = os.getenv("BUCKET_NAME")
glue_database_name = os.getenv("GLUE_DATA")
API_KEY = os.getenv("NBA_API_KEY")
endpoint= os.getenv("NBA_ENDPOINT")

# Create clients
s3_client = boto3.client("s3", region_name=region)
glue_client = boto3.client("glue", region_name=region)
athena_client = boto3.client("athena", region_name=region)




athena_output_location = f"s3://{bucketName}/athena-results/"

# Create S3
def create_s3_bucket():
    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucketName)
        else:
            s3_client.create_bucket(
                Bucket=bucketName,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

# Creating Glue Database
def create_glue_database():
    try:
        glue_client.create_database(
            DatabaseInput={
                "Name": glue_database_name,
                "Description": "Glue database for NBA Data.",
            }
        )
        print(f"Glue database '{glue_database_name}' created successfully.")
    except Exception as err:
        print(f"Error creating Glue database: {err}")


def fetch_nba_data():
    try:
        header = {"Ocp-Apim-Subscription-Key": API_KEY}
        response = requests.get(endpoint, headers=header)
        response.raise_for_status()
        print("Fetch NBA data successfully..... YAY")
        return response.json()
      
    except Exception as err: 
        print(f"Ooops ===> Error fetching data {err}")
        return []
    

def convert_to_line_delimited_json(data):
    print("Converting data to line-delimited JSON format...")
    return "\n".join([json.dumps(record) for record in data])

# Uploading data to S3
def upload_data_to_s3(data): 
    try: 
        line_delimited_data = convert_to_line_delimited_json(data)


        # This define S3 object key
        file_key = "raw-data/nba_player_data.json"

        # Now this upload json data to s3
        s3_client.put_object(
            Bucket=bucketName,
            Key=file_key,
            Body=line_delimited_data
        )
        print(f"Successfully uploaded data to S3: {file_key}")
    except Exception as err:
        print(f"Ooops ===> Error uploading data to S3: {err}")

#Creating Glue table
def create_glue_table():
   
    try:
        glue_client.create_table(
            DatabaseName=glue_database_name,
            TableInput={
                "Name": "nba_players",
                "StorageDescriptor": {
                    "Columns": [
                        {"Name": "PlayerID", "Type": "int"},
                        {"Name": "FirstName", "Type": "string"},
                        {"Name": "LastName", "Type": "string"},
                        {"Name": "Team", "Type": "string"},
                        {"Name": "Position", "Type": "string"},
                        {"Name": "Points", "Type": "int"}
                    ],
                    "Location": f"s3://{bucketName}/raw-data/",
                    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                    "SerdeInfo": {
                        "SerializationLibrary": "org.openx.data.jsonserde.JsonSerDe"
                    },
                },
                "TableType": "EXTERNAL_TABLE",
            },
        )
        print(f"Glue table 'nba_players' created successfully.")
    except Exception as e:
        print(f"Ooops ===> Error creating Glue table: {e}")    

def configure_athena():
    """Set up Athena output location."""
    try:
        athena_client.start_query_execution(
            QueryString="CREATE DATABASE IF NOT EXISTS nba_analytics",
            QueryExecutionContext={"Database": glue_database_name},
            ResultConfiguration={"OutputLocation": athena_output_location},
        )
        print("Athena output location configured successfully.")
    except Exception as e:
        print(f"Error configuring Athena: {e}")

def main(): 
    print("Setting up data lake for NBA sports analytics...")
    create_s3_bucket()
    time.sleep(5)
    create_glue_database()
    nba_data = fetch_nba_data()
    if nba_data:
        upload_data_to_s3(nba_data)
    create_glue_table()
    configure_athena

    print("Data lake setup complete.")

if __name__ == "__main__":
    main()
