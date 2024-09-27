from datetime import datetime

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    elif 18 <= hour < 22:
        return "Good Evening!"
    else:
        return "Good Night!"

def main():
  
    now = datetime.now()
    hour = now.hour

    
    greeting = get_greeting(hour)

   
    print(greeting)

if __name__ == "__main__":
    main()
