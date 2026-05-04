import csv
from collections import defaultdict

import matplotlib.pyplot as plt


def load_grouped_csv(path, group_key):
    grouped = defaultdict(lambda: {"workers": [], "speedup": [], "efficiency": [], "communication_ratio": []})

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            group = row[group_key]
            grouped[group]["workers"].append(int(row["workers"]))
            grouped[group]["speedup"].append(float(row["speedup"]))
            grouped[group]["efficiency"].append(float(row["efficiency"]))
            grouped[group]["communication_ratio"].append(float(row["communication_ratio"]))

    return grouped


def plot_grouped_metric(grouped, metric, xlabel, ylabel, title, output_path):
    plt.figure(figsize=(7, 4))

    for group, values in grouped.items():
        plt.plot(values["workers"], values[metric], marker="o", label=group)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(title="Scenario")
    plt.grid(True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")


gradient_data = load_grouped_csv(
    "results/gradient_size_benchmark.csv",
    "gradient_size_mb",
)

plot_grouped_metric(
    gradient_data,
    metric="speedup",
    xlabel="Number of Workers",
    ylabel="Speedup",
    title="Speedup vs Workers by Gradient Size",
    output_path="results/gradient_size_speedup.png",
)

plot_grouped_metric(
    gradient_data,
    metric="communication_ratio",
    xlabel="Number of Workers",
    ylabel="Communication Ratio",
    title="Communication Ratio vs Workers by Gradient Size",
    output_path="results/gradient_size_comm_ratio.png",
)

bandwidth_data = load_grouped_csv(
    "results/bandwidth_benchmark.csv",
    "bandwidth_gbps",
)

plot_grouped_metric(
    bandwidth_data,
    metric="speedup",
    xlabel="Number of Workers",
    ylabel="Speedup",
    title="Speedup vs Workers by Bandwidth",
    output_path="results/bandwidth_speedup.png",
)

plot_grouped_metric(
    bandwidth_data,
    metric="communication_ratio",
    xlabel="Number of Workers",
    ylabel="Communication Ratio",
    title="Communication Ratio vs Workers by Bandwidth",
    output_path="results/bandwidth_comm_ratio.png",
)

print("Saved experiment plots to results/")
