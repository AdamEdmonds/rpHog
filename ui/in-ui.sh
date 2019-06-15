#!/bin/bash

echo Install nginx
sudo apt-get install nginx

echo cp rpHog ui to defalt site
cp index.html /var/www/html/index.html
cp style.css /var/www/html/style.css
