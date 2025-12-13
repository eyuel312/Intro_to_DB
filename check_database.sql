SELECT CASE
    WHEN DATABASE() = 'alx_book_store' THEN 'Correct Database'
    ELSE 'Wrong Database'
END AS db_check;
