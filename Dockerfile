FROM ubuntu:20.04
RUN apt-get update && apt-get install -y wget
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN apt-get install -y python3-pip
ENV GECKODRIVER_VERSION=v0.33.0
RUN wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKO>
RUN tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver
RUN rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz
RUN apt install -y firefox
RUN pip3 install selenium requests
ADD main.py . usernames .
CMD ["python]
