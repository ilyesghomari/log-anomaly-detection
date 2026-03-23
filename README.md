# Log Anomaly Detection (ML)

## Overview
This project implements an anomaly detection pipeline for system logs using machine learning (Isolation Forest). It is inspired by SOC (Security Operations Center) workflows for identifying suspicious activities in log data.

## Method
- Data preprocessing using StandardScaler
- Unsupervised anomaly detection using Isolation Forest
- Detection based on statistical deviation in log patterns

## Features
- Handles structured log-like data
- Identifies anomalies without labeled data
- Lightweight and fast training

## Usage
Run the script:
```bash
python anomaly_detection.py
