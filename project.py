#testing 


#testing commit/push

#opemimg amd readimg the file
file = open('user.txt', 'r')

#skip the header lines in the file
next(file)
next(file)

#for loop to loop through text file
for line in file:
  fields = line.split(",") #spilt using ,
  name = fields[0]
  age = fields[1]
  status = fields[2]
  hobby = fields[3]
  study = fields[4]
  
  #for test purposes 
  print("print info \n")
  print(name, "\n")
  print(age)
  
  
# --- Matching Algorithm --- #
# for the specified mentee
#   loop through mentors
#       if interests match, age is in range (mentor 5-10 yrs older??), locations near (etc?)
#           add mentor to list of matches (mentee gets to choose who they want to talk to)

#if mentor, loop through to find mentee with similar hobbies 
#if(status == 'mentor'):
#    #loop through array etc..
#    continue
#else: # if mentee then conect with mentor with same interests 
#    continue 
#file.close()
