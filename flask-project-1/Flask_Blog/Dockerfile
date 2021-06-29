FROM custompython
COPY . /Flask_Blog
WORKDIR /Flask_Blog
RUN apt-get update && apt-get -y upgrade && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN chmod +x /Flask_Blog/docker-entrypoint.sh
ENTRYPOINT ["/Flask_Blog/docker-entrypoint.sh"]