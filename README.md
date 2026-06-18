# Smart System Monitor

## Overview

Smart System Monitor is a Python learning project focused on understanding system behavior, monitoring computer resources, and analyzing log files.

The project combines two areas:

* System Monitoring
* Log Analysis

The goal is to build a practical understanding of how operating systems expose performance metrics and how logs can be used to understand system activity.

---

## Current Features

### System Monitoring

The monitor currently tracks:

* CPU Usage

using the `psutil` library.

### Log Analysis

The analyzer can currently:

* Read log files
* Count log levels
* Generate basic statistics for:

  * INFO logs
  * WARNING logs
  * ERROR logs

---

## Project Purpose

This project is being built to learn:

* Python programming
* File handling
* Data structures
* Operating system metrics
* Logging concepts
* Cybersecurity fundamentals
* Git and GitHub workflows
=======
Smart System Monitor is a Python-based project designed to help me understand how computer systems behave under different workloads while building practical skills in Python, operating systems, cybersecurity, logging, and system monitoring.

The project begins with basic resource monitoring and gradually evolves into a system capable of generating logs, analyzing events, detecting suspicious activity, and visualizing system behavior.

---

## Purpose

The primary purpose of this project is to learn:

* How operating systems expose system metrics
* How monitoring tools collect performance data
* How logs are generated and analyzed
* How abnormal system behavior can be detected
* How cybersecurity monitoring systems work

This project serves as a bridge between programming, operating systems, and cybersecurity.

---

## What This Project Tracks

### Current Metrics

* CPU Usage
* Memory Usage
* Disk Usage
* Network Activity

### Future Metrics

* Process Activity
* Failed Login Attempts
* Error Events
* Suspicious IP Addresses
* Resource Usage Trends
---

## System Baseline (Phase 1)

The first phase focuses on understanding what normal system behavior looks like on my machine.

### Typical Observations

| Metric                      | Observation    |
| --------------------------- | -------------- |
| CPU Usage (Idle)            | ~30%           |
| CPU Usage (Coding/Browsing) | ~50–60%        |
| Memory Usage                | ~40–50%        |
| Disk Activity               | Changes slowly |
| Network Connections         | Moderate       |

These values will be used later when implementing anomaly detection and alerting features.

---

## Project Structure

```text
smart_system_monitor/
│
├── logs/
│   ├── sample.log
│   └── monitor.log
│
├── log_analyzer.py
├── system_monitor.py
└── README.md
```

---

## Current Learning Goals

* Parse log entries
* Extract timestamps
* Generate detailed reports
* Monitor additional system metrics
* Save monitoring data to log files

---

## Status

🚧 Work in Progress

Current milestone: Building the log parsing module.
=======
The purpose of establishing a baseline is to understand what "normal" looks like on my machine before attempting anomaly detection.

| Metric                      | Typical Observation |
| --------------------------- | ------------------- |
| CPU Usage (Idle)            | ~30%                |
| CPU Usage (Coding/Browsing) | ~50-60%             |
| Memory Usage                | ~40-50%             |
| Disk Usage Changes          | Slow and gradual    |
| Network Activity            | Moderate            |

Future versions of the project will compare live metrics against these baseline values to identify unusual behavior.

---

## Project Timeline

### Phase 1: Foundations

* Read and analyze log files
* Count log levels (INFO, WARNING, ERROR)
* Monitor CPU usage
* Establish system baseline

### Phase 2: Log Parsing

* Extract timestamps
* Extract log levels
* Parse messages
* Generate structured log reports

### Phase 3: Pattern Detection

* Extract IP addresses
* Use regular expressions
* Identify recurring errors
* Generate statistics

### Phase 4: Security Monitoring

* Detect repeated failed logins
* Flag suspicious IP activity
* Generate alerts

### Phase 5: Advanced Features

* Command Line Interface (CLI)
* Real-time monitoring
* Dashboards and visualizations
* Historical analysis

---

## Current Status

🚧 In Development

Completed:

* Project setup
* Git initialization
* Basic log level analysis

Currently Working On:

* Log parsing and structured log analysis
