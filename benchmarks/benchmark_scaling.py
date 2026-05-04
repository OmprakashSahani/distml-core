from distml.simulator import simulate_step_time, scaling_efficiency


def run_benchmark():
    compute_time = 0.1
    gradient_size_mb = 100
    bandwidth_gbps = 10

    single = simulate_step_time(
        num_workers=1,
        compute_time=compute_time,
        gradient_size_mb=gradient_size_mb,
        bandwidth_gbps=bandwidth_gbps,
    )

    single_time = single["step_time"]

    print("workers,step_time,speedup,efficiency")

    for n in [1, 2, 4, 8, 16]:
        result = simulate_step_time(
            num_workers=n,
            compute_time=compute_time,
            gradient_size_mb=gradient_size_mb,
            bandwidth_gbps=bandwidth_gbps,
        )

        step_time = result["step_time"]

        speedup, efficiency = scaling_efficiency(
            single_worker_time=single_time,
            distributed_step_time=step_time,
            num_workers=n,
        )

        print(f"{n},{step_time:.6f},{speedup:.4f},{efficiency:.4f}")


if __name__ == "__main__":
    run_benchmark()
