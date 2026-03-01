# Endpoint Monitoring & Keystroke Exfiltration Simulation Lab

## Overview

This project demonstrates how keystroke capture and HTTP-based data exfiltration can occur in a controlled lab environment.  

The purpose of this project is educational — to understand how such behavior works and how defenders can detect and prevent it.

This project is intended strictly for authorized testing and cybersecurity learning.

---

## What This Lab Demonstrates

- Keyboard event capture using Python
- Data exfiltration over HTTP
- Server-side logging of received input
- Basic client-server architecture
- Detection and mitigation discussion

---

## Architecture

Client Machine  
→ Captures keystrokes  
→ Sends data via HTTP POST  
→ Logging server stores timestamped entries  

---

## Educational Goals

This lab helps security professionals understand:

- How input capture techniques work
- How simple data exfiltration channels are built
- Why outbound monitoring is important
- How endpoint detection tools identify suspicious behavior

---

## Defensive Considerations

A real-world security team would detect or block this behavior using:

- EDR monitoring of keyboard hooks
- Network monitoring for unusual outbound HTTP traffic
- Firewall egress filtering
- Application whitelisting
- Process behavior analytics
- TLS inspection (if encrypted exfiltration is used)

MITRE ATT&CK Reference:
T1056 – Input Capture

---

## Improvements for Production Security

This example intentionally omits:
- Authentication
- Encryption (HTTPS)
- Rate limiting
- Logging controls
- Access restrictions

These should always be implemented in real-world systems.

---

## Disclaimer

This repository is for educational and defensive security research purposes only.  
Do not deploy or execute this software on systems without explicit authorization.

Unauthorized use may violate laws and regulations.