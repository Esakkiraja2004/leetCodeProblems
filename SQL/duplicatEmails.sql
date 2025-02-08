select count(email) as Email from emails 
group by email having count(email) >1