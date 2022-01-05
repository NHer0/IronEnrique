![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

**Author:** Enrique Hernani Ros

**Objective:** The target is to build an ML model for flexible sentiment analysis prediction capable of having a good performance in different contexts. 

**Project Phases:** Three major milestones are planned:

1. Build a benchmark model based on traditional NLP techniques and classification algorithms
2. Build a deep learning model using transfer learning and the Universal Language Model Fine-tuning (ULMFit) approach
3. Adapt the model for news headlines sentiment analysis using a small labeled dataset 


**Data**: IMDb Reviews Binary Sentiment Dataset (https://ai.stanford.edu/~amaas/data/sentiment/):

-   50,000 records
-   2 features: review body text and sentiment label


0. Continue Reading, studyng and ganining knowledge on RNNs, in particular LTSM **Day 1 - Day5**

1. Exploring the data **Day 1**
	- The initial IMDB dataset has only two variables: the text body of the review (x) and the associated labeled binary sentiment(y)
	- I will carry out some basic checks in terms of missing values, correct data types, data imbalance etc. Nevertheless due to the nature of the text data and the good quality of the data set no much effort is expected during the data exploration.


2. Cleaning and normalising the text data **Day 2**
	- Text cleaning
        - html parsing
        - removing special characters as in [&#<>{}\[\]\\]
        - removing sequences of hyphens like ==
        - others
    - Text normalization
        - hyphenation
        - unicode
        - fancy quotation marks
        - remove accents
        - mask URLS and emails
        - mask emojis

3. Processing the text data for the modelling **Day 3**

	- Tokenization
	- POS tagging
	- Lemmatization
	- Named entity recognition
    - Convert Text into numbers with TF-IDF approach

4. Classification Modelling **Day 4**
    
    - Explore different modelling options
	    - SVM (Support Vector Machine)
        - Naive Bayes
        - Extreme Gradient Boost
    - Generate Performance metrics and tune the models to improve performance
        - k-fold cross validation
        - gridsearch fine tuning
        - consider other options, depending on the achieved accuracy

5. Building the LSTM sentiment analysis Model - Phase 1 **Day 5**
    - Implement the pretrained wikipedia model in my notebook.
    - Check that is fully functional and roughly test his performance
    - Tune Hyperparemeters if required

6. Building the LSTM sentiment analysis Model - Phase 2 **Day 6**
    - Start the fine tuning of the model with the IMDB text data (without labels)
    - Check that is fully functional
    - Tune Hyperparemeters
    - Explore the performance of the model generating film reviews

7. Building the LSTM sentiment analysis Model - Phase 3 **Day 8**
    - Complete the model adding extra layers for classification
    - Fine tune the model for film review sentiment analysis using the labeled IMDB data
    - Study how the model architecture and parameters affect the performance
    - Compare with the benchmark model

8. Adapt the model for news headlines sentiment analysis using a small labeled dataset - **Day 9**

9. Prepare and practice the Presentation **Day 10**
	- Prepare the presentation 
	- Practice presentation
    - Timebank






