#!/bin/bash

echo Install Node-Red
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)

sudo systemctl enable nodered.service
