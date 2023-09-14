# import module
# from module import *
# import module as helper

# from module import validate_and_execute, user_input_message
#
# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)
#     days_and_unit = user_input.split(":")
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     validate_and_execute(days_and_unit_dictionary)
#     # module.validate_and_execute(days_and_unit_dictionary)

# import os
#
# print(os.name)

import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")