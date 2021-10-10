# demo-flask

### deployed link
http://6156-final-proj-front-end.s3-website-us-east-1.amazonaws.com/

### install back-end (first time)
```
cd back-end
python3 -m venv venv (only first time)
source venv/bin/activate
python3 -m pip install Flask==1.1.2
python3 -m pip freeze > requirements.txt
```

### run back-end (locally)
```
cd back-end
python3 app.py
```

### run front-end (locally)
```
cd front-end
npm start  

(endpoints)
"localhost:3000/", 
"localhost:3000/username/news/"
"localhost:3000/username/discover/"
"localhost:3000/username/profile/"
```
