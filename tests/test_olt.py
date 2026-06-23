from devices.olt import OLT


def test_requirement_mapping():
    test_case = {
        "id": "TC001",
        "objective": "Verify OLT status",
        "priority": "High",
        "expected_result": "Online"
    }
    assert test_case["objective"] != ""
    assert test_case["priority"] == "High"
    assert test_case["expected_result"] == "Online"


def test_olt_status():
    olt = OLT()
    assert olt.status == "Online"


def test_onu_connection():
    olt = OLT()
    assert olt.onu_status == "Connected"


def test_cpu_usage():
    olt = OLT()
    assert olt.cpu < 90


def test_memory_usage():
    olt = OLT()
    assert olt.memory < 90


def test_ptp_sync():
    olt = OLT()
    assert olt.ptp_offset_ns < 100


def test_ntp_sync():
    olt = OLT()
    assert olt.ntp_status == "PASS"


def test_omci_service():
    olt = OLT()
    assert olt.omci_service == "Active"


def test_software_version():
    olt = OLT()
    assert olt.software_version == "OLT_SW_1.0.0"


def test_reboot_regression():
    olt = OLT()
    result = olt.reboot()
    assert result == "Reboot Success"
    assert olt.status == "Online"
    assert olt.onu_status == "Connected"