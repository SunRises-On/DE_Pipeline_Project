### Set up redshift table

1. Create Redshift in same region as your s3 bucket.
2. Add IAM role to Redshift table to allow it to read s3 bucket.
3. Copy the ARN of the IAM role.
4. Add to the setup_external_schema.sql script.
4. Run setup_external_schema.sql in the SQL client.
5. Run setup_external_table.sql in the SQL client.
