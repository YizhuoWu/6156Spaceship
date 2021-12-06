
# ref: https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/
import boto3
import botocore
from newsapi import NewsApiClient

# API_KEY = 'a7ba9dae22dd4951b49770d53ffb61de'

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table("news")
# print("table.creation_data_time:{}".format(table.creation_date_time))

# newsid = '1004'

# try:
# 	response = table.get_item(
# 		Key={
# 			'newsid': newsid
# 		}
# 	)
# 	item = response["Item"]
# 	print("item: ", int(item["num_likes"]))
# except Exception as e:
#     print("get item error, highly likely item does not exist.")
#     table.put_item(
# 	   Item={
# 	        'newsid': newsid,
# 	        'num_likes': 0
# 	    }
# 	)

"""
# get an item
response = table.get_item(
    Key={
        'newsid': '1003'
    }
)
print("response: ", response)
item = response['Item']
print(item)
"""


"""
# create new item
table.put_item(
   Item={
        'newsid': "1002",
        'num_likes': 2
    }
)
print("sucessfully put an item!")
"""


"""
# get an item
response = table.get_item(
    Key={
        'newsid': '1002'
    }
)
item = response['Item']
print(item)
"""

"""
# Init
newsapi = NewsApiClient(api_key=API_KEY)

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')


# /v2/top-headlines/sources
# sources = newsapi.get_sources()



LABELS = ["sports", "music", "politics", "science", "technology"]

for label in LABELS:
	print("====label:{}====".format(label))
	# /v2/everything
	res = newsapi.get_everything(q=label,
                                      # sources='bbc-news,the-verge',
                                      # domains='bbc.co.uk,techcrunch.com',
                                      # from_param='2017-12-01',
                                      # to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

	status = res['status']
	# totalResults = res['totlaResults']
	articles = res['articles'] # []

	for article in articles:
		source = article["source"]
		author = article["author"]
		title = article["title"]
		description = article["description"]
		content = article["content"]
		print("source: ", source)
		print("author: ", author)
		print("title: ", title)
		print("description: ", description)
		print("content: ", content)
		print("")
"""

"""
user-labels table schema
{
    username: "charles57",
    labels: {
        "business": 2,
        "technolgy": 1
    }
}

news table schema
{
    "news_id": "",
    "num_likes": 3,
}
"""
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    users_table = dynamodb.Table("user-labels")

    # params extracted from body
    newsid = '1004'
    username = "testuser_alpha_001"
    
    try:
    	response = users_table.get_item(
    		Key={
    			'username': username
    		}
    	)
    	item = response["Item"] # may raise exception!
    	print("item: ", item)
    	labels_freq_map = item["labels"]
    	for label, freq in labels_freq_map.items():
    		print("label={}, freq={}".format(label, freq))
    	return None
    	# return {
    	#     'statusCode': 200,
    	#     'body': json.dumps({
    	#         'username': username,
    	#         'newsid': newsid
    	#     })
    	# }
    except Exception as e:
        print("get item error, highly likely item does not exist.")
        default_labels = ["business","entertainment","general","health","science","sports","technology"]
        users_table.put_item(
    	   Item={
    	        'username': username,
    	        'labels': {label: 0 for label in default_labels}
    	    }#Item
    	)#table.put_item
        return None

lambda_handler(None, None)
