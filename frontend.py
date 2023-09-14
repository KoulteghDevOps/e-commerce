# time_in_units = 20*24*60*60
#
# def time_in_seconds():
#     print(time_in_units)
#
# time_in_seconds()##

# calculation_to_units = 24
# name_of_unit = "hours"
#
# # def days_to_units(num_of_days):
# # ##    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
# #     return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
# #
# # ## my_var = days_to_units(35)
# #
# # user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
# # user_input_number = int(user_input)
# # # print(my_var)
# # calculated_value = days_to_units(user_input_number)
# # print(calculated_value)
#
# def days_to_units(num_of_days):
# #    print(num_of_days > 0)
#
#     condition_check = num_of_days > 0
#     print(type(condition_check))
#
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#     elif num_of_days == 0:
#         return f"You entered 0 and you have to enter a positive number, dey play"
#     # else:
#     #     return "you entered a negative value, so no conversion for you!"
#
# user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
# if user_input.isdigit():
#     calculated_value = days_to_units(int(user_input))
#     print(calculated_value)
# else:
#     print("your input is not a number. Don't ruin my program!")
# # user_input_number = int(user_input)
# # calculated_value = days_to_units(user_input_number)

# Cleaning up my code

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):

    # if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    # elif num_of_days == 0:
    #     return f"You entered 0 and you have to enter a positive number, dey play"

def validate_and_execute():

    # this is a sample with nested if
#     if user_input.isdigit():
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
# #           calculated_value = days_to_units(int(user_input))
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered a 0, please enter a valid positive number!")
#     else:
#         print("your input is not a number. Don't ruin my program!")


    # nested if made try/and except to cover any form of errors
    try:
        user_input_number = int(number_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            #           calculated_value = days_to_units(int(user_input))
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number!")
        else:
            print("you entered a negative number, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    for number_of_days_element in user_input.split(", "):
        validate_and_execute()

# while True:
#     user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
#     validate_and_execute()

# user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
# validate_and_execute()
#
# print(type(30))
# print(type(30.99))
# print(type("This is suppose to be a string!"))