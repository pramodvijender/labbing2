FROM python:3.9
FROM --platform=linux/amd64 python:3.9
FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb

ENV GECKODRIVER_VERSION=v0.33.0
RUN wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz 
RUN tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver
RUN rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    apt-get purge firefox && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    #ln -s /opt/firefox/firefox /usr/bin/firefox && \
    mv /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP


RUN pip3 install selenium requests
ADD main.py . usernames .
