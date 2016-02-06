#!/bin/bash
cp -R lib/python2.7/site-packages/* ./build
cp lambda_function.py ./build
cp config.json ./build
cd build
zip -r ../icinga2ack-lambda.zip ./*
