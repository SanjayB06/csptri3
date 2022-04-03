{% include nav.html %}

## Challenges

### Menu
```py
def presentMenu(menu):
    buildMenu(menu)  # print out menu and take input
    choice = int(input())
    while choice not in menu:  # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if choice in menu:
        if menu[choice]["type"] == "func":  # determine whether recursion is needed
            menu[choice]["exec"]()  # run function

        else:
            presentMenu(menu[choice]["exec"])  # display submenu

```

### List and Loops

```py
InfoDb = [] #defining DB
InfoDb.append({  #adding item to DB
               "Title": "Jurassic Park",  
               "Year": "1993",  
               "Director": "Steven Spielberg",  
               "Genres": ["Sci-fi", "Action"]
              })  
InfoDb.append({  
               "Title": "The Dark Knight",  
               "Year": "2008",  
               "Director": "Christopher Nolan",  
               "Genres": ["Action", "Crime", "Thriller"]
              })  
InfoDb.append({  
               "Title": "The Godfather",  
               "Year": "1972",  
               "Director": "Francis Ford Coppola",  
               "Genres": ["Crime", "Drama"]
              })  
InfoDb.append({  
               "Title": "The Batman",  
               "Year": "2022",  
               "Director": "Matt Reeves",  
               "Genres": ["Crime", "Superhero", "Action"]
              })  

```

### Classes
```py
class Factorial: #defining class
    def __init__(self, n): #initializing function
        self.n = n

    def factorial(self, y=None): #factorial method
        y = self.n if y is None else y
        product = 1
        for x in range(1, y+1):
            product *= x
        return product

    def __call__(self): #what will be run on call
        series = [str(self.factorial(x)) for x in range(1, self.n+1)]
        return " ".join(series)
```