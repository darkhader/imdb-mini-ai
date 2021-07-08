import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask
from flask import request
import json

class AppService:
    tasks = [
        {
            'id': 1,
            'name': "task1",
            "description": "This is task 1"
        },
        {
            "id": 2,
            "name": "task2",
            "description": "This is task 2"
        },
        {
            "id": 3,
            "name": "task3",
            "description": "This is task 3"
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get(self, title):
                ###### helper functions. Use them when needed #######
        def get_title_from_index(index):
            return df[df.index == index]["title"].values[0]

        def get_index_from_title(title):
            if df[df.title == title]["index"].size == 0:
                return title
            else:
                return df[df.title == title]["index"].values[0]
        ##################################################

        ##Step 1: Read CSV File
        df = pd.read_csv("move1.csv",encoding='iso-8859-1')
    #print df.columns
    ##Step 2: Select Features

        features = ['title','description']
    ##Step 3: Create a column in DF which combines all selected features
        for feature in features:
            df[feature] = df[feature].fillna('')

        def combine_features(row):
            try:
                return row['title'] +" "+row['description']
            except:
                print("Error:", row)

        df["combined_features"] = df.apply(combine_features,axis=1)

        #print "Combined Features:", df["combined_features"].head()

        ##Step 4: Create count matrix from this new combined column
        cv = CountVectorizer()

        count_matrix = cv.fit_transform(df["combined_features"])

        ##Step 5: Compute the Cosine Similarity based on the count_matrix
        cosine_sim = cosine_similarity(count_matrix) 
        movie_user_likes = title
        movie_index = title
        ## Step 6: Get index of this movie from its title
        movie_index = get_index_from_title(movie_user_likes)

        similar_movies =  list(enumerate(cosine_sim[movie_index]))

        ## Step 7: Get a list of similar movies in descending order of similarity score
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
        print(sorted_similar_movies)
        ## Step 8: Print titles of first 50 movies
        i=0
        output = []
        for element in sorted_similar_movies:
                print(element[0])
                output.append(get_title_from_index(element[0]))
                i=i+1
                if i>50:
                    break
            return json.dumps(output)