a=5
print(a)

name = 'Pooja Ravi'
name
type(name)

#First letters in Caps
name.title()
#Capital letter
name.upper()
#small letter
name.lower()

#f string
first_name='Pooja'
last_name='Ravi'
full_name=f' Hi {first_name} {last_name}'
print(full_name)

print("python")
#One tab
print(" \t python")

# One tab #Next line
#One tab
print(" \n \t python")

# One tab #Next line
print("Languages: \n\t Python \n\t SQL \n\t Java")

language='Python '
# To see the length of the string
# as it counts space too - The o\p is 7
len(language)
# To remove the left spaces
language.lstrip()
# To remove the right spaces
language.rstrip()
language[0]
language[4]

message='This is python class'
message[10:14]
#Indexing starts form 0 

#Last string
message[-1]
#To count the letters
message.count('t')
#To find the index
message.index('t')
#To find the index
message.index('T')
# To find the count -- Total count
message.count('')
# To replace a word
message=message.replace('python','SQL')
message
