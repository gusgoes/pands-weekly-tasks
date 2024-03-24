#Write a program that reads in a text file and 
#outputs the number of e's it contains. 
#Think about what is being asked here, 
#document any assumptions you are making.


with open('text.txt', 'r') as file:
    
    contents = file.read()
    
    count = contents.count('e')
    
    print(f"There are {count} occurrences of 'e' on that file.")