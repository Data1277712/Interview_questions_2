import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    newsalary = employee["salary"].drop_duplicates().nlargest(2)
    if len(newsalary)<2:
        salary=pd.DataFrame({"SecondHighestSalary":[pd.NA]})
    else : 
        salary= pd.DataFrame({"SecondHighestSalary":[newsalary.iloc[1]]})
    return salary    
    
