import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# -----------------------------------------------------------------------------
# БЛОК 1: ПОДКЛЮЧЕНИЕ И ИЗВЛЕЧЕНИЕ ДАННЫХ
# -----------------------------------------------------------------------------

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5430",
        user="postgres_user",
        password="postgres_password",
        database="postgres_db"
    )
    print("√ Подключение установлено")

    df_categories = pd.read_sql("""
        SELECT
            p.category,
            ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
            COUNT(pr.id) AS total_prices
        FROM prices pr
        JOIN products p ON pr.product_id = p.id
        GROUP BY p.category
        ORDER BY avg_price DESC
    """, connection)

    df_products_count = pd.read_sql("""
        SELECT
            category,
            COUNT(*) AS product_count
        FROM products
        GROUP BY category
        ORDER BY product_count DESC
    """, connection)

    df_all = pd.read_sql("SELECT price FROM prices", connection)

    df_single_price = pd.read_sql("""
        SELECT
            p.name AS product_name,
            p.category,
            COUNT(pr.id) AS price_count
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        GROUP BY p.id, p.name, p.category
        HAVING COUNT(pr.id) = 1
    """, connection)

    print(f"Категорий в выборке: {len(df_categories)}")
    print(f"Всего записей о ценах: {len(df_all)}")
    print(f"Товаров с одной ценой (ан.): {len(df_single_price)}")

except Exception as error:
    print(f"Ошибка подключения: {error}")
    raise SystemExit

finally:
    connection.close()
    print("√ Соединение закрыто\n")

# -----------------------------------------------------------------------------
# БЛОК 2: ПОДГОТОВКА ДАННЫХ
# -----------------------------------------------------------------------------

median_price = df_all["price"].median()
overall_avg = df_categories["avg_price"].mean()

bar_colors = [
    "#d9534f" if avg < median_price else "#4a90d9"
    for avg in df_categories["avg_price"]
]

pie_labels = [
    f"{row.category} ({row.product_count} шт.)"
    for row in df_products_count.itertuples()
]

# -----------------------------------------------------------------------------
# БЛОК 3: ПОСТРОЕНИЕ ГРАФИКОВ (простая сетка 2x2, без наслоений)
# -----------------------------------------------------------------------------

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Анализ базы данных интернет-магазина", fontsize=14, fontweight="bold")

# ----- ГРАФИК 1: Средняя цена по категориям (горизонтальный) -----
ax1 = axes[0, 0]
bars1 = ax1.barh(df_categories["category"], df_categories["avg_price"],
                 color=bar_colors, edgecolor="white", height=0.6)
for bar, val in zip(bars1, df_categories["avg_price"]):
    ax1.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2,
             f"{val:.2f}", va="center", fontsize=8)
ax1.axvline(overall_avg, color="darkorange", linestyle="--", linewidth=1.3,
            label=f"Среднее: {overall_avg:.2f}")
ax1.set_xlabel("Средняя цена (руб.)")
ax1.set_title("Средняя цена по категориям", fontweight="bold")
ax1.legend(handles=[
    Patch(facecolor="#4a90d9", label=f"Выше медианы (≥ {median_price:.0f})"),
    Patch(facecolor="#d9534f", label=f"Ниже медианы (< {median_price:.0f})")
], fontsize=8, loc="lower right")

# ----- ГРАФИК 2: Количество товаров по категориям -----
ax2 = axes[0, 1]
bars2 = ax2.bar(df_products_count["category"], df_products_count["product_count"],
                color="#5cb85c", edgecolor="white", width=0.6)
for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(int(bar.get_height())), ha="center", fontsize=9)
ax2.set_ylabel("Количество товаров")
ax2.set_title("Количество товаров по категориям", fontweight="bold")
ax2.set_xticklabels(df_products_count["category"], rotation=40, ha="right", fontsize=8)

# ----- ГРАФИК 3: Доля товаров по категориям (круговая) -----
ax3 = axes[1, 0]
pie_colors = ["#7b68ee", "#4a90d9", "#2ecc71", "#f0ad4e", "#d9534f"]
wedges, texts, autotexts = ax3.pie(
    df_products_count["product_count"],
    labels=None, autopct="%1.0f%%",
    colors=pie_colors[:len(df_products_count)],
    startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    pctdistance=0.7
)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")
ax3.set_title("Доля товаров по категориям", fontweight="bold")
ax3.legend(wedges, pie_labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)

# ----- ГРАФИК 4: Распределение цен (гистограмма) -----
ax4 = axes[1, 1]
ax4.hist(df_all["price"], bins=20, color="#f0ad4e", edgecolor="white", alpha=0.8)
ax4.axvline(df_all["price"].median(), color="crimson", linestyle="--",
            linewidth=1.5, label=f"Медиана: {df_all['price'].median():.0f}")
ax4.axvline(df_all["price"].mean(), color="darkorange", linestyle=":",
            linewidth=1.5, label=f"Среднее: {df_all['price'].mean():.0f}")
ax4.set_xlabel("Цена (руб.)")
ax4.set_ylabel("Количество записей")
ax4.set_title("Распределение цен", fontweight="bold")
ax4.legend(fontsize=8)

stats_text = (
    f"Всего цен: {len(df_all)}\n"
    f"Среднее: {df_all['price'].mean():.2f}\n"
    f"Медиана: {df_all['price'].median():.2f}\n"
    f"Мин: {df_all['price'].min():.2f}\n"
    f"Макс: {df_all['price'].max():.2f}\n"
    f"Ст. откл.: {df_all['price'].std():.2f}"
)
ax4.text(0.97, 0.95, stats_text, transform=ax4.transAxes,
         va="top", ha="right", fontsize=8,
         bbox={"boxstyle": "round,pad=0.4", "facecolor": "lightyellow", "alpha": 0.8})

# Аномалии
if len(df_single_price) > 0:
    fig.text(0.5, -0.02,
             f"▲ Аномалия: {len(df_single_price)} товаров имеют только одну цену",
             ha="center", fontsize=9, color="#8b0000",
             bbox={"boxstyle": "round,pad=0.4", "facecolor": "#fff3f3", "edgecolor": "#d9534f"})
else:
    fig.text(0.5, -0.02,
             "✓ Аномалий не обнаружено: у всех товаров минимум 2 цены",
             ha="center", fontsize=9, color="#2ecc71",
             bbox={"boxstyle": "round,pad=0.4", "facecolor": "#f0fff0", "edgecolor": "#2ecc71"})

plt.tight_layout()
plt.savefig("shop_analysis.png", dpi=150, bbox_inches="tight")
plt.show()