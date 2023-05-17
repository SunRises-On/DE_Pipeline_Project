### Set up redshift table

1. Create Redshift in same region as your s3 bucket.
2. Follow AWS instructions to set up your Redshift Serverless data warehouse.
4. Follow AWS instructions to make your Redshift Serverless public accessible.
5. Add your ip address to the inbound and outbound VPC security rules.
6. In setup fill out the config file with need variables.
7. Run the ingestion_main.py to set up external schema and tables.

