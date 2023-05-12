Directions to connect to local postgreSQL server:

# In the Airflow header go to Admin>Connection
# Create new connection using these parameters

Connection Type = Postgres
# inorder for docker ran in airflow to connect to localhost use host.docker.internal
Host = host.docker.internal
Schema = DE # Your schema
Login = postgres
Password = password