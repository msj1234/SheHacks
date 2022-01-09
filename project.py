
from person import Person

# declaring mentor and mentee lists
mentors = []
mentees = []

#opemimg amd readimg the file (file is a data set of signed up users)
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

  # create instance of Person
  newPerson = Person(name,age,status,hobby,study)

  # add new person to corresponding lists
  if(status == "mentor"):
      mentors.append(newPerson)
  else:
      mentees.append(newPerson)
  
  ##for test purposes 
  #print("print info \n")
  #print(name, "\n")
  #print(age, "\n")
  #print(newPerson.status,'\n')
  #print(mentors,'\n')
  #print(mentees,'\n')
  
  
# --- Matching Algorithm --- #
# for the specified mentee
def findMatches(mentee):
    matches = []

    for mentor in mentors:
        # if field of interest/experience match
        if(mentee.field == mentor.field):
            # add mentor to list of matches so that mentee can choose
            matches.append(mentor)

    return matches


# Testing:
myMatches = findMatches(mentees[0])
for match in myMatches:
    print(match.toString())
