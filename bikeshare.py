import time
import pandas as pd
import numpy as np

CITY_DATA= { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv','washington': 'washington.csv' }
cities     = [ "new york city", "chicago", "washington" ]
months     = [ "all","january", "february", "march", "april", "may", "june"]
days       = [ "all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def input_user(selections, message):
    select = ""
    while len(select) == 0:
        select = input(message)
        select= select.strip().lower()

        if select in selections:
            return select
        else:
            select = ""
            print("please enter a valid selecion")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n ---- Hello! Let\'s explore some US bikeshare data! ----\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_user(cities, "please enter the city(new york city,chicago or washington):")
    # get user input for month (all, january, february, ... , june)
    month = input_user(months, "please enter the month:(january, february, march, april, may, june or all):")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_user(days, "please enter the day you want:")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city], index_col = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["month"] = df['Start Time'].dt.month
    df["week_day"] = df['Start Time'].dt.weekday_name
    df["start_hour"] = df['Start Time'].dt.hour
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']
   

    if month != 'all':
        month_index =months.index(month) + 1 
        df = df[df["month"] == month_index ] 

    if day != 'all':
        df = df[df["week_day"] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nCalculating The Most Frequent Times of Travel ... \n')
    start_time = time.time()

    # display the most common month
    month_index = df["month"].mode()[0] - 1
    most_common_month = months[month_index]

    print("the most common month is: ", most_common_month)

    # display the most common day of week
    most_common_day = df["week_day"].mode()[0]
    print("the most common day is: ", most_common_day)

    # display the most common start hour
    most_common_hour = df["start_hour"].mode()[0]
    print("the most common hour is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip ...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    print("the most used start is: ", most_used_start)

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    print("the most used end is: ", most_used_end)

    # display most frequent combination of start station and end station trip
    most_common_combination = df["start_end"].mode()[0]
    print("the most frequent combination of start station and end station trip is: ", most_common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration ...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("the total time of travel is: ", total_travel_time)

    # display mean travel time
    average_time = df["Trip Duration"].mean()
    print("the mean travel time is: ", average_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def user_stats(df):
    """Displays statistics on bikeshare users."""
   
    print('\nCalculating User Stats ...\n')
    start_time = time.time()
    # Display counts of user types
    print("counts of user type is:{}".format(df['User Type'].value_counts()))

    # Display counts of gender
    if 'Gender' in df.columns:
        print("counts of gender is:{}".format(df['Gender'].value_counts()))
    else:
        print('there is no gender info')

    # Display earliest, most recent, and most common year of birth
    if 'year of birth' in df.columns:
        print("the earliest year of birth is: {}".format(df['year_of_birth'].min()))
        print("the recent year of birth is: {}".format(df['year_of_birth'].max()))
        print("the most common year of birth is: {}".format(df['year of birth'].mode()[0]))
    else:
        print('there is no year of birth information')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()  
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
