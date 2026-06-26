from tests.test_olt import TEST_CASES
from devices.olt import OLT

# ---------------- PERFORMANCE TEST ----------------
def test_cpu_usage():
    tc = TEST_CASES["TC004"]
    olt = OLT()
    assert olt.cpu < tc["expected_result"]


def test_memory_usage():
    tc = TEST_CASES["TC005"]
    olt = OLT()
    assert olt.memory < tc["expected_result"]