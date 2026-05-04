def ring_all_reduce_time(num_workers, gradient_size_mb, bandwidth_gbps):
    """
    Estimate ring all-reduce communication time.

    Formula:
    time ≈ 2 * (N - 1) / N * (gradient_size / bandwidth)

    Args:
        num_workers: number of workers
        gradient_size_mb: gradient size in MB
        bandwidth_gbps: network bandwidth in GB/s

    Returns:
        Communication time in seconds
    """
    if num_workers <= 1:
        return 0.0

    gradient_size_gb = gradient_size_mb / 1024
    return 2 * (num_workers - 1) / num_workers * (gradient_size_gb / bandwidth_gbps)
