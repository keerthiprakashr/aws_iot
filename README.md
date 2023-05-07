# AWS IOT Device management

## authenticate with aws cli to  provide access to aws iot  core services
https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html

run command to see the profile "aws configure list"

## to start the app 
flask run

## To Create thing in aws iot core
http://localhost:5000/registerdevice?thingname=gateway_123

## To delete thing in aws iot core
http://localhost:5000/deletedevice?thingname=gateway_123