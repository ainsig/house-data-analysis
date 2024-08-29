"""Arlo Insigne, SDEV300, Lab 5"""

import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def show_stats(column):
    """Function to print the count, mean, standard deviation,
    minimum, and maximum of the selected column"""

    # Printing statistics: count, mean, standard deviation,
    # min, and max
    print("The statistics for this column are: \n")

    try:
        print(f"Count: {column.count().round(2)}")
    except TypeError as type_err:
        print(type_err)
    try:
        print(f"Mean: {column.mean().round(2)}")
    except AttributeError as attr_err:
        print(attr_err)
    try:
        print(f"Standard deviation: {column.std().round(2)}")
    except AttributeError as attr_stdev_err:
        print(attr_stdev_err)
    try:
        print(f"Min: {column.min().round(2)}")
    except AttributeError as attr_min_err:
        print(attr_min_err)
    try:
        print(f"Max: {column.max().round(2)}")
    except AttributeError as attr_max_err:
        print(attr_max_err)
        print("\n")

    # Using pyplot to display the histogram of the column
    try:
        x = np.random.normal(column.mean(), column.std(), 500)
        plt.hist(x, bins=20)
        plt.grid(True)
        plt.show()
        print("The histogram of this column is now displayed." + "\n")

    except AttributeError as rand_err:
        print(rand_err)
        print("\n")

def show_column(col_name, file_name):
    """Function that reads the file from present working directory and
    uses the show_stats function to generate data."""

    # Catching error if the file does not exist
    try:
        c_name = ""
        # Allows user to access file in present working directory
        current_directory = os.getcwd()
        csv_reader = pd.read_csv(fr'{current_directory}/{file_name}')

        try:
            c_name = csv_reader[col_name]
        except KeyError as key_error:
            print("The following column was not found: ")
            print(key_error)
            print("\n")
        try:
            show_stats(c_name)
        except UnboundLocalError as u_err:
            print(u_err)
    except FileNotFoundError as file_err:
        print(file_err)

if __name__ == '__main__':
    try:
        is_on = True
        while is_on:

            is_invalid_main = False
            main_menu_format = re.compile(r'[123]')
            selection = ""

            while not is_invalid_main:
                try:
                    print("\n" + "***************** Welcome to the "
                                 "Python Data Analysis App********** \n"
                          "\n" + "Select the file you want to analyze: \n"
                          "\n" + "1. Population Data \n"
                          "2. Housing Data \n"
                          "3. Exit the Program \n")
                    selection = input()
                    if selection == "":
                        raise EOFError
                    elif main_menu_format.match(selection) is None:
                        raise ValueError
                    else:
                        is_invalid_main = True
                except EOFError:
                    print("You left the field blank. " + "\n"
                          "Please provide option from the menu (1, 2, 3).")
                except ValueError:
                    print("Please provide option from the menu (1, 2, 3).")

            # Selecting population data
            if selection == "1":

                print(f"You selected {selection}: population data. \n")
                is_on_pop_data = True
                while is_on_pop_data:

                    is_invalid_pop = False
                    pop_menu_format = re.compile(r'[abcd]')
                    select_pop_data = ""

                    # Input validation for the population data main menu
                    while not is_invalid_pop:
                        try:
                            print("Select the Column you want to analyze: \n"
                                  "a. Pop Apr 1 \n"
                                  "b. Pop Jul 1 \n"
                                  "c. Change Pop \n"
                                  "d. Exit Population Data \n")
                            select_pop_data = input()
                            if select_pop_data == "":
                                raise EOFError
                            elif pop_menu_format.match(select_pop_data) is None:
                                raise ValueError
                            else:
                                is_invalid_pop = True
                        except EOFError:
                            print("You left the field blank. " + "\n"
                                  "Please provide a letter from the menu (a, b, c ,d).")
                        except ValueError:
                            print("Please only enter letters from the menu (a, b, c, d).")

                    # Main menu for the population data
                    if select_pop_data == "a":
                        print(f"You selected {select_pop_data}: Pop Apr 1 \n")
                        show_column("Pop Apr 1", "PopChange.csv")
                    elif select_pop_data == "b":
                        print(f"You selected {select_pop_data}: Pop Jul 1 \n")
                        show_column("Pop Jul 1", "PopChange.csv")
                    elif select_pop_data == "c":
                        print(f"You selected {select_pop_data}: Change Pop \n")
                        show_column("Change Pop", "PopChange.csv")
                    elif select_pop_data == "d":
                        print(f"You selected {select_pop_data}: Return to main menu.")
                        is_on_pop_data = False

            # Selecting housing data
            elif selection == "2":

                print(f"You selected {selection}: house data. \n")
                is_on_house_data = True

                while is_on_house_data:
                    is_invalid_house = False
                    house_menu_format = re.compile(r'[abcdef]')
                    select_house_data = ""

                    # Input validation for the housing data menu
                    while not is_invalid_house:
                        try:
                            print("Select the Column you want to analyze: \n"
                                  "a. Age \n"
                                  "b. Bedrooms \n"
                                  "c. Year Built \n"
                                  "d. Rooms \n"
                                  "e. Utility \n"
                                  "f. Exit Housing Data \n")
                            select_house_data = input()
                            if select_house_data == "":
                                raise EOFError
                            elif house_menu_format.match(select_house_data) is None:
                                raise ValueError
                            else:
                                is_invalid_house = True
                        except EOFError:
                            print("You left the field blank. " + "\n"
                                  "Please provide a letter from the menu (a, b, c, d, e, f).")
                        except ValueError:
                            print("Please only enter letters from the menu (a, b, c, d, e, f).")

                    # Using show_column function to analyze and display column stats
                    if select_house_data == "a":
                        print(f"You selected {select_house_data}: AGE \n")
                        show_column("AGE", "Housing.csv")
                    elif select_house_data == "b":
                        print(f"You selected {select_house_data}: BEDROOMS \n")
                        show_column("BEDRMS", "Housing.csv")
                    elif select_house_data == "c":
                        print(f"You selected {select_house_data}: BUILT \n")
                        show_column("BUILT", "Housing.csv")
                    elif select_house_data == "d":
                        print(f"You selected {select_house_data}: ROOMS \n")
                        show_column("ROOMS", "Housing.csv")
                    elif select_house_data == "e":
                        print(f"You selected {select_house_data}: UTILITY \n")
                        show_column("UTILITY", "Housing.csv")
                    elif select_house_data == "f":
                        print(f"You selected {select_house_data}: Return to main menu.")
                        is_on_house_data = False

            # Exiting the application
            elif selection == "3":
                print(f"You selected {selection}: Thank you for using the application. Goodbye!")
                is_on = False

    except KeyboardInterrupt:
        print("\n" + "The application was terminated. Thank you. Goodbye!")
