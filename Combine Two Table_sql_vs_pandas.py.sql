SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId)

or 

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A on P.personId=A.personId

#pandas solution
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged=pd.merge(left=person,right=address,on="personId",how="left")[['firstName', 'lastName', 'city', 'state']]
    return merged
