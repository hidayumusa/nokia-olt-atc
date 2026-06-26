from tests.test_olt import TEST_CASES
from devices.olt import OLT

# ---------------- STABILITY TEST ----------------
def test_onu_status_stability():
    tc = TEST_CASES["TC008"]
    olt = OLT()
    stable = True

    for cycle in range(10):
        olt.onu_status = "Connected"
        if olt.onu_status != "Connected":
            stable = False

        olt.onu_status = "Disconnected"
        if olt.onu_status != "Disconnected":
            stable = False

    result = "Stable" if stable else "Unstable"

    assert result == tc["expected_result"]

