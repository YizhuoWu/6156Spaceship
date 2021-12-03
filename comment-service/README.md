# comment-service readme

### deployed link
http://ec2-18-206-107-25.compute-1.amazonaws.com/
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

GET /discover/<username>/<newsid>

POST /discover/post
input data example:
{
    "news_id": 1,
    "username": "username1",
    "comment_info": "test comment again",
    "timestamp": "2021-10-10 10:10:11"
}

DELETE /discover/delete
input data example:
{
    "news_id": 1,
    "username": "username1",
    "comment_info": "test comment again",
    "timestamp": "2021-10-10 10:10:11"
}
```
