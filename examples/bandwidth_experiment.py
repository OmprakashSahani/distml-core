from distml.simulator import simulate_step_time, scaling_efficiency


def run_experiment():
    compute_time = 0.1
    gradient_size_mb = 100

    bandwidths = [1, 10, 100]  # GB/s
    workers_list = [1, 2, 4, 8, 16]

    for bandwidth in bandwidths:
        print(f"\nBandwidth: {bandwidth} GB/s")
        print("workers\tstep_time\tspeedup\tefficiency\tcomm_ratio")

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
                f"{n}\t{result['step_time']:.4f}\t{speedup:.2f}\t"
                f"{efficiency:.2f}\t{result['communication_ratio']:.2f}"
            )


if __name__ == "__main__":
    run_experiment()
