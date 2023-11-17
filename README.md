Player based optimization of wikipedia for Wikispeedia! 
================================================================

Abstract
-----------
Through Wikispeedia, a game which tracks user paths from a source to a target article through a reduced Wikipedia dataset,  West and Leskovec (2012) explore how humans navigate information networks on platforms like Wikipedia. Most notably, they note that compared to algorithmic shortest path methods, humans tend to use "hub" nodes and leverage content cues to guide their navigation. As such, using this same dataset, we propose to (1) rank the performance of players in order to assess (2) how their success is tied to the content of articles as well as (3) how the interconnections between articles determine the outcome of their attempts relative to category connections proposed by wikipedia. Thus, we study these effects both to gain insight into how Wikipedia's structure shapes player navigation in the context of human search preferences, and to propose potential optimizations for its articles’ organization with regards to Wikispeedia. 


Research questions
-----------------------
Within the Wikispeedia gameplay,  what potential optimizations can we suggest to both Wikipedia articles’ inner organization and linkage, given how they affect player navigation performance?


- Do the existing categories in this abridged Wikipedia reflect optimal shortest paths and/or the path effectively taken by players?
- What content features of Wikipedia articles (e.g., number of links, length of article, etc…) may influence the efficiency of player navigation in Wikispeedia?
- How do different network centrality and clustering measures affect player paths and can it give us insight into the way humans perceive and utilize hubs in an information network?
- How do the hub and content cue characteristics humans may be optimizing for comparing with the organizational structure of Wikipedia's categories?





Methods
-----------


### Phase 1: Data Acquisition and Preprocessing

#### Step 1: Data Collection and Preprocessing
- We import the dataset built from a condensed version of Wikipedia (4604 articles), which includes data on article categories, linking relations, and player paths (both completed and uncompleted). The article names are URL-encoded, however, at this stage, we do not decode them since it is easier to load articles and find links with URL-encoded strings.

After preliminary visualization of our data, we go to Phase 2.

### Phase 2: Exploratory Data Analysis

#### Step 2: Initial Metrics For Articles and Players 
(note: not all variables are named as such in the current notebook, this is just for readability of the project proposal)

- Article Metrics: 
    - `ratio_I/O_links`: the ratio between the number of incoming/outgoing links for each article,
    - `article_length`: length of articles from the plain text size of each article,
    - `link_position`: identify the positions of links within the articles by parsing HTML,
    - `category_level`: identify main categories and two sublevels of categories.
- Player path specific metrics:
    - `completion`: binary indicator of whether a player completed a path,
    - `speed`: continuous variable representing the time taken to finish a path,
    - `average_duration_per_step`: total duration of attempt divided by the number of steps in the path,
    - `average_length_of_articles`: Get average length of articles in a player path,
    - `position_of_links_per_step`: we exclude paths with back clicks,
    - `average_position_per_step`: average positions of links for each path.
- Player specific information
    - `number_of_attempts_per_player`: note that this will be the number of attempts up to that attempt,
    - `win_rates`: number of games finished divided by the `number_of_attempts_per_player`.

 
### Phase 3: Hub Identification and Path Analysis

#### Step 3: Building the Wikipedia Graph and Identifying Hubs

- Generate an unweighted graph using Networkx where articles are nodes and links are edges,
- We will characterize wikipedia article using NetworkX's centrality algorithms (`degree_centrality`, `betweenness_centrality`, `closeness_centrality`, `eigenvector_centrality_numpy`) on our wikipedia graph,
- We use NetworkX's clustering algorithm to determine `clustering_coefficients` of nodes. 

Note: We will look at the distribution of these metrics and arbitrarily decide a threshold to make these nodes a hub or not a hub (method tbd).

#### Step 4: Pathway Analysis
- shortest_possible_path: shortest paths computed by Dijkstra's algorithm (via NetworkX's shortest_path function) will be compared using the scipy.spatial.distance module. We will use this measure later as a confound, as the shortest possible path necessarily limits the player’s shortest path.
- Hub prioritization metric: For each path we calculate the number of hubs per path:
    - `nb_hubs_degree`
    - `nb_hubs_betweennes`
    - `nb_hubs_closeness`
    - `nb_hubs_eigenvector`
    - `nb_hubs_clustering`
- Category prioritization metric: For each path calculate the number of wikipedia categories the player went through to get to his target:
    - `nb_categories`
 

### Phase 4: Comparative Analysis and Statistical Modeling

#### Step 5: Feature Impact Assessment
- Regression models from statsmodels library will be utilized to evaluate the effect of article features (`article_length`, `link_position`, `ratio_I/O_links`) on navigation performance, with pandas facilitating data manipulation for model inputs, all ultimately helping to quantify the features that differentiate difficulty of article navigation. Note, the model will be similar to the one presented below but we will use the three article features of interest as predictors in the same model, and as we have two dependent variables (completion and speed), we will build two models, one determining if our features affect the success of the attempt and the second assessing if our features affect the speed of completion of the attempt.

#### Step 6: Hub & Category Impact Assessment
- We will look at the effects of (1) hub centrality measurements/clustering-coefficients and (2) categories on player performance metrics using MixedLM from statsmodels. We also account for confounds and random effects. We therefore have 12 univariate models (one for each predictor & dependent variable combination). Note, we use separate univariate models as we are interested in each effect individually, and choose not to use a multivariate model as univariate models are more easily interpretable and the number of effects studied is still sufficiently small. 

#### Model Variables

##### Dependent Variables:
- `completion`
- `speed`

##### Independent Variables (Predictors):
- **Hub Prioritization**: A metric indicating how often players select hub nodes during navigation. We make six models one for each following predictor:
  - `nb_hubs_degree`
  - `nb_hubs_betweennes`
  - `nb_hubs_closeness`
  - `nb_hubs_eignevector`
  - `nb_hubs_clustering`
  - `nb_categories`

##### Covariates (Potential Confounds):
- `number_of_attempts_per_player`: suggesting familiarity with the task.
- `shortest_possible_path`: accounting for inherent path difficulty.

##### Random Effects (in MixedLM):
- **Player-Specific Effects**: Random intercepts for players to account for difficulty of the path they chose:
  - `Average_lengths_of_articles` in player’s path
  - `Average_position_of_links` in a player’s path

---

## Proposed timeline and organization within team

### Week 9: 
- Finish preliminary analysis and submit milestone 2 (all)

### Week 10: 
- Finish exploratory analysis & visualizations (Marie-Lou, Sara, Enes)
- Perform hub identification and pathway analysis (Matthew, Tong)

### Week 11: 
- Feature Impact Assessment (Marie-Lou, Sara)
- Hub & Category Impact assessment (Matthew, Tong, Enes)

### Week 12: 
- Finish Impact Assessment (All)
- Work on visualization (All)

### Week 13: 
- Writing up results & content for website (Matthew, Marie-Lou, Sara)
- Build datastory website (Tong, Enes)

### Week 14: 
- Writing up results & content for website (Matthew, Marie-Lou, Sara)
- Build datastory website (Tong, Enes)


