FROM python:3.7
COPY . /app
WORKDIR /app
RUN python setup.py install
ADD crontab /etc/cron.d/cx-cron
RUN chmod 0644 /etc/cron.d/cx-cron
RUN touch /var/log/cron.log
RUN apt-get update
RUN apt-get -y install cron
CMD ["./start_server.sh"]
