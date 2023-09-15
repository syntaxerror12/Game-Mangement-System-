import json # importing the modules needed for program.
import time
import sys
import os #end of importing
def menu(): # start of main menu for whole program, this will serve as the main area for the user can navigate through the main function of my program.
    menu_choice = ""
    while menu_choice !="0" : #until the user presses 0 or any other int or alphabet it will keep running
        print("""
        Welcome to my menu, please choose a number to move forward
        1) Enter New Player 
        2) Enter New individual Event
        3) Player Stats
        4) Player Scores
        0) Exit menu
        """)

        menu_choice = input("Please Enter a number from above: ")
        if menu_choice == "1": 
            enter_player() # enter_player function
        elif menu_choice == "2" :
            indivudual_player_register()  # run indiivudal player function
        elif menu_choice == "3" : 
            player_stats() # run player stats function
        elif menu_choice =="4":
            player_scores() # run player scores function
        elif menu_choice == "0":
            exit_program() # run exit menu
		# When the user presses 1 - 4 from the menu choice it is going to run the repecive function
        
def tournament_entry():# start of function. This function is used for entering a user into the tornament before registering into a team or individual events.
	print("Hello, I am Friday. Your personal assistant, I am going to provide instructions and directions throughout the duration of the tornament.", "\n", "Before entering into any events you would have register into the tornament, so please follow the instructions below ")
	time.sleep(2)
	user_first_name =  input("What is your first name? ") # assingning varibale for asking first name for registartion into tournament database
	user_lastname  =  input("What is your last name? ") # assigning variable for asking last name for registartion into tournament database.
	f = open('participants_name.txt', 'a+') #open file to store info
	f.write(str(user_first_name) + " ") # Writing the file the full name into the file
	f.write(str(user_lastname) + "" + "\n")
	f.close() # clsoing file
	#end of function

def checking_player(): # start function. This function checks if the name entered by the user actually is in the tornamnet database. This also done before registring into a team event.
    user_first_name = input(str("What is your first name "))
    user_lastname = input(str("What is your last name  "))
    print("Checking your name... ") 
    time.sleep(5)
    filename = 'participants_name.txt' # assinging a file to open it later

    with open(filename) as fo: # opening the participants file
        find = fo.read()

    if user_lastname in find: # if statment checking if the name entered is in the file
        print("Name Found. Hello", user_first_name, "Please proceed to registartion ") # if match,found then print statment
        time.sleep(3)
        fo.close()
    else: # if name not found then run the following
        print("Name not found. There might be a problem with your enrollement into the tournament please register yourself again. You will now be taken to the tornament registation")
        print("After registration you will be taken to the menu, where you can choose your options")
        tournament_entry() # run tornament entry
        time.sleep(2)
        menu() # end of funcition
            
def enter_player(): # start function. This function will serve as the main loop for entering a player into a team.
	tournament_entry() # entering the user into the tounament
	user_descsion = input("Do you want to join a team. yes or no?: ") # official descsion, for user to join team or individual
	user_Team_choice = ''

	while user_Team_choice != '5': # the main loop of the function. unitl 5 is not entered the loop will repeat
		if user_descsion == "yes".lower(): # if choose yes
			print("""
        1) Astecs
        2) Chargers 
        3) Dominators 
        4) Avengers
        5) Go back
        """)

			user_Team_choice = input("Which team do you want to join?:")

        ## user_Team_choice is the variable for what team they want to choose. This information all goes and stores in specfic text files.
		if user_Team_choice == "1": # registation into actecs
			# calling all local varibales needed for function
			count = 1
			user_first_name = input("Input your first name for registartion: ") 
			user_lastname = input("Input your lastname for registartion: ")
			team_choices = ['Astecs', 'Chargers', 'Dominators', 'Avengers']
			team_events = ["Football", "Basketball", "Swimming", "Science Bowl", "Golf"] 
			
			
			
			my_dict={} # opening a new dictnarory to store info
			try:
				with open('Astecs.json') as fp: # trying to entering a player in the file
					my_dict = json.load(fp)
				with open('count.json') as fp: # trying to count the number of player in the file
					count = json.load(fp)
			except:
				pass # if nothing in file then the program will pass

			if count > 5 : # checking if there is also 5 members in a team
				print("Sorry, This team is full.")
				confirmation = input("Would you like to join individual events or choose another yes or no? ") # giving choice to enter into indiviual
				if confirmation == "yes".lower(): 
					print("You will now be taken to individual registartion")
					indivudual_player_register() # taking the user to register into individual events. 
				elif confirmation == "no".lower(): # if choose no run enter_player function
					print("You will now be taken through the team registartion process again.") 
					enter_player()
			elif count < 5: # if number of player less than 5 then move on.
				pass 

			userid = "Team Member" + str(count) 
			count += 1 # adding one to member.
			rank = 1 # assigning the rank
			my_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Team": team_choices[0], "Rank" : rank}}) # updating the dictionary with the user's infomation

			with open('Astecs.json','w') as fp: 
				json.dump(my_dict, fp, sort_keys = True, indent=4) # writing the information into file
          
			with open('count.json', 'w') as fp:
				json.dump(count, fp, sort_keys = True, indent=4) # writing to count file, to update the counter function in file.

			print("You have been entered into", team_choices[0]) # confirmation message
			time.sleep(6)
			print("After playing the flowwing events", "\n",team_events,  "Here is the rank that your team has placed", "\n", rank) # telling what rank that the user got 
			print("Please remember these ranks as they will be used to calculate your points", "\n")
			time.sleep(3)
			print("You will now be taken to main menu")

		elif user_Team_choice == "2" : # registartion into chargers team
				count = 1
				user_first_name = input("Input your first name for registration: ")
				user_lastname = input("Input your last name for registration: ")
				team_choices = ['Astecs', 'Chargers', 'Dominators', 'Avengers']
				team_events = ["Football", "Basketball", "Swimming", "Science Bowl", "Golf"]
				chargers_dict = {}
				rank2 = 2
				try:
					with open('Chargers.json') as fp: 
						chargers_dict = json.load(fp)
					with open('count1.json') as fp: 
						count = json.load(fp)
				except:
					pass
				
				
				if count > 5 :
					print("Sorry, This team is full.")
					confirmation = input("Would you like to join individual events or choose another yes or no? ")
					if confirmation == "yes".lower():
						print("You will now be taken to individual registartion")
						indivudual_player_register()
					elif confirmation == "no".lower():
						print("You will now be taken through the team registartion process again.")
						enter_player()
				elif count < 5:
					pass
				userid = "Team Member" + str(count)
				count += 1

				chargers_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Team": team_choices[1], "Rank" : rank2}})

				with open('Chargers.json','w') as fp:
					json.dump(chargers_dict, fp, sort_keys = True, indent=4)

				with open('count1.json', 'w') as fp:
					json.dump(count, fp, sort_keys = True, indent=4)

				print("You have been entered into", team_choices[1])
				time.sleep(6)
				print("After playing the flowwing events", "\n",team_events,  "Here is the rank that your team has placed", "\n", rank2)
				print("Please remember these ranks as they will be used to calculate your points", "\n")
				time.sleep(3)
				print("You will now be taken to main menu")
                  
		elif user_Team_choice == "3": # registartion for dominators team
				user_first_name = input("Input your first name for registration: ")
				user_lastname = input("Input your last name for registration: ")
				team_choices = ['Astecs', 'Chargers', 'Dominators', 'Avengers']
				team_events = ["Football", "Basketball", "Swimming", "Science Bowl", "Golf"]
				count = 1
				dominators_dict = {}

				rank3 = 3

				try:
					with open('Dominators.json') as fp: 
						dominators_dict = json.load(fp)
					with open('count2.json') as fp: 
						count = json.load(fp)
				except:
					pass
				
				if count > 5 :
					print("Sorry, This team is full.")
					confirmation = input("Would you like to join individual events or choose another yes or no? ")
					if confirmation == "yes".lower():
						print("You will now be taken to individual registartion")
						indivudual_player_register()
					elif confirmation == "no".lower():
						print("You will now be taken through the team registartion process again.")
						enter_player()
				elif count < 5:
					pass
				

				userid = "Team Member" + str(count)
				count += 1
				dominators_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Team": team_choices[2], "Rank" : rank3}})

				with open('Dominators.json','w') as fp:
					json.dump(dominators_dict, fp, sort_keys = True, indent=4)

				with open('count2.json', 'w') as fp:
					json.dump(count, fp, sort_keys = True, indent=4)
				print("You have been entered into", team_choices[2])
				time.sleep(6)
				print("After playing the flowwing events", "\n",team_events,  "Here is the rank that your team has placed", "\n", rank3)
				print("Please remember these ranks as they will be used to calculate your points", "\n")
				time.sleep(3)
				print("You will now be taken to main menu")

				
				


		elif user_Team_choice == "4" : # registration into avenger team
				user_first_name = input("Input your first name for registration: ")
				user_lastname = input("Input your last name for registration: ")
				team_choices = ['Astecs', 'Chargers', 'Dominators', 'Avengers']
				team_events = ["Football", "Basketball", "Swimming", "Science Bowl", "Golf"]
				count = 1
				avengers_dict = {}

				rank4 = 4

				try:
					with open('Avengers.json') as fp: 
						avengers_dict = json.load(fp)
					with open('count3.json') as fp: 
						count = json.load(fp)
				except:
						pass

				if count > 5 :
					print("Sorry, This team is full.")
					confirmation = input("Would you like to join individual events or choose another yes or no? ")
					if confirmation == "yes".lower():
						print("You will now be taken to individual registartion")
						indivudual_player_register()
					elif confirmation == "no".lower():
						print("You will now be taken through the team registartion process again.")
						enter_player()
				elif count < 5:
					pass

				count += 1
				userid = "Team Member" + str(count)


				avengers_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Team": team_choices[3], "Rank" : rank4}})

				with open('Avengers.json','w') as fp:
					json.dump(avengers_dict, fp, sort_keys = True, indent=4)

				with open('count3.json', 'w') as fp:
					json.dump(count, fp, sort_keys = True, indent=4)

				print("You have been entered into", team_choices[3])
				time.sleep(6)
				print("After playing the flowwing events", "\n",team_events,  "Here is the rank that your team has placed", "\n", rank4)
				print("Please remember these ranks as they will be used to calculate your points", "\n")
				time.sleep(3)
				print("You will now be taken to main menu")


		elif user_Team_choice == "5": 
				menu()

		elif user_descsion == "no".lower(): # when the the user enter no for team choice they will be taken to the individual players menu
				print("You will be taken to the individual menu, please follow the instruction respectively ")
				time.sleep(2)
				indivudual_player_register()
		else: # any invalid entries run the following
			time.sleep(3)
			"\n"
			print("Please Enter a captial letter for descsion about wheter you want to join a team event or not. You will now be taken the beginning again","\n")
			enter_player()
        

		break # breaking the while loop
#end of function

def indivudual_player_register(): # start of function. Used for user who wants to enter into individual events
    
    print(""" 
   
    1) Enter into individual events
    2) Enter into Team events
    3) Menu""") # printing the individual menu

    user_input = input("Please choose a number, to proceed: ") # user choosing a choice

    if user_input == "1": # when user input is 1
        user_confirmation = input("Have you been registered into the tournament? ") # checking if the user has entered into the tornament before entering into individual events 
        if user_confirmation == "yes".lower():
            checking_player() # running function that validates if user in tournament database
            user_first_name = input("Please input your name for regisration into individual events: ") # asking the user firstname for registration
            user_lastname = input("Please input your name for regisration into individual events: ") # asking user lastname for registartion
            rank = 0 # counting the rank each player got
            count = 0 # for counting the number of player
            indivudual_dict = {} # creating a new individual dictionary
            individual_events = ['Badminton', 'Chess', 'Track & Feild', 'Archery', 'Maths Quiz'] # all the individual events
            try:
                with open('Individual_player_register.json') as fp:  # opening a file first to check if we can enter a player
                    indivudual_dict = json.load(fp)
                with open('count4.json') as fp: 
                        count = json.load(fp) # checking if we can count the number of player in the file
                with open('ranks.json') as fp:
                        rank = json.load(fp)
            except:
                pass # if nothing in file then pass

            if count > 20 : # checking if only 20 individual can be entered into file
                print("Sorry, This all spots have been occupied.") # if number of people exceeded then print this meesage
                confirmation = input("Would you like to join team events. Yes or No? ") # checking to see if they would like to join team events
                if confirmation == "yes".lower():
                    print("You will now be taken to team registartion") # if user says yes to join team
                    time.sleep(2)
                    enter_player()
                elif confirmation == "no".lower(): # if user says no for team registartion
                    print("Sorry, currently there are places for individual events, if you would not like to to join team events, then you will be taken to main menu.")
                    time.sleep(2)
                    menu()
            elif count < 20:
                pass
            
            count += 1 # adding on the counter
            userid = "Player" + str(count) 
            rank +=1
            indivudual_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Rank" : rank}}) # updating the users infomation 

            with open('Individual_player_register.json','w') as fp:
                json.dump(indivudual_dict, fp, sort_keys = True, indent=4) # writing the updated dict into respective file

            with open('count4.json', 'w') as fp:
                json.dump(count, fp, sort_keys = True, indent=4) # wrting the counted infomation into respective file
            
            with open('ranks.json', 'w') as fp:
                json.dump(rank, fp, sort_keys = True, indent=4) # writing the ranks file into file.

            print("Thank you for entering into individual events")
            time.sleep(5)
            print("After playing the following events", "\n", individual_events)
            print("The rank that you got was", rank)
            print("Please remember this as this will later be used to calculate your final score")
            menu()

        elif user_confirmation == "no".lower(): # user says no to registration into tornament 
            print("You will be taken to tornament registration now")
            tournament_entry()# user says no to registration into tornament, run the regirstation function
            print("You will be taken to main menu, where you can choose your options")
            menu()   

    elif user_input == "2": # user chooses 2 
            print("You will now be taken to team registartion")
            enter_player() # running the enter player function

    elif user_input == "3":
            menu()
# end function
    
def player_stats(): #begin player_stas function, this function procides user with all the events that they have been entered into and also procided a check wheter they have been registered into the tornament correctly.
    print(''' 


       1) Verification of player
       2) View Team stats
       3) View individual stats
       4) Exit to menu''') # will print out the main menu for the program


    user_descsion = input("Please choose a number to proceed")

    if user_descsion == "1":
        checking_player() # provides the user a form of wheter they have been entred into tounament database correctly

    elif user_descsion == "2":
        print("""
        1) Astecs
        2) Chargers
        3) Dominators
        4) Avengers""")

        user_input = input("What team did you get rejistered in? ") # asking user for the team register in, so that it can later be used in when updating dict
        team_events = ["Football", "Basketball", "Swimming", "Science Bowl", "Golf"] # all team events
        individual_events = ["Badminton", "Chess", "Archery", "Track & Feild", "Golf"] # all individual events
        scores = 0
		
        if user_input == "1": # for actecs team
            print("Cheking your information...")
            time.sleep(3)
            print("Infomration Found")
            print("The members in your team are:")
            time.sleep(3)

            fp = open('Astecs.json', 'r')
            search = json.load(fp)
            for i in search:
                for j in search[i]:
                    time.sleep(3)
                    print(j, ":", search[i][j],"\n") # print out values of the nested dict
            print("Your team has been entered into the following events", team_events)
            print("Your team currently has", scores ,"points. Please go to the player scores option to know your scores")
            time.sleep(2)
            menu()

        elif user_input == "2": # chargere team
            print("Cheking your information...")
            time.sleep(3)
            print("Infomration Found")
            print("The members in your team are:")
            time.sleep(3)
            fo = open('Chargers.json', 'r') # opening the respective team file that has to be read
            find =  json.load(fo) 
            for i in find: # using for loop to print all contents in file, getting into the first level dict
              for j in find[i]: # getting into second nested dict 
                time.sleep(3)
                print(j, ":", find[i][j],"\n") # print out values of the nested dict
                fo.close()
            print("Your team has been entered into the following events", team_events)
            print("Your team currently has", scores ,"points. Please go to the player scores option to know your scores")
            time.sleep(2)
            menu()


        elif user_input == "3": # for this dominators
            print("Cheking your information...") 
            time.sleep(3)
            print("Infomration Found")
            print("The members in your team are:")
            time.sleep(3)
            fo = open('Dominators.json', 'r')
            find =  json.load(fo)
            for i in find:
              for j in find[i]:
                time.sleep(3)
                print(j, ":", find[i][j],"\n")
                fo.close()
            print("Your team has been entered into the following events", team_events)
            print("Your team currently has", scores ,"points. Please go to the player scores option to know your scores")
            time.sleep(2)
            menu()


        elif user_input == "4": # for avengers team
          print("Cheking your information...")
          time.sleep(3)
          print("Infomration Found")
          print("The members in your team are:")
          time.sleep(3)
          fo = open('Avengers.json', 'r')
          find =  json.load(fo)
          for i in find:
            for j in find[i]:
              time.sleep(3)
              print(j, ":", find[i][j],"\n")
              fo.close()
          print("Your team has been entered into the following events", team_events)
          print("Your team currently has", scores ,"points. Please go to the player scores option to know your scores")
          time.sleep(2)
          menu()

    elif user_descsion == "3": # for printing out the file contents from individual player file
          print("Cheking your information...")
          time.sleep(3)
          print("Infomration Found")
          print("Your Fellow compititors are:")
          time.sleep(3)
          fo = open('Individual Register.json', 'r') #opening the individiual players file
          find =  json.load(fo)
          for i in find:
            for j in find[i]: # accesssing secong level(nested) dictonary
              time.sleep(3) # going to print out contents after 3 pausing for 3secs
              print(j, ":", find[i][j],"\n") # printing the second nested dict
              fo.close() # closing file
          print("All you fellow comprtitors are entered into", individual_events)
          menu()
    elif user_descsion == "4": # when user chooses four in the player stats menu
            menu() 
# end function

def player_scores(): # begin function, for calculating the scores for the team and individuals
    print('''
    Welcome to my scores menu
    1) Update Team scores
    2) Update Individual Scores
    3) View overall scores
    4) Main Menu''') # printing out the main menu
    user_descsion_scores = input("Please choose an option above")
    if user_descsion_scores == "1":
        print('''
        This is the full list of the teams
        1) Astecs
        2) Chargers
        3) Dominators
        4) Avengers''') # full list of teams avalable
        
        user_confirmation = input("Please enter the full name of your team? ") # asking user to typw in full name of the team registered in to store the respective team name into dict
        user_rank = input("What rank did you get placed for your team events? ") # user entering their respective rank recieved
        team_dict = {} # opening a new dict to store the scores and ranks for team 
        count = 1
        rank1 = 60 # for 1st rank
        rank2 = 40 # for 2nd rank
        rank3 = 20 # for 3rd rank
        rank4 = 10 # for 4th rank
        try:
            with open('Teams_updated_rank.json') as fp: 
                    team_dict = json.load(fp)
            with open('count6.json') as fp: 
                    count = json.load(fp)
        except:
            pass
        
        userid = user_confirmation  # setting an user id
        if user_rank == "1":
            team_dict.update({userid :{ "Rank" : user_rank, "Scores" : rank1, "Team" : user_confirmation}}) # user enter rank 1, the dict is going to update with the respective scores for that team
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
        elif user_rank == "2":
            team_dict.update({userid :{ "Rank" : user_rank, "Scores" : rank2, "Team" : user_confirmation}}) # for 2nd rank dict update
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
        elif user_rank == "3":
            team_dict.update({userid :{ "Rank" : user_rank, "Scores" : rank3, "Team" : user_confirmation}}) # 3rd rank dict update
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
        elif user_rank == "4":
            team_dict.update({userid :{ "Rank" : user_rank, "Scores" : rank4, "Team" : user_confirmation }}) # for 4th rank dict upddate
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()

        with open('Teams_updated_rank.json','w') as fp:
            json.dump(team_dict, fp, sort_keys = True, indent=4) # writing updated dict into the file
            
        count += 1

        with open('count6.json', 'w') as fp:
            json.dump(count, fp, sort_keys = True, indent=4) # writing the number members in the file to count6 file
            
    elif user_descsion_scores == "2": # for individual scores update
        user_first_name = input("What is your first name: ") # input user firstname for dict update
        user_lastname = input("What is your lastname: ") # input user lastname for dict update
        rank = input("What rank did you get in your events") # rank input for individual events
        indivudual_dict = {} # opening new dict for ranks and scores
        count = 1
        rank1 = 60
        rank2 = 40
        rank3 = 20
        rank4 = 10
        try:
            with open('Individual_player_updated_rank.json') as fp: 
                indivudual_dict = json.load(fp)
            with open('count5.json') as fp: 
                    count = json.load(fp)
        except:
            pass
        
        userid = user_first_name 
        if rank == "1": # for ist rank
            indivudual_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Rank" : rank, "Scores" : rank1}})
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
            
        elif rank == "2": # for 2nd rank
            indivudual_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Rank" : rank, "Scores" : rank2}})
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
        elif rank == "3": # for 3rd rank
            indivudual_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Rank" : rank, "Scores" : rank3}})
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()
        elif rank == "4": # 4th rank
            indivudual_dict.update({userid :{"FName" : user_first_name, "LName" : user_lastname, "Rank" : rank, "Scores" : rank4}})
            print("Scores updated, please choose 3 in the sub menu to knsow your scores")
            player_scores()

        with open('Individual_player_updated_rank.json','w') as fp:
            json.dump(indivudual_dict, fp, sort_keys = True, indent=4)
        count += 1
        with open('count5.json', 'w') as fp:
            json.dump(count, fp, sort_keys = True, indent=4)

    elif user_descsion_scores == "3": # user to view their scores and leaderboard
        print('''
        
        1) Team Events
        2) Individual Events
        ''')

        user_decide = input("Which event did you register into? Please enter a number: ") # user decides to which events leaderboard they want to see
        if user_decide == "1": # retreiving info of leaderboard for indiivdual ranks and scores
            print("Reteving Score borad...")
            time.sleep(3)
            print("Information found")
            print("The teams in the first 4 places are:")
            time.sleep(3)
            with open('Teams_updated_rank.json') as fo:
                find = json.load(fo)
                ranking = []
    
                for team in find:
                    ranking.append((find[team]["Scores"],team))

                ranking.sort(reverse=True)
                print("\tLeaderboard:")
                x = 0
                for team in ranking:
                    print(team[1],'\t\t',team[0])
                    x += 1
                time.sleep(2)  
                print("Thank you for participating in the tournament , please visit us again") # ending comment

        
        elif user_decide == "2": # retreiving info of leaderboard for indiivdual ranks and scores
            print("Reteving Score borad...")
            time.sleep(3)
            print("Information found")
            print("The people in the first 4 places are")

            with open('Individual_player_updated_rank.json') as fo:
                discover = json.load(fo)
                ranking = []
    
                for team in discover:
                    ranking.append((discover[team]["Scores"],team))

                ranking.sort(reverse=True)
                print("\tLeaderboard:")
                x = 0
                for team in ranking:
                    print(team[1],'\t\t',team[0])
                    x += 1
                time.sleep(2)  
                print("Thank you for participating in the tournament , please visit us again") # ending comment

                
                    
    elif user_descsion_scores == "4": # user wants to go main menu
        menu() # run main menu function
# ebd function
def exit_program(): # begin function. # for user to exit the program
    print('''
    1) Save and exit
    2) Clear all contents''')

    user_descion = input("Please choose an option to proceed")
    if user_descion == "1":
        print("Saving all information...")
        time.sleep(4)
        print("Infomation saved exiting program, thank for participating in the tounament") # print conformation message
        sys.exit() # program will stop running
    elif user_descion == "2":
        print("Deleting all files") 
        time.sleep(3) # short pause
        target = 'C:\\Users\\shara\\Desktop\\Sharath Python stuff\\Python files\\scoring system json files\\' # going to the correct directory where files are stored.
        for x in os.listdir(target): # using a for loop 
            if x.endswith('.json'): # if files ends with .json, then it will delete those files using the for loop
                os.unlink(target + x) # unlink all json files
            elif x.endswith('.txt'): # delete all files that has extension of .txt
                os.unlink(target + x) # unlink all txt files
        print("All content cleared") # print confimation message
        sys.exit() # exit system
menu() # running menu to initiate program