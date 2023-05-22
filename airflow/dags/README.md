### Airflow Create Connection
#### How to:
1. Go to Menu.
2. Cick on Admin.
3. Click on Connections.
4. Create new connectino.

#### Create these connections:
-----------------------------------------------------------------------------------------

### Connect to local postgreSQL server.
#### Fill out connection information :

Connection Id = postgres_local

Connection Type = Postgres

("Host will change if you aren't running airism in docker.
Host = host.docker.internal

Schema = DE

Login = postgres

Password = password

Port = 5432

-----------------------------------------------------------------------------------------

### Connect to S3 bucket 
#### Fill out connection information 

Connection Id = S3_conn

Connection Type = Amazon Web Services

AWS Access Key ID = <your access key>

AWS Secret Access Key = <your secret access key>

Extra =  { "aws_access_key_id": "your_access_key",
           "aws_secret_access_key": "your_secret_access_key",
           "region_name" : "your region" }

-----------------------------------------------------------------------------------------

### Airflow Create Variables
#### How to:
1. Go to Menu.
2. Click on Admin.
3. Click on Variable.
4. Create new variable.

#### Create these variables : 

##### BUCKET_NAME = < S3 bucket name>
##### LOCAL_PATH = C:\\Users\\<user name>\\<airflow_folder>\\plugins\\user_purchase.csv
##### aws_default = aws://
----------------------------------------------------------------------------------------

Since this is an airflow run from a docker in Windows 10. 
Change the permission to allow all for the plugins folder.
Or postgres will not be able to write to it.

1. Go to Properties of that particular file by right clicking on it.
2. Then, go to Security tab of the displayed Properties dialog box. 
3. Click on Edit option.
4. Permissions dialog box appears, then click on Add button. 
5. Type 'Everyone' (without apostrophes) in the "Enter the object names to select" description box 
    and click on OK button. 
6. Then, make sure all the checkboxes of "Permissions for Everyone" are selected by 
    just ticking the "Full Control" check box to allow the control access without any restriction.
7. Then, Apply and OK all the tabs to apply all the changes done.
