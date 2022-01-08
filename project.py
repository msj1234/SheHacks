#testing 


#testing commit/push

#opemimg amd readimg the file
f = open('user.txt', 'r')
#for loop to loop through text file
for line in f:
  fields = line.split(",") #spilt using ,
  name = feilds[0]
  age = feilds[1]
  status = feilds[2]
  hobby = feilds[3]
  study = feilds[4]
  
  #for test purposes 
  print("print info \n")
  print(name \n)
  print(age)
  
# --- Matching Algorithm --- #
# for the specified mentee
#   loop through mentors
#       if interests match, age is in range (mentor 5-10 yrs older??), locations near (etc?)
#           add mentor to list of matches (mentee gets to choose who they want to talk to)
