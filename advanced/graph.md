---
layout: page
---

[Advanced Assignments](./)

### Graph Analysis 

* Released:
* Due:
* Max team of 2

  
Many graph analyses compute network centrality, density, shortest paths, and other path-based statistics about a graph.  It may seem that writing a one-off Python script is a good way to perform this analysis, but it turns out that SQL is pretty great at doing this type of analysis!  


For this assignment, you will replicate a summer research project to analyze Tweets from [Twitch streamers](http://www.twitch.com).  Twitch is an online platform for live-streaming people playing video games (and other activities such as cooking).   Our research group downloaded the tweets written by a set of Twitch streamers and are interested in understanding the types of tweets and the relationships between Twitch streamers.  


**Logistics**

* Extra credit: up to 3%
* Team size: 1-2

**Submission Details**

### Assignment Details

#### Refresher

You will write queries or short Python programs to answer the following questions about the dataset.  

In the simple case, graphs have the following schema:

        nodes(id int primary key, <attributes>)
        edges(
          src int NOT NULL references nodes(id),
          dst int NOT NULL references nodes(id),
          <attributes
        )

Recall that in graph analysis, you are interested in finding neighbors of nodes or paths between nodes.    Following an edge in the graph corresponds to a JOIN.  For example, the following finds all neighbors of node id 2:

        SELECT dst FROM edges WHERE src = 2;

Similarly, if we have a table `goodnodes` that contains IDs of nodes that we are interested in, the following query finds neighbors of these good nodes:

        SELECT dst FROM edges, goodnodes WHERE edges.src = goodnodes.id;



Take a look at the following documentation about recursive WITH queries to see how they can be used.

* https://www.postgresql.org/docs/9.1/static/queries-with.html
* https://www.sqlite.org/lang_with.html


#### The Twitter dataset

In reality, the twitter dataset isn't as neat as the above example.  Instead it contains the following attributes:

        idx                 INTEGER   # aribtrary idx value
        create_time         STRING 
        id                  FLOAT     # Tweet id
        in_reply            STRING    # id of Tweet that this row is replying to, or Null
        like_num            FLOAT     # number of likes
        quoted_org_id       FLOAT     # id of orig tweet if this row quotes another tweet
        retweet_num         FLOAT     # number of times this row was retweeted
        retweet_org_id      FLOAT     # id of orig tweet if this row is a retweet
        text                STRING    
        twitter_username    STRING    
        twitch_username     STRING   

The edges in the graph are based on the `in_reply` attribute, which is the `id` of the Tweet that the current tweet is in response to.  Alternatively, there may be implicit edges if the `text` of the Tweet contains an "@USERNAME" substring.  

#### Setup

We have [provided a starter script for you to edit](./graph.py).  To use this script, you will need to setup your local development environment.  [Click here for the google documentation](https://cloud.google.com/python/setup).  The short story is:

1. use virtualenv
2. install the Google python libraries:

        pip install --upgrade google-cloud-storage click
3. Download the credentials json file from the staff and store it on your laptop

Once you have done this, then you can edit [graph.py](./graph.py) to update the `PATHTOCRED` variable to where you stored the credentials file and then run the script.  

        python graph.py <path to credentials file>

References

* https://cloud.google.com/bigquery/create-simple-app-api#bigquery-simple-app-local-dev-python


### Queries

Implement the functions in the Python file to return the rows corresponding to the answers to the following questions:

##### Q1

Many Twitch streamers will tweet that they are starting a live broadcast beforehand as a way to advertise themselves.  
Find the `id` of Tweets that contain both the phrase "going live" and a URL to twitch.com.  

For example:

* "I'm going live now at http://www.twitch.com/blah/stream/" is a match
* "I'm going live!" is not a match


##### Q2

Twitch streamers sometimes @ mention other streamers in their tweets by adding a "@" prefix to the other streamer's Twitter username.  For instance, the following tweet mentions `anotheruser`. 

      Thanks to @anotheruser for a great broadcast!

Take a look at the [regular expressions documentation for BigQuery](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#regexp_extract).    

Find all the tweets that @ mention another user, and return the tweeter and the user mentioned in the tweet.  You can assume that each tweet mentions at most one other streamer.


##### Q3 

The answer to Q2 actually forms a graph where each row is an edge between a tweeter and the user that the tweet @ mentions.  


##### Q4 
##### Q5 





