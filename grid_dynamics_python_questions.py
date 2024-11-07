data= { 'Name': ['John', 'Jane', 'Mary', 'Peter', 'David'],
       'Age': [25, 30, 35, 40, 45], 'Salary': [50000, 60000, 70000, 80000, 90000],
 'Department': ['IT', 'HR', 'IT', 'HR', 'Finance'] }

import pandas as pd

df =pd.DataFrame(data)

# top 3 salary from IT department
filter_IT_DF= df[df["Department"]=="IT"].nlargest(1, "Salary")
#largest salary from IT department
filter_IT_DF= df[df["Department"]=="IT"].nlargest(1, "Salary")
# second largest salary from IT department
filter_IT_DF= df[df["Department"]=="IT"].nlargest(2, "Salary").iloc[-1]


top_3_it_salaries = df[df["Department"] == "IT"].nlargest(3, "Salary")
print("Top 3 IT Salaries:\n", top_3_it_salaries)

# 2. Find the largest salary from IT department
largest_it_salary = df[df["Department"] == "IT"]["Salary"].max()
print("\nLargest IT Salary:", largest_it_salary)

# 3. Find the second largest salary from IT
second_largest_it_salary = df[df["Department"] == "IT"].nlargest(2, "Salary").iloc[-1]["Salary"]
print("\nSecond Largest IT Salary:", second_largest_it_salary)

# 4. Find the average salary of people from IT department
avg_it_salary = df[df["Department"] == "IT"]["Salary"].mean()
print("\nAverage IT Salary:", avg_it_salary)

# 5. Find the average salary of people from HR department
avg_hr_salary = df[df["Department"] == "HR"]["Salary"].mean()
print("\nAverage HR Salary:", avg_hr_salary)


print(filter_IT_DF)
