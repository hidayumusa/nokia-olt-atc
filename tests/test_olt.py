from devices.olt import OLT


# ---------------- TEST CASE DESIGN ----------------
TEST_CASES = {
    # ---------------- FUNCTIONAL TEST ----------------
    "TC001": {"scenario": "Verify GPON type", "expected_result": "GPON"},
    "TC002": {"scenario": "Verify OLT status online", "expected_result": "Online"},
    "TC003": {"scenario": "Verify ONU connected", "expected_result": "Connected"},

    # ---------------- PERFORMANCE TEST ----------------
    "TC004": {"scenario": "Verify CPU normal usage", "expected_result": 90},
    "TC005": {"scenario": "Verify memory normal usage", "expected_result": 90},

    # ---------------- STABILITY TEST ----------------
    "TC008": {"scenario": "Verify ONU stability", "expected_result": "Stable"}, 

    # ---------------- COMPATIBILITY TEST ----------------
    "TC009": {"scenario": "Verify GPON ONU compatibility", "expected_result": True},
    "TC010": {"scenario": "Verify unsupported ONU compatibility", "expected_result": False},

    # ---------------- SOFTWARE/REBOOT TEST ----------------
    "TC011": {"scenario": "Verify software update", "expected_result": "OLT_SW_2.2.0"},
    "TC012": {"scenario": "Verify OLT reboot", "expected_result": "Online"},

    # ---------------- CLOCK SYNCHRONIZATION TEST ----------------
    "TC013": {"scenario": "Verify PTP status enabled", "expected_result": "Enabled"},
    "TC014": {"scenario": "Verify NTP status enabled", "expected_result": "Enabled"},
    "TC015": {"scenario": "Verify IEEE 1588v2 supported", "expected_result": True},
    "TC016": {"scenario": "Verify clock offset within threshold", "expected_result": 100},
    "TC017": {"scenario": "Verify clock synchronization locked", "expected_result": "Locked"},
}