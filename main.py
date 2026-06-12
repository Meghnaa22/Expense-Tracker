from database import DB
from expense_manager import ExpenseManager
from report import Report
from charts import Charts

def main():
    db = DB()
    mgr = ExpenseManager(db)
    rep = Report(db)

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Report by Category (bar chart)")
        print("4. Report by Month (pie chart)")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            desc = input("Description: ")
            mgr.add_expense(date, category, amount, desc)
            print("✅ Expense added.")
        elif choice == "2":
            df = mgr.get_all()
            print(df)
        elif choice == "3":
            df = rep.total_by_category()
            Charts.bar_by_category(df)
        elif choice == "4":
            df = rep.total_by_month()
            Charts.pie_by_month(df)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
