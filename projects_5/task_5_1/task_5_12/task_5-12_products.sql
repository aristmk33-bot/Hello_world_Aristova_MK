SELECT category, COUNT(*) FROM products GROUP BY category;

SELECT category, COUNT(*) FROM products GROUP BY category ORDER BY COUNT(*) DESC;