import unittest
from unittest.mock import patch, MagicMock
import boto3
from moto import mock_dynamodb2
from cloudresumetestapi.lambda_function import lambda_handler

@mock_dynamodb2
class TestLambdaHandler(unittest.TestCase):

    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table_name = 'hikmet-cloud-resume-challenge'
        self.table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'ID',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'ID',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        self.table.put_item(Item={
            'ID': '1',
            'views': 0
        })

    @patch('cloudresumetestapi.lambda_function.dynamodb', boto3.resource('dynamodb', region_name='us-east-1'))
    def test_lambda_handler(self):
        event = {}
        context = {}

        response = lambda_handler(event, context)
        self.assertEqual(response, 1)

        item = self.table.get_item(Key={'ID': '1'})
        self.assertEqual(item['Item']['views'], 1)

if __name__ == '__main__':
    unittest.main()
