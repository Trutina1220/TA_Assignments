class Fridge:
    def __init__(self,user):  #INITIALIZE THE VARIABLE THAT ARE GOING TO BE USED
        self.surface = '--------------------------------'
        self.freezer1 = []
        self.freezer2 = []
        self.refrigerator1=[]
        self.refrigerator2=[]
        self.refrigerator3=[]
        self.inside_fridge=[]
        self.space = [self.freezer1,self.freezer2,self.refrigerator1,self.refrigerator2,self.refrigerator3,'']
        self.user = user
        self.inventory = ['milk','donut','chicken sandwich','cheese',"celery", "oolong tea",'ice cream','frozen fruit','nuts',
                          'frozen veggies']
        self.places = ['freezer1','freezer2','refrigerator1','refrigerator2','refrigerator3','']
        print("README!!! , TYPE 'EXIT' IF YOU WANT TO EXIT THE COMMAND")

    def check_the_fridge(self): #METHOD TO CHECK THE FRIDGE , IF ITS UPDATED OR NOT
        opening_command = input('Hello '+self.user+', Do you want to check the fridge? (Y/N)\n\n')
        if opening_command.upper()=='Y':
            for i in range(0,6):
                print(self.surface,'\n',self.space[i],self.places[i])
        else:
            print("Okay, good day "+self.user)

    def checking_inventory(self):       #METHOD TO PRINTING THE INVENTORY
        print(self.inventory)

    def checking_which_to_put(self,stored_stuff,index_stored): #METHOD TO CHECK WHICH TO PUT
        for i in range(5):
            if len(self.space[i]) <= 3 and index_stored == self.places[i]:
                self.space[i].append(stored_stuff)
                self.inside_fridge.append(stored_stuff)

    def checking_which_to_retrieve(self,retrieved_stuff,index_stored):  #METHOD TO CHECK WHICH TO RETRIEVE
        for i in range(5):
            if index_stored == self.places[i]:
                self.space[i].remove(retrieved_stuff.lower())
                self.inventory.append(retrieved_stuff.lower())

    def storing_stuff(self):    #METHOD TO STORE STUFF TO THE FRIDGE
        stored_stuff = input('What do you want to store? ')
        if stored_stuff == "exit":
            return
        while stored_stuff.lower() not in self.inventory:
            print("That stuff doesn't exist in the inventory")
            stored_stuff = input('What do you want to store? ')
        index_stored = input('Where do you want to put? (Freezer1/2/Refrigerator1/2/3) ')
        if index_stored == "exit":
            return
        while index_stored.lower() not in self.places:
            print("That place don't exist")
            index_stored = input('Where do you want to put? (Freezer1/2/Refrigerator1/2/3) ')
        if stored_stuff.lower() == 'exit' or index_stored.lower() == 'exit':
            exit()
        if stored_stuff.lower() in self.inventory:
            self.inventory.remove(stored_stuff.lower())
        self.checking_which_to_put(stored_stuff,index_stored)
        self.check_the_fridge()

    def retrieve_it(self):  #METHOD TO RETRIEVE STUFF FROMM FRIDGE
        retrieved_stuff = input('What do you want to retrieve?' )
        if retrieved_stuff == "exit":
            return
        while retrieved_stuff not in self.inside_fridge:
            print("That stuff doesn't exist inside the fridge")
            retrieved_stuff = input('What do you want to retrieve?')
        index_stored = input('Where is the stuff you want to retrieve? (Freezer1/2/Refrigerator1/2/3) ')
        if index_stored =="exit":
            return
        while index_stored not in self.places:
            print("That place doesn't exist in the fridge")
            index_stored = input('Where is the stuff you want to retrieve? (Freezer1/2/Refrigerator1/2/3) ')
        if retrieved_stuff.lower() in self.inside_fridge:
            self.inside_fridge.remove(retrieved_stuff.lower())
        self.checking_which_to_retrieve(retrieved_stuff,index_stored)
        self.check_the_fridge()
        self.checking_inventory()
    def auto_put(self):
        print(self.user+", i'm gonna help you put all your groceries in , so you don't put it in the wrong place :D ")
        self.freezer1.extend(['ice cream','frozen fruit'])
        self.freezer2.extend(['nuts','frozen veggies'])
        self.refrigerator1.extend(['milk','donut'])
        self.refrigerator2.extend(['celery','tuna sandwich'])
        self.refrigerator3.extend(['oolong tea','cheese'])
        del self.inventory[0:10]
        print('your inventory is',self.checking_inventory())
        print("this way , all your frozen groceries will last longer and it will taste good when you use it :D ")

fridge = Fridge(input('Enter your Name: '))
while True:
    print("What do you wanna do today?\n1.Check The Fridge\n2.Check the Groceries Bag\n3.Store groceries inside the fridge"
          "\n4.Retrieve the groceries\n5.Auto put groceries")
    command=str(input('Please input the command: '))
    if command == '1':
        fridge.check_the_fridge()
        print('\n\n\n')
    elif command == '2':
        fridge.checking_inventory()
        print('\n\n\n')
    elif command == '3' :
        fridge.storing_stuff()
        print('\n\n\n')
    elif command == '4' :
        fridge.retrieve_it()
        print('\n\n\n')
    elif command == '5':
        fridge.auto_put()
        print('\n\n\n')
    elif command == 'exit':
        break







