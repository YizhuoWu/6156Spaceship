# demo-flask

### architecture
https://lucid.app/lucidchart/851b555d-060d-4b80-a17a-c498403d5a3d/edit?beaconFlowId=D158BA96BCCC408B&invitationId=inv_3d733721-3ba3-4205-99fe-c1da5663e045&page=0_0#

### deployed link
http://6156-final-proj-front-end.s3-website-us-east-1.amazonaws.com/

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

### first time run front-end (locally)
```
cd front-end
touch .env  (add REACT_APP_API_KEY=XXXXXXXXXX in .env)
npm install
npm start
(localhost:3000)
```

### run front-end (locally)
```
cd front-end
npm install react-router-dom@5.2.0
npm start
```


# user-service

### deployed link
http://ec2-107-23-18-108.compute-1.amazonaws.com:5000/


### endpoints
```
GET /api/v1/users/danielleboyd
output data example:
{
    "address": "41506 Eric Port\nLoweland, DE 40062",
    "city": "New Ryan",
    "email": "Christina.Stokes@columbia.edu",
    "links": [
        {
            "rel": "self",
            "url": "/api/v1/users/danielleboyd"
        }
    ],
    "state": "New Mexico",
    "username": "danielleboyd"
}
```

# comment-service

### deployed link
http://ec2-34-201-102-112.compute-1.amazonaws.com
port: 5000

### endpoints
```
GET /discover/<newsid>
output data example:
{
    "newsid": 1,
    "comments": [
        {
            "username": "username1",
            "comment_info": "test comment info",
            "timestamp": "2021-10-10 10:10:11"
        },
        {
            "username": "charles57",
            "comment_info": "im charles57",
            "timestamp": "2021-10-11 10:11:11"
        }
        ...
    ]
}

POST /discover/post
input data example:
{
    "news_id": 1,
    "username": "username1",
    "comment_info": "test comment again",
    "timestamp": "2021-10-10 10:10:11"
}

DELETE /discover/delete  (temporaliy depreciated)
input data example:
{
    "news_id": 1,
    "username": "username1",
    "comment_info": "test comment again",
    "timestamp": "2021-10-10 10:10:11"
}
```

# news-service

### deployed link


### endpoints
```
GET /news
body: {
    labels: ["business", "technology"]
}

Description: Get a list of corresponding news with specific label via querying news RDS

output data example:
{
    "totalResults": 10,
    "news": [
        {
            "news_id": 0,
            "label": "business",
            "title": "business news title 0",
            "url": "www.google.com",
            "description": "business news description"
        },
        {
            "news_id": 3,
            "label": "technology",
            "title": "technology news title 3",
            "url": "",
            "description": "technologt news description"
        },
        ...
    ]
}
```


```
GET /news?newsid=1

Description: Get detailed news information with specific label 

output data example:
{
    "newsid": 1,
    "label": "technology",
    "title": "technology news title 3",
    "url": "",
    "description": "technology news description"
}
```

# user-labels-service

### deployed link

### dynamodb schema
```
user-labels table schema
{
    username: "charles57",
    labels: {
        "business": 2,
        "technolgy": 1
    }
}
```

### endpoints
```
GET /labels?username=charles57

Description:
1.Query users Dynamodb Table based on username (users table contains 2 keys: username(strin), labels(a list of strings))
2.Get user's labels (ex: labels:["business", "technology"])

```

# news-likes-service

### deployed link

### dynamodb schema
```
news table schema
{
    "news_id": "",
    "num_likes": 3,
}
```

### endpoints
```
GET /likes?newsid=<newsid>
Description: return number of likes associated with specific news
output data example:
{
    "news_id": 0,
    "num_likes": 11
}


POST /likes
body: {
    newsid: "1002"
}

1.Update "news" dynamodb table

(2).Update users labels
   fetch(GET newsid's labels)
   fetch(POST update "users-labels" dynamodb table)

Descirption: when user likes a news

1.Update dynamodb "news" 
increment num_likes value by 1

(2).Update "users" table
When user likes a news, add current news label to labels,
ex: (charles57's initial labels is {"business":2}, after he likes a news with "technology" label, update charles57's label to {"business":2, "technology:1"})
```


### Others
```
Avaialbale news labels:
business
entertainment
general
health
science
sports
technology

Discover Page (directly fetch news 3rd party API, independent from news service)
````
