import math


def ring_all_reduce_time(num_workers, gradient_size_mb, bandwidth_gbps):
    """
    Estimate ring all-reduce communication time.

    Formula:
    time ≈ 2 * (N - 1) / N * (gradient_size / bandwidth)
    """
    if num_workers <= 1:
        return 0.0

    gradient_size_gb = gradient_size_mb / 1024
    return 2 * (num_workers - 1) / num_workers * (
        gradient_size_gb / bandwidth_gbps
    )


def tree_all_reduce_time(num_workers, gradient_size_mb, bandwidth_gbps):
    """
    Estimate tree-based all-reduce communication time.

    Formula:
    time ≈ log2(N) * (gradient_size / bandwidth)
    """
    if num_workers <= 1:
        return 0.0

    gradient_size_gb = gradient_size_mb / 1024
    return math.log2(num_workers) * (gradient_size_gb / bandwidth_gbps)
