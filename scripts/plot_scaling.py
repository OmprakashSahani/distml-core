import csv
import matplotlib.pyplot as plt


workers = []
step_times = []
speedups = []
efficiencies = []

with open("results/scaling_benchmark.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        workers.append(int(row["workers"]))
        step_times.append(float(row["step_time"]))
        speedups.append(float(row["speedup"]))
        efficiencies.append(float(row["efficiency"]))


plt.figure(figsize=(7, 4))
plt.plot(workers, step_times, marker="o")
plt.xlabel("Number of Workers")
plt.ylabel("Step Time (seconds)")
plt.title("Step Time vs Number of Workers")
plt.grid(True)
plt.savefig("results/step_time_scaling.png", dpi=150, bbox_inches="tight")

plt.figure(figsize=(7, 4))
plt.plot(workers, speedups, marker="o")
plt.xlabel("Number of Workers")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Workers")
plt.grid(True)
plt.savefig("results/speedup_scaling.png", dpi=150, bbox_inches="tight")

plt.figure(figsize=(7, 4))
plt.plot(workers, efficiencies, marker="o")
plt.xlabel("Number of Workers")
plt.ylabel("Scaling Efficiency")
plt.title("Scaling Efficiency vs Number of Workers")
plt.grid(True)
plt.savefig("results/efficiency_scaling.png", dpi=150, bbox_inches="tight")

print("Saved scaling plots to results/")
