# demo-flask

### architecture
https://lucid.app/lucidchart/851b555d-060d-4b80-a17a-c498403d5a3d/edit?beaconFlowId=D158BA96BCCC408B&invitationId=inv_3d733721-3ba3-4205-99fe-c1da5663e045&page=0_0#

### deployed link
http://6156-final-proj-front-end.s3-website-us-east-1.amazonaws.com/

### Endpoints
```
GET /profile/:username/
return data format
    {
        "username": "",
        "address": ""
    }

POST /discover/:username?query="sports"

return data format
    {
        "username": "",
        "num_news": 2,
        "news": [
            {
                "news_id": 123,
                "content_summary": "",

            },
            {
                "news_id": 321,
                "content_summary": "",
            },
            ...
        ]
    }

GET /discover/:username/:newsid
    {
        "username": "",
        "news": {
            "news_id": 123,
            "content_full": "",
            "comments": [
                {
                    "username": "username2",
                    "comment_info": "test comment2",
                    "timestamp": "2021-10-31 14:12:11"
                },
                {
                    "username": "username1",
                    "comment_info": "test comment3",
                    "timestamp": "2021-10-31 14:02:11"
                },
                ...
            ]
        }
    }

POST /discover/post
body: {
    "news_id": 123,
    "username": "test_username"
    "comment_info": "test comment3"
}
return data type: 
{
    "username": "",
    "news": {
        "news_id": 123,
        "content_full": "",
        "comments": [
            {
                "username": "username2",
                "comment_info": "test comment2",
                "timestamp": "2021-10-31 14:12:11"
            },
            {
                "username": "username1",
                "comment_info": "test comment3",
                "timestamp": "2021-10-31 14:02:11"
            },
            ...
        ]
    }
}

```

### file-structure
```
/user-service
    /app.py
/news-service
    /app.py
/comment-service
    /app.py
/front-end
    /App.js
```

### install back-end 
```
cd user-service
python3 -m venv venv (only first time)
source venv/bin/activate
python3 -m pip install Flask==1.1.2
python3 -m pip freeze > requirements.txt
```

### run back-end (locally)
```
cd user-service
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
