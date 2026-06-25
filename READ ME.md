GPON OLT Automation Testing Framework (Python + Pytest)

Project Overview

This project is a simulated GPON OLT automation testing framework developed using Python and Pytest to demonstrate the software validation workflow of a telecom Test Engineer.

The project simulates the validation of a newly released GPON OLT software version before deployment. It covers requirement analysis, test design, functional testing, performance testing, regression testing, automated execution, and HTML report generation.

Project Workflow
Requirement Analysis
        ↓
Test Design
        ↓
Test Case Development
        ↓
Functional Testing
        ↓
Performance Testing
        ↓
Regression Testing
        ↓
CI/CD Pipeline (GitHub Actions)
        ↓
HTML Report Generation

Tools Used
Python
Pytest
pytest-html
GitHub Actions
VS Code
Git

Test Coverage
Test Case ID	Category	Description
TC001	Functional	Verify GPON Type
TC002	Functional	Verify OLT Status
TC003	Functional	Verify ONU Connection
TC004	Functional	Verify Alarm Status
TC005	Performance	Verify CPU Usage
TC006	Performance	Verify Memory Usage
TC007	Regression	Verify Software Upgrade
TC008	Regression	Verify OLT Reboot

Project Structure
nokia_olt_atc/
│
├── devices/
│   └── olt.py
│
├── tests/
│   └── test_olt.py
│
├── reports/
│
├── requirements.txt
│
└── .github/
    └── workflows/
        └── python-ci.yml

How to Run

Run all automated tests:
python -m pytest -v

Generate HTML report:
python -m pytest -v --html=reports/report.html

Learning Outcome

Through this project, I gained hands-on experience in:
Requirement Analysis
Test Design
Test Case Development
Functional Testing
Performance Testing
Regression Testing
Python Automation using Pytest
HTML Report Generation
CI/CD using GitHub Actions
Note

This project is a simulation created for learning purposes to demonstrate GPON OLT automation testing concepts. It does not interact with a physical Nokia OLT device.