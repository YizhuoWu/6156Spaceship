# comment-service readme

### deployed link
http://ec2-18-206-107-25.compute-1.amazonaws.com/
port: 5000

### endpoints
```
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