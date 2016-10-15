
# coding: utf-8

# In[1]:

# story line and poster image are from imdb


# In[2]:

import media, fresh_tomatoes


# In[3]:

avatar= media.Movie("Avatar", 
                    "Alien Planet", \
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                    
                   )

print (avatar.title)
#avatar.show_trailer()


# In[4]:

coherence= media.Movie("Coherence",                       "On the night of an astronomical anomaly, eight friends at a dinner party experience a troubling chain of reality bending events. ",                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQ3ODUzNDY2M15BMl5BanBnXkFtZTgwNzg0ODY2MTE@._V1_UX182_CR0,0,182,268_AL_.jpg",                      "https://www.youtube.com/watch?v=sEceDz1Rodc"
                       
                      )
print(coherence.show_info())


# In[5]:

predestination= media.Movie("Predestination",
                           "PREDESTINATION chronicles the life of a Temporal Agent sent on an intricate series of time-travel journeys designed to ensure the continuation of his law enforcement career for all eternity. Now, on his final assignment, the Agent must pursue the one criminal that has eluded him throughout time. ",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=-FcK_UiVV40"
                            
                           )
print (predestination.show_info())


# In[6]:

breaking_bad=media.TVShow("Breaking Bad",
                         "When chemistry teacher Walter White is diagnosed with Stage III cancer and given only two years to live, he decides he has nothing to lose. He lives with his teenage son, who has cerebral palsy, and his wife, in New Mexico. Determined to ensure that his family will have a secure future, Walt embarks on a career of drugs and crime. He proves to be remarkably proficient in this new world as he begins manufacturing and selling methamphetamine with one of his former students. The series tracks the impacts of a fatal diagnosis on a regular, hard working man, and explores how a fatal diagnosis affects his morality and transforms him into a major player of the drug trade. ",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=HhesaQXLuRY",
                          1,
                          1,
                          "AMC",
                          True
                         )


# In[7]:

sherlock=media.TVShow("Sherlock",
                     " In this modernized version of the Conan Doyle characters, using his detective plots, Sherlock Holmes lives in early 21st century London and acts more cocky towards Scotland Yard's detective inspector Lestrade because he's actually less confident. Doctor Watson is now a fairly young veteran of the Afghan war, less adoring and more active.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNTA2MTE1NDI5OV5BMl5BanBnXkFtZTcwNzM2MzU3Nw@@._V1_UY268_CR17,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=qlcWFoNqZHc",
                     1,
                     1,
                     "BBC",
                     False)


# In[8]:

game=media.TVShow("Game of throne",
                 "RR Matin's Story",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_UY190_CR0,0,128,190_AL_.jpg",
                 "https://www.youtube.com/watch?v=EI0ib1NErqg",
                 6,
                 1,
                 "HBO",
                 False)


# In[9]:

movies=[avatar, coherence, predestination]
tvshows=[breaking_bad, sherlock, game]


# In[10]:


fresh_tomatoes.open_movies_page(movies+tvshows)


# In[ ]:



