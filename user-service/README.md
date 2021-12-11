# user-service readme

### Setup

First you need to connect to the EC2 instance:

```bash
ssh ec2-user@<user-service-ec2-ip> -i <user-services-key>
```

### Build

In the EC2 session, issue the commands as follow:

```bash
cd /home/ec2-user/6156Spaceship/user-service
docker build -t userservice:latest . # if the docker image is up-to-date, there is no need to issue this command
docker run -d -p 5000:5000 userservice
```

### Test

If the docker container runs successfully, you can test the user-service's api from anywhere. For example:

```bash
curl http://<user-service-ec2-ip>:5000/api/v1/users/wcunningham
```

Then it should return something like this:

```bash
{"address":"7024 Holly Park Apt. 410\nWilliamsfort, RI 48411","city":"North Kyleview","email":"Timothy.Watkins@columbia.edu","links":[{"rel":"self","url":"/api/v1/users/wcunningham"}],"state":"New Mexico","username":"wcunningham"}
```

### End Points

```bash
# return the profile of user with specified username
/users/<string:username> GET

# set the profile of user with specified username
# valid attributes: state, city, address, username, email
/users/<string:username> POST

# delete the profile of user with specified email
/users/<string:email> DELETE

# get profiles of all users
# supported filter: state, city, username, email
# supported pagination: offset, limit
/users GET
```

### Example Usage

```bash
GET http://127.0.0.1:5000/api/v1/users/danielleboyd
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
STATUS = 200

POST http://127.0.0.1:5000/api/v1/users/virginia14?update
body: {
    "street": "West 100 Street",
    "street2": "792 columbus avenue",
    "city": "new york city",
    "state": "NY",
    "zipcode": ""
}
response: {
    "address": "627 Hammond Extensions Apt. 851\nCookhaven, WV 81869",
    "city": "new york city",
    "email": "Anthony.Arnold@columbia.edu",
    "links": [
        {
            "rel": "self",
            "url": "/api/v1/users/virginia14"
        }
    ],
    "state": "NY",
    "username": "virginia14"
}

GET http://127.0.0.1:5000/api/v1/users?state=Florida
[
    {
        "address": "9095 Weber Vista\nGriffinview, CT 45795",
        "city": "Josephborough",
        "email": "Ronald.Nielsen@columbia.edu",
        "links": [
            {
                "rel": "self",
                "url": "/api/v1/users/jamesrichards"
            }
        ],
        "state": "Florida",
        "username": "jamesrichards"
    },
    {
        "address": "1238 Tamara Port Suite 681\nLake Danielle, WY 62671",
        "city": "Port Susan",
        "email": "Ashley.Walter@columbia.edu",
        "links": [
            {
                "rel": "self",
                "url": "/api/v1/users/phyllis90"
            }
        ],
        "state": "Florida",
        "username": "phyllis90"
    },
]
STATUS = 200
```
