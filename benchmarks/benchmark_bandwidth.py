from distml.simulator import simulate_step_time, scaling_efficiency


def run_benchmark():
    compute_time = 0.1
    gradient_size_mb = 100

    bandwidths = [1, 10, 100]
    workers_list = [1, 2, 4, 8, 16]

    print("bandwidth_gbps,workers,step_time,speedup,efficiency,communication_ratio")

    for bandwidth in bandwidths:
        single = simulate_step_time(
            num_workers=1,
            compute_time=compute_time,
            gradient_size_mb=gradient_size_mb,
            bandwidth_gbps=bandwidth,
        )
        single_time = single["step_time"]

        for n in workers_list:
            result = simulate_step_time(
                num_workers=n,
                compute_time=compute_time,
                gradient_size_mb=gradient_size_mb,
                bandwidth_gbps=bandwidth,
            )

            speedup, efficiency = scaling_efficiency(
                single_worker_time=single_time,
                distributed_step_time=result["step_time"],
                num_workers=n,
            )

            print(
                f"{bandwidth},{n},{result['step_time']:.6f},"
                f"{speedup:.4f},{efficiency:.4f},"
                f"{result['communication_ratio']:.4f}"
            )


if __name__ == "__main__":
    run_benchmark()
