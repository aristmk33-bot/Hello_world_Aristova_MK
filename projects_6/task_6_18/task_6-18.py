import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    port="5430",
    user="postgres_user",
    password="postgres_password",
    database="postgres_db"
)

query = """
SELECT
    p.id AS price_id,
    p.product_id,
    pr.name AS product_name,
    pr.category,
    p.price,
    p.created_at
FROM prices p
JOIN products pr ON p.product_id = pr.id
"""

df = pd.read_sql(query, conn)
conn.close()

print("=== 1. Первые строки данных ===")
print(df.head())

print("\n=== 2. Общая статистика по ценам ===")
print(f"Среднее: {df['price'].mean():.2f} руб.")
print(f"Медиана: {df['price'].median():.2f} руб.")
print(f"Стандартное отклонение: {df['price'].std():.2f} руб.")
print(f"Минимум: {df['price'].min():.2f} руб.")
print(f"Максимум: {df['price'].max():.2f} руб.")

q1 = df['price'].quantile(0.25)
q2 = df['price'].quantile(0.50)
q3 = df['price'].quantile(0.75)
iqr = q3 - q1

print("\n=== 3. Квартили и IQR ===")
print(f"Q1: {q1:.2f} руб.")
print(f"Q2 (медиана): {q2:.2f} руб.")
print(f"Q3: {q3:.2f} руб.")
print(f"IQR: {iqr:.2f} руб.")

expensive = df[df['price'] > q3]
print(f"\nТовары дороже Q3 (цена > {q3:.2f} руб.):")
print(expensive[['product_name', 'category', 'price']].to_string(index=False))

cat_stats = df.groupby('category')['price'].agg(
    count='count',
    mean='mean',
    median='median',
    std='std'
).round(2).sort_values('mean', ascending=False)

print("\n=== 4. Статистика по категориям ===")
print(cat_stats.to_string())

price_range = df.groupby('product_id').agg(
    product_name=('product_name', 'first'),
    category=('category', 'first'),
    min_price=('price', 'min'),
    max_price=('price', 'max')
)
price_range['range'] = price_range['max_price'] - price_range['min_price']
top5_range = price_range.sort_values('range', ascending=False).head(5)

print("\n=== 5. Топ-5 товаров с наибольшим разбросом цен ===")
print(top5_range[['product_name', 'category', 'min_price', 'max_price', 'range']].to_string(index=False))