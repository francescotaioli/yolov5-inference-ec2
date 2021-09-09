# Yolov5 trained on nlf helmet detection - inference on ec2

## installation (on ec2 console)
- pull this repository
- create conda env
- in the root folder, execute ```pip install -r requirements.txt```
- in the root folder, execute ```gunicorn --bind=0.0.0.0:8080 server:app```

you should see 
```
[2021-09-09 12:52:20 +0000] [45903] [INFO] Starting gunicorn 20.1.0
[2021-09-09 12:52:20 +0000] [45903] [INFO] Listening at: http://0.0.0.0:8080 (45903)
[2021-09-09 12:52:20 +0000] [45903] [INFO] Using worker: sync
[2021-09-09 12:52:20 +0000] [45904] [INFO] Booting worker with pid: 45904
```

## model
in the ```model``` folder you can find the weigths for the yolov5s trained on nfl dataset. More details: https://www.kaggle.com/c/nfl-health-and-safety-helmet-assignment

**Note**: this was for educational purpose, trained with few epochs. Performance was not the main goal!