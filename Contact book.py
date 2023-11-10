#Python  Program for COntact Book
#Requirements for the contact program
#1. Name of the contact person
#2. Phone number of contact person
#3. Date and time
#4. CSV file (TO save created contacts in the table format)

#include some important modules like-
import os
import csv
import datetime

#First we will create a function for a title
def title():
    line_1 = "-----------------------------------------------"
    title = "Contact Management System"
    line_2 ="-------------------------------------------------"

    print(line_1.center(130)) #Here. center() function is used to give the text align to the text.
    print(title.center(130))
    print(line_2.center(130))

#Now we will create a class and in that we will define all the functions for option
class contact_function:
    contact_fields = ["Name", "Mobile_no"] #Column Names
    contact_database = "contact.csv"
    contact_data = [] #this list is used to temporarily store the contact data such as name, mobile no, 
    #data.

    def create(self):
        os.system('cls')
        title()
        print("       Create contact: ")
        print("       ---------------")
        print("")

        #Nowone by one we iterate the contact_fields and get input from the user according to that field
        for fields in self.contact_fields:
            contact_details = input("    Enter " + fields + ":")
            print("")
            self.contact_data.append(contact_details)

        #Now, we get date from the system
        Date = datetime.datetime.today()
        d = Date.strftime("%B %d %Y") #strftime()function is used to give the format of the date
        self.contact_data.append(d)

        #Here, using above statements we will get success to get input from an user.
        #Now, we will insert these inputs into the csv file.
        with open(self.contact_database, 'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

        self.contact_data = [] #Using this statement we will clear the contact_data list to get more input
        print("")
        print("Contact is created successfully".center(129))
        print("\n")

    #view() function
    def view(self):
        os.system('cls')
        title()

        print("Contacts: ".center(10))
        print("----------".center(10))
        print("")

        count = 0
        #now, we will open the csv file to read the data
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count = count + 1
            print("Total Contacts: ", count)
            print('')

        #Now, we display all data
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("Contact book is empty, Please create contact".center(129))
            else:
                for fields in self.contact_fields:
                    print('{0:<10}'.format(fields).center(10), end = "\t\t")
                print('{0:<10}'.format("Date"))
                print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----', '---------', '----'))
                print("")

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(10), end = "\t\t")
                    print("")

        print("\n")
        input("\t Press Enter key to continue..".center(120))
        os.system('cls')

    #search() function
    def search(self):
        os.system('cls')
        title()

        print("Search Contact: ".center(10))
        print("---------------".center(10))
        print("")

        self.contact_match = 'false'
        search_value = input("Enter your name: ")
        print("")

        #First we display field name
        for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10), end = "\t\t")
        print('{0:<10}'.format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----', '---------', '----'))
        print("")

        #Now, we read the database for match.
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))

        if self.contact_match == 'false':
            print("")
            print("Sorry! there is no contact by this name".center(129))

        print("")

    #delete() function
    def delete(self):
        os.system('cls')
        title()

        print("Delete Contact: ".center(10))
        print("---------------".center(10))
        print("")

        self.contact_match = 'false'
        delete_value = input("Enter your name: ")
        update_list = [] #this empty list help to update databse

        #Reading file to get match of the search
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'

        #condition to delete matched contacts
        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print("")
                print("Contact is deleted successfully!".center(129))
                print("")

        if self.contact_match == 'false':
            print("")
            print("Sorry! data not found".center(129))
            print("")            
           

#creating oblect of the class
contact_class = contact_function()

#Now, using os module we will clear the console and we create menu page
os.system('cls') 
title()

while True:
    #Here, we are using while loop for the repetition.
    print("1. View Contact".center(128))
    print("2. Create Contact".center(129))
    print("3. Search Contact".center(129))
    print("4. Delete Contact".center(129))
    print("5. Exit".center(120))
    print("_____________________".center(131))
    option = int(input("\t\t\t\t\t\t\tChoose your option: "))

    #Now we, put some condition to access above option and using that condition we call there 
    # function like view(), create(), search(), and delete() function

    #first condition
    if option == 1:
        contact_class.view()
        title()

    #second condition
    if option == 2:
        #we call create() function in a while loop
        while True:
            contact_class.create()
            ans = input("\t\t\t\t\tDo you want to create another contact number?[Y/N]: ")

            if ans == 'Y' or ans =='y':
                continue
            else: break

        os.system('cls')
        title()
        

    #third condition
    if option == 3:
        #we use while loop for the repetition
        while True:
            contact_class.search()
            print("")
            ans = input("\t\t\t\t\tDo you want to search another contact number?[Y/N]: ")

            if ans == 'Y' or ans =='y':
                continue
            else: break

        os.system('cls')
        title()

    # fourth condition
    if option == 4:
        while True:
            contact_class.delete()
            ans = input("\t\t\t\t\tDo you want to delete another contact number?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else: break

        os.system('cls')
        title()

    if option == 5:
        os.system('cls')
        line_1 = "-------------------------------------------"
        msg    = "    THANKYOU FOR USING THIS SOFTWARE"
        line_2 = "-------------------------------------------"

        print(line_1.center(130))
        print(msg.center(130))
        print(line_2.center(130))
        break
