{% include nav.html %}

# 2022 AP CSP Create Task
[Link to Video](https://drive.google.com/file/d/1CZEkf9FkYtXkrSZYNXruStK5O1kByXRv/view?usp=sharing)
## Written Responses

## 3a

### Overall Purpose
The purpose of this program is to recommend books to the users based on their prior preferences. It is meant to help people who are interested in a particular book/genre and would like to discover books that are similar. 


### Functionality in vieo
The entire functionality is shown in the video. The user inputs a book that they have recently enjoyed. The program then confirms the users selection and parses the data for similar books. The user is then presented with a list of similar books. 

### Input/Output
The input is the book that the user likes and would like similar books to. It is in string form. The output is a list of 5 books and their respective genres that are most similar to the user choice. 

## 3b

### List
```py
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
```
### Usage
```py
    results = {books.loc[k,"Book title"]:books.loc[k,"genres"].strip('][').split(",") for k in list(data.keys())[:5]}
    print(dispDict(results,"-"))
```
### Identification of list
The list is a dictionary called data. 

### List contents
The dctionary contains book IDs and their corresponding similarity value. Each key, value pair represents a given book and how similar it is to the book the user likes. 

### Managing complexity
THe list manages complexity by storing all the neccessary data in one variable. This allows the next line of code to look at the IDs in the sorted list and isolate the top 5, and then match them up with the dataset to get the genre list for each of them. Without this, it would be difficult if not impossible to sort every single book since they would not be in one location. Furthermore, outputting it in a nice way would be tedious as there would not be a single function that could do it for the entire list. 

## 3c

### Student Developed Procedure
```py
def dispDict(dict,delim):
    output = ""
    for key,value in dict.items(): #iteration
        if type(value) is not list: #selection
            output += (f"{key} {delim*10} {value}\n")
        else:
            val = ' , '.join(value) #sequencing
            output += (f"{key} {delim*10} {val}\n")
    return output #string output

```
### Call to function in program
```py
print(dispDict(options,"="))
```
### Explanation of Algorithm
The program takes in two parameters, a dictionary and a delimiter. The delimiter is simply a character that will be repeated to separate key from value. The program then uses a for loop to iterate through each key value pair in the dictionary. An if/else conditional is then used to determine what must be done with the key value pair. If the value pair contains a list, then the program converts the list to a string joined by commas. Otherwise the value is left as is. The key and new value are then separated by the delimiter and added to the output string. The output string is then returned. 

## 3d

### Call to function 1
```py
print(dispDict(options,"="))
```

### Call to function 2
```py
print(dispDict(data,"-"))
```

## Tessted Conditions
The test cases are what data type the value in the dictionary is. If there is a list value, then the function will have to join the list with commas and add them to the final string that will be returned. In the event that the value is a string rather than a list, it will be joined with its key and added to the final list. 

### Results of calls
The result of the first call is a multiline string. Inside this string are several lines, each of which contain a number/ID. Each line also contains the title of a book. The ID and title in each row are separated by 10 equal signs for readability. 
The result of the second call is a multiline string with several lines. Each line contains the title of a book that the reader is being recommended. Each line also contains a list of that books genres. The title and list of genres are separated by 10 hyphens. 