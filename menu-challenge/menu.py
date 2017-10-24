def show_menu():
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Add A Person")
    print ("2. View People")
    print ("3. Stats")
    print ("4. Exit")
    print (30 * '-')
    
    option = input('Enter your choice [1-4] : ')
    return option

def add_a_person():
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    team = input("Please enter in your team: ")
    age = input("Please enter in your age: ")
    f = open("person.txt", "a")
    f.write(first + " , " + last + " , " + team + " , " + age + " , " + '\n') 
    f.close()

def view_people():
    with open('person.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    print(lines)
    
def stats():
    num_lines = sum(1 for line in open('person.txt'))
    print(num_lines)
    
def average():
    with open("person.txt", "r") as people_file:
        people = []
        lines = people_file.read().splitlines()
        for line in lines:
            fields= line.split(",")
            people.append(fields)
        print(people)
        
    print("List of People")
    
    for person in people:
        print
    
                
def menu_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_a_person()
            print("You selected 'Add A Person'")
        elif option == "2":
            view_people()
            print("You selected 'View People'")
        elif option == "3":
            stats()
            average()
            print("You selected 'Stats'")
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")

menu_loop()