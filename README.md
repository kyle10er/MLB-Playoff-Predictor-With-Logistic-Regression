# Project-4-Blue-Team

PROJECT INTRODUCTION:

Baseball is considered to be among the top 4 popular sports in America and among the top 10 popular sports globally.  Many consider baseball to be 'America's favorite pastime' due to its long rooted history compared to the other 3 major sports.  The first official baseball game was played in 1846 in Hoboken, NJ between the New York Nine and the Knickerbockers.   Today, MLB generates revenues in the billions of dollars with $11.6 billion generated in 2023.

Our group wanted to determine if a machine learning model could be made to determine which teams make it into the playoffs.  To summarize the overall outcome of our project, our machine learning model is 'better than a coin flip' but wouldn't use it for betting.

We used 5 years of data from 2018-2023 without using 2020.  We decided that 2020 should not be used due to a modified baseball season during the height of the Covid pandemic.  Our data came from the Baseball Reference website.  Three different machine learning models were assessed including Random Forest, KNN, and Logistic Regression.  The initial thought was to use Random Forest and to use the Feature Importance for the machine learning model.  However, the model was almost 100% accurate which made us look at KNN and Logistic Regression. Furthermore, our class TA helped understand that we wanted to use features from Random Forest that were unqiue and had no connection to other features. This is why we selected 'Bk' (Balk), 'CG_y',(Complete Game) 'Ch' (Defensive Chances =  putouts+assists+errors), 'GF' (Games Finisheed), 'cSho' (Shutout), 'SB'(Stolen Base).  We used these features in KNN and Logistic Regression, and determined that Logistic Regression was the best machine learning model to use.  We achieved a Training Data Score of 0.64 (64%) which means the model correctly predicted 64% of the outcomes in the training dataset.  The Testing Data Score was 0.66 (66%) which means the model correctly predicted 66% of the outcomes on the testing data.  These values are good in machine learning because the testing score is slightly higher than the training score indicating the model is not overfitting to the training data.

LOGISTIC REGRESSION MODEL:
We used SQL to pull in our 2018-2023 data into Jupyter Notebook. Then we calculated the correlations between the playoff column and all the other columns and selected the correlations between -0.1 and 0.1.  This gave us 'Bk', 'CG_y', 'Ch', 'CG', 'cSho', 'SB'.   The 'liblinear' parameter was used for optimization because it works well with small datasets. We used the 'joblib' library as recommended by our TA................
Our next step was to introduce the 2024 MLB data into out machine learning model and created a for loop to run 100 times.  We kept a count of each time a team was selected to make it into the playoffs based on the machine alogrithm.  


1) BK = Balks. A call against the pitcher for making an illegal motion that the umpire views as an attempt to deceive a baserunner
2) CG= Complete Game. Pitcher throws an entire game with any relief
3) cSho = complete shut out. A complete game thrown by the pitcher where the losing team did not score
4) Ch = Defensive Chances.  The number of putouts plus assists committed by the fielder.  A fielder is credited with a putout if the fielder is the one who physically records the act of completing an out
5) SB = Stolen Bases. The number of bases successfully stolen by a baserunner
6) GF = Game Finished.  A pitcher is credited with a game finished if he is the last pitcher to pitch for his team in a given game, provided he was not the starting pitcher. Starters are not credited for a game finished when they pitch a complete game



DATA SOURCES:
https://www.baseball-reference.com/leagues/majors/2018.shtml#site_menu_link
mlb.com
Jake Byford - TA for the UPenn Data Analytics Class assisted with code to run the 2024 data in our machine model and the joblib library