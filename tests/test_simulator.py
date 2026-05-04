from distml.all_reduce import ring_all_reduce_time
from distml.simulator import simulate_step_time, scaling_efficiency


def test_ring_all_reduce_single_worker():
    time = ring_all_reduce_time(
        num_workers=1,
        gradient_size_mb=100,
        bandwidth_gbps=10,
    )

    assert time == 0.0


def test_ring_all_reduce_multi_worker():
    time = ring_all_reduce_time(
        num_workers=4,
        gradient_size_mb=100,
        bandwidth_gbps=10,
    )

    assert time > 0.0


def test_simulate_step_time():
    result = simulate_step_time(
        num_workers=4,
        compute_time=0.1,
        gradient_size_mb=100,
        bandwidth_gbps=10,
    )

    assert result["num_workers"] == 4
    assert result["compute_time"] == 0.025
    assert result["communication_time"] > 0.0
    assert result["step_time"] > result["compute_time"]


def test_scaling_efficiency():
    speedup, efficiency = scaling_efficiency(
        single_worker_time=1.0,
        distributed_step_time=0.4,
        num_workers=4,
    )

    assert speedup == 2.5
    assert efficiency == 0.625
