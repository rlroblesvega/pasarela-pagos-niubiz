FROM ubuntu:latest
MAINTAINER My Name "royer@somecompany.com"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
EXPOSE 8081
CMD ["nginx","-g","daemon off;"]