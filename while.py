# while can loop a set of statement as long as the condition is true

count = 2
while count <=4:
    print(count)
    count += 1
    
# break Statement 
#used to exit the loop when a certain condition is meant

count = 2
while count <=5:
    if count ==4:
        break
    print(count)
    count +=1
    
# continue Statement
#used to skip the current iteration of the loop and continue to the next iteration

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    
    
#Guessing game
# Generate a random number between 1 and 10 keep asking the user to guess the number until they get it right.