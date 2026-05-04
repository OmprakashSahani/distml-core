from distml.all_reduce import ring_all_reduce_time


def simulate_step_time(
    num_workers,
    compute_time,
    gradient_size_mb,
    bandwidth_gbps,
):
    effective_compute_time = compute_time / num_workers

    communication_time = ring_all_reduce_time(
        num_workers=num_workers,
        gradient_size_mb=gradient_size_mb,
        bandwidth_gbps=bandwidth_gbps,
    )

    step_time = effective_compute_time + communication_time

    communication_ratio = communication_time / step_time if step_time > 0 else 0.0

    bottleneck = (
        "communication-bound"
        if communication_time > effective_compute_time
        else "compute-bound"
    )

    return {
        "num_workers": num_workers,
        "compute_time": effective_compute_time,
        "communication_time": communication_time,
        "step_time": step_time,
        "communication_ratio": communication_ratio,
        "bottleneck": bottleneck,
    }


def scaling_efficiency(single_worker_time, distributed_step_time, num_workers):
    speedup = single_worker_time / distributed_step_time
    efficiency = speedup / num_workers

    return speedup, efficiency
