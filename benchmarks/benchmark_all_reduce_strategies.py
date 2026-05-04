from distml.simulator import simulate_step_time


def run_benchmark():
    compute_time = 0.1
    gradient_size_mb = 100
    bandwidth_gbps = 10
    workers_list = [1, 2, 4, 8, 16]

    print("strategy,workers,step_time,communication_time,communication_ratio,bottleneck")

    for strategy in ["ring", "tree"]:
        for n in workers_list:
            result = simulate_step_time(
                num_workers=n,
                compute_time=compute_time,
                gradient_size_mb=gradient_size_mb,
                bandwidth_gbps=bandwidth_gbps,
                strategy=strategy,
            )

            print(
                f"{strategy},{n},{result['step_time']:.6f},"
                f"{result['communication_time']:.6f},"
                f"{result['communication_ratio']:.4f},"
                f"{result['bottleneck']}"
            )


if __name__ == "__main__":
    run_benchmark()
