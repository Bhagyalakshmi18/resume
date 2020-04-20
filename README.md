# Resume Ease

A web application designed for Hiring Managers powered by Natural Language Processing

## Introduction:

More than 90% of large companies use Applicant Tracking Systems. This analyzer is one such system that are meant to take some of the workload off the recruiter, so they try to mimic the human process. A model that analyzes resumes to surface top candidates that match the position. We have researched the top systems and built our algorithm based on Natural Language Processing(NLP). When a recruiter or hiring manager receives a stack of resumes, he or she won’t likely have the time to read each one thoroughly. So, they can search for keywords related to the position they are looking to fill. This project makes the searching much easier and automated to save time and avoid any oversights or human error. 

__Our process: Posting a Job Description ---> Uploading Resumes ---> Performing Pattern Matching Model ---> Surface top 10 candidates__

## Repository Structure:

This Repository contains:

1. Linkedin_Resume_Scraper - Scrapes the Linkedin Resumes by taking a list of LinkedIn user URLs as an input. It will visit each profile on your behalf and extract every single piece of publicly available data from it and collects the resumes.
2. Pdf_extract_cleaning - Cleaning the data by removing stopwords and unnecessary words and punctuations. Extracting the data into dataframes and storing into .csv file

## Development Environment:

1.  OS: Windows 10 64-bit
2.	Libraries: spaCy, nltk, Numpy, Pandas
3.	Programming language: Python 3.6 
4.	Framework: Django 
5.	Development Environment: Jupyter Notebook
