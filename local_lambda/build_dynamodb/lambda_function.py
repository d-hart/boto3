import boto3
import logging

# set logging level; value options = CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logger = logging.getLogger('create_table')
logger.setLevel(logging.DEBUG)


def lambda_handler(client, boto):

    print("Starting the Lambda Function \n------------------------------------")
    print("Log stream name:", context.log_stream_name)
    print("Log group name:", context.log_group_name)
    print("Request ID:", context.aws_request_id)

    
    # We can use the low-level client to make API calls to DynamoDB.
    client = boto3.client('dynamodb', region_name='us-east-1')
    table_creation = table(client)
    logger.debug('Output from the table creation'+ str(table_creation))
    
def table(client):
    '''Create the dynamodb table

    Args:
        client: Dynamo DB boto3 client

    Returns:
        N/A
    '''
    try:
        resp = client.create_table(
            TableName="Books",
            # Declare your Primary Key in the KeySchema argument
            KeySchema=[
                {
                    "AttributeName": "Author",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "Title",
                    "KeyType": "RANGE"
                }
            ],
            # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
            AttributeDefinitions=[
                {
                    "AttributeName": "Author",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "Title",
                    "AttributeType": "S"
                }
            ],
            # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
            # You can control read and write capacity independently.
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        )
        print("Table created successfully!")
    except Exception as e:
        print("Error creating table:")
        print(e)
