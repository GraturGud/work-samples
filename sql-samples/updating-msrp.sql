/*Updating MSRP by 10$ for Classic Cars product line*/
UPDATE products 
SET 
    MSRP = MSRP + 10
WHERE
    productLine = 'Classic Cars';