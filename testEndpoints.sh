#!/bin/bash

ENDPOINT=https://9ismrec2of.execute-api.eu-west-1.amazonaws.com/Prod/

echo GET /
curl $ENDPOINT'?param0=foo&param1=bar'
echo


echo POST /
curl -d "param1=value1&param2=value2" -X POST $ENDPOINT
echo


echo GET /preview
curl $ENDPOINT'/preview/?param0=foo&param1=bar'
echo