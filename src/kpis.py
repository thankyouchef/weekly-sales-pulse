import pandas as pd

def kpi_summary(fact: pd.DataFrame) -> str:
    total_rev = fact["revenue"].sum()
    # Practice boolean Series + .loc
    new_rev = fact.loc[fact["is_new_customer"] == True, "revenue"].sum()
    repeat_rev = total_rev - new_rev

    by_week = fact.groupby("order_week", as_index=False)["revenue"].sum()
    latest_week = by_week.sort_values("order_week").iloc[-1]  # positional with .iloc

    lines = [
        "# Weekly Sales Pulse",
        f"- Total revenue (all data loaded): ${total_rev:,.2f}",
        f"- Latest week ({latest_week['order_week'].date()}): ${latest_week['revenue']:,.2f}",
        f"- New vs. repeat revenue split: ${new_rev:,.2f} new / ${repeat_rev:,.2f} repeat",
        "",
        "## Notes",
        "- Data comes from merged orders/products/customers.",
        "- New customer = signup within 30 days of order date.",
    ]
    return "\n".join(lines)
