import csv
from collections import defaultdict

import matplotlib.pyplot as plt


data = defaultdict(lambda: {"workers": [], "step_time": []})

with open("results/all_reduce_strategy_benchmark.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        strategy = row["strategy"]
        data[strategy]["workers"].append(int(row["workers"]))
        data[strategy]["step_time"].append(float(row["step_time"]))


plt.figure(figsize=(7, 4))

for strategy, values in data.items():
    plt.plot(
        values["workers"],
        values["step_time"],
        marker="o",
        label=strategy,
    )

plt.xlabel("Number of Workers")
plt.ylabel("Step Time (seconds)")
plt.title("Ring vs Tree All-Reduce Performance")
plt.legend()
plt.grid(True)

plt.savefig("results/all_reduce_comparison.png", dpi=150, bbox_inches="tight")

print("Saved plot to results/all_reduce_comparison.png")
