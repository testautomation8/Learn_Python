import pymongo
server_name = "mongodb+srv://m001-student:m001-mongodb-basics@cluster0-jxeqq.mongodb.net/test?retryWrites=true"
client = pymongo.MongoClient(server_name)
print(client.list_database_names())
client.close()
