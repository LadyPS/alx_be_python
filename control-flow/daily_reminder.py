task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority: 
     case "high":
          if time_bound == "yes":
               print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
          elif time_bound == "no":
               print(f"Note: '{task}' is a high priority task. cosider completiing it when you have free time.")
     case "medium":
          if time_bound == "yes":
               print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
          elif time_bound == "no":
               print(f"Note: '{task}' is a medium priority task. consider completing it when yu have free time.")
     case "low": 
          if time_bound == "yes":
               print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
          else:
               print(f"Note: '{task}' is a low priority task. consider completing it when you have free time.")
