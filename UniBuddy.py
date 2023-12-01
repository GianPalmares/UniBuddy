
# Welcome message
print("""\n\t\t\tHI! I'M UNIBUDDY YOUR PERSONLISED CHAT BOT!""")

# Error handling for name input
while True:

    # User input for name, age, and favorite color
    name = input("\nHi! What's your name? ").title()

    if name.replace(" ", "").isalpha():
        break

    else:
        print("Invalid name! Please enter alphabets only.")


# Checks if name has a space, then just takes the first name
if " " in name:

    name = name.split()
    name = name[0]

# Error handling for age input
while True:
    try:
        age = int(float(input("How old are you? ")))

        if age < 0:
            print(f"{name}! Age must be a positive integer.")
            continue
        
        elif age <= 15:
            print(f"You are too young to be using UniBuddy, {name}! I will now shut down.")
            exit()
        
        break
    
    except Exception:
        print(f"Hey {name}! That is not a valid age!")


# Error handling for favourite colour input
while True:

    fav_colour = input("What's your favourite colour? ").upper()

    if fav_colour.replace(" ", "").isalpha():
        break

    else:
        print(f"\nHey {name}! {fav_colour} is not a colour.")
        print("Please enter a valid colour!\n")    


# Personalized greeting based on favorite color
greeting = f"""
Hey there, {name}! I can see your favourite colour is {fav_colour}.
I have some suggestions for you, based on your choice, for a smoother
transition in University!
"""

# Club suggestions based on favorite color
if fav_colour == "BLUE":
    greeting += f"\nSince you love {fav_colour}, you might enjoy the vibrant activities at the 'Blue Art Club'."

elif fav_colour == "GREEN":
    greeting += f"\n{fav_colour} is such a refreshing color! You might want to check out the 'Environmental Science Society'."

elif fav_colour == "RED":
    greeting += f"\n{fav_colour}, the color of passion! Explore your interests at the 'Drama Club'."

elif fav_colour == "YELLOW":
    greeting += f"\n{fav_colour}, the color of sunshine! You might find joy in the 'Outdoor Adventure Club'."

elif fav_colour == "PURPLE":
    greeting += f"\n{fav_colour} is a majestic color! Discover the world of creativity at the 'Art and Design Society'."

elif fav_colour == "PINK":
    greeting += f"\n{fav_colour}, the color of sweetness! Consider joining the 'Baking Club' for some delicious experiences."

elif fav_colour == "ORANGE":
    greeting += f"\n{fav_colour}, the color of energy! Explore the vibrant activities at the 'Energy and Engineering Club'."

elif fav_colour == "TEAL":
    greeting += f"\n{fav_colour}, a unique and calming color! Check out the 'Mindfulness and Wellness Club' for a peaceful experience."

elif fav_colour == "SILVER":
    greeting += f"\n{fav_colour}, a color of sophistication! Delve into the world of business at the 'Business and Finance Society'."

elif fav_colour == "GOLD":
    greeting += f"\n{fav_colour}, a color associated with excellence! Consider joining the 'Academic Excellence Society' for scholarly pursuits."

elif fav_colour == "MAROON":
    greeting += f"\n{fav_colour}, a deep and rich color! Explore cultural events and diversity at the 'Cultural Exchange Club'."

elif fav_colour == "TURQUOISE":
    greeting += f"\n{fav_colour}, a refreshing color! Dive into aquatic activities with the 'Aquatic Adventure Club'."

elif fav_colour == "LAVENDER":
    greeting += f"\n{fav_colour}, a lovely and calming color! Join the 'Gardening Club' for a peaceful connection with nature."

elif fav_colour == "OLIVE":
    greeting += f"\n{fav_colour}, a unique and earthy color! Explore environmental initiatives with the 'Green Earth Society'."

elif fav_colour == "CORAL":
    greeting += f"\n{fav_colour}, a vibrant and lively color! Consider joining the 'Performing Arts Club' for theatrical experiences."

elif fav_colour == "NAVY":
    greeting += f"\n{fav_colour}, a classic and timeless color! Explore intellectual discussions with the 'Debating Society'."

elif fav_colour == "INDIGO":
    greeting += f"\n{fav_colour}, a deep and mysterious color! Join the 'Astronomy Club' for stargazing and cosmic exploration."

elif fav_colour == "VIOLET":
    greeting += f"\n{fav_colour}, a beautiful and enchanting color! Discover the world of arts and culture with the 'Arts Appreciation Club'."

elif fav_colour == "PEACH":
    greeting += f"\n{fav_colour}, a soft and warm color! Connect with fellow students through the 'Social Harmony Club' for friendly gatherings."

elif fav_colour == "STEEL":
    greeting += f"\n{fav_colour}, a modern and industrial color! Dive into technological advancements with the 'Tech Enthusiasts Club'."

# Default suggestion for unknown colors
else:
    greeting += f"\nHey {name}! Your favorite color, {fav_colour} is unique! Unfortunately, I don't have any suggestions regarding you colour choice. But feel free to explore the various clubs and activities on campus."


# Additional message for freshmen under 18
if age <= 18:
    greeting += f"\n\nBeing {age}, there are some fantastic freshman events happening this week. Please check our bulletin boards!"


# Print the personalized greeting
print(greeting)


# Chatbot(UniBuddy) interaction loop
while True:
    
    user_query = input(f"\nHi, {name}! What can I help you with(Type 'exit' to end)? ").lower()
    
    if user_query == "exit":
        print(f"Goodbye, {name}! If you have more questions, feel free to ask later.")
        break

    # Respond to specific queries
    if "library" in user_query:
        print("Ah, the library, a great place to dive into knowledge! Head straight past the main entrance, and you'll find it on your left. Need help with anything else?")
    
    elif "join" in user_query and "debate club" in user_query:
        print("Fantastic choice! To join the debate club, swing by the student activities fair tomorrow at the main building. Look for the 'Debate Club' booth, and they'll get you all set up. Exciting, right?")
    
    elif "clubs" in user_query or "student organizations" in user_query:
        print("There are numerous student clubs and organizations on campus! You can explore them at the student activities fair or check the university website for a list of clubs.")
    
    elif "cafeteria" in user_query or "food options" in user_query:
        print("Hungry? The cafeteria is located near the student center. They offer a variety of delicious options. Enjoy your meal!")

    elif "schedule" in user_query or "classes" in user_query:
        print("You can find your class schedule on the university portal. Make sure to check it regularly for any updates.")
    
    elif "sports" in user_query or "athletics" in user_query:
        print("Interested in sports? Check out the university's athletics department for information on upcoming games, tryouts, and sports clubs.")
    
    elif "housing" in user_query or "accommodation" in user_query:
        print("If you have questions about housing or accommodation, reach out to the university's housing office. They can provide details on available options and the application process.")
    
    elif "transportation" in user_query or "bus" in user_query:
        print("For transportation around campus, there's a bus service with regular routes. You can find the bus stops marked across the university.")
    
    elif "study tips" in user_query or "exam preparation" in user_query:
        print("Looking for study tips? Consider joining study groups, using the library resources, and creating a schedule to manage your study time effectively.")
    
    elif "events" in user_query or "social activities" in user_query:
        print("Stay updated on university events and social activities by checking bulletin boards around campus and following the university's social media accounts.")
    
    elif "career services" in user_query or "job opportunities" in user_query:
        print("Explore career services for job fairs, resume workshops, and internship opportunities. The career center can help you kickstart your professional journey.")
    
    elif "health services" in user_query or "medical facilities" in user_query:
        print("For health services and medical facilities, visit the university health center. They provide medical assistance, counseling, and wellness programs.")
    
    elif "tuition" in user_query or "financial aid" in user_query:
        print("For information on tuition, fees, and financial aid options, contact the university's financial aid office. They can provide guidance on scholarships, grants, and payment plans.")
    
    elif "technology" in user_query or "IT support" in user_query:
        print("Need tech help? The university's IT support team can assist you with issues related to your computer, internet, and software. Reach out to them for a quick resolution.")
    
    elif "volunteer opportunities" in user_query or "community service" in user_query:
        print("Explore volunteer opportunities and community service programs through the university's community engagement office. It's a great way to give back to the community and build connections.")
    
    elif "weather" in user_query or "climate" in user_query:
        print("For weather updates, you can check local news channels or use weather apps. The climate here varies, so be prepared for different seasons throughout the year.")
    
    elif "mentorship programs" in user_query or "academic guidance" in user_query:
        print("Looking for academic guidance? The university may offer mentorship programs or academic advising services. Connect with your academic advisor for personalized support.")
    
    elif "graduation requirements" in user_query or "degree completion" in user_query:
        print("To understand graduation requirements and ensure you're on track for degree completion, review the university's academic catalog or speak with your academic advisor.")
    
    elif "language clubs" in user_query or "language exchange" in user_query:
        print("Interested in language clubs or language exchange programs? Check out the university's international programs office or language departments for opportunities to practice and learn new languages.")
    
    elif "swimming" in user_query or "swim club" in user_query or "swimming pool" in user_query:
        print("If you're into swimming, the university has a fantastic swimming pool available for students. You can also explore joining the swim club to meet fellow swimmers and participate in events.")
    
    elif "running trails" in user_query or "jogging paths" in user_query:
        print("If you enjoy running or jogging, there are scenic running trails and jogging paths around the campus. Lace up your shoes and explore the beauty of the outdoors while staying active!")
    
    elif "bike trails" in user_query or "cycling routes" in user_query:
        print("Cycling enthusiasts can explore bike trails and cycling routes around the campus. It's a great way to stay fit and enjoy the outdoor scenery. Don't forget your helmet!")
    
    elif "outdoor events" in user_query or "campus festivals" in user_query:
        print("Stay tuned for outdoor events and campus festivals throughout the year. These events often feature live music, food, and various outdoor activities. Keep an eye on announcements for upcoming festivities!")
    
    elif "fitness classes" in user_query or "group workouts" in user_query:
        print("Joining fitness classes or group workouts is a fantastic way to stay active and meet new friends. Check the university's fitness center schedule for classes like yoga, Zumba, and more.")
    
    elif "climbing" in user_query or "rock climbing" in user_query or "bouldering" in user_query:
        print("If you're into climbing, the university has a dedicated climbing wall and bouldering area at the sports complex. It's a great way to challenge yourself physically and mentally. Check the schedule for open climbing sessions and events!")

    elif "chess club" in user_query or "chess tournaments" in user_query:
        print("For chess enthusiasts, the university has an active Chess Club. You can join the club to participate in tournaments, improve your skills, and connect with fellow chess lovers. Keep an eye out for upcoming chess events on campus!")
    
    elif "e-sports" in user_query or "gaming club" in user_query:
        print("If you're into e-sports and gaming, check out the university's Gaming Club. They organize gaming tournaments, events, and provide a space for gamers to connect and play together. Stay updated on gaming club activities through their social media channels!")

    # Default response for unknown queries            
    else:
        print("I'm here to help! If you have any specific questions, feel free to ask.")
    