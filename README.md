# Yolov5 trained on nlf helmet detection - inference on ec2

## installation (on ec2 console)
- clone this repository
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

## how to use
In  ```main.py``` you can find two endpoint:
-  ```[base_path]/``` -> ```[GET]``` return a simple string, useful for testing the connectivity
-  ```[base_path]/predict``` ->```[POST]``` accept image as param, return the bounding boxes for each helmet detected in this format:
```
{
   "b_boxes_positions":[
      {
         "class":0.0,
         "confidence":0.8507136106491089,
         "x1":980.6962890625,
         "x2":1015.0054931640625,
         "y1":523.5577392578125,
         "y2":555.052978515625
      },
      ...
      ]
   }
```
## model
in the ```model``` folder you can find the weigths for the yolov5s trained on nfl dataset. More details: https://www.kaggle.com/c/nfl-health-and-safety-helmet-assignment

**Note**: this was for educational purpose, trained with few epochs. Performance was not the main goal!