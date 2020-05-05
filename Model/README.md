## Building Model

__PhraseMatcher:__ Several PhraseMatcher methods are provided by spaCy. The method we used in this project is add.

PhraseMatcher.add: This method adds a standard to the matcher, that comprises of an ID key, at least one pattern, and also a callback capacity to follow up on the matches. This function will get the contentions matcher, i, doc and matches. In the event that a pattern as of now exists for given ID, these examples will be broadened. An on_match callback will be overwritten.

__Prerequisite Installations__

	pip install -U spacy
	python -m spacy download en_core_web_sm


__Importing Packages__

	import spacy
	import pandas as pd
	import matplotlib.pyplot as plt
	from spacy.matcher import PhraseMatcher
	nlp = spacy.load('en_core_web_sm')
	stopwords = nlp.Defaults.stop_words

### Process done:

 1. Read the .csv files of Resume_Data and keywords_dict.csv
 2. Filter the candidates who has either Masters/PhD degree and people with a total experience of less than 12 years
 3. Building a model with PhraseMatcher that categorizes people with count of keywords that are present in their resumes
 4. Filtering top 10 candidates using pandas sorting values
 5. Plot a bar graph for visualization
