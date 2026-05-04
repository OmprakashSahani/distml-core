from distml.simulator import simulate_step_time, scaling_efficiency


def run_benchmark():
    compute_time = 0.1
    bandwidth_gbps = 10

    gradient_sizes = [10, 100, 1000]
    workers_list = [1, 2, 4, 8, 16]

    print("gradient_size_mb,workers,step_time,speedup,efficiency,communication_ratio")

    for grad_size in gradient_sizes:
        single = simulate_step_time(
            num_workers=1,
            compute_time=compute_time,
            gradient_size_mb=grad_size,
            bandwidth_gbps=bandwidth_gbps,
        )
        single_time = single["step_time"]

        for n in workers_list:
            result = simulate_step_time(
                num_workers=n,
                compute_time=compute_time,
                gradient_size_mb=grad_size,
                bandwidth_gbps=bandwidth_gbps,
            )

            speedup, efficiency = scaling_efficiency(
                single_worker_time=single_time,
                distributed_step_time=result["step_time"],
                num_workers=n,
            )

            print(
                f"{grad_size},{n},{result['step_time']:.6f},"
                f"{speedup:.4f},{efficiency:.4f},"
                f"{result['communication_ratio']:.4f}"
            )


if __name__ == "__main__":
    run_benchmark()
