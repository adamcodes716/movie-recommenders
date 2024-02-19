# movie-recommenders
Machine learning examples of various recommender systems

# author
adamcodes716  (https://adamcodes716.com)

# Description
This is an ongoing effort to demonstrate the various recommender systems.  
I am a HUGE fan of movies, and I love to mix my hobbies together. 

# Environment
This repo is light on packages so you shouldn't have a problem with versioning.  At time of this writing, I am using python 3.11.6
In the individual scripts, there are optional instructions for creating and activing virtual environments.

# ----------SCRIPTS-------------------

# MovieRecommender - Collaborative
This is an example of a collaborabitive recommender system.  
The script first compiles a list of movie reviews. It then allows us to compare a user's individual reviews in order to find user's with
similar tasts (e.g. nearest neighbors).  It then uses the neighbor's likes to provide a list of suggested movies for the user.
Note that this script requires a set of movie files.  I included /sample-data-small in the repo, but there are also instructions for using a large dataset.  Note that the key field here is "Item", which is the TMDB ID.  

# MovieRecommender - Individual
This script uses a list of movie reviews in order to find movies that are similar to a movie recommended by the user.

# MovieRecommender - Deep Learning
This script vectorizes a list of movies.  A movie is then submitted to the model and the script returns the movies that it sees
as being the most similar.

