import pandas as pd

def prepare_fact_sales(orders: pd.DataFrame, products: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    # Ensure types
    for col in ["qty", "price"]:
        if col in orders.columns:
            orders[col] = pd.to_numeric(orders[col], errors="coerce")

    fact = (
        orders
        .merge(products, on="product_id", how="left")
        .merge(customers, on="customer_id", how="left")
        .copy()
    )

    # New columns
    fact["revenue"] = fact["qty"] * fact["price"]
    fact["order_week"] = fact["order_date"].dt.to_period("W").dt.start_time

    # new vs repeat: signup within 30 days of order
    fact["is_new_customer"] = (fact["order_date"] - pd.to_datetime(fact["signup_date"]))\
        .dt.days.between(0, 30, inclusive="both")

    # Practice .loc selection: keep tidy set of columns in a defined order
    keep = ["order_date","order_week","order_id","product_id","product_name","category",
            "customer_id","region","qty","price","revenue","is_new_customer"]
    fact = fact.loc[:, keep]  # label-based selection with .loc
    return fact

def weekly_top_products(fact: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    # Aggregate by week × product
    agg = (
        fact.groupby(["order_week","product_name"], as_index=False)["revenue"]
            .sum()
            .sort_values(["order_week","revenue"], ascending=[True, False])
    )
    # Get top N per week
    agg["rank"] = agg.groupby("order_week")["revenue"].rank(method="first", ascending=False)
    return agg.loc[agg["rank"] <= top_n, ["order_week","product_name","revenue","rank"]]

# Additional function
import pandas as pd

def weekly_summary_pivot(fact: pd.DataFrame) -> pd.DataFrame:
    # revenue by week × product (columns = product names)
    tbl = pd.pivot_table(
        fact,
        index="order_week",
        columns="product_name",
        values="revenue",
        aggfunc="sum",
        fill_value=0,
    )
    # total column
    tbl["Total"] = tbl.sum(axis=1)
    # tidy index for CSV
    tbl = tbl.sort_index()
    tbl.index = tbl.index.date
    tbl.reset_index(names="order_week", inplace=True)
    return tbl
