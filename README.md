
University of Dayton

Department of Computer Science

CPS 491 - Spring 2022

Dr. Phu Phung


## Capstone II Project


# Phishing Email Sentiment Analysis


# Team members



1.  John (Jack) Conroy, conroyj4@udayton.edu
2.  Will Manzella, manzellaw2@udayton.edu
3.  Jon Moran, moranj13@udayton.edu
4.  James Oei, oeij01@udayton.edu


# Company Mentors

Jeffrey Archer

Senior Staff Cybersecurity Researcher

GE Aviation

Cincinnati, Ohio

## Project homepage

[Team 3 Website](https://cps491s22-team3.bitbucket.io)
https://cps491s22-team3.bitbucket.io


# Overview
Latest Commit: 
https://bitbucket.org/cps491s22-team3/cps491s22-team3/commits/0623e41538c4b244b3a8d8ba5247b931a362a3b4


![Overview Architecture](https://i.ibb.co/JQ3yHgK/c9f8e4e230791947c6a9751099749428.png)

Figure 1. - A Sample of Overview Architecture of the proposed project.

# Project Context and Scope


The GE Aviation Cyber Intelligence, Active Defense, and Enterprise Vulnerability Management Team currently uses a data engineering framework, dubbed “Magnus”, to extract features from phishing emails sent to GE Employees and use these to score how “suspicious” an email appears using automation.

The Magnus framework is currently used to calculate a suspiciousness score automatically by translating some common patterns looked for by human analysts in email content to automated “signatures” or “feature patterns”. 

While this kind of automation works well with email metadata and header data, it would be optimal to also include information about the message contents, which the Magnus framework does not examine today.

One particularly valuable feature set that can be extracted from email message contents is the sentiments of the message – the overall opinions or emotions underlying the phrases used in a document’s text. Sentiment Analysis of email contents will be the topic of this project and will be used to augment the current Magnus framework by adding features based on the text contents and sentiments of email data.

This project will be able to provide an analysis of sentiment from an email to provide an awareness to the possible intention of the email (e.g. phishing).


# High-level Requirements

1. Create Base NLP Algorithm
2. Find, Clean, and Format Email Data
3. Create Testing Dataset
4. Determine the polarity of given text
5. Implement the Advanced Emotional State Algorithm
6. Implement Phrase Recognition
7. Implement Spell Check Dictionary


# Technology

Jupyter Notebooks: Allows for simple segmented and easily testable python scripts

Python Natural Language Processing: Breaks down sentences into its most identifiable components

Kaggle: Provides thousands of useful datasets, including email and sentiment data

Textblob: Sentiment analysis library 


# Impacts


Sentiment Analysis is the computational study of people’s opinions, sentiments, emotions, and attitudes. It often involves employing Natural Language Processing (NLP) techniques to tokenize the words of a document and analyze the content and context of the text to determine – on a basic level - the polarity of a given text (whether the expressed opinion is positive, negative, or neutral) and – on an advanced level - emotional states such as enjoyment, anger, disgust, sadness, fear, and surprise.

The goal of this project is to develop a sentiment analysis tool that, given the input of the contents of an email, can analyze the email text contents and determine the emotional states present in the text.

The output of the project should include the detected emotional states, and, if possible, which tokens/phrases contributed to the detection of that emotional state. See the sample input and output provided below.

The emotional states detected by the project can include any number of emotions (standard emotions used in sentiment analysis are Happiness, Sadness, Fear, Anger, Surprise, Scare, Shame, and Disgust). Of particular interest for this project are emotions having to do with shaming, intimidation, or harassment, as this category of emotions is often used in phishing emails to influence a victim to complete an action, e.g.:

• “Please click on this link immediately to view your banking statement.”

• “This request requires your urgent attention”

• “I need you to change the banking information ASAP”

• “If you do not respond in 24 hours, we will release this embarrassing information about
you”

• “Change your password here before your account is deleted!”


The technology we'll use — Jupter Notebooks, Python Natural Language Processing, Kaggle, and Textblob — will directly allow us to complete this project and hopefully exceed expectations.



# Project Management

Trello Board: https://trello.com/b/TAupdl0o/team-3-capstone-ii-spring-2022
Team Repository: https://bitbucket.org/cps491s22-team3/cps491s22-team3/src/master/

We'll follow the Scrum and Agile methodologies approach throughout the development of this project. We'll use Trello to stay organized and maintain our productivity. Multiple team meetings will take place throughout each week of the Spring semester.

Sprint Outlook:

Sprints 1-4

    These Sprints are focused on building the framework necessary to read the text of emails and set up Natural Language Processing

        Sprint 1: Create Base NLP Algorithm
        Sprint 2: Find Email Data
        Sprint 3: Clean and Format Email Data
        Sprint 4: Create Testing Dataset

Sprints 5-8

    These Sprints are focused on implementing sentiment analysis into the framework of previous 3 sprints
    
        Sprint 5: Determine the polarity of given text
        Sprint 6: Design Advanced Emotional State Algorithm
        Sprint 7: Implement Advanced Emotional State Algorithm
        Sprint 8: Test Advanced Emotional State Implementation

Sprints 9-10

    If all goes well in Sprints 4-7 then we would like to add some advanced features to optimize the program. 
    
        Sprint 9: Implement Phrase Recognition
        Sprint 10: Implement Spell Check Dictionary

Sprints 11-12

    These Sprints are reserved for extra time needed for any unforeseen blocks that we may encounter.
    This is a time to optimize and clean our coding.



Tentative Meeting Schedule:

    Monday: 5-5:30pm
    Tuesday: 5-5:30pm
    Wednesday: 5-5:30pm
    Thursday: 5-5:30pm
	Friday: 5-5:30pm

![Spring 2022 Timeline](https://i.ibb.co/N2ZDVkF/trellosc.png)


# Implementation

![spell&process](https://i.ibb.co/PWt08zj/Screenshot-267.png)

These fucntions are used pre-analysis in order to format the data set into the correct format for the algorithim. 
Text_process removed any punctuations and unnesscary words from the data set. Spellcheck does exactly that in looks for any misplled words and tries to find the correct word.


![analyze](https://i.ibb.co/HzZ523K/Screenshot-268.png)

This is the anaylysis part of our algorithim. Here we utulize the CountVectorizer from the sklearn libary in order to count the frequency of each word in a dataset. This number is then used to determine other aspects of the emotional state of the dataset.

![post-processing](https://i.ibb.co/hY2CmvH/Screenshot-266.png)

In this portion of the code we are fitting the data to a model that can be read by an analyst. We used this by once again using the sklearn library. MultinomialNB is a machine learning algorthim populary used to analyze text into probabilities.



## Scrum process

### Sprint 0

Duration: 10/01/2022-10/01/2022

#### Completed Tasks: 

1. Outlined direction of the project
2. Created environment for the prototype
3. Setup work flow systems
4. Created Bitbucket Repository
5. Researched technologies needed for the project.

#### Contributions: 

1. James Oei, 20/20 (150  minutes, 2 commits)
2. John Conroy, 20/20 (150 minutes, 0 commits)
3. Will Manzella, 20/20 (150 minutes, 0 commits)
4. Jon Moran, 20/20 (150 minutes, 0 commits)


### Sprint 1

Duration: 01/18/2022-01/25/2022

#### Completed Tasks: 

1. Set up coding envrionemnt
2. Created base architecture for code
3. Created Machine Learning Algo
4. Implemented Machine Learning Algo
5. Set up prelimary normalization and modeling for incoming text

#### Contributions: 

1.  James Oei, 1 commits, 150 min, contributed in updating ReadMe and researching normalization
2.  Jack Conroy, 0 commits, 150 min, contributed in reasearching Machine Learning Algorithim and assisting Will in implementing Algo
3.  Jon Moran, 0 commits, 150 min, contributed in reasearching Machine Learning Algorithim and assisting Will in implementing Algo
4.  Will Manzella, 1 commits, 150 min, contributed in implementing MultinomialMB machine learning algorithim into the protoype.

#### Sprint Retrospection:

Because we have experience working together a lot of things went well for us during this sprint. We know our strenghts and weaknesses so each memeber only took on task that they were comfortable handling. In addition our meetings were very productive and sometimes ran shorter because we were already on the same page. We accomplishmed a lot more than we had initially thought and find ourselves slightly ahead of schedule.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Productivity and Teamwork        |   We could try to be healthier                          |      Eat Flintstones vitamins             |


### Sprint 2

Duration: 01/25/2022-02/01/2022

#### Completed Tasks: 

1. Modified Machine Learning Algorithim
2. Reorganized order of notebook
3. Researched Text processing methods for python 3
4. Implemented Text processing methods

#### Contributions: 

1.  James Oei, 1 commits, 150 min, contributed in updating ReadMe and refining Machine Learning Algorithim
2.  Jack Conroy, 0 commits, 150 min, contributed in refining MachineLearning Algorithim to improve efficiancy
3.  Jon Moran, 0 commits, 150 min, contributed in reasearching text processing methods and possible ways to implement
4.  Will Manzella, 1 commits, 150 min, contributed in implementing text processing functionality in prototype

#### Sprint Retrospection:

Because we have experience working together a lot of things went well for us during this sprint. We know our strenghts and weaknesses so each memeber only took on task that they were comfortable handling. In addition our meetings were very productive and sometimes ran shorter because we were already on the same page. We accomplishmed a lot more than we had initially thought and find ourselves slightly ahead of schedule.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Productivity and Teamwork        |   Focus on details                          |      Peer review work             |


### Sprint 3

Duration: 02/01/2022-02/08/2022

#### Completed Tasks: 

1. Implemented Spell Check
2. Updated Repository for Release 1
3. Prepared Presentation for Release 1

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in preparing Release 1 for presentation
2.  Jack Conroy, 0 commits, 150 min, contributed in preparing Release 1 for presentation
3.  Jon Moran, 1 commits, 150 min, contributed in preparing Release 1 for presentation
4.  Will Manzella, 1 commits, 150 min, contributed in implementing spell check

#### Sprint Retrospection:

During this sprint we focused on fine tuning what we have and adding spell check to our algorithm. It went really well because we were able to communicate what needed to be done and pursue our goals. We successfully were able to prepare for Release 1.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Organization        |   Clarify concerns about algorithm                          |      Reach out to Jeff             |

### Sprint 4

Duration: 02/08/2022-02/15/2022

#### Completed Tasks: 

1. Analyzed algorithm in its current state
2. Brainstormed alternative design strategies
3. Checked in with Jeff Archer and received new advice moving forward

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in algorithm/design research and Jeff meeting.
2.  Jack Conroy, 0 commits, 150 min, contributed in algorithm/design research and Jeff meeting.
3.  Jon Moran, 0 commits, 150 min, contributed in algorithm/design research and Jeff meeting.
4.  Will Manzella, 1 commits, 150 min, contributed in algorithm/design research and Jeff meeting.

#### Sprint Retrospection:

During this sprint we focused on analyzing and researching the state of our program's design/algorithm prior to and after our meeting with Jeff. It went well as we were able to identify our current state and what needed to be done.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Checking in with Jeff        |   More progression with code other than researching                          |      Implement our new research and advice into the program             |

### Sprint 5

Duration: 02/15/2022-02/22/2022

#### Completed Tasks: 

1. Program can classify emotions
2. Created word lists for each emotion
3. Researched emotion prediction

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in emotion word list creation, researched emotion prediction processes.
2.  Jack Conroy, 0 commits, 150 min, contributed in emotion word list creation, researched emotion prediction processes.
3.  Jon Moran, 0 commits, 150 min, contributed in emotion word list creation, researched emotion prediction processes.
4.  Will Manzella, 1 commits, 150 min, contributed in emotion word list creation, researched emotion prediction processes.

#### Sprint Retrospection:

During this sprint we focused on classifying emotions using our emotion word lists. Classifying emotions was a success, and then we focused on researching how we will use this emotion classification to prediction emotion.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Emotion classification success        |   Made progress in the program on emotion prediction                          |      Use our emotion prediction research to code the prediction process into the program.             |

### Sprint 6

Duration: 02/22/2022-03/01/2022

#### Completed Tasks: 

1. Emotion prediction process successful
2. Fine tuned emotion classification word list
3. Completed Release 2 and Release 2 presentation

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in fine tunining emotion classification word list and creating release 2 presentation.
2.  Jack Conroy, 0 commits, 150 min, contributed in fine tunining emotion classification word list and creating release 2 presentation.
3.  Jon Moran, 0 commits, 150 min, contributed in fine tunining emotion classification word list and creating release 2 presentation.
4.  Will Manzella, 1 commits, 150 min, contributed in coding emotion prediction process, fine tunining emotion classification word list, and creating release 2 presentation.

#### Sprint Retrospection:

During this sprint we focused on implementing the emotion prediction process and fine tuning our emotion classification word lists. Predicting emotions was a success, and then we focused on preparing our presentation for Release 2.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Emotion prediction process successful        |   More emotions in our word list                          |      More emotions will be added to our word list in future sprints.             |

### Sprint 7

Duration: 03/01/2022-03/08/2022

#### Completed Tasks: 

1. Four more emotions were added to the word list
2. Researched optimization methods for spell check
3. Troubleshooted and fixed a bug regarding punctuation errors

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in adding more emotions to our word list, researched optimization methods regarding spell check, and troubleshooted the punctuation error bug. 
2.  Jack Conroy, 0 commits, 150 min, contributed in adding more emotions to our word list, researched optimization methods regarding spell check, and troubleshooted the punctuation error bug.
3.  Jon Moran, 0 commits, 150 min, contributed in adding more emotions to our word list, researched optimization methods regarding spell check, and troubleshooted the punctuation error bug.
4.  Will Manzella, 1 commits, 150 min, contributed in adding more emotions to our word list, researched optimization methods regarding spell check, and troubleshooted the punctuation error bug.

#### Sprint Retrospection:

During this sprint we focused on adding more emotions to our emotion word lists and researching optimization methods for spell check. We were able to successfully troubleshoot and fix a big with punctuation errors.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Punctuation errors were fixed        |  Word list could be more comprehensive / finalized                          |      We can add our final emotions to our emotion word list and finalize the emotions.             |

### Sprint 8

Duration: 03/08/2022-03/15/2022

#### Completed Tasks: 

1. Finalized the emotion word list
2. Received and began preliminary trials on data samples from Jeff Archer
3. Researched sentiment scoring techniques 

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in testing the phishing email data samples and researching sentiment scoring techniques for sentiment analysis. Aided in the finalization of the emotion word lists.
2.  Jack Conroy, 0 commits, 150 min, contributed in testing the phishing email data samples and researching sentiment scoring techniques for sentiment analysis. Aided in the finalization of the emotion word lists.
3.  Jon Moran, 0 commits, 150 min, contributed in testing the phishing email data samples and researching sentiment scoring techniques for sentiment analysis. Aided in the finalization of the emotion word lists.
4.  Will Manzella, 1 commits, 150 min, contributed in testing the phishing email data samples and researching sentiment scoring techniques for sentiment analysis. Aided in the finalization of the emotion word lists.

#### Sprint Retrospection:

During this sprint we focused on testing our new phishing email data and researching sentiment scoring techniques. In this sprint we were also able to finalize the emotion word list.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  Finalized the emotion word list         |  Could have finalized the sentiment socring techniques                          |      We will finalize the sentiment scoring techniques using our new phishing email data             |

### Sprint 9

Duration: 03/22/2022-03/29/2022

#### Completed Tasks: 

1. Obtained and implemented a new dataset
2. Developed a new scoring system for the sentiment analysis
3. Reconfigured old methodology in the code to conform to the new dataset

#### Contributions: 

1.  James Oei, 0 commits, 150 min, contributed in finding and implementing the new dataset, developed the new scoring system, and reconfigured old methods in the code to work with the new dataset.
2.  Jack Conroy, 0 commits, 150 min, contributed in finding and implementing the new dataset, developed the new scoring system, and reconfigured old methods in the code to work with the new dataset.
3.  Jon Moran, 0 commits, 150 min, contributed in finding and implementing the new dataset, developed the new scoring system, and reconfigured old methods in the code to work with the new dataset.
4.  Will Manzella, 1 commits, 150 min, contributed in finding and implementing the new dataset, developed the new scoring system, and reconfigured old methods in the code to work with the new dataset.

#### Sprint Retrospection:

During this sprint we focused on implementing the new dataset and reconfiguring our old methodology in the code to work with the new dataset. We also developed a new scoring system for the sentiment analysis result.

| Good     |   Could have been better    |  How to improve?  |
|----------|:---------------------------:|------------------:|
|  A new and improved dataset was found and implemented         |  Not having to re develop old code to work with the dataset                          |      Practice scalable code in the future so it works with new datasets without having to rewrite code             |

Current Results:
![Results 1](https://i.ibb.co/QQ85Ptn/output1.png)
![Results 2](https://i.ibb.co/KwrJcTw/output2.png)



# Company Support

We'll be in contact with our mentor, Jeff Archer, throughout the entirety of this project. It has been made clear that Jeff make time available to answer any questions, help with any issues, and we'll meet with him a few times throughout the project's duration to check-in and provide updates. Jeff provided his contact information and made sure that if we needed anything or particular guidance (in or out of the project) we can feel free to reach out.