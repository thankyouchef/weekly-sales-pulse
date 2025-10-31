from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def plot_top_products(fact: pd.DataFrame, chart_path: Path, top_n: int = 5) -> None:
    # sum revenue per product (all weeks combined) for a simple first chart
    prods = fact.groupby("product_name", as_index=False)["revenue"].sum()
    prods = prods.sort_values("revenue", ascending=False).head(top_n)

    plt.figure()
    plt.bar(prods["product_name"], prods["revenue"])
    plt.title(f"Top {top_n} Products by Revenue")
    plt.ylabel("Revenue")
    plt.xticks(rotation=0)
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
