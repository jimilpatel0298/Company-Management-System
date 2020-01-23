import pymongo
import datetime


def salary_management():
    def sub_menu_salary():
        print("\n############# EMPLOYEE SALARY MANAGEMENT ################")
        print("1. Add Employee Salary")
        print("2. Display Employee Salary")
        switch_example_function(int(input("Enter the function number to proceed: ")))

    def switch_example_function(argument):
        switcher = {
            1: add_salary,
            2: display_salary,
        }
        function = switcher.get(argument, lambda: "Invalid Selection")
        function()

    def add_salary():
        name = input("Enter Name of employee: ")
        mobile = input("Enter Mobile number of employee: ")
        employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
        if employee_exists is False:
            print("Please add the employee first.")
        else:
            salary = int(input(f"Enter the decided salary of employee, {name}: "))
            myEmployee.find_one_and_update({"Name": name, "Mobile": mobile}, {"$set": {"Salary": salary}}, upsert=True)
            print(f"Salary of {salary} is added to Employee {name}. ")

    def display_salary():
        name = input("Enter Name of employee: ")
        mobile = input("Enter Mobile number of employee: ")
        employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
        if employee_exists is False:
            print("Please add the employee first.")
        else:
            try:
                salary_decided = int(myEmployee.find_one({"Name": name, "Mobile": mobile},
                                                         {"_id": 0, "Salary": 1})["Salary"])
                total = myAttendance.find_one({"Name": name, "Mobile": mobile})
                list_present = total['Attendance']
                present_occur = [sub['Present'] for sub in list_present]
                total_presents = len(present_occur)
                print(f"{name} was present for a total of {total_presents} days. ")

                per_day_salary = salary_decided / 30
                sum_salary = per_day_salary * total_presents
                print(f"Total salary of {name} is : ", sum_salary)
            except KeyError:
                print("Please Enter Employer Salary First.")
    sub_menu_salary()


def attendance_management():
    def sub_menu_attendance():
        print("\n############# EMPLOYEE ATTENDANCE MANAGEMENT ################")
        print("1. Add Employee Attendance")
        print("2. Display All Employee Attendance")
        print("3. Display Particular Employee Attendance")
        switch_example_func(int(input("Enter the function number to proceed: ")))

    def switch_example_func(argument):
        switcher = {
            1: add_attendance,
            2: display_attendance,
            3: display_attendance_employee,
        }
        function = switcher.get(argument, lambda: "Invalid Selection")
        function()

    def add_attendance():

        name = input("Enter Name of employee: ")
        mobile = input("Enter Mobile number of employee: ")
        employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
        if employee_exists is False:
            print("Please add the employee first.")
        else:
            day, month, year = map(int, input(f"Enter Date for attendance in DD/MM/YY: ").split('/'))
            value = input("Enter Present/Absent: ")
            if (myAttendance.count_documents({"Name": name, "Mobile": mobile}) > 0) is False:
                myAttendance.insert_one({"Name": name, "Mobile": mobile, "Attendance": [
                    {value: datetime.datetime(year, month, day).strftime("%y/%m/%d")}]})
                print(f"Attendance of {name} for {day}/{month}/{year} as {value} is successfully added.")
            else:
                my_data = myAttendance.find_one({"Name": "Jimil", "Mobile": "7567438095"})
                list_data = my_data['Attendance']
                list_data.append({value: (datetime.datetime(year, month, day).strftime("%y/%m/%d"))})
                myAttendance.update_many({"Name": name, "Mobile": mobile}, {"$set": {"Attendance": list_data}})
                print(f"Attendance of {name} for {day}/{month}/{year} as {value} is successfully added.")

    def display_attendance():
        for x in myAttendance.find({}, {"_id": 0, "Name": 1, "Attendance": 1}):
            print(x)

    def display_attendance_employee():
        name = input("Enter Name of employee: ")
        mobile = input("Enter Mobile number of employee: ")
        employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
        if employee_exists is False:
            print("Please add the employee first.")
        else:
            for x in myAttendance.find({"Name": name, "Mobile": mobile}):
                print(x["Attendance"])

    sub_menu_attendance()


def annual_functions_management():
    def sub_menu_hol():
        print("\n############# ANNUAL FUNCTIONS MANAGEMENT ################")
        print("1. Add New Function")
        print("2. Display All Functions")
        switch_example_func(int(input("Enter the function number to proceed: ")))

    def switch_example_func(argument):
        switcher = {
            1: add_function,
            2: display_functions,
        }
        function = switcher.get(argument, lambda: "Invalid Selection")
        function()

    def add_function():
        title = input("Enter function title: ")
        new_function = {"Title": title}
        myFunctions.insert_one(new_function)
        print("Annual Function Successfully Added!")

    def display_functions():
        print("\n------ List of Annual Functions ------")
        for x in myFunctions.find():
            print(x['Title'])

    sub_menu_hol()


def holiday_management():
    def sub_menu_hol():
        print("\n############# HOLIDAY MANAGEMENT ################")
        print("1. Add New Holiday")
        print("2. Display All Holidays")
        print("3. Display Holidays of Particular Month")
        switch_example_hol(int(input("Enter the function number to proceed: ")))

    def switch_example_hol(argument):
        switcher = {
            1: add_holiday,
            2: display_holiday,
            3: display_holiday_month,
        }
        function = switcher.get(argument, lambda: "Invalid Selection")
        function()

    def add_holiday():
        title = input("Enter holiday title: ")
        day, month, year = map(int, input(f"Enter Date for {title} in DD/MM/YY: ").split('/'))
        new_holiday = {"Title": title, "Date": datetime.datetime(year, month, day)}
        myHoliday.insert_one(new_holiday)
        print("Holiday Successfully Added!")

    def display_holiday():
        print("\n------ List of Holidays ------")
        for x in myHoliday.find():
            print(x['Date'].date(), " : ", x['Title'], sep="")

    def display_holiday_month():
        month = input("Enter month (MM) to display holidays: ")
        print("\n------ List of Holidays ------")
        for x in myHoliday.find({"Month": month}):
            print(x['Date'].date(), " : ", x['Title'], sep="")

    sub_menu_hol()


def add_employee():
    name = input("Enter name: ")
    address = input("Enter address: ")
    status = input("Fresher / Experience ?")
    dob = input("Enter Date of Birth: ")
    email = input("Enter email address: ")
    mobile = input("Enter mobile number: ")

    new_employee = {"Name": name, "Address": address, "DOB": dob, "Email": email, "Mobile": mobile, "Status": status}
    myEmployee.insert_one(new_employee)
    print("Employee Data Successfully added!")


def delete_employee():
    name = input("Enter the name of the employee to delete: ")
    mobile = input("Enter Mobile number of employee: ")
    employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
    if employee_exists is False:
        print("Please add the employee first.")
    else:
        myEmployee.delete_one({"Name": name, "Mobile": mobile})
        print("Employee Data Successfully Deleted")


def update_employee():
    name = input("Enter the name of Employee to edit data: ")
    mobile = input("Enter Mobile number of employee: ")
    employee_exists = myEmployee.count_documents({"Name": name, "Mobile": mobile}) > 0
    if employee_exists is False:
        print("Please add the employee first.")
    else:
        parameter = input("Update Name/Address/DOB/Email/Mobile/Status ?")
        new = input(f"Enter new {parameter}: ")
        myEmployee.update_one(
            {"Name": name, "Mobile": mobile}, {"$set": {parameter: new}}
        )


def displaye_employee():
    for x in myEmployee.find():
        print(x)


def menu():
    print("\n############# COMPANY MANAGEMENT SYSTEM ################")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Edit Employee Details")
    print("4. Display all Employee Details")
    print("5. Salary Management")
    print("6. Attendance Management")
    print("7. Annual Functions Management")
    print("8. Holiday Management")
    print("9. Exit")
    switch_example(int(input("Enter the function number to proceed: ")))


def switch_example(argument):
    switcher = {
        1: add_employee,
        2: delete_employee,
        3: update_employee,
        4: displaye_employee,
        5: salary_management,
        6: attendance_management,
        7: annual_functions_management,
        8: holiday_management,
        9: exit

    }
    function = switcher.get(argument, lambda: "Invalid Selection")
    function()


if __name__ == "__main__":
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = myClient['Company_Data']
    myEmployee = myDB['Employee_Data']
    myFunctions = myDB['Annual_Functions']
    myHoliday = myDB['Holiday_List']
    myAttendance = myDB['Employee_Attendance']
    while True:
        menu()
