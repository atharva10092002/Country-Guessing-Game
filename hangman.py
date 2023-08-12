import random

#creating a function that joins a character list to a word
def joinlist(word):
    return " ".join(word)

#list of countries
with open('countries.txt','r') as f:
    countries = f.readlines()

#choosing a random country and creating a blank word
country = random.choice(countries)[:-1]
country_lower = country.lower()
random_country = []
blank = []
for x in country:
    random_country.append(x.lower())
    if x == " ":
        blank.append(" ")
    else:
        blank.append("_")
    
length = len(random_country)

print(joinlist(blank))

count = 0
points = 110
for turns in range(7):
    print(" ")
    usr_in = input("Guess the word or letter of the country: ")
    size = len(usr_in)
    points -= 10
    for pos in range (length):
        if size != 1:
            if usr_in == country_lower:
                print(f"You Win! With {points} points")
                count += 1
                break
            else:
                if turns != 6:
                    print("Oops, wrong guess. Try again!")
                    break
                else:
                    print(f"You Lose! The country was {country}")
        else:
            if usr_in == random_country[pos]:
                blank[pos] = usr_in
        if "".join(blank) == country_lower:
            print(f"You Win! With {points} points")
            count += 1
            break
    if count == 1:
        break
    if joinlist(blank) == country_lower:
        print(f"You Win! with {points} points")
        break
    else:
        if turns != 6:
            print(joinlist(blank))
        else:
            print(f"You Lose! The country was {country}")    
