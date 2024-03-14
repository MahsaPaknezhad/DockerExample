# Simple Dockerfile Example

## Install Docker

```
sudo apt install -y docker.io docker-compose python3-pip
```

Start Docker Deamon:

```
sudo systemctl start docker
```

Build Docker Image:

```
docker build -t python_modeltrainer .
```

Run the Image:

```
docker run python_modeltrainer
```

Run in an interactive way to see outputs of code:
```
docker run -t -i python_modeltrainer
```

Other useful commands:

```
docker ps # to see running docker images
docker ps -a # to see all docker images
docker start python_modeltrainer
docker exec -it python_modeltrainer /bin/sh # to enter the Image and execute commands
docker stop python_modeltrainer
docker run -p 8000:8000 python_modeltrainer # specify port number
```