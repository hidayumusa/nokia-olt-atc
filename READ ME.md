# Nokia OLT ATC Simulator (Python + Pytest)

## Project Overview

This project is a Python and Pytest-based OLT ATC (Automated Test Case) simulator developed to understand Nokia's telecom testing workflow for OLT products.

The project simulates several testing activities commonly performed by a Nokia Test Engineer, including functional testing, OLT/ONU end-to-end validation, performance testing, clock synchronization testing, version verification and regression testing.

## Tools Used

* Python
* Pytest
* VS Code
* HTML Report
* GitHub Copilot

## Test Coverage

| Test Case                | Description                          |
| ------------------------ | ------------------------------------ |
| test_requirement_mapping | Simulate requirement analysis        |
| test_olt_status          | Verify OLT status                    |
| test_onu_connection      | Verify ONU connectivity              |
| test_cpu_usage           | Verify CPU performance               |
| test_memory_usage        | Verify memory performance            |
| test_ptp_sync            | Verify PTP synchronization           |
| test_ntp_sync            | Verify NTP synchronization           |
| test_omci_service        | Verify OMCI service                  |
| test_software_version    | Verify software version              |
| test_reboot_regression   | Verify system stability after reboot |

## How to Run

Execute the following command:

python -m pytest -v

To generate HTML report:

python -m pytest -v --html=reports/report.html

## Learning Outcome

This project was developed to strengthen my understanding of Nokia's OLT testing workflow, automation testing concepts, regression testing and telecom network validation.
