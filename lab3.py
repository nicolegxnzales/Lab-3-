# Program Name: Lab1.py (use the name the program is saved as)
 # Course: IT1114/Section XXX
 # Student Name: John Doe
 # Assignment Number: Lab#
#Due Date: xx/xx/ 20XX
# Purpose: What does the program do (in a few sentences)?
 # List specific resources used to complete the assignment

 #determine and display the total sales for the department

#function to calculate sales
def getsalesforsalesperson ():
      totalsales = 0
      #loop to gather weekly sales for a saleperson
      for week in range (1,5):
         sales = float(input(f"Salesperson week {week}: "))
         totalsales += sales
      return totalsales

 #main function
def main():
    salesgoal = float(input("Enter the sales goals: "))
    totalsales = 0
    totalemployees = 0

    #loop for each salesperson
    while True:
        print(f"\nEntering sales for salesperson {totalemployees + 1}")

        #get total sales for the current salesperson
        salesperson_sales = getsalesforsalesperson()

        #update total sales and number of employees
        totalsales += salesperson_sales
        totalemployees += 1

        #ask if there is another salesperson
        another = input("Another salesperson? (y/n): ").lower()
        if another != 'y':
            break

    #step 3: calculate the manager's bonus
    if totalsales > salesgoal:
        bonus_percentage = 5
    else:
        bonus_percentage = 2

    manager_bonus = (bonus_percentage / 100) * totalsales

    #output
    print("\nDepartment Monthly Sales and Commission")
    print(f"Number of employees: {totalemployees}")
    print(f"Department Sales Goal: {salesgoal}")
    print(f"TotalSales: {totalsales}")
    print(f"Mgr. Bonus: {manager_bonus}")

#start the program
if __name__ == "__main__":
    main()

