\# Weekly Sales Pulse



A tiny, repeatable reporting script that merges orders/products/customers, then outputs:

\- `out/<YYYY-MM-DD>/clean\_sales.csv` – tidy merged table

\- `out/<YYYY-MM-DD>/weekly\_summary.csv` – revenue by week × product (pivot\_table)

\- `out/<YYYY-MM-DD>/chart\_top\_products.png` – bar chart of top products

\- `out/<YYYY-MM-DD>/summary.md` – KPI bullets

\- `out/<YYYY-MM-DD>/widgets\_midwest\_loc.csv` – .loc filtering practice

\- `out/<YYYY-MM-DD>/sample\_iloc\_slice.csv` – .iloc selection practice



\## Setup

```bash

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt



