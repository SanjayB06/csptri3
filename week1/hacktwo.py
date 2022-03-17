from hackone import InfoDb

# Hack 2a
def for_loop():
    for x in InfoDb:
        for key,value in x.items():
            print(f"{key}: {value}")
        print()
        print("-"*10)
        print()

for_loop()