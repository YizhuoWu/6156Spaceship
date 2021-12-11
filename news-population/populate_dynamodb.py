# ref: https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/
from newsapi import NewsApiClient
from RDB_Application.RDBService import RDBService as RDBService

API_KEY = 'a7ba9dae22dd4951b49770d53ffb61de'

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')


# /v2/top-headlines/sources
# sources = newsapi.get_sources()

def insert_into_db(news_id, title, description, url, label):
	db_connection = RDBService.get_db_connection("news")
	cur_news_connection = db_connection

	with cur_news_connection:
		with cur_news_connection.cursor() as cursor:
			insert_sql = "INSERT INTO `db-news-schema`.`news_table` (`news_id`, `description`, `title`, `url`, `category`) VALUES (%s, %s, %s, %s, %s)"
			cursor.execute(insert_sql, (str(news_id), description, title, url, label))
		#cur_news_connection.commit()

	print("Finish insert all news to news-db.")
	print("")

def fetch_from_news_api():
	# Init
	newsapi = NewsApiClient(api_key=API_KEY)

	LABELS = ["sports", "business", "general", "science", "health", "technology", "entertainment"]
	ID = 1 #Initialize as 1

	for label in LABELS:
		print("====label:{}====".format(label))
		# /v2/everything
		# page size = 100 by default
		# Get 500 news for each labels
		res = newsapi.get_top_headlines(category=label,
										language='en',
										page_size=100,
									 	page = 1)

		status = res['status']
		# totalResults = res['totlaResults']
		articles = res['articles'] # []

		for article in articles:
			news_id = ID

			title = article["title"]
			description = article["description"]
			url = article["urlToImage"]

			print("news_id: ", news_id)
			print("url: ",url)
			print("title: ", title)
			print("description: ", description)
			print("")
			ID += 1

			#insert current news into news-db
			insert_into_db(news_id, title, description, url, label)


def main():
	#connect to news-db
	#db_connection = RDBService.get_db_connection("news")

	#fecth from news-api then insert into RDS DB
	fetch_from_news_api()

"""
execute script
"""
if __name__ == "__main__":
	main()