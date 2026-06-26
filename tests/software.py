from tests.test_olt import TEST_CASES
from devices.olt import OLT



# ---------------- SOFTWARE UPDATE TEST ----------------
def test_software_update():
    tc = TEST_CASES["TC011"]
    olt = OLT()
    olt.upgrade_software("OLT_SW_2.2.0")
    assert olt.software_version == tc["expected_result"]


# ---------------- REBOOT TEST ----------------
def test_reboot_olt():
    tc = TEST_CASES["TC012"]
    olt = OLT()
    assert olt.reboot() == tc["expected_result"]
