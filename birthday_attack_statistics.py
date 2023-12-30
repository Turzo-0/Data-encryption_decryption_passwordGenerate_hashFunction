

from random import randint
from datetime import datetime, timedelta


def look_for_a_collision(   
                    max_attempts : int, 
                    date_from : datetime, 
                    date_to : datetime
                    ):
    """Returns a list of birthdays prepended with True or False as the first element.

    Parameters
    ----------
    max_attmpets : str, mandatory
        The maximumnumber of tries to find a collision

    date_from : datetime, mandatory
        The first date (inclusive) in the search space to look for collision

    date_to : datetime, mandatory
        The last date (inclusive) in the search space to look for collision. Must be larger than fate_from.

    """

    found_collision = False
    attempt = 1

    list_of_birthdays = []
    number_of_days_between = (date_to - date_from).days + 1
    print ("date range: ",number_of_days_between)
    
    #loop through until finding a collision of birthdays.
    # If there is a collision then add True as the first element in the list
    # If there is no colision after a number of attempts, then add False as the first element of the list
    while ( (not found_collision) and (attempt <= max_attempts ) ) :
        random_birthday = date_from + + timedelta(days = randint(0, number_of_days_between))
        if random_birthday in list_of_birthdays:
            found_collision = True
            list_of_birthdays = [True] + list_of_birthdays
        list_of_birthdays.append(random_birthday)
        attempt += 1
    
    if not found_collision:
        list_of_birthdays = [False] + list_of_birthdays
    
    return list_of_birthdays



def run_number_of_tests( number_of_runs : int, 
                         max_attempts_per_run : int, 
                         date_from : datetime, 
                         date_to : datetime
                         ):
    """Runs the look_for_a_collision function a number of times with specified parameters"""
    if type(number_of_runs) == int and number_of_runs > 0:
        run = 1
        sum_of_number_of_attempts = 0
        while (run <= number_of_runs):
            print("==========")
            print("Run ", run)
            result_list = look_for_a_collision( max_attempts_per_run, date_from, date_to )
            print("found a collision? ", result_list[0])
            sum_of_number_of_attempts = sum_of_number_of_attempts + len(result_list) - 1
            print("number of attempts tried: ", len(result_list) - 1)
            [print(x.strftime('%Y-%m-%d'), end = ", ") for x in result_list if type(x) == datetime] # list comprehension for printing
            print("\n==========")
            run += 1
        print("average number of attempts to find a collision over the ", number_of_runs, " runs is ", sum_of_number_of_attempts / (run -1))


def main():
    """starting from here"""
    date_to_start_from = datetime( 1999, 7, 27)
    date_to_end_at = datetime( 2023, 9, 24 )
    run_number_of_tests( 1000, 1000, date_to_start_from, date_to_end_at )


# this will make sure that main() is the function that gets called 
# first when this file is executed on its own (and not included as
# part of another file or import).
if __name__ == "__main__":
    main()