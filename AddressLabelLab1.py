firstName = "Cody"
lastName = "Nelson"
address = "1021 8th St SE"
city = "East Grand Forks"
state = "MN"
zipCode = "56721"
#above are all used variables
print(firstName," ",lastName,"\n",address,"\n",city, ", ",state, "  ",zipCode, sep="") #making use of \n to keep this to one print
#below does the exact thing as above but in more statements, uses the end= to make this one work
print(firstName, end=" ")
print(lastName)
print(address)
print(city, ",",end=" ", sep="")
print(state, end="  ")
print(zipCode)
      