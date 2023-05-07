"""
Author: Keerthhi
Date: 7th May 2023
Description: sample python code for working with aws iot core
"""
import time
from typing import Any
import boto3
from .thing_properties import ThingProperties


class ThingManager:
    """
    Class object to manage things in AWS IoT Core.
    """

    def __init__(self) -> None:
        self.client = boto3.client('iot')

    def create_thing(self) -> ThingProperties:
        """
        Creates a new thing in AWS IoT Core.
        In a real project, you may want to keep some information in a database.
        For example, you may want the thing assigned to a tenant, site, etc.
        """
        # Create an object to hold all the properties of the thing
        newthing_obj = ThingProperties()

        # Add a new thing
        newthing_obj.thing_name = 'gateway_1'
        response = self.client.create_thing(thingName=newthing_obj.thing_name)

        # Wait for the thing to be created
        time.sleep(5)

        # Create a certificate for the thing
        response = self.client.create_keys_and_certificate(setAsActive=True)

        # Download the certificate files
        newthing_obj.cert_pem = response['certificatePem']
        newthing_obj.private_key_pem = response['keyPair']['PrivateKey']
        newthing_obj.public_key_pem = response['keyPair']['PublicKey']

        # Attach the certificate to the thing
        response = self.client.attach_thing_principal(
            thingName=newthing_obj.thing_name,
            principal=response['certificateArn'])

        # Get the IoT endpoint
        newthing_obj.endpoint = self.client.describe_endpoint(
            endpointType='iot:Data-ATS')['endpointAddress']

        return newthing_obj

    def delete_thing(self, thing_name: str) -> Any:
        """
        Deletes a thing from AWS IoT Core.
        In a real project, you may want to update the database accordingly.
        """

        # Get the certificate ARN for the thing
        lst_prince = self.client.list_thing_principals(thingName=thing_name)
        if len(lst_prince['principals']) > 0:
            certificate_arn = lst_prince['principals'][0]
            certificate_id = certificate_arn.split('/')[-1]

            # Detach the certificate from the thing
            response = self.client.detach_thing_principal(
                thingName=thing_name, principal=certificate_arn)

            # Update certificate status to INACTIVE
            response = self.client.update_certificate(
                certificateId=certificate_id, newStatus='INACTIVE')

            # Delete the certificate
            response = self.client.delete_certificate(
                certificateId=certificate_id)

        # Delete the thing
        response = self.client.delete_thing(thingName=thing_name)
        return response
