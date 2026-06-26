class OLT:

    def __init__(self):
        self.pon_type = "GPON"                    # PON type
        self.status = "Online"                    # OLT status
        self.onu_status = "Connected"             # ONU status
        self.cpu = 45                             # CPU usage %
        self.memory = 60                          # Memory usage %
        self.software_version = "OLT_SW_2.2.0"    # Software version
        self.onu_model = "GPON_ONU"               # ONU model

        # Clock sync status
        self.ptp_status = "Enabled"               # PTP status
        self.ntp_status = "Enabled"               # NTP status
        self.ieee_1588v2 = True                   # IEEE1588v2 support
        self.time_offset_ns = 50                  # Clock offset
        self.sync_status = "Locked"               # Sync status

    def upgrade_software(self, new_version):      # Upgrade software
        self.software_version = new_version

    def reboot(self):                             # Reboot OLT
        self.status = "Rebooting"
        self.status = "Online"
        return self.status

    def is_onu_compatible(self):                  # Check ONU compatibility
        return self.pon_type == "GPON" and self.onu_model == "GPON_ONU"

    def is_clock_synchronized(self):              # Check clock sync
        return self.sync_status == "Locked" and self.time_offset_ns < 100
    