months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

for key in months:
    if key.startswith("M"):
        print(months[key])

        
Joy = {"name":"Joy Patterson", "age": 16, "classes": {"1":"Lang", "2":"DSW", "3":"Jazz", "4":"Calc", "5":"APES", "6":"MB"}}
Jocelyn = {"name":"Jocelyn Gallardo", "age": 16, "classes": {"2":"DSW", "3":"Math", "4":"Lang", "5":"APES", "6":"Sculpture"}}
Karleigh = {"name":"Karleigh Dehlsen", "age": 16, "classes": {"1":"Lang", "2":"DSW", "3":"APES", "4":"Calc", "5":"Marine Bio", "6":"Swim"}}

if '6' in Joy["classes"]:
    print("has 6th period")
else:
    print("has 6th period")
    
my_people = [Joy, Jocelyn, Karleigh]

print(my_people[2]["name"])
print(my_people[1]["classes"]["2"])