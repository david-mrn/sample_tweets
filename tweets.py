import random
random.seed(44)

# Sample user data
users = [
    {"name": "John Doe", "username": "@johndoe123", "verified": False},
    {"name": "Alice Smith", "username": "@alice23", "verified": True},
    {"name": "Bob Johnson", "username": "@bob88", "verified": False},
]

# Sample tweet content
tweet_content = [
    "Just had a fantastic weekend getaway! 🌞🏖️ #WeekendVibes",
    "Excited to announce our new product launch! 🚀 #ProductLaunch",
    "Enjoying some delicious tacos in Mexico City! 🌮 #MexicanFood",
    "Happy Independence Day, Mexico! 🇲🇽 #VivaMexico",
    "Exploring the beautiful beaches of Cancun! 🏖️ #Travel",
    "Watching the sunset over the Mayan ruins in Tulum. 🌅 #Tulum",
    "Join us for our upcoming webinar on AI and technology! 🤖 #Webinar",
    "Celebrating my birthday with friends and family! 🎉🍰 #Birthday",
    "Just finished a great workout at the gym. Feeling pumped! 💪 #Fitness",
    "Attending a conference on renewable energy in Mexico City. ♻️ #Conference",
]

# Sample hashtags
hashtags = ["#WeekendVibes", "#ProductLaunch", "#MexicanFood", "#VivaMexico", "#Travel", "#Tulum", "#Webinar", "#Birthday", "#Fitness", "#Conference"]

# Generate 250 tweets with geodata in Mexico and 250 tweets with random geodata
tweets = []
used_timestamps = set()

for _ in range(1000):
    user = random.choice(users)
    content = random.choice(tweet_content)
    timestamp = None
    while timestamp is None or timestamp in used_timestamps:
        timestamp = f"2023-09-{random.randint(1, 30):02d} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    used_timestamps.add(timestamp)
    
    retweets = random.randint(0, 1000)
    likes = random.randint(0, 2000)
    hashtags_used = random.sample(hashtags, random.randint(0, len(hashtags)))
    
    # Generate fictional geodata (latitude and longitude)
    if random.random() < 0.5:
        location = {
            "latitude": random.uniform(20.0, 30.0),  # Mexico latitude range
            "longitude": random.uniform(-120.0, -90.0),  # Mexico longitude range
            "place_name": "Mexico",
        }
    else:
        location = {
            "latitude": random.uniform(-90.0, 90.0),  # Random latitude range
            "longitude": random.uniform(-180.0, 180.0),  # Random longitude range
            "place_name": "Random Location",
        }
    
    tweet = {
        "user": user,
        "content": content,
        "timestamp": timestamp,
        "retweets": retweets,
        "likes": likes,
        "hashtags": hashtags_used,
        "mentions": [],
        "media_attachments": [],
        "geodata": location,
        "reply_to_tweet": None,
        "reply_to_user": None,
    }
    tweets.append(tweet)

# Print the list of simulated tweets
#for i, tweet in enumerate(tweets, start=1):
#    print(f"Tweet {i}:")
#    print(tweet)
#    print()
