def date_girls(boy_age):
    boy_date = boy_age/2 + 7
    return boy_date
  
  
for dude_age in range(20, 100, 30):
    print(dude_age)
    print("Dude aged", dude_age, "can date of girls aged", int(date_girls(dude_age)), "or later")
