from tests.test_olt import TEST_CASES
from devices.olt import OLT


# ---------------- COMPATIBILITY TEST ----------------
def test_gpon_onu_compatibility():
    tc = TEST_CASES["TC009"]
    olt = OLT()
    olt.pon_type = "GPON"
    olt.onu_model = "GPON_ONU"
    assert olt.is_onu_compatible() == tc["expected_result"]


def test_unsupported_onu_compatibility():
    tc = TEST_CASES["TC010"]
    olt = OLT()
    olt.pon_type = "GPON"
    olt.onu_model = "UNKNOWN_ONU"
    assert olt.is_onu_compatible() == tc["expected_result"]