import time
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    city=""
    month=""
    day=""
    while(True):
        try:
            city=str(input("please enter the name of the city"))
            month=str(input("pleae enter the month"))
            day=str(input("pleae enter the day"))
            if(city in ['chicago','new york city','washington'] and month in ['all','january', 'february', 'march', 'april', 'may', 'june'] and day in  [range(1,32),'all']):
                break
            else:
                print("there is an input error ")
        except Exception as ex:
            print("there is an input error ")

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
    db=pd.read_csv(CITY_DATA[city])
    
    db['Start Time']=pd.to_datetime(db['Start Time'])
    if(city=='washington'):
        db['Birth Year']='1998.0'
        db['Gender']='male'
        pass
    db['hour'] = db['Start Time'].dt.hour
    db['month'] = db['Start Time'].dt.month
    db['day_of_week']=db['Start Time'].dt.day_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        db = db[db['month'] == month]
    if day != 'all':
        db = db[db['day_of_week'] == day.title()]
    return db


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'].mode())

    # display the most common day of week
    print(df['day_of_week'].mode())


    # display the most common start hour
    print(df['hour'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode())

    # display most commonly used end station
    print(df['End Station'].mode())


    # display most frequent combination of start station and end station trip
    print(df[['End Station','Start Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df['Trip Duration'].sum())

    # display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df:DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df.groupby(['User Type']).count())

    # Display counts of gender
    print(df.groupby(['Gender']).count())


    # Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min())
    print(df['Birth Year'].max())
    print(df['Birth Year'].mode())
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
