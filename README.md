# Sentiment Analysis and Similarity Calculator: HyperionDev final capstone

This repository contains code for sentiment analysis of a dataset of Amazon product reviews downloaded via Kaggle. The analysis involves cleaning the data, analysing sentiment, and calculating similarity between reviews.


## Table of Contents

    What does this code do?
    How I cleaned, analysed and compared the data
    Building the code
      Step 1: Read in and clean the data
      Step 2: Create the sentiment analysis function
      Step 3: Compare similarity between reviews
    Installing the code
      Dependencies
    Usage
    Credits

    
## What does this tool do?

###### Checks the sentiment of reviews.
This code analyses the sentiment a customer has towards a product according to their online review. 'Sentiment' is a positive, negative or neutral response described by polarity (a score of -1 to 1, with -1 being negative and 1 being positive), and subjectivity (a score beteween 0 and 1), which tells us about how much of the review is due to subjective reasons or facts.

###### Examines the similarity between specific reviews and two randomly selected reviews.
This code analyses the similarity between reviews chosen by the data scientist, and chosen at random. It will present a similarity score between 0 and 1.


## Installation
Please install spaCy, pandas and TextBlob. 
The spaCy NLP model you will need is en_core_web_md. 


## Usage

###### Sentiment analysis
The sentiment analysis function of this code is useful in understanding customer opinion of a product or product category. It could also be applied to people insights and survey responses across industries. 



###### Similarity calculator
The similarity function of this code is useful in understanding the deviation in opinion (how broad opinions are) of a product or product category. If user data were captured, you could even analyse similarities between opinions expressed by the same user. As an expansion, you could also adapt the calculator to assess similarity across every review, and across reviews of the same product. This information could be presented in a Word Cloud, which is easily shared with non-technical specialists.




## Credits
This tool was built by me, Kirsten Levermore, with great support from my mentors at HyperionDev, Keenan Du Plessis, Ruud Fusha and Tselena Moeti. 

## Feel free to adapt and use the provided functions for your own projects.
