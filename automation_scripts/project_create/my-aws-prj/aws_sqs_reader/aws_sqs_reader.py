import time
import boto3

def read_sqs_queue(queue_url):
    """
    Reads messages from an SQS queue and prints the message body to the console.

    :param queue_url: The URL of the SQS queue to read from.
    """

    # Create an SQS client
    sqs = boto3.client('sqs')

    # Receive messages from the SQS queue
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )

        # Check if any messages were received
        if 'Messages' in response:
            # Process each message
            for message in response['Messages']:
                # Extract the message body
                message_body = message['Body']

                # Print the message body
                print(f'Received message: {message_body}')

                # Delete the message from the queue
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        else:
            # No messages were received, sleep for 5 seconds and try again
            print('No messages received. Sleeping for 5 seconds...')
            time.sleep(5)
            