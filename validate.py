import csv
from pathlib import Path
root=Path(__file__).parent/"data"
def rows(name):
    with (root/f"{name}.csv").open() as f:return list(csv.DictReader(f))
c,p,d=map(rows,["claims","payments","denials"])
ids={x["ClaimID"] for x in c}
assert len(ids)==len(c) and all(x["ClaimID"] in ids for x in p+d)
allowed=sum(int(x["AllowedCents"]) for x in c)
paid=sum(int(x["PaidCents"]) for x in p)
ar=sum(int(x["OpenARCents"]) for x in c)
assert allowed==paid+ar
assert sum(int(x["DeniedFlag"]) for x in c)==len(d)
print(f"Claims: {len(c)} | Denial rate: {len(d)/len(c):.1%} | Collection rate: {paid/allowed:.1%}")
print(f"Allowed: ${allowed/100:,.2f} | Paid: ${paid/100:,.2f} | Open AR: ${ar/100:,.2f}")
print("Checks passed.")
