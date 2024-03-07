# Sentiment Analysis and Similarity Calculator: HyperionDev final capstone

This repository contains code for sentiment analysis of a dataset of Amazon product reviews downloaded via Kaggle. The analysis involves cleaning the data, creating a function for sentiment analysis, and calculating similarity between reviews.

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

• Check the sentiment and polarity of reviews.
• Examine the similarity between specific reviews and two randomly selected reviews.
• Feel free to adapt and use the provided functions for your own projects.

## Building

###### Step 1: Read in and clean the data

To read in and clean the data, the following steps are taken:

    Import necessary libraries: spaCy, pandas, and TextBlob.
    Load the spaCy NLP model (en_core_web_md).
    Read in the review data from a CSV file (amazon_product_reviews.csv).
    Remove missing values in the 'reviews.text' column.
    Define a function (clean_reviews) to tokenize reviews and remove stop words.
    Apply the clean_reviews function to create a new column ('ready_reviews') in the DataFrame with cleaned reviews.

###### Step 2: Create a Function for Sentiment Analysis

A function (analyse_sentiment) is created for sentiment analysis. It uses the TextBlob library to analyze sentiment and calculate polarity for cleaned customer reviews. The function returns both sentiment and polarity for further analysis.

###### Step 3: Calculate Similarity Between Reviews

To calculate the similarity between reviews, specific reviews are selected based on the PDF instructions. The similarity is measured using spaCy's semantic similarity score. Additionally, a personal idea involves comparing similarity between two randomly selected reviews for reusability.

###### Dependencies

• spaCy
• pandas
• TextBlob

## Usage


{{ADD PICTURES}}

## Credits
