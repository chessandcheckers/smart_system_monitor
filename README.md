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
