import json
names = []
counter = 0
avg = 0
with open ("imdb_movies_1985to2022.json") as in_file:

    for line in in_file:
        movie = json.loads(line)
        
        actors = movie['actors']
        for actor in actors:
            counter += 1
            actor_name=actor[1]

            if actor_name == "Hugh Jackman":
                rating = movie["rating"]
                avg = rating['avg']/counter


        

    print(avg)
        
        


