import time
def get_greetings():
    somoy = time.strftime(("%H:%M"))
    print(somoy)

    hour = int(time.strftime("%H"))
    if hour < 12:
        print("Good Mornign sir!")
    elif hour < 15:
        print("It's Noon sir! You should rest")
    elif hour < 17:
        print("Good Afternoon sir!")
    elif hour < 19:
        print("Good Evening sir!")
    elif hour < 21:
        print("It's night sir!")
    else:
        print("It's late night sir! You should rest")
get_greetings()