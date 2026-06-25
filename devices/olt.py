class OLT:
    def __init__(self):
        self.pon_type = "GPON"
        self.status = "Online"
        self.cpu = 35
        self.memory = 50
        self.onu_status = "Connected"
        self.alarm = "No Alarm"
        self.software_version = "OLT_SW_1.0.0"

    def upgrade_software(self, new_version):
        self.software_version = new_version
        return self.software_version

    def reboot(self):
        self.status = "Online"
        return self.status