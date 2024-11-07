#Given two tables, Sales and Products, write a query to find the top 3 best-selling products in each category.
 #Assume Sales has columns product_id, quantity, and date, and Products has product_id, product_name, and category.
 # Include the total sales quantity in the result.

SELECT 
    p.category,
    p.product_id,
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold
FROM 
    Sales s
JOIN 
    Products p ON s.product_id = p.product_id
GROUP BY 
    p.category, p.product_id, p.product_name
ORDER BY 
    p.category, total_quantity_sold DESC
LIMIT 3;


--------------

Question: Suppose you have a Users table where each row contains a purchases column, which is an ARRAY of STRUCTs with fields item_id and amount.
Write a query to find the total amount spent on each item_id across all users.

SELECT 
    purchase.item_id,
    SUM(purchase.amount) AS total_amount_spent
FROM 
    Users,
    UNNEST(purchases) AS purchase
GROUP BY 
    purchase.item_id
ORDER BY 
    total_amount_spent DESC;


Using an Employees table with columns employee_id, name, salary, and department, 
write a query to categorize each employee’s salary into "High", "Medium", or "Low" based on thresholds: above 100,000 as "High," 50,000–100,000 as "Medium," and below 50,000 as "Low." 
Include employee name, department, and salary category in the output.

select name,department, case when salary>=100,000 then "high" else when salary between 50,000 and 100,000 then "Medium" else when salery <50,000 then "Low" as salary_category from Employees




