#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        csvContent = csv.DictReader(file, dialect = "empDialect")
        employeeList = []
        for row in csvContent:
            employeeList.append(row)
    return employeeList

employeeList = read_employees("/home/student-01-c7d9301f3607/data/employees.csv")
print(employeeList)
def process_data(employeeList):
    departmentList = []
    for department in employeeList:
        departmentList.append(department["Department"])

    departmentData = {}
    for departmentCount in departmentList:
        if departmentCount in departmentData:
            departmentData[departmentCount] += 1
        else:
            departmentData[departmentCount] = 1
    
    return departmentData

dictionary = process_data(employeeList)
print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as writeFile:
        for dept in sorted(dictionary):
            writeFile.write("{}:{}\n".format(dept, dictionary[dept]))
    return