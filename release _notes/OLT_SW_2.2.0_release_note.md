OLT Software Release Note
Product: Nokia GPON OLT
Software Version: OLT_SW_2.2.0
Release Type: Minor Feature Release
Release Date: 20 June 2026

Release Summary
This software release introduces improvements to OLT system stability, software maintenance, telecom clock synchronization, ONU compatibility and alarm handling. The release also includes several bug fixes identified during previous validation.

New Features
Feature 1 – OLT System Stability 
Description
Improved OLT operational stability after system startup and reboot.
Expected Behaviour
    • OLT shall reach Online state after boot. 
    • ONU connection shall remain Connected during normal operation. 
    • OLT shall maintain stable operation without unexpected status changes. 

Feature 2 – Performance Optimization
Description
Optimized CPU and memory utilization during normal system operation.
Expected Behaviour
    • CPU utilization shall remain below 90%. 
    • Memory utilization shall remain below 90%. 

Feature 3 – ONU Compatibility Enhancement
Description
Improved compatibility validation for supported GPON ONU devices.
Expected Behaviour
    • Supported GPON ONU shall register successfully. 
    • Unsupported ONU models shall be rejected. 

Feature 4 – Software Upgrade
Description
Software upgraded from OLT_SW_2.1.0 to OLT_SW_2.2.0.
Expected Behaviour
    • Software upgrade completes successfully. 
    • OLT reports software version OLT_SW_2.2.0. 
    • OLT returns to Online state after reboot. 

Feature 5 – Telecom Clock Synchronization
Description
Added support for telecom clock synchronization validation.
Expected Behaviour
    • PTP service shall remain Enabled. 
    • NTP service shall remain Enabled. 
    • IEEE 1588v2 support shall remain available. 
    • Clock synchronization status shall be Locked. 
    • Clock offset shall remain below 100 ns. 

Feature 6 – Alarm Handling
Description
Improved alarm monitoring for normal operation and Loss of Signal (LOS).
Expected Behaviour
    • Normal operation shall report No Alarm. 
    • LOS event shall trigger LOS Alarm. 

Fixed Issues
Issue ID	Description
FN-2031	Fixed intermittent ONU disconnect after reboot
FN-2045	Fixed incorrect software version display after upgrade
FN-2052	Improved clock synchronization initialization
FN-2063	Improved GPON ONU compatibility validation
FN-2068	Fixed LOS alarm reporting delay

Validation Required
Validation Item	Expected Result
OLT Status	Online
ONU Status	Connected
CPU Usage	< 90%
Memory Usage	< 90%
GPON Compatibility	Pass
Software Version	OLT_SW_2.2.0
Software Upgrade	Successful
Reboot	Online
PTP	Enabled
NTP	Enabled
IEEE 1588v2	Supported
Clock Synchronization	Locked
Clock Offset	< 100 ns
Alarm	No Alarm
LOS Alarm	Detected
