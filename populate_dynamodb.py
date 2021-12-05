
# ref: https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/
import boto3
from newsapi import NewsApiClient

API_KEY = 'a7ba9dae22dd4951b49770d53ffb61de'

dynamodb = boto3.resource('dynamodb')

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

table = dynamodb.Table("news")
print("table.creation_data_time:{}".format(table.creation_date_time))
