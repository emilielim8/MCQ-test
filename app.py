print("Title of program: MCQ- test")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 12 + 9?")
  print("   a) 3")
  print("   b) 21")
  print("   c) 108")
  print("   d) 6")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not subtraction."
    score -=1
  elif answer == "c":
    output = "Wrong. This is not multiplication."
    score -=1
  elif answer == "b":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two helium atoms")
  print("   c) one oxygen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as He He"
    score -=1
  elif answer == "c":
    output = "Wrong. O is oxyegen."
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a metal?")
  print("   a) 2,1")
  print("   b) 2,8")
  print("   c) 2,7")
  print("   d) 2,8,8")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "d":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
