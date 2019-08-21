import random
articles = ["The", "Two", "Ten", "Your", "Four", "Three", "Five"]
adjective = ["Fumbling", "United", "Serene", "Calm", "Agitated", "Crazy", "Jumping", "Leaping"]
noun = ["Lunatics", "Animals", "Mountains", "Ballerinas", "Snowflakes", "Spiders"]

articles_len = len(articles) -1
adj_len = len(adjective) -1
noun_len = len(noun) -1

articles_rand = random.randint(0, articles_len)
adj_rand = random.randint(0, adj_len)
noun_rand = random.randint(0, noun_len)

print(articles[articles_rand] + " " + adjective[adj_rand] + " " + noun[noun_rand])
