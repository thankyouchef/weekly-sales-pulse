from datetime import date
from pathlib import Path

from src.io_utils import load_orders, load_dim
from src.transform import (
    prepare_fact_sales,
    weekly_summary_pivot,
    filter_widgets_midwest,
    sample_iloc_slice,
)
from src.kpis import kpi_summary
from src.viz import plot_top_products


def main():
    AS_OF = date.today().isoformat()
    OUT = Path(f"out/{AS_OF}")
    OUT.mkdir(parents=True, exist_ok=True)

    orders = load_orders("data")
    products = load_dim("data/products.csv", key="product_id")
    customers = load_dim("data/customers.csv", key="customer_id")

    fact = prepare_fact_sales(orders, products, customers)

    # Weekly pivot table
    weekly_tbl = weekly_summary_pivot(fact)
    weekly_tbl.to_csv(OUT / "weekly_summary.csv", index=False)

    # Main outputs
    fact.to_csv(OUT / "clean_sales.csv", index=False)
    plot_top_products(fact, OUT / "chart_top_products.png")
    (OUT / "summary.md").write_text(kpi_summary(fact), encoding="utf-8")

    # Practice outputs (.loc / .iloc)
    widgets_midwest = filter_widgets_midwest(fact)
    widgets_midwest.to_csv(OUT / "widgets_midwest_loc.csv", index=False)

    iloc_sample = sample_iloc_slice(fact)
    iloc_sample.to_csv(OUT / "sample_iloc_slice.csv", index=False)

    # Confirmations
    print(f"Wrote: {OUT/'weekly_summary.csv'}")
    print(f"Wrote: {OUT/'clean_sales.csv'}")
    print(f"Wrote: {OUT/'chart_top_products.png'}")
    print(f"Wrote: {OUT/'summary.md'}")
    print(f"Wrote: {OUT/'widgets_midwest_loc.csv'}")
    print(f"Wrote: {OUT/'sample_iloc_slice.csv'}")


if __name__ == "__main__":
    main()
