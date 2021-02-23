import boto3 #pour l'accessibilité aux services AWS
import os #importer des fonctionalités de base 
from filecmp import cmp #comparer le contenu des fichiers


#les variables d'accessibilité 
cle_accee="minio"
cle_secret="miniokey"
bucket="mybucket"
chemin_repertoir="Path-to-the-Folder"

#connexion au service local
S3=boto3.client("s3",
		  endpoint_url="http://172.17.0.2:9000/",
                  aws_access_key_id=cle_accee, 
                  aws_secret_access_key=cle_secret)

#la liste des fichiers contenu dans Bucket
contenu=S3.list_objects(Bucket=bucket)

#si un fichier existe en local mais pas dans le bucket, on l’upload

for file in os.listdir(chemin_repertoir):
  if file not in contenu:
    S3.upload_file(Filename=file,Bucket=bucket,Key=file)

#si un fichier existe dans les deux, on met à jour la version du bucket si nécessaire
  if file in contenu:
    S3.download_file(Filename="compar.txt",Bucket=bucket,Key=file) #comparaison des deux fichiers 
    if cmp("compar.txt",file):
        S3.delete_object(Bucket=bucket,Key=file)
        S3.upload_file(Filename=file,Bucket=bucket,Key=file)

#si un fichier existe dans le bucket mais pas en local, on le supprime du bucket
for fileb in contenu:
  if fileb not in os.listdir(chemin_repertoir):
    S3.delete_object(Bucket=bucket,Key=fileb)




      
    





