""" 
Sentiment analysis of a dataset of product reviews downloaded via Kaggle. 
Step 1: Read in and clean the data.
Step 2: Create a function for sentiment analysis.
Step 3: Calculate similarity between reviews.
"""

""" -------- Step 1: read in and clean the data ------ """

# Import spaCy and pandas and TextBlob
import pandas as pd
import spacy
from textblob import TextBlob

# Load NLP model. Used md instead of sm as instructed in the PDF so I could measure similarity.
nlp = spacy.load('en_core_web_md')

# Read in review data from csv
# Import csv method learned from geeksforgeeks
customer_reviews_df = pd.read_csv('amazon_product_reviews.csv')

# Remove missing values in review.txt column with dropna
customer_reviews_df = customer_reviews_df.dropna(subset=['reviews.text'])   #from pdf materials

# Make text cleaning function
def clean_reviews(reviews):
    """ 
    Tokenize reviews and remove stop words
    Methods suggested in pdf instructions
     Parameters: 
    - reviews.text (str):product reviews from amazon_product_reviews.csv
    
    Returns: 
    - ready_reviews (str): cleaned product reviews
    """
    doc = nlp(reviews)
    ready_reviews = [token.text for token in doc if not token.is_stop]
    # Make lowercase and strip
    ready_reviews = ' '. join(ready_reviews).lower().strip()

    return ready_reviews

# Apply the clean_text function to the review text in the df.
#Save as a new ready_reviews column in the df.
customer_reviews_df['ready_reviews'] = customer_reviews_df['reviews.text'].apply(clean_reviews)

# Print first ten reviews of cleaned reviews to check if everything is working
print(customer_reviews_df['ready_reviews'].head(10))


""" -------- Step 2: create a function for sentiment analysis ------ """


def analyse_sentiment(ready_reviews):
    """
    Two-part function to analyse sentiment in cleaned customer reviews of products.
    Incorporating .sentiment and .polarity attributes.

    Parameters: 
    - ready_reviews (str):cleaned product reviews from 'review.text' in amazon_product_reviews.csv
    
    Returns: 
    - sentiment (str): predicted sentiment positive, negative or neutral sentiment
    - polartiy (float): predicted sentiment -1 to 1, -1 being negative and 1 being positive
    """
    #Create TextBlob object
    blob = TextBlob(ready_reviews)
    # Using the polarity attribute
    polarity = blob.polarity
    # Using the sentiment attribute
    sentiment = blob.sentiment

    return sentiment, polarity


# Test and print model on five product reviews with index for easy referencing in other uses.
# pdf instructions say to print both sentiment and polarity – not sure what to do as sentiment includes polarity score. Have printed both as instructed. I have only printed sentiment (polarity and subjectivity)
for i, review in enumerate(customer_reviews_df['ready_reviews'].head(5)):
    sentiment, polarity = analyse_sentiment(review)
    # print sentiment and polarity for the fist 5 sample reviews
    print(f"Customer review {i + 1} - {sentiment}, {polarity}")

# Semi-supervise: confirm by reading each of the reviews to check good/bad extreme sentiment.


""" -------- Step 3: Calculate similarity between reviews ------ """
print("----- Similarity -----")

# Select specific reviews per pdf instructions
my_review_of_choice = customer_reviews_df['ready_reviews'][3]
my_second_review_of_choice = customer_reviews_df['ready_reviews'][37]


def calculate_chosen_similarity(my_review_of_choice, my_second_review_of_choice):
    """
    Measures semantic similarity between two chosen cleaned reviews. 
    Returns similarity score to help us understand deviation in customer opinion.
    
    Parameters:
    - my_review_of_choice(list): one item list containing a randomly selected cleaned review
    - my_second_review_of_choice(list): one item list containing a randomly selected cleaned review

    Returns:
    - Similarity score
    """

    #Process the review texts
    chosen_review_1 = nlp(my_review_of_choice)
    chosen_review_2 = nlp(my_second_review_of_choice)

    #Calculate similarity
    chosen_similarity_score = chosen_review_1.similarity(chosen_review_2)

    return chosen_similarity_score


# Apply to randomly selected reviews
chosen_similarity_score = calculate_chosen_similarity(my_review_of_choice, my_second_review_of_choice)
# Round up similarity
rounded_chosen_similarity_score = round(chosen_similarity_score, 2)
# Print orginial comments and similarity score

print(f"Similarity between customer reviews 3 and 37 is {rounded_chosen_similarity_score}.")

""" --------------- Personal Idea --------------

For reusability, I have tried to also look at similarity with randomly selected reviews, below. """

# Randomly select two cleaned product reviews (so we are not comparing stop words).
#I am not using random_state, so the test can be run as many times as possible on different reviews.
# Learned from https://practicaldatascience.co.uk/data-science/how-to-use-pandas-sample-to-show-a-sample-of-data
random_review_samples = customer_reviews_df['ready_reviews'].sample(n=2)

# Save the two samples as my_review_of_choice variables
random_review_1 = random_review_samples.iloc[0]
random_review_2 = random_review_samples.iloc[1]

# Compare similarity between the two cleaned reviews
def calculate_similarity(random_review_1, random_review_2):
    """
    Measures semantic similarity between two chosen cleaned reviews. 
    Returns similarity score to help us understand deviation in customer opinion.
    
    Parameters:
    - random_review_1(list): one item list containing a randomly selected cleaned review
    - random_review_2(list): one item list containing a randomly selected cleaned review

    Returns:
    - Similarity score
    """

    #Process the review texts
    review_1 = nlp(random_review_1)
    review_2 = nlp(random_review_2)

    #Calculate similarity
    similarity_score = review_1.similarity(review_2)

    return similarity_score

# Apply to randomly selected reviews
similarity_score = calculate_similarity(random_review_1,random_review_2)
# Round up similarity
rounded_similarity_score = round(similarity_score, 2)
# Print orginial comments and similarity score

print(f"The similarity between two randomly selected reviews is {rounded_similarity_score}.")
