
create external schema myspectrum_schema 
from data catalog 
database 'myspectrum_db' 
iam_role 'arn:aws:iam::552163833597:role/service-role/AmazonRedshift-CommandsAccessRole-20230512T054146'
create external database if not exists;
