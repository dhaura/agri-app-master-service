# agri-app-master-service

Use below command to build docker image for Master Service compatible with RPI
```
docker build --platform=linux/arm/v7 -t dhaura/agri-app-master-new:latest -f Dockerfile .
```

Push to the DockerHub repo
```
docker push dhaura/agri-app-master-new:latest
```
