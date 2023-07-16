import pandas as pd
import time

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

setMonth = [     
    'all', 
    'january', 
    'february', 
    'march', 
    'april', 
    'may', 
    'june'
]
setDay = [
    'all', 
    'monday', 
    'tuesday', 
    'wednesday', 
    'thursday', 
    'friday', 
    'saturday', 
    'sunday'
]

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington)
    city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    while city not in CITY_DATA:
        print("Invalid city name. Please try again.")
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    
    # Get user input for month (all, january, february, ... , june)
    month = input("Which month? (all, january, february, ... , june) ").lower()
    while month not in setMonth:
        print("Invalid month. Please try again.")
        month = input("Which month? (all, january, february, ... , june) ").lower()
    
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? (all, monday, tuesday, ... sunday) ").lower()
    
    while day not in setDay:
        print("Invalid day. Please try again.")
        day = input("Which day? (all, monday, tuesday, ... sunday) ").lower()
    
    print('-'*40)
    return city, month, day

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Display the most common month
    common_month = df['Month'].mode()[0]
    print('Most Common Month:', common_month)
    
    # Display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', common_day)
    
    # Display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # Display the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)
    
    # Display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    
    # Display the most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Start-End Station'].mode()[0]
    print('Most Common Trip:', common_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')
    
    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time, 'seconds')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:')
    print(user_types)
    
    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nGender data is not available for this city.')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year:', int(earliest_birth_year))
        print('Most Recent Birth Year:', int(most_recent_birth_year))
        print('Most Common Birth Year:', int(common_birth_year))
    else:
        print('\nBirth year data is not available for this city.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()

        df = pd.read_csv(CITY_DATA[city])
        
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        
        df['Month'] = df['Start Time'].dt.month
        df['Day of Week'] = df['Start Time'].dt.day_name()
        df['Hour'] = df['Start Time'].dt.hour
        
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['Month'] == month]
        
        if day != 'all':
            df = df[df['Day of Week'] == day.title()]
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start_row = 0
        end_row = 5
        raw_data = input("Would you like to see the raw data? (yes/no) ").lower()
        while raw_data == 'yes':
            print(df.iloc[start_row:end_row])
            start_row += 5
            end_row += 5
            raw_data = input("Would you like to see more raw data? (yes/no) ").lower()
        
        restart = input('\nWould you like to restart? (yes/no) ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
