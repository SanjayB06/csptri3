import pandas as pd
from scipy import spatial
import math
import warnings
warnings.filterwarnings("ignore")

def dispDict(dict,delim):
    output = ""
    for key,value in dict.items():
        if type(value) is not list:
            output += (f"{key} {delim*10} {value}\n")
        else:
            val = ' , '.join(value)
            output += (f"{key} {delim*10} {val}\n")
    return output
def createTask():
    books = pd.read_csv("data/bookfinal.csv")
    books.set_index("Wikipedia article ID",inplace=True)

    userSelection = input("What is a book you have recently read and liked? ")
    options = {}
    for x in books.iterrows():
        data = x[1]
        bookTitle = data['Book title']
        if userSelection.lower() in bookTitle.lower():
            options[x[0]] = data['Book title']


    if len(options) > 1:
        print(dispDict(options,"="))
        selection = int(input("Which of these is your selection? "))
        while selection not in options:
            selection = int(input("Which of these is your selection? "))
        finalSelection = [(selection),options[selection]]
    elif len(options) ==0:
        print("Sorry, we have nothing for that book. ")
        quit()
    else:
        print(options)
        finalSelection = [(list(options.keys())[0]),list(options.values())[0]]
    user_authors = books.loc[finalSelection[0],"Author"].split('/')
    user_genres = books.loc[finalSelection[0],"genres"]
    user_genres = user_genres.strip('][').split(', ')
    data = {}
    for x in books.iterrows():
        if x[0] == finalSelection[0]:
            continue
        meta = x[1]
        genres = (meta['genres'])
        if type(genres) is float:
            continue
        genres = genres.strip('][').split(', ')
        if type(meta["Author"]) is float:
            continue
        authors = meta["Author"].split("/")
        commonGenres = len(list(set(genres).intersection(user_genres)))
        commonAuthors = len(list(set(authors).intersection(user_authors)))
        data[x[0]] = spatial.distance.cosine([commonGenres,5*commonAuthors],[len(user_genres),5*len(user_authors)])
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    data = {books.loc[k,"Book title"]:books.loc[k,"genres"].strip('][').split(",") for k in list(data.keys())[:5]}
    print(dispDict(data,"-"))