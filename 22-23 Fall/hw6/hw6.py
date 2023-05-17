
def name_correction(name):
  words = name.split()
  
  # Initialize a list to store the corrected name parts
  result_words = []
  
  # Iterate through the parts
  for word in words:
    # Check if the part is "von" or "de"
    if word.lower() in ['von', 'de']:
      # If yes, append it as it is
      result_words.append(word.lower())
    else:
      # If not, make the first letter uppercase and all others lowercase
      result_words.append(word[0].upper() + word[1:].lower())
  
  # Join the corrected name parts and return
  return ' '.join(result_words)

def salary_increment(date, position, salary):
  # Extract the year from the date
  year = int(date.split('.')[-1])
  
  # Check if the year is before 2010 or not
  if year < 2010:
    # If yes, apply the salary increment according to the position
    if position.lower().split()[-1] == 'manager':
      return 8000
    else:
      return 2500
  else:
    # If not, apply the salary increment according to the position
    if position.lower().split()[-1] == 'manager':
      return 5000
    else:
      return 0

def main():
    isDone = False
    while not isDone :
        # Get the employee name
        name = input("Enter employee name: ")
        
        # Correct the employee name
        corrected_name = name_correction(name)
        
        # Get the base salary
        salary = int(input("Enter employee base salary: "))
        
        # Get the position
        position = input("Enter employee position: ")
        
        # Get the employment date
        date = input("Enter employment date = ")
        
        # Calculate the salary increment
        increment = salary_increment(date, position, salary)
        newSalary = salary + increment
        
        # Print the fixed employee name and incremented salary
        print(f"{corrected_name}'s current salary should be $ {newSalary}")
        print()
        

        isCommandRead = False
        while not isCommandRead :
            # Ask if the user wants to enter information for another employee
            answer = input("Do you want to enter another employee (Y/N)? ")
            
            # Check if the answer is "Y", "N" or something else
            if answer[0].upper() == 'Y':
                print()
                isCommandRead = True
            elif answer[0].upper() == 'N':
                isDone = True
                isCommandRead = True
            else:
                # If something else, print a warning and continue the loop
                print("Can you please enter a valid answer.")

# Call the main function
main()
