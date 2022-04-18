{% include nav.html %}
## User input


```py
userSelection = input("What is a book you have recently read and liked? ")
```

## Data collection
```py
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

```

## Procedure

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

## Calls to student procedure
```py
print(dispDict(options,"="))
```

```py
print(dispDict(data,"-"))
```

## Output

```py
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
data = {books.loc[k,"Book title"]:books.loc[k,"genres"].strip('][').split(",") for k in list(data.keys())[:5]}
print(dispDict(data,"-"))
```
