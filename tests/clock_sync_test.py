from tests.test_olt import TEST_CASES
from devices.olt import OLT

# ---------------- CLOCK SYNCHRONIZATION TEST ----------------
def test_ptp_status_enabled():
    tc = TEST_CASES["TC013"]
    olt = OLT()
    assert olt.ptp_status == tc["expected_result"]


def test_ntp_status_enabled():
    tc = TEST_CASES["TC014"]
    olt = OLT()
    assert olt.ntp_status == tc["expected_result"]


def test_ieee_1588v2_supported():
    tc = TEST_CASES["TC015"]
    olt = OLT()
    assert olt.ieee_1588v2 == tc["expected_result"]


def test_clock_offset_within_threshold():
    tc = TEST_CASES["TC016"]
    olt = OLT()
    assert olt.time_offset_ns < tc["expected_result"]


def test_clock_synchronization_locked():
    tc = TEST_CASES["TC017"]
    olt = OLT()
    assert olt.sync_status == tc["expected_result"]


def test_clock_synchronized_status():
    olt = OLT()
    assert olt.is_clock_synchronized() is True