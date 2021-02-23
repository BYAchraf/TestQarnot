# Synchronisation S3
### Avant d’exécuter le fichier il faut renommer:
- Bucket=""
- Chemin_répertoire=""
- Installer boto3, installer Docker et exécuter cette ligne:

```docker run -it -e MINIO_ACCESS_KEY=minio -e MINIO_SECRET_KEY=miniokey minio/minio server /data```

- Par la suite il faut éxecuter le code.py.
