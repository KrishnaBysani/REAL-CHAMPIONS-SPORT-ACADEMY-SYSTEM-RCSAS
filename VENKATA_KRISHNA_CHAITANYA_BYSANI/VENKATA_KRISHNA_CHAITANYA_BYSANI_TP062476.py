#VENKATA_KRISHNA_CHAITANYA_BYSANI
#TP062476

def get_coaches_data(filename = 'coaches.txt'):
    '''
    Get the data from the coaches.txt file by reading everyline inside the
    file and creating a list of lists of coaches
    '''
    fil = open(filename, 'r').read().split('\n')
    coaches = []
    for i in fil:
        coach = i.split(',')
        coaches.append(coach)
    return coaches

def get_sport_data(filename = 'sport.txt'):
    '''
    Get the data from the sport.txt file by reading everyline inside the
    file and creating a list of lists of sports
    '''
    fil = open(filename, 'r').read().split('\n')
    sports = []
    for i in fil:
        sport = i.split(',')
        sports.append(sport)
    return sports

def get_students(filename = 'students.txt'):
    '''
    Get the data from the students.txt file by reading everyline inside the
    file and creating a list of lists of students
    '''
    fil = open(filename, 'r').read().split('\n')
    students = []
    for i in fil:
        student = i.split(',')
        students.append(student)
    return students

def get_admin(filename = 'admin.txt'):
    '''
    Get the data from the admin.txt file by reading everyline inside the
    file and creating a list of lists of admin
    '''
    fil = open(filename, 'r').read().split('\n')
    admins = []
    for i in fil:
        admin = i.split(',')
        admins.append(admin)
    return admins

def write_data(data, filename = 'coaches.txt'):
    '''
    Writing the modified data into the files after the program is exited
    or after every modification event
    '''
    data_str = []
    for i in data:
        dat = ','.join(i)
        data_str.append(dat)
    data_line = '\n'.join(data_str)
    fil = open(filename, 'w')
    fil.write(data_line)
    fil.close()

def menu():
    '''
    Display the starting message and getting the user response
    '''
    msg='''
Welcome to REAL CHAMPIONS SPORT ACADEMY
1.  Admin panel
2.  Registered student panel
3.  Non registered student panel
    '''
    print(msg)
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > 3 or choice <= 0:
                raise Exception
            return choice
        except Exception:
            print("The choice can only be an integer value of 1, 2 or 3. Try again...")

def login(data):
    '''
    Loging in the system with the correct ID and password
    '''
    while True:
        uid = input("Enter your ID: ")
        pwd = input("Enter your password: ")
        log = False
        for i in data:
            if uid == i[-2] and pwd == i[-1]:
                log = True
                print("Welcome %s" % i[0])
                return log
        print("You have entered wrong ID or password")
        return log

def display_coach(coaches):
    '''
    Display the coaches in a nice format
    '''
    print("Coach ID|       Name       |  Date Joined  |Date Terminated|Hourly Rate|     Phone     |       Address       |Sport Centre Code|      Sport Center Name      |Sport Code|   Sport Name   |Rating")
    for i in coaches:
        print("{:<8s}|{:<18s}|{:<15s}|{:<15s}|{:<11s}|{:<15s}|{:<21s}|{:<17s}|{:<29s}|{:<10s}|{:<16s}|{:<6s}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))

def display_sport(sport):
    '''
    Display sports in a nice format
    '''
    print("Sport Code|  Sport Name  |  Daily Schedule  |Weekly Schedule")
    for i in sport:
        print("{:<10s}|{:<14s}|{:<18s}|{:<15s}".format(i[0],i[1],i[2],i[3]))

def display_student(students):
    '''
    Display students in a nice format
    '''
    print("   Student  Name   |      Student Email      |Student ID")
    for i in students:
        print("{:<19s}|{:<25s}|{:<10s}".format(i[0],i[1],i[2]))



def admin_menu():
    '''
    Displaying the menu in case the user successfully logs in as an admin
    '''
    msg='''
1.  Add records
2.  Display records
3.  Search specific Records
4.  Sort and display records
5.  Modify records
6.  Exit
    '''
    print(msg)
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > 6 or choice <= 0:
                raise Exception
            return choice
        except Exception:
            print("The choice can only be an integer value between 1 and 6. Try again...")


def admin():
    '''
    The function handeling all the functionality of the admin
    '''
    # obtaining the required data to run the system
    admins = get_admin()
    coaches = get_coaches_data()
    students = get_students()
    sport = get_sport_data()
    print("Please login with your ID and password")
    # run the if statement after successful login
    if login(admins):
        # a loop which breaks only after the admin decides to exit out the system
        while True:
            choice = admin_menu()
            # every response for every valid option provided by the admin
            if choice == 1:
                print("1.   Coach")
                print("2.   Sport and sport schedule")
                mod = input("Which record do you want to add to? ")
                if mod == '1':
                    print("Enter the record in the format as: ")
                    print("Coach ID, Name, Date Joined, Date Terminated, Hourly Rate, Phone, Address, Sport Centre Code, Sport Center Name, Sport Code, Sport Name, Rating")
                    new = input("(Seperated by comma): ")
                    new = new.split(',')
                    new = [i.strip() for i in new]
                    if len(new) == 12:
                        coaches.append(new)
                        write_data(coaches)
                        print("The record has been entered successfully.")
                    else:
                        print("You have entered an invalid record")
                elif mod == '2':
                    print("Enter the record in the format as:")
                    print("Sport code, Sport name, Daily schedule, Weekly schedule")
                    new = input("(Seperated by comma): ")
                    new = new.split(',')
                    new = [i.strip() for i in new]
                    if len(new) == 4:
                        sport.append(new)
                        write_data(sport,"sport.txt")
                        print("The record has been entered successfully.")
                    else:
                        print("You have entered an invalid record")
                else:
                    print("You have entered an invalid response")
            elif choice == 2:
                print("1.   Display coaches record")
                print("2.   Display sport record")
                print("3.   Display registered students")
                mod = input("Enter your choice: ")
                if mod == '1':
                    display_coach(coaches)
                elif mod == '2':
                    display_sport(sport)
                elif mod == '3':
                    display_student(students)
                else:
                    print("You have entered an invalid response")
            elif choice == 3:
                print("1.   Coach by coach ID")
                print("2.   Coach by performance")
                print("3.   Sport by Sport ID")
                print("4.   Student by Student ID")
                mod = input("Your choice: ")
                if mod == '1':
                    cid = input("Enter coach ID: ")
                    coach = [i for i in coaches if i[0] == cid]
                    if coach != []:
                        display_coach(coach)
                    else:
                        print("No coach with this ID was found")
                elif mod == '2':
                    cid = input("Enter coach rating: ")
                    coach = [i for i in coaches if i[-1] == cid]
                    if coach != []:
                        display_coach(coach)
                    else:
                        print("No coach with this rating was found")
                elif mod == '3':
                    cid = input("Enter sport ID: ")
                    sp = [i for i in sport if i[0] == cid]
                    if sp != []:
                        display_sport(sp)
                    else:
                        print("No sport with this ID was found")
                elif mod == '4':
                    cid = input("Enter student ID: ")
                    student = [i for i in students if i[2] == cid]
                    if student != []:
                        display_student(student)
                    else:
                        print("No student with this ID was found")
                else:
                    print("You have entered an invalid response")
            elif choice == 4:
                print("Sort coaches by:")
                print("1.   Name")
                print("2.   Hourly rate")
                print("3.   Performance")
                mod = input("Enter your choice: ")
                if mod == '1':
                    coaches.sort(key=lambda x: x[1])
                    display_coach(coaches)
                elif mod == '2':
                    coaches.sort(key=lambda x: int(x[4]))
                    display_coach(coaches)
                elif mod == '3':
                    coaches.sort(key=lambda x: int(x[11]))
                    display_coach(coaches)
                else:
                    print("You have entered an invalid response.")
            elif choice == 5:
                print("1.   Coach record")
                print("2.   Sport record")
                mod = input("Which record you want to modify? ")
                if mod == '1':
                    cid = input("Enter the coach ID you want to modify the record of: ")
                    coach = [i for i in coaches if i[0] == cid]
                    if coach != []:
                        ind = coaches.index(coach[0])
                        print("Enter the record in the format as: ")
                        print("Coach ID, Name, Date Joined, Date Terminated, Hourly Rate, Phone, Address, Sport Centre Code, Sport Center Name, Sport Code, Sport Name, Rating")
                        new = input("(Seperated by comma): ")
                        new = new.split(',')
                        new = [i.strip() for i in new]
                        if len(new) == 12:
                            coaches[ind] = new
                            print("The record has been modified successfully.")
                        else:
                            print("You have entered an invalid record")
                    else:
                        print("No coach with this ID was found")
                elif mod == '2':
                    sid = input("Enter the sport ID you want to modify the record of: ")
                    sp = [i for i in sport if i[0] == sid]
                    if sp != []:
                        ind = sport.index(sp[0])
                        print("Enter the record in the format as:")
                        print("Sport code, Sport name, Daily schedule, Weekly schedule")
                        new = input("(Seperated by comma): ")
                        new = new.split(',')
                        new = [i.strip() for i in new]
                        if len(new) == 4:
                            sport[ind] = new
                            print("The record has been entered successfully.")
                        else:
                            print("You have entered an invalid record")
                else:
                    print("You have entered an invalid response")
            elif choice == 6:
                write_data(coaches)
                write_data(sport, 'sport.txt')
                break
            else:
                print("You have entered an invalid response")


def student():
    admins = get_admin()
    coaches = get_coaches_data()
    students = get_students()
    sport = get_sport_data()
    print("Please login with your Student ID and password")
    stu = []
    while True:
        uid = input("Enter your ID: ")
        pwd = input("Enter your password: ")
        log = False
        for i in students:
            if uid == i[-2] and pwd == i[-1]:
                log = True
                print("Welcome %s" % i[0])
                stu = i
                break
        if log == True:
            break
        else:
            print("You have entered wrong ID or password")
    if log:
        while True:
            menu = '''
1.  View coach details
2.  View self record
3.  View sports details
4.  Modify self record
5.  Provide feedback to coach
6.  Exit
Your choice:
            '''
            choice = input(menu)
            if choice == '1':
                cid = input("Enter coach ID: ")
                coach = [i for i in coaches if i[0] == cid]
                if coach != []:
                    display_coach(coach)
                else:
                    print("No coach with this ID was found")
            elif choice == '2':
                print("Your details are as follows:")
                print("Name", stu[0])
                print("Student ID", stu[2])
                print("Email", stu[1])
            elif choice == '3':
                cid = input("Enter sport ID: ")
                sp = [i for i in sport if i[0] == cid]
                if sp != []:
                    display_sport(sp)
                else:
                    print("No sport with this ID was found")
            elif choice == '4':
                students = get_students()
                print("Enter your details in the format:")
                print("Name, Email, Student ID, Password")
                new = input()
                ind = students.index(stu)
                new = new.split(',')
                new = [i.strip() for i in new]
                if len(new) == 4:
                    students[ind] = new
                    write_data(students, 'students.txt')
                    print("You have modified your record successfully.")
                else:
                    print("You have entered an invalid record")
            elif choice == '5':
                cid = input("Enter coach ID: ")
                coach = [i for i in coaches if i[0] == cid]
                ind = coaches.index(coach[0])
                rat = input("Enter the rating for the coach (integer between 1-5): ")
                coach[0][11] = rat
                coaches[ind] = coach[0]
                print("Feedback was recorded successfully")
            elif choice == '6':
                write_data(coaches)
                break



def non_registered():
    sports = get_sport_data()
    while True:
        print("1.   View Sport details")
        print("2.   Register as a new student")
        print("3.   Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print('''
1.    Swimming
2.    Badminton
3.    Football
4.    Archery
5.    Gymnastics
6.    Volleyball
7.    Basketball
8.    Cricket
9.    Tennis
10.   Table Tennis
            ''')
            sid = input("Enter sport ID:")
            sp = [i for i in sports if i[0] == sid]
            if sp != []:
                display_sport(sp)
            else:
                print("You have entered an invalid response")
        elif choice == '2':
            students = get_students()
            print("Enter your details in the format:")
            print("Name, Email, Student ID, Password")
            new = input()
            new = new.split(',')
            new = [i.strip() for i in new]
            if len(new) == 4:
                students.append(new)
                write_data(students, 'students.txt')
                print("You have successfully registered in the system.")
            else:
                print("You have entered an invalid record")
        elif choice == '3':
            print("Good bye")
            break
        else:
            print("You have entered an invalid record")






def main():
    option = menu()
    if option == 1:
        admin()
    elif option == 2:
        student()
    elif option == 3:
        non_registered()



if __name__ == "__main__":
    main()





