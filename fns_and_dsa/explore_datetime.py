from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate and display a future date by adding specified days to the current date.
    
    Args:
        current_date (datetime): The current date and time
        days_to_add (int): Number of days to add to the current date
    """
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    """
    Main function to demonstrate datetime operations.
    """
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        future_date = calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
