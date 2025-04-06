def main():
    print("This Program calculates the number of seconds in a normal and leap year.")
    
    no_of_days_in_normal_year: int = 365
    no_of_days_in_leap_year: int = 366
    hours_ina_day: int = 24
    min_ina_hour: int = 60
    sec_ina_min: int = 60
    
    normal_year_sec: int = no_of_days_in_normal_year * hours_ina_day * min_ina_hour * sec_ina_min
    
    leap_year_sec: int = no_of_days_in_leap_year * hours_ina_day * min_ina_hour * sec_ina_min
    
    print(f"\n- The number of seconds in a normal year is: {normal_year_sec} seconds")
    
    print(f"\n- The number of seconds in a leap year is: {leap_year_sec} seconds")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()