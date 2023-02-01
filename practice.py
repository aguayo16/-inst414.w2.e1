import json
names = []
counter = 0
avg = 0
total_rating = 0
with open ("imdb_movies_1985to2022.json") as in_file:

    for line in in_file:
        movie = json.loads(line)
        
        actors = movie['actors']
        for actor in actors:
            
            actor_name=actor[1]

            if actor_name == "Hugh Jackman":
                counter += 1
                rating = movie["rating"]
                total_rating += rating['avg']
        
print(total_rating/counter)
        
        


