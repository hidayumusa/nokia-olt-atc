from tests.test_olt import TEST_CASES
from devices.olt import OLT

# ---------------- FUNCTIONAL TEST ----------------
def test_gpon_type():
    tc = TEST_CASES["TC001"]
    olt = OLT()
    assert olt.pon_type == tc["expected_result"]


def test_olt_status_online():
    tc = TEST_CASES["TC002"]
    olt = OLT()
    assert olt.status == tc["expected_result"]


def test_onu_connection():
    tc = TEST_CASES["TC003"]
    olt = OLT()
    assert olt.onu_status == tc["expected_result"]
