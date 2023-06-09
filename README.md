# AWS IOT Device management

#### Note
This code has been tested on Ubuntu 22.10. Please note that the instructions provided in this README may differ slightly if you are using a different operating system such as Windows or macOS.

## Prerequisites

First you need to configure access to AWS. The easiest method is to login using AWS CLI on the server where this code has to run. 

To configure your AWS access keys, follow these steps:

1. Install the AWS CLI on your local machine.
2. Run `aws configure` and follow the prompts to enter your access keys.
3. Run `aws configure list` to verify that your keys were configured correctly.

Authenticate with AWS CLI to provide access to AWS IoT Core services

Refer to [this documentation](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html) for instructions on how to authenticate with AWS CLI.


## Run this app

To run this app, please follow these steps:

1. Clone the code to your server.
2. Navigate to the `device_manager` folder.
3. Activate the virtual environment. 
```sh
. .venv/bin/activate
```
4. Install the dependencies using the `requirements.txt` file.
```sh
pip install -r requirements.txt
```

### Steps to start the app
```sh
flask run
```

## Methods
### To create a thing in AWS IoT Core
```sh
GET http://localhost:5000/registerdevice?thingname=<thing_name>
```
This will create a new thing in AWS IoT Core with the specified name.
example:
```sh
GET http://localhost:5000/registerdevice?thingname=gateway_123
```
### To delete a thing in AWS IoT Core
```sh
GET http://localhost:5000/deletedevice?thingname=<thing_name>
```
This will delete the specified thing from AWS IoT Core.
ecample:
```sh
GET http://localhost:5000/deletedevice?thingname=gateway_123
```

## License

This code is licensed under the MIT License. 
