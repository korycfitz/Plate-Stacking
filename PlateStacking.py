import warnings
# Steps
# 1. Define a list at file scope
# 2. Stub up a function for each menu item
    # 0. Stub up a function to [Exit]
    # 1. Stub up a function that will be used to add a plate to the top of the stack
    # 2. Stub up a function that will be used to print the plates to the terminal
    # 3. Stub up a function that will be used to remove 1-to-n plates from the top of the stack
# 3. Develop the stubbed up function to ensure they work as they are intended
# 4. Test the functions by giving them user input, in order to make sure they work as intended 
# 5. Stub up any extra non-required utility functions and develop these functions
# 6. Test to make sure these new functions work as intended

# Decisions
# 1. Do I want to write each menu item in its own file, and import the functions to other files?
    # I will just write them all in the same file to make it easier to naviage for the user
# 2. What will my default starting list contain? 
    # I will define an empty list
# 3. How will we make sure larger plates are 'stacked below' (further to the left in the list) smaller plates
    # We can use .sort(), but this sorts in ascencing order. We can reverse the list afterwords but I might think of a simpler solution as I code
# What loops?

# What data is needed?
    # 1. We need user input, and we need to convert it into an int as a plate is represented by its size

# Which data types are appropriate? 
    # 1. integer data type is appropriate. Also, when we use input() to get a users input, this gives us a string, so this is also an appropriate data type, but we will need to convert this input into an integer in order to use certain methods on it correctly, like sort() onces its appended to the list

# Does creating a function simplify the problem?
    # Yes, as it makes the code much cleaner and easier to follow

stack = [] # define an empty plate

# stub up a function to exit so I am just having it return nothing, which will exit us out of the function
def exit():
  return

# I could use cases instead of if/elif statements, but because there arent many cases, if/elif statements are about the same amount of code, thus I think it is fair to use either
def addPlate(stack):
  plate = int(input("Please enter a plate size: "))
  # If the plate is less than or equal to zero
  if (plate <= 0):
    # Issue a warning and don't add the plate.
    # I will import warnings module for this
    warnings.warn("The Plate Size Can Not Be Less Than or Equal to 0")
  elif (len(stack) == 0): #If there are no plates on the stack, add it.
    stack.append(plate)  
    # If the current plate is too big, issue a warning and don't add the plate.
  elif (stack[-1] < plate):
    warnings.warn("The Plate You are Trying to Add is Larger than the Top Plate, and Therefore can not be Added.")
  else: #there are plates on the stack, and the top plate on the stack is not smaller than the plate the user is trying to add
    stack.append(plate) #Therefore we can add it to the top of the stack.

# testing the addPlate() function
addPlate(stack)

