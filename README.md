# Information of HTTP server

[![CircleCI](https://circleci.com/gh/tuimac/servertools.svg?style=shield)](https://circleci.com/gh/tuimac/servertools)

This repository is small web application to get information from host server or container itself.
You can track the http accesses to each container or each host Server by this service.

## Who use it

If you want to test the communications through Load Balancer or Ingress,
maybe this application fit that.

## How it works

This application consist of Django Rest Framework which doesn't have models.
This application have several APIs to get information from each resources like EC2 meta-data or 
Container Network Interface Information and so on.
Each APIs return information is formatted by JSON and just display it.

If you want addtional information from different resources,
you can add APIs by `python3 manage.py startapp <resource name>`.

## How to deploy

There are three ways to deploy this application. This program need root privilege.

First, `git clone` like below
(Example)
```
$ git clone https://github.com/tuimac/servertools.git
$ cd servertools/servertools
$ sudo python3 manage.py runserver 0.0.0.0:80
```

Second, you can use the docker image I created.
(Example)
```
$ docker pull tuimac/servertools:latest
$ docker run -itd --name servertools -p 80:80 tuimac/servertools:latest
```

Third, use pip3 to install package to your python3 module directory and
create execution command. This program need root privilege.
(Example)
```
$ pip3 install git+https://github.com/tuimac/servertools.git
$ sudo servertools -m start
```
Help of servertools below:

```
usage: servertools [-h] -m MODE [-p PORT] [-i IPADDRESS]

Track HTTP request to the end of the host. 
ex) servertools --mode start -p 80

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  [Required]Select modes which are 'start', 'restart', 'stop' to execute servertools.
  -p PORT, --port PORT  [Optional]Direct port which servertools process use. Default is 80/tcp.
  -i IPADDRESS, --ipaddress IPADDRESS
                        [Optional]Direct listen ip address which servertools process use. Default is 0.0.0.0 .
```
Here is option for deploying this package to AWS EC2. Copy it and paste it to UserData section.

```
#!/bin/bash

yum update -y
yum install -y python3 git
pip3 install git+https://github.com/tuimac/servertools.git
servertools -m start -p 80
```
## How to uninstall

It's easy if you use `pip3`. 
This program deployed to the location need root privilege.

```
$ sudo pip3 uninstall servertools
```

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/servertools/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tuimac/servertools/LICENSE.md) file for details.
