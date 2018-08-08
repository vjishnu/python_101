cars = int(input("Enter the no.of cars :"))
people = int(input("Enter the no.of people :"))

trucks = int(input("Enter the no.of trucks :"))



if cars>people:
   print("We should take cars")
elif people>cars:
     print("We should not take cars")
elif trucks>cars:
     print("That too many trucks")
elif trucks>cars:
     print("That too many trucks")
elif cars>trucks:
     print("mayb we could take cars")
else:
     print("We still cant decide")

     
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
   
