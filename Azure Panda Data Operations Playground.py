# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:51:54 2023
At some point I was playing around with this in Azure
A config.json file will need to be created to use this.  Here is the sample
{
    "subscription_id": "91a0451cxxxxx",
    "resource_group": "movie-recommender",
    "workspace_name": "movie-recommender-first"
}
@author: adamcodes716
"""

from azureml.core import Workspace, Dataset

import pandas as pd

# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
#az_store          = Datastore.get(ws, 'movierecommenderfiles')
reviewer1_dataset = Dataset.get_by_name(ws, 'reviewer1_reviews')
reviewer2_dataset = Dataset.get_by_name(ws, 'reviewer2_reviews')
movies_dataset = Dataset.get_by_name(ws, 'movies')
ratings_dataset = Dataset.get_by_name(ws, 'ratings')
#az_default_store  = ws.get_default_datastore()


# -----------------------------------------------------
# Load the Azureml Dataset into the pandas dataframe
# -----------------------------------------------------
df_reviewer1 = reviewer1_dataset.to_pandas_dataframe()
df_reviewer2 = reviewer2_dataset.to_pandas_dataframe()
df_movies = movies_dataset.to_pandas_dataframe()
df_ratings = ratings_dataset.to_pandas_dataframe()
df_ratings.reset_index(drop=True, inplace=True)
print (df_ratings)

from lenskit.algorithms import Recommender
from lenskit.algorithms.user_knn import UserUser

num_recs = 10  #<---- This is the number of recommendations to generate. You can change this if you want to see more recommendations

user_user = UserUser(15, min_nbrs=3) #These two numbers set the minimum (3) and maximum (15) number of neighbors to consider. These are considered "reasonable defaults," but you can experiment with others too
algo = Recommender.adapt(user_user)
algo.fit(df_ratings)

print("Set up a User-User algorithm!")

# joined_data = reviewer1_recs.join(data.movies['genres'], on='item')   
joined_data = df_reviewer1.join(df_movies['genres'], on='item')






