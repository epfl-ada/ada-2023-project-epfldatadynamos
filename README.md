Deciphering the web of knowledge through Wikispeedia gameplay
================================================================

Abstract
-----------
In Wikispeedia, players seek to reach a target article from another through the network of Wikipedia links. From the published data set [citation], we propose to investigate the structural organization of the articles in the abridged Wikipedia and its potential impacts on player behaviors. On one hand, we would analyze the paths taken and time spent by the players and the success rate of players to finish the games, in order to evaluate or classify players based on their performance. On the other hand, we explore how the players’ performance or strategies may be influenced by article categories, the positioning of links within articles, and the centrality of articles in the overall link network. From Wikispeedia gameplay, we aim to gain insights into how Wikipedia's structure shapes player navigation and to propose potential optimizations for its article organization and link system.


Research questions
-----------------------
Given players’ differential behavior in searching for the optimal path from one link to another, is there an optimal way to categorize wikipedia based on wikispeedia paths? 

Article organization
- Do the existing categories in the abridged Wikipedia for their articles reflect the optimal shortest path and/or the path effectively taken by the players?
- Can we identify new categorization methods for Wikipedia articles derived from the linking relationships between these articles and the navigation patterns in Wikispeedia?

Player behaviour
- What features of Wikipedia articles (such as number of outgoing/incoming links, article length and position of links within the text) may influence the efficiency of player navigation in Wikispeedia?
- Can distinct player strategies be identified based on their navigation paths, time spent on articles, and overall success rates? Do these strategies suggest any prioritization or preference of certain article features?


Methods
-----------

### Preprocessing & Data-Construction

First, we import the dataset, which includes data on article categories, linking relations, and player paths (both completed and uncompleted). The article names are URL-encoded, however, at this stage, we do not decode them since it is easier to load articles and find links within them using URL-encoded strings.

After visualizing the structures of these data, we carry out preliminary analysis to define measures that may be helpful for a more in-depth analysis.

Notably, we extract or compute the following information in link to the data:
- Number of incoming and outgoing links for each article: the ratio between the number of incoming/outgoing links is also computed for each article
- Length of articles: from the plain text size of each article
- Link Positions within Articles: identify the positions of links within the articles by parsing HTML
- Different category levels: identify main categories and two sublevels of categories
- Player path information:
    - Average duration per step: by dividing total duration by the number of steps in the path
    - Positions of the links clicked in each step: for now, we exclude paths with backclicks
    - Maximum and average positions of the links clicked for each path
- Player information
    - Number of games played
    - Win rates: number of games finished divided by the total number of attempts

### Analysis

We will perform descriptive analysis to gain a basic understanding on the distribution of several variables, such as the number of incoming/outgoing links, the winning rates of players, the position of links in articles. This can also serve as a preliminary analysis to see what article features may be different significantly in finished and unfinished paths.

To tackle the article relations part of our research questions, we will analyze the network of articles, looking at the different centrality measures of articles and visualizing the network. We will then use unsupervised learning algorithms to try to cluster and find “natural” categories based on the linking positions as well as the paths effectively taken by players.

To analyze players behaviour, we will group paths by the hased IP of players and attempt to characterize how each player navigate through the network of articles.

Additional dataset
—---------------------
The current version of Wikipedia articles (instead of the school selection) may complement our analysis to either confirm our results or indicate the limitations of our analysis.

We would still keep the selection of articles the same to make the data analysis feasible (only ~4600 articles), but we will use the full, updated linking network from the current Wikipedia.

Proposed timeline
------------------------
Week 11: analyze article organization and player performance
Week 12: investigate player strategies and articles clustering
Week 13: create visualizations
Week 14: writing up the results and build the website


Organization within the team
--------------------------------------
Players behaviour analysis => Enes, Marie Lou
Articles organization analysis => Sara, Matthew, Tong
Website => Matthew, Tong, Enes
Compose notebook => Tong, Enes

Questions for TAs
------------------------


