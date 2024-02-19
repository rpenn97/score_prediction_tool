# score_prediction_tool

< A project in generating score predictions in the "top 5" European football leagues based on historical data, trends and statistical prediction methods. >

This is an end-to-end data science project, where information from matches in the top 5 european football leagues (England's Premier League, France's Ligue 1, Germany's Bundesliga, Italy's Serie A and Spain's La Liga) shall be scraped from Understat.com, in order to generate predictions for future match outcomes.

--Backend--

From Understat, I'm currently looking to collect data from a rolling season's worth of games (~380 matches for 20 team leagues, ~306 for 18 team leagues) - this is because I believe that matches previous to this may offer little insight to the team we're trying to predict in the current day (Managers and players from top teams often don't stay in the same place for too long at the top levels, and match insight against teams no longer in these leagues due to relegation is only slightly helpful to one side of the predictive model). Ideally, scraping will be automated to run every tuesday morning, as the majority of gameweeks end on a monday night at the latest.

The metrics I've included so far in the data scraping process will all have their reasons mentioned below, but individual weightings will hopefully be calculated after EDA.

Goals scored, conceded and xG: Quite often in football, the scoreline in of itself does not fully explain how the match has played out - Team A beating Team B one nil gives us a clear view on who won the match, but not necesarily on who deserved to win. In my opinion, expected goals (xG) acts as a more accurate reflection of team chance creation and general match flow than simply collecting goals scored and conceded could, but not in isolation - a team with a high xG and a low conversion rate consistently over time can be labelled as wasteful, and a team with low xG and high conversion rate can similarly be classed as clinical.Ultimately, xG and goals work best in tandem to highlight team clinicality / wastefulness.

Shots vs Quality Shots: As xG acts as a sum of all the shots in a game, given their distance and scenario, the end figure can be misleading. Team A may generate 1.5xG in a match, but this only explains so much without added context - for example, is a team creating 6 shots of a 0.25xG quality more valuable than a team that has 15 shots of a 0.1xG likelihood? How about a team that has 2 penalties (~0.75xG per shot)? To try see through the lines, I've included shots/shots faced, and quality shots/quality shots faced - where "quality" signifies a chance measured over 0.25xG (or > 25% chance of a goal, given the average conversion rate for a player of that level).

Points gained and opposition: Goals are collateral to a team's attempts to win 3 points during a match. Scoring 1 goal and gaining 3 points is infinitely more important than scoring 3 goals and losing the match. Therefore, Points should be included in the predictive outcome to try and understand team intent and strength. If a team scores and concedes few goals but gains a high amount of points, we can say that they may not have difficulties infront of goal, but value a solid defence and tactially slow the game down when ahead. Similarly, if a team scores and concedes a lot of goals but doesn't gain points at a similar metric, they may have less control in matches and need to vastly outscore their opponents to feel safe. Importantly, many teams also switch up how they play against certain ranks of opposition to play to their personal strengths, and attempt to neutralise the enemies'. For example, weaker teams often try to approach tougher games with a couter-attacking style of play, but may play more posession based when they feel like they are the stronger team in a fixture. Therefore, I believe that these metrics may explain how a team will/should setup (Some managers are more predictable than others in how they will play and line up...)

First Goal vs First Conceded: As mentioned above, teams often change gameplan dependant on the level/style of opposition - but this is also true during matches. If Team A is losing, how will they will try and make changes to reverse their fortunes? How effective are these teams at implementing "Plan B"? I believe that goals in games are not independent of one another, and trying to work out who is more likely to score the first goal may impact the pattern of play thereafter. 

BTTS, Clean Sheets and Blanks: These metrics are binary collections for goals scored and conceded, in the sense that they're either 0 (for team failed to score, or kept a clean sheet) or a 1 (Anything other than 0 goals scored or conceded). Although not individually that insightful, may be helpful in use with other statistics to highlight strong attacks/defences, and team styles.

--Excel Dataframes, EDA and Predictive Modelling --

These are Excel documents storing the dataframes generated in the Backend (Understat scraping tool). Exploratory Data Analysis will be conducted either through these documents (likely storing separate dataframes for recent form, home vs away strength, team setup based of difficulty/rank etc.) or keeping to the dataframes in python. Other documents will reside here when looking into trends and correlations between metrics during EDA.

Score predictions will rely on the latest and ever-evolving information, opposition data, and a lot of applied maths yet to be fully established. This is not an exact science, but predictive models will be built upon findings in EDA to calculate values for home and away goals, with respect given to the likelihood of a blank, clean sheet, both teams to score given factors like the first team to score, the chance of an equaliser given team A scores first etc. 


--Frontend--

Findings will be uniquely generated on a weekly basis, given the fixtures that are to be played on any given weekend across the top 5 leagues - Ideally pushed to an API/webpage of some sort (Eg. Streamlit) - it could be fun to compare the score predictions generated (in the Premier League, at the very least) against pundit predictions (like BBC Sport's weekly prediction blog, or Sky's Super 6 etc).
