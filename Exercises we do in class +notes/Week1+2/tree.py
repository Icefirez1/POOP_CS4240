#Al Pagar
#8/27/21
#we just gotta make a christmas tree


#way number 1 
print('''
      *       
     * *     
    * * *      
   * * * * 
  * * * * * 
 * * * * * *
* * * * * * * 
     * * 
''')

#way numer 2

stars =  "*"
spaces = 6   
for i in range(7):
    for j in range(spaces):
        print(" ", end = "")
    spaces = spaces - 1
    print(stars)
    stars = stars + " *"
print("     * *")

print("      *\n     * *\n    * * *\n   * * * *\n  * * * * *\n * * * * * *\n* * * * * * *\n     * *")

