# SMART BUDGET: DAILY EXPENSE TRACKER (GROUP PROJECT)
# Global variables shared across all 4 group members
expenses_list = []      # List storing all expense dictionaries
monthly_budget = 500.0  # Default monthly budget limit in dollars


# ==============================================================================
# SECTION 1: MEMBER 1 - SETUP, BANNER & INPUT VALIDATION HELPERS (LINES 1-100)
# Member 1 Responsibilities: Welcome screen, menu headers, date & amount checks
# ==============================================================================

def print_welcome_banner():
    """Displays a friendly title banner when the program starts."""
    print("============================================================")
    print("      WELCOME TO SMART BUDGET TRACKER - GROUP PROJECT      ")
    print("          A Simple & Easy Daily Expense Tracking Tool       ")
    print("============================================================")


def print_divider_line():
    """Helper function to print a simple line divider."""
    print("------------------------------------------------------------")


def print_section_header(title_text):
    """Helper function to print styled section headers."""
    print("\n" + "=" * 50)
    print("  " + title_text.upper())
    print("=" * 50)


def get_valid_amount():
    """
    Prompts the user for a dollar amount.
    Uses a while loop and try-except block to make sure input is a positive float.
    """
    while True:
        user_input = input("Enter expense amount ($): ").strip()
        try:
            amount = float(user_input)
            if amount > 0:
                return amount
            else:
                print(" Invalid amount! Please enter a number greater than 0.")
        except ValueError:
            print(" Invalid input! Please enter a valid number (e.g., 15.50).")


def get_valid_date():
    """
    Prompts the user for a date in YYYY-MM-DD format.
    Uses basic string length and character checks for validation.
    """
    while True:
        print("Enter date (YYYY-MM-DD) or press Enter for default [2026-11-25]:")
        date_input = input("Date: ").strip()
        
        if date_input == "":
            return "2026-11-25"
        
        if len(date_input) == 10:
            if date_input[4] == "-" and date_input[7] == "-":
                return date_input
            else:
                print(" Incorrect format! Hyphens (-) must be at positions 5 and 8.")
        else:
            print(" Invalid date length! Please use YYYY-MM-DD (10 characters).")


def get_valid_category():
    """
    Prompts user to enter or select an expense category.
    Ensures the category name is not left blank.
    """
    while True:
        print("\nCommon Categories: Food, Transport, Rent, Shopping, Bills")
        category_input = input("Enter expense category: ").strip()
        
        if category_input != "":
            return category_input.title()
        else:
            print(" Category name cannot be empty! Please try again.")




# --- END OF SECTION 1 (MEMBER 1: LINES 1 TO 100) ---
# ==============================================================================
# SECTION 2: MEMBER 2 - ADD EXPENSES & VIEW EXPENSE RECORDS (LINES 101-200)
# Member 2 Responsibilities: Adding new expenses & listing expense records
# ==============================================================================

def add_single_expense():
    """
    Asks the user for expense details and adds the dictionary to expenses_list.
    """
    print_section_header("Member 2: Add New Expense")
    
    # Get validated inputs using Member 1's functions
    expense_date = get_valid_date()
    expense_category = get_valid_category()
    expense_amount = get_valid_amount()
    
    note_input = input("Enter a brief description/note (optional): ").strip()
    if note_input == "":
        note_input = "No note provided"

    # Store expense details inside a dictionary
    new_expense_record = {
        "date": expense_date,
        "category": expense_category,
        "amount": expense_amount,
        "note": note_input
    }

    # Add dictionary record to the global expenses list
    expenses_list.append(new_expense_record)
    print("\n Success: New expense added to your records!")


def add_multiple_expenses():
    """
    Allows the user to enter multiple expenses in a loop until choosing to stop.
    """
    print_section_header("Member 2: Batch Add Expenses")
    
    adding_items = True
    while adding_items:
        add_single_expense()
        
        user_response = input("\nAdd another expense? (yes/no): ").strip().lower()
        if user_response == "yes" or user_response == "y":
            adding_items = True
        else:
            adding_items = False
            print("Exiting batch addition mode.")


def view_all_expenses():
    """
    Displays all recorded expenses line by line using a for loop.
    Calculates cumulative total spending using an accumulator variable.
    """
    print_section_header("Member 2: View All Expenses")
    
    if len(expenses_list) == 0:
        print("ℹ No expenses recorded yet! Please add an expense first.")
        return

    print(f"{'ID':<4} | {'Date':<10} | {'Category':<15} | {'Amount':<10} | {'Note'}")
    print_divider_line()

    total_spending_sum = 0.0
    item_counter = 1

    # for loop iterating over all expense records in expenses_list
    for expense_item in expenses_list:
        d = expense_item["date"]
        c = expense_item["category"]
        a = expense_item["amount"]
        n = expense_item["note"]
        
        print(f"{item_counter:<4} | {d:<10} | {c:<15} | ${a:<9.2f} | {n}")
        
        total_spending_sum = total_spending_sum + a
        item_counter = item_counter + 1

    print_divider_line()
    print(f"TOTAL CUMULATIVE SPENDING: ${total_spending_sum:.2f}")


def view_quick_summary():
    """Prints a quick count and sum of current expenses."""
    print_section_header("Member 2: Quick Spending Summary")
    
    total_count = len(expenses_list)
    total_sum = 0.0
    
    for item in expenses_list:
        total_sum = total_sum + item["amount"]
        
    print(f"Total Number of Entries : {total_count}")
    print(f"Total Dollars Spent     : ${total_sum:.2f}")



# --- END OF SECTION 2 (MEMBER 2: LINES 101 TO 200) ---
# ==============================================================================
# SECTION 3: MEMBER 3 - CATEGORY ANALYTICS, BUDGET ALERTS & SEARCH (LINES 201-300)
# Member 3 Responsibilities: Category breakdown, budget warnings, search feature
# ==============================================================================

def show_category_breakdown():
    """
    Calculates total spending for each category using a dictionary and for loop.
    """
    print_section_header("Member 3: Category Breakdown")
    
    if len(expenses_list) == 0:
        print(" No data available to calculate category totals.")
        return

    category_totals_dict = {}

    # Accumulate spending per category using a for loop
    for item in expenses_list:
        cat_name = item["category"]
        amt_val = item["amount"]
        
        if cat_name in category_totals_dict:
            category_totals_dict[cat_name] = category_totals_dict[cat_name] + amt_val
        else:
            category_totals_dict[cat_name] = amt_val

    print(f"{'Category Name':<20} | {'Total Spent':<12}")
    print_divider_line()

    for category_key in category_totals_dict:
        amount_spent = category_totals_dict[category_key]
        print(f"{category_key:<20} | ${amount_spent:.2f}")


def check_budget_status():
    """
    Calculates total spending and checks against monthly_budget limit.
    Uses if/elif/else decision statements to display warning messages.
    """
    print_section_header("Member 3: Budget Status & Alerts")
    
    total_spent = 0.0
    for item in expenses_list:
        total_spent = total_spent + item["amount"]

    print(f"Monthly Budget Limit : ${monthly_budget:.2f}")
    print(f"Total Amount Spent   : ${total_spent:.2f}")

    # Decision logic for budget alerts using if / elif / else
    if total_spent > monthly_budget:
        over_budget_amount = total_spent - monthly_budget
        print("\ CRITICAL ALERT: You have EXCEEDED your budget limit!")
        print(f"   You are over budget by: ${over_budget_amount:.2f}")
    elif total_spent >= 0.8 * monthly_budget:
        remaining_budget = monthly_budget - total_spent
        print("\n WARNING: You have spent over 80% of your monthly budget!")
        print(f"   Remaining allowance: ${remaining_budget:.2f}")
    else:
        remaining_budget = monthly_budget - total_spent
        print("\n GOOD STATUS: You are well within your monthly budget.")
        print(f"   Remaining allowance: ${remaining_budget:.2f}")


def search_expenses_by_category():
    """
    Allows the user to search for expenses matching a specific category.
    """
    print_section_header("Member 3: Search Expenses by Category")
    
    if len(expenses_list) == 0:
        print("ℹ No expenses available to search.")
        return

    search_query = input("Enter category name to search for: ").strip().title()
    match_count = 0
    match_total = 0.0

    print(f"\nMatching results for '{search_query}':")
    print_divider_line()

    for item in expenses_list:
        if item["category"] == search_query:
            print(f"- Date: {item['date']} | Amount: ${item['amount']:.2f} | Note: {item['note']}")
            match_count = match_count + 1
            match_total = match_total + item["amount"]

    print_divider_line()
    if match_count == 0:
        print(f"No records found matching category '{search_query}'.")
    else:
        print(f"Found {match_count} record(s) totaling ${match_total:.2f}")

# --- END OF SECTION 3 (MEMBER 3: LINES 201 TO 300) ---
# ==============================================================================
# SECTION 4: MEMBER 4 - FILE I/O (SAVE/LOAD), BUDGET SETTINGS & MENU (LINES 301-400)
# Member 4 Responsibilities: Text file saving/loading, settings & menu loop
# ==============================================================================

def save_expenses_to_file():
    """Saves current expenses to plain text file ('expenses.txt')."""
    print_section_header("Member 4: Save Data to File")
    try:
        file_handle = open("expenses.txt", "w")
        for item in expenses_list:
            line_str = item["date"] + "," + item["category"] + "," + str(item["amount"]) + "," + item["note"] + "\n"
            file_handle.write(line_str)
        file_handle.close()
        print(" Success: Expenses saved to 'expenses.txt'!")
    except Exception as error_msg:
        print(f" Error saving file: {error_msg}")


def load_expenses_from_file():
    """Reads expenses from 'expenses.txt' into expenses_list."""
    print_section_header("Member 4: Load Data from File")
    try:
        file_handle = open("expenses.txt", "r")
        all_lines = file_handle.readlines()
        file_handle.close()
        expenses_list.clear()
        for line in all_lines:
            clean_line = line.strip()
            if clean_line != "":
                parts = clean_line.split(",")
                if len(parts) >= 4:
                    exp = {"date": parts[0], "category": parts[1], "amount": float(parts[2]), "note": parts[3]}
                    expenses_list.append(exp)
        print(f" Loaded {len(expenses_list)} record(s) from 'expenses.txt'.")
    except FileNotFoundError:
        print(" File 'expenses.txt' not found. Starting fresh.")
    except Exception as error_msg:
        print(f" Error loading file: {error_msg}")


def change_monthly_budget():
    """Allows updating the monthly budget limit."""
    global monthly_budget
    print_section_header("Member 4: Update Budget Limit")
    print(f"Current Monthly Budget Limit: ${monthly_budget:.2f}")
    try:
        new_limit = float(input("Enter new monthly budget limit ($): "))
        if new_limit > 0:
            monthly_budget = new_limit
            print(f" Budget limit set to ${monthly_budget:.2f}")
        else:
            print(" Limit must be greater than zero.")
    except ValueError:
        print(" Invalid entry! Must be a number.")


def main_menu():
    """Main menu application loop."""
    print_welcome_banner()
    load_expenses_from_file()
    while True:
        print("\n" + "=" * 50)
        print("          SMART BUDGET MAIN MENU          ")
        print("=" * 50)
        print("1. Add Single Expense        (Member 2)")
        print("2. Add Multiple Expenses     (Member 2)")
        print("3. View All Expenses         (Member 2)")
        print("4. Quick Spending Summary    (Member 2)")
        print("5. Category Breakdown        (Member 3)")
        print("6. Check Budget Status       (Member 3)")
        print("7. Search Category           (Member 3)")
        print("8. Change Budget Limit       (Member 4)")
        print("9. Save Expenses to File     (Member 4)")
        print("10. Load Expenses from File   (Member 4)")
        print("11. Exit Application")
        print("=" * 50)
        user_choice = input("Select an option (1-11): ").strip()
        if user_choice == "1": add_single_expense()
        elif user_choice == "2": add_multiple_expenses()
        elif user_choice == "3": view_all_expenses()
        elif user_choice == "4": view_quick_summary()
        elif user_choice == "5": show_category_breakdown()
        elif user_choice == "6": check_budget_status()
        elif user_choice == "7": search_expenses_by_category()
        elif user_choice == "8": change_monthly_budget()
        elif user_choice == "9": save_expenses_to_file()
        elif user_choice == "10": load_expenses_from_file()
        elif user_choice == "11":
            print("\nAuto-saving records before exit...")
            save_expenses_to_file()
            print("Thank you for using Smart Budget Tracker! Goodbye.\n")
            break
        else:
            print(" Invalid option! Enter number 1-11.")


if __name__ == "__main__":
    main_menu()
# --- END OF SECTION 4 (MEMBER 4: LINES 301 TO 400) ---
