/*Deleting cancelled orders from 'orders' table*/
DELETE FROM orders WHERE status='Cancelled';