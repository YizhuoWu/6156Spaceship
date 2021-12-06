import boto3
import json

notify_paths = {"path": ["/users"], "method": ["GET"]}


def notify(request):
    if request.path in notify_paths["path"] and request.method in notify_paths["method"]:
        message = {"path": request.path, "method": request.method}
        NotificationMiddlewareHandler.send_sns_message(
            "arn:aws:sns:us-east-1:951841085043:Service-Nofificaiton-Lambda",
            message
        )


class NotificationMiddlewareHandler:
    sns_client = None

    def __init__(self):
        pass

    @classmethod
    def get_sns_client(cls):

        if NotificationMiddlewareHandler.sns_client is None:
            NotificationMiddlewareHandler.sns_client = sns = boto3.client("sns",
                                                                          region_name="us-east-1")
        return NotificationMiddlewareHandler.sns_client

    @classmethod
    def send_sns_message(cls, sns_topic, message):

        s_client = NotificationMiddlewareHandler.get_sns_client()
        response = s_client.publish(
            TargetArn=sns_topic,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        print("Publish response = ", json.dumps(response, indent=2))
