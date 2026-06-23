class OLT:
    def __init__(self):
        self.status = "Online"
        self.cpu = 35
        self.memory = 50
        self.ptp_offset_ns = 80
        self.ntp_status = "PASS"
        self.onu_status = "Connected"
        self.omci_service = "Active"
        self.software_version = "OLT_SW_1.0.0"
        self.alarm = "No Alarm"

    def reboot(self):
        self.status = "Online"
        self.onu_status = "Connected"
        return "Reboot Success"