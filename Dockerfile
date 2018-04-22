# Set the base image
FROM ubuntu:16.04

# Dockerfile author / maintainer
MAINTAINER Gearoid Coughlan <gearoidc@gmail.com>

RUN apt-get update --fix-missing
RUN apt-get install -y apache2 python-pygame python-pathlib

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Expose apache.
EXPOSE 80

# Update the default apache site with the config we created.
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND
