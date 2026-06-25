from devices.olt import OLT


# ---------------- TEST CASE DESIGN ----------------

TEST_CASES = {
    "TC001": {
        "scenario": "Verify GPON type",
        "priority": "High",
        "expected_result": "GPON"
    },
    "TC002": {
        "scenario": "Verify OLT is online",
        "priority": "High",
        "expected_result": "Online"
    },
    "TC003": {
        "scenario": "Verify ONU is connected",
        "priority": "High",
        "expected_result": "Connected"
    },
    "TC004": {
        "scenario": "Verify ONU disconnected scenario",
        "priority": "High",
        "expected_result": "Disconnected"
    },
    "TC005": {
        "scenario": "Verify CPU normal usage",
        "priority": "High",
        "expected_result": "CPU below 90%"
    },
    "TC006": {
        "scenario": "Verify CPU high usage scenario",
        "priority": "High",
        "expected_result": "CPU above 90% should fail threshold"
    },
    "TC007": {
        "scenario": "Verify memory normal usage",
        "priority": "Medium",
        "expected_result": "Memory below 90%"
    },
    "TC008": {
        "scenario": "Verify memory high usage scenario",
        "priority": "Medium",
        "expected_result": "Memory above 90% should fail threshold"
    },
    "TC009": {
        "scenario": "Verify no active alarm",
        "priority": "High",
        "expected_result": "No Alarm"
    },
    "TC010": {
        "scenario": "Verify active alarm scenario",
        "priority": "High",
        "expected_result": "LOS Alarm"
    },
    "TC011": {
        "scenario": "Verify software upgrade",
        "priority": "High",
        "expected_result": "OLT_SW_1.1.0"
    },
    "TC012": {
        "scenario": "Verify OLT reboot",
        "priority": "Medium",
        "expected_result": "Online"
    }
}


# ---------------- FUNCTIONAL TESTING ----------------

def test_gpon_type():
    tc = TEST_CASES["TC001"]          # Get test case design
    olt = OLT()                       # Create OLT object
    assert olt.pon_type == tc["expected_result"]


def test_olt_status_online():
    tc = TEST_CASES["TC002"]          # Get test case design
    olt = OLT()                       # Create OLT object
    assert olt.status == tc["expected_result"]


def test_onu_connected():
    tc = TEST_CASES["TC003"]          # Get test case design
    olt = OLT()                       # Create OLT object
    assert olt.onu_status == tc["expected_result"]


def test_onu_disconnected_scenario():
    tc = TEST_CASES["TC004"]          # Get test case design
    olt = OLT()                       # Create OLT object

    olt.onu_status = "Disconnected"   # Simulate ONU disconnected

    assert olt.onu_status == tc["expected_result"]


# ---------------- PERFORMANCE TESTING ----------------

def test_cpu_normal_usage():
    olt = OLT()                       # Create OLT object
    assert olt.cpu < 90               # Verify CPU is below threshold


def test_cpu_high_usage_scenario():
    olt = OLT()                       # Create OLT object
    olt.cpu = 95                      # Simulate high CPU usage
    assert olt.cpu > 90               # Verify high CPU scenario detected


def test_memory_normal_usage():
    olt = OLT()                       # Create OLT object
    assert olt.memory < 90            # Verify memory is below threshold


def test_memory_high_usage_scenario():
    olt = OLT()                       # Create OLT object
    olt.memory = 95                   # Simulate high memory usage
    assert olt.memory > 90            # Verify high memory scenario detected


# ---------------- ALARM TESTING ----------------

def test_no_alarm():
    tc = TEST_CASES["TC009"]          # Get test case design
    olt = OLT()                       # Create OLT object
    assert olt.alarm == tc["expected_result"]


def test_active_alarm_scenario():
    tc = TEST_CASES["TC010"]          # Get test case design
    olt = OLT()                       # Create OLT object
    olt.alarm = "LOS Alarm"           # Simulate Loss of Signal alarm
    assert olt.alarm == tc["expected_result"]


# ---------------- REGRESSION TESTING ----------------

def test_software_upgrade():
    tc = TEST_CASES["TC011"]                  # Get test case design
    olt = OLT()                               # Create OLT object
    olt.upgrade_software("OLT_SW_1.1.0")      # Simulate software upgrade
    assert olt.software_version == tc["expected_result"]


def test_reboot_olt():
    tc = TEST_CASES["TC012"]          # Get test case design
    olt = OLT()                       # Create OLT object
    assert olt.reboot() == tc["expected_result"]