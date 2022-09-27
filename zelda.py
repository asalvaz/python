import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# print the enum member as a string
print ("The enum member as a string is : ",end="")
print (Days.Mon)

# print the enum member as a repr
print ("he enum member as a repr is : ",end="")
print (repr(Days.Sun))

# Check type of enum member
print ("The type of enum member is : ",end ="")
print (type(Days.Mon))

# print name of enum member
print ("The name of enum member is : ",end ="")
print (Days.Tue.name)

print ("The enum members are : ")
for weekday in (Days):
   print(weekday)

# Hashing to create a dictionary
Daytype = {}
Daytype[Days.Sun] = 'Sun God'
Daytype[Days.Mon] = 'Moon God'

# Checkign if the hashing is successful
print(Daytype =={Days.Sun:'Sun God',Days.Mon:'Moon God'})

print('enum member accessed by name: ')
print (Days['Mon'])
print('enum member accessed by Value: ')
print (Days(1))