# WESLEY'S CAPSTONES 4 PROJECT #

# Capstone project 4

# Importing modules to use in code:

import datetime # Reasearched how to use this on (W3schools.com) / allows me to add the current date.

# Welcome message:

print("Welcome to Task Manager!\n")

# Creating user menu:

user_menu = "\nPlease select one of the following options(Note! Program will only exit when 'e' is selected): \na - Add task\nva - View all tasks\nvm - View my task\ne - Exit"

# Creating admin menu:

admin_menu = "\nPlease select one of the following options(Note! Program will only exit when 'e' is selected): \nr - Register user\na - Add task\nva - View all tasks\nvm - View my task\ngr - Generate reports\nds - View statistics\ne - Exit"

# Opening and reading text file  / assigning it to a variable:

with open ("user.txt","r") as user_data:
    user_data = user_data.read()
    user_data = user_data.split("\n")
    
initiate = False # Assigning default value  to false to use in the following while loop.
while initiate == False: # While loop will only run when the variable above is False.
    username = input("Please enter your username: ") # Asking the user to enter their username.
    password = input("Please enter your password: ") # Asking the user to enter their password.

# Only the correct username with the corresponding correct password will allow this while loop to exit.
    for line in user_data: # Making sure it uses a valid username and password combination.
        crrt_username, crrt_password = line.split(", ") # Assigning a index to a variable.
        if username == crrt_username and password == crrt_password: # Making sure the Username is correct and that the Password is correct.
           initiate = True

    if initiate == False: # If a incorrect Username or Password is entered , this error message will show and the loop will run again.
        print("Incorrect Username or Password! Please make sure your username and password is entered correctly.")

# Functions for my menu:

# Register user function:
def reg_user(username,password):
    if username == "admin": # Only allows the admin to select this option.
        with open ("user.txt","r") as new_data: # Opening the user.txt file and allowing to read from it.
            data = new_data.read()
            pswrd_check = False
            while pswrd_check == False:
                new_username = input("Please enter a new username: ")
                if new_username in data: # if the new username that is being assigned is already in the user.txt file then an error message will show and prompt for the new username again.
                    print("This username already exists! Please enter a different username.")
                    pswrd_check = False
                else:
                    new_passwrd = input("Please enter a new password: ")
                    confirm = input("Please confirm the password: ") 
                    with open("user.txt","a+") as adding_to_file:
                        if new_passwrd == confirm: # Making sure both password entries are the same to continue, if not a error message will apear and promt the questions again.
                            adding_to_file.write(f"\n{new_username}, {new_passwrd}") # Writing new user with corresponding password to text file.
                            print("\nNew User added successfully!")
                            pswrd_check = True
                        else:
                            print("Please make sure you entered the password correctly both times!")
                            pswrd_check = False               
    else: # If a normal user enters this option the standard error message will show, which is at the bottom of this menu while loop(line 128).
        print("Invalid selection! Please make sure you have entered a valid option from the menu.")

# Adding tasks function:
def add_task():
    with open("tasks.txt","a+") as task_data:
            name = input("Please enter the username that the task is assigned to: ")
            project_title = input("Please enter the project title: ")
            description = input("Please enter the description of the task: ")
            due_date = input("Please enter the due date of the task (Enter format must be: yyyy-mm-dd): ")
            start_date = datetime.date.today() # Using this to automatically assign todays date when a new task is make (learned how to use datetime functions on W3schools.com).
            completed = "No"
            task_data.write(f"\n{name}, {project_title}, {description}, {start_date}, {due_date}, {completed}") # Writing to the text file.
            print("\nTask added successfully!")

# Viewing all tasks function:
def view_all():
    with open ("tasks.txt","r") as read_tasks:
            read_tasks = read_tasks.readlines()
            for line in read_tasks:
                splitting = line.split(", ")
                print(f"Task: {splitting[1]}\nAssigned to: {splitting[0]}\nDate assigned: {splitting[3]}\nDue date: {splitting[4]}\nDescription: {splitting[2]}\nTask complete: {splitting[5]}")

# Viewing my tasks function:
def view_mine(username):
    with open("tasks.txt","r") as my_tasks:
            print("THESE ARE YOUR TASKS:\n")
            my_tasks = my_tasks.readlines()
            count = 0
            their_tasks = []
            for line in my_tasks:
                name, project_title, description, start_date, due_date, completed = line.split(", ") # Assigning a index to a variable
                if username == name: # If the logging username is equal to the name variable in the line above , it will print every task that the username is in.
                    their_tasks.append(line)
                    count+=1
                    print(f"Task {count}: {project_title}\nAssigned to: {name}\nDate assigned: {start_date}\nDue date: {due_date}\nDescription: {description}\nTask complete: {completed}""")
            if count == 0: # If user has no tasks assigned the following message will appear.
                print("You currently have no tasks!")
            else:
                edit_task = input("\nWhich task would you like to edit (Enter number of task or Enter '-1' to return to main menu): ")
                if edit_task != "-1":
                    crrt_index = int(edit_task)-1 # Going to use this to reference the correct index value in the list.
                    line_in_list = their_tasks[crrt_index]
                    name, project_title, description, start_date, due_date, completed = line_in_list.split(", ") # Splitting up the selected line into variables so i can edit it.
                    if completed == completed.strip("\n"): 
                        new_line = False # Indicator variable to check if there was a "\n" in the completed variable above or not so i can add it again later if nec.
                    else:
                        new_line = True
                    completed = completed.strip("\n") # So the if statement below works regardless if there is a "\n" or not.
                    if completed.lower() == "no": # This is the only instence something needs to be changed
                        choice = input("Would you like to complete or edit the task (Enter C for complete or E for edit): ")
                        if choice.lower() == "c": # To complete selected task.
                            completed = "Yes"
                            print("\nTask successfully completed!")
                        elif choice.lower() == "e": # To edit selected task.
                            name = input("Who would you like to assign this task to: ")
                            due_date = input("What is the new due date (Enter format must be: yyyy-mm-dd): ")
                            print("\nTask successfully edited!")
                        if new_line == True: # To add new line if necessary to make sure the format in text file is correct.
                                completed += "\n"
                        edited_task = f"{name}, {project_title}, {description}, {start_date}, {due_date}, {completed}" # To reformat the selected (edited) task for the text file.
                        # The below finds the index of the changed task in the text file so it can be replaced with the edited version
                        old_task = their_tasks[crrt_index] 
                        task_index = 0
                        for i in my_tasks:
                            if old_task == i:
                                my_tasks[task_index] = edited_task # Only selected task has been changed in my_tasks.
                            task_index+=1
                        with open ("tasks.txt","w") as new_data: # Overwriting text file with the new version(with changed task).
                            new_data.writelines(my_tasks) # Writelines writes each object in a list as a new line in the text file (Researched on Stackoverflow.com)      
                    else:
                        print("\nThis task is already completed. You cannot edit a completed task!") # If the task is complete and a user attempt to edit it, this error message will appear.

# View statistics on terminal function:
def statistics(username):
    if username == "admin": # Only allows the admin to select this option else error message will appear for normal user.
            reports(username) # Generating the reports first with my reports function.
            with open("task overview.txt","r")as task_overview_data:
                task_overview_data = task_overview_data.read() # reading the data.
                print(task_overview_data) # Printing it to the terminal.
            with open ("user overview.txt","r")as user_overview_data:
                user_overview_data = user_overview_data.read() # reading the data.
                print(user_overview_data) # Printing it to the terminal.
    # If a normal user enters this option the standard error message will show, which is at the bottom of this menu while loop(line 128).
    else:
        print("Invalid selection! Please make sure you have entered a valid option from the menu.")

# Generating reports function:
def reports(username):
    if username == "admin": # Only allows the admin to select this option else error message will appear for normal user.
        # For the Task overview report:
        with open("tasks.txt","r")as task_reporting:
            task_reporting = task_reporting.readlines()#Gives a list where each element is a line of the tasts.txt file
            ttl_tasks = len(task_reporting) # Counting how many tasks there are.
            tasks_complete = 0 # Counting how many completed tasks there are.
            overdue = 0 # Counting how many tasks are overdue.
            for i in task_reporting:
                name, project_title, description, start_date, due_date, completed = i.split(", ") # Assigning a index to a variable
                if "Yes" in completed:
                    tasks_complete += 1
                if "No" in completed:
                    today = datetime.datetime.today()
                    cvrt_due_date = datetime.datetime.strptime(due_date,"%Y-%m-%d")# reformats the due date so it can be compared to the datetime variable (Learned how to use this on W3schools.com)
                    if cvrt_due_date < today: # If the due date was before today then it is overdue
                        overdue += 1     
            incompleted = ttl_tasks - tasks_complete # to work out how many incompleted task there are.
            perc_incompleted = (incompleted/ttl_tasks)*100 # Percentage incomplete
            perc_overdue = (overdue/ttl_tasks)*100 # Percentage overdue
        with open("task overview.txt","w") as rprt_tasks:# The following writes the overview to the text file
            rprt_tasks.write(f"#TASK OVERVIEW REPORT#\n\nTotal tasks: {ttl_tasks}\nTotal of completed tasks: {tasks_complete}\nTotal of uncompleted tasks: {incompleted}\nTotal of overdue tasks: {overdue}\nPercentage of incomplete tasks: {round(perc_incompleted,2)} %\nPercentage of overdue tasks: {round(perc_overdue,2)} %\n")
        # For the User overview report:
        with open("user.txt","r")as user_reporting:
            user_reporting = user_reporting.readlines()
            ttl_users = len(user_reporting) # Working out total users.
            userlist = [] 
            for i in user_reporting: #This createes a list with all the usernames in it so that the next block of code can run through each user
                name, pword = i.split(", ")
                userlist.append(name)
            with open("user overview.txt","w") as rprt_users:
                rprt_users.write(f"#USER OVERVIEW REPORT#\n\tTotal users registered: {ttl_users}\n\tTotal tasks: {ttl_tasks}\n\n#OVERVIEW OF USERS#") # Creating heading information for the user overview textfile.
                for user in userlist: # To allow the code to run through each user
                    user_task = [] # This will allow us to make a list with only to current users tasks for ease of calcultion
                    for line in task_reporting: # This creates the list wth the current users tasks by checking if the name is correct
                        name, project_title, description, start_date, due_date, completed = line.split(", ")
                        if name == user:
                            user_task.append(line) # Adds the line to the users task list if it has the correcct username
                    user_total_tasks = len(user_task) # the length of user task gives the number of tasks that the user has
                    user_overdue = 0 # Initiate counters to for overdue and complete
                    user_tasks_complete = 0
                    for i in user_task: # Follows the same logic as for the full task list, just with a reduced set of tasks
                        name, project_title, description, start_date, due_date, completed = i.split(", ") # Assigning a index to a variable
                        if "Yes" in completed:
                            user_tasks_complete += 1
                        if "No" in completed:
                            today = datetime.datetime.today()
                            cvrt_due_date = datetime.datetime.strptime(due_date,"%Y-%m-%d")
                            if cvrt_due_date < today:
                                user_overdue += 1
                    user_tasks_incomplete = user_total_tasks - user_tasks_complete # Calculating amount of incompleted tasks for user.
                    perc_assigned = (user_total_tasks / ttl_tasks)*100 # Calculation percentage tasks assigned to user
                    if user_total_tasks > 0: # if the user has zero tasks this wouldve thrown a div error
                        perc_user_complete = (user_tasks_complete / user_total_tasks)*100
                        perc_user_incomplete = (user_tasks_incomplete / user_total_tasks)*100
                        perc_user_overdue = (user_overdue / user_total_tasks)*100
                    elif user_total_tasks == 0: # To avoid an error if the user has no tasks assigned to them
                        perc_user_complete = 100
                        perc_user_incomplete = 0
                        perc_user_overdue = 0
                    # Writing to the text file.
                    rprt_users.write(f"\nUser: {user}\n\tTotal tasks of user: {user_total_tasks}\n\tPercentage of tasks assigned to user: {round(perc_assigned,2)} % \n\tPercentage completed: {round(perc_user_complete,2)} %\n\tPercentage incomplete: {round(perc_user_incomplete,2)} %\n\tPercentage overdue: {round(perc_user_overdue,2)} %\n")
    else:
        print("Invalid selection! Please make sure you have entered a valid option from the menu.")


user_selection = False # Assigning default value to false to use in the following while loop.

# Using a main while loop to run my menu in:
# This while loop will only execute if the username and password is entered correctly.
# The following while loop contains the menu:

while user_selection == False:
    if username == "admin" and password == "adm1n": # If the admin logs in successfully a special menu will show with more options than a regular user.
        option = input(admin_menu + "\nPlease enter your option now: ") # Asks to enter the specific options
        option = option.lower() # converts the options choice to lowercase
        print()
        
    else:
        option = input(user_menu + "\nPlease enter your option now: ") # if the normal user logs in a specific menu will show with less options then the admin menu.
        option = option.lower() # converts the options choice to lowercase
        print()

# Once a user is done using one of the following options, it will always revert back to the main menu until "e" is selected to exit.
# If "r" is selected the following will happen (Feature for the admin only):

    if option == "r":
        reg_user(username, password)

# If "a" is selected the following will happen:
  
    elif option == "a":
        add_task()

# If "va" is selected the following will happen:

    elif option == "va":
        view_all()

# If "vm" is selected the following will happen:

    elif option == "vm":
        view_mine(username)

# If "gr" is selected the following will happen:

    elif option == "gr":
        reports(username)
        if username == "admin":
            print("Reports successfully generated!")

# If "s" is selected the following will happen (Feature for the admin only):

    elif option == "ds":
        statistics(username)

# If "e" is selected the program will end (The loop will exit):

    elif option == "e":
        user_selection = True
        print("Task Manager exited!")

# Else if none of the options are selected the following error message will display:

    else:
        print("Invalid selection! Please make sure you have entered a valid option from the menu.")

                    
            
                
                 
                
                    
                
                

                
                
                


            





