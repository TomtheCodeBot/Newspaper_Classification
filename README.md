# Newspaper_Classification
Thus repository contains the newspaper classification project which uses a variety of deep learning techniques for the task at hand

## Types of newspapers :
Currently, types of newspapers includes:
* Sport - Short form: sp 
* Education - Short form: 
* Health - Short form: hp
* Culture - Short form: ct
* Entertainment and Celebrities - Short form: ec
* Science and Technology - Short form: st 

## Preprocessing order:
1. The process of preprocessing data will be like so:
2. Scrape data. ( includes: scraping links, scraping data, remove duplicates)
3. Lowercase data.
4. Correct misformatted words. 
5. Tokenize data (in this, we use a library to merge 2 words that go with each other. Ex:” ỉ ôi = ỉ_ôi, “nghệ thuật” = “nghệ_thuật”) (We’ll be using vncorenlp tokenizer)
6. Remove links 
7. Remove html tags 
8. Remove emojis 
9. Remove punctuation (one removes all punctuation, one removes all punctuation except for “.”) 
10. Remove stopwords, 1 letter words *Depends on data*
11. Normalize white space
12. Check for noise words (create a vocabulary list, check for weird words)

## Train-Valid-Test splits:
We used a 8:1:1 ratio. It is more ideal if we use a 8:2 Train:Valid ratio and create a new set of test data separately to better validate data.

## Types of models used.
* Fasttext (fasttext)
* LSTM (tensorflow)
* Hierarchical Attention Network (pytorch)

## Data.

All data and scraping script for those data can be found here: https://drive.google.com/drive/folders/1Co0kLKFm6yNASg9d-WVqs8hjDNWuASSu?usp=sharing
