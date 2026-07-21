# Write your MySQL query statement below
update salary
SET sex=CASE
    when sex='m' then 'f'
    else 'm'
    END;