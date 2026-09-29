
#List
list=[8,2.3,[-4,5],["apple","banana"]]
print(list)
print()

#Tuple
tuple=(("parrot","sparrow"),("Lion","Tiger"))
print(tuple)
print()

#Dictionary
dict={"name":"kamlesh","age":32,"canvote":True}
print(dict)
print()

 #practice 1
a=20      #int(input("Enter First Value"))
b=30      #int(input("Enter Second Value"))
print("Addiction",a+b)
print("Substraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print()

#String
name = "kamlesh"
friend1 = "Amit"
friend2 = "sumit"
msg = '''i am from pune         
i am now learn python 
i am a freshaer '''                 #multiple lines can mi type in '''.......'''
print()

print("Hello "+ name)
print("Hello "+ friend1)
print(msg)
print()

#indexing
print(name[0])
print(name[1])
#print(name[8])              #Throws an error = IndexError
print()

#print all Character in String
print("Lets Use the for loop\n")
for character in friend2:
    print(character)
    print()

#String Slicing & Operations On String
names = "kamlesh,amit"
print(names[0:7])       #use for print specific string
print(len(names))       #Use for count lenth of string
print()

#example
fruit = "mango"
len1   = len(fruit)
print("mango is a",len1,"Letter Word.")
print(fruit[0:3])
print(fruit[:3])        #inter Python interpreter auto cout from zero
print(fruit[0:])        #same as above interpreter auto count full lenght 
print()

#negative Slicing
print(fruit[0:-3])                  #see next line what is interpreter consider for this
print(fruit[0:len(fruit)-3])        #it means intereprete consider start with zero & count full index minus asign digit
print(fruit[-3:-1])                 #count whole atring start with zero then minus specific no in that 
print()

#Practice - Quick Quiz :r
nm = "Harry"
print(nm[-4:-2])
