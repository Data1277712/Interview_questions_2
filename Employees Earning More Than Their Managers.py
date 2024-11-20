import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge_ids=employee.merge(employee,how='inner',left_on="managerId",right_on="id")
    filter_ids=merge_ids[merge_ids["salary_x"]>merge_ids["salary_y"]][["name_x"]]
    new_df=filter_ids.rename(columns={"name_x" : "Employee"})
    return new_df

#sql version

select name as Employee from Employee e
where salary >(select m.salary from Employee m where m.id=e.manager)
