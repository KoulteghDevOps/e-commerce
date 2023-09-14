# calculation_to_units = 24
# name_of_unit = "hours"
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute():
 # nested if that was changed try/and except to handle any form of errors
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
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
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
    # days_and_unit_dictionary = {"days": 20, "unit": "hours"}

    # print(type(user_input.split(", ")))
    # print(user_input.split(", "))
    #
    # print(list_of_days)
    # print(set(list_of_days))
    #
    # print(type(list_of_days))
    # print(type(set(list_of_days)))
    # # for number_of_days_element in user_input.split(", "):
    # for number_of_days_element in set(user_input.split(", ")):
    #     validate_and_execute()

# my_list = ["20", "30", "40"]
# print(my_list[2]) # use index to ref an element of a list
#
# my_dictionary = {"days": 20, "unit": "hours"}
# print(my_dictionary["unit"])  # use the key to access element of dictionary
