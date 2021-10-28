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
curl http://<user-service-ec2-ip>:5000/api/v1/users/js
```

Then it should return something like this:

```bash
{"address":"columbusave","links":[{"rel":"self","url":"/api/v1/users/js"}],"username":"js"}
```