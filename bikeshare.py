import time
import pandas as pd
import numpy as np

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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Hello! Let\'s explore some US bikeshare data! \nEnter city name you would like to see the data for Chicago, new york city, washington? \n")
        if city.lower() not in ["chicago", "new york city", "washington"]:
            print("The city you enter is not in the lists. Please try again")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter Month: january, february, march, april, may, june?\n")
        if month.lower() not in ["all", "january", "february", "march", "april", "may", "june"]:
            print("invalid month")
        else:
            break

   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day: sunday, monday, tuesday, wednesday, thursday, friday, saturday?\n")
        if day.lower() not in ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
            print("invalid day")
        #if day.lower() in ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
        else:
            break

    #print('-'*40)


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract month from start time to create a new column
    df['month'] = df['Start Time'].dt.month

    # Filter by month if applicable
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index (month) + 1

        # Filter by month to create a new dataframe
        df = df[df['month'] == month]

        # Extract day of week from start time to create a new column
        df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by day of week if applicable
    if day != "all":

    # Filter by day of week to create a new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("The most common month : \n", common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week : \n", common_day)

    # TO DO: display the most popular hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour : \n", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The common start station is \n", common_start_station)

   
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The common end station is \n", common_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_trip = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent trip from start station to end station: \n", frequent_trip)

    return frequent_trip

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_travel_time = np.sum(df['Travel Time'])
    print("The total traveling time \n", total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = np.mean(df['Travel Time'])
    print("The average traveling time \n", average_travel_time)

    return total_travel_time, average_travel_time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User Type: \n", user_type)

    # TO DO: Display counts of gender
    try:        
        gender_types = df['Gender'].value_counts()
        print("Gender Type: \n", gender_types)
    except:
        print("There is no gender data.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].max()
        print("The earlist birth year : \n", earliest_birth)

        latest_birth = df['Birth Year'].min()
        print("The latest birth year : \n", latest_birth)

        common_birth = df['Birth Year'].mode()[0]
        print("The most common birth year : \n", common_birth)
    
    except:
        print("There is no birth year data.")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    row_index = 0

    view_data = input("Would you like to see rows of the data ? Please type 'yes' or 'no' \n").lower()

    while True:

        if view_data == 'no':
            return

        if view_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5


        view_data = input("Would you like to see five more rows of the data ? Please type 'yes' or 'no' \n").lower()


def main():
    while True:
       
        city, month, day = get_filters()        
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
