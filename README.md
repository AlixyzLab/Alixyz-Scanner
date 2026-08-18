# 🛡️ Alixyz-Scanner

A lightweight, efficient Python network port scanner designed for security auditing and network diagnostic workflows.

---

## 📌 Features
- **TCP Socket Connection Analysis:** Scans target IPs for active open services.
- **Error Handling:** Graceful handling of host resolution failures, manual interrupts, and timeout socket exceptions.
- **Clean Output:** Clear timestamps and structured port state reporting.

---

## ⚙️ How It Works
The scanner utilizes Python's native `socket` library to attempt TCP three-way handshakes against specified target ports (`connect_ex`). If the target accepts the handshake (returns code `0`), the port status is flagged as **OPEN**.

---

## 🚀 Quick Start & Usage

### Prerequisites
- Python 3.x installed

### Running the Scanner
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AlixyzLab/Alixyz-Scanner.git](https://github.com/AlixyzLab/Alixyz-Scanner.git)
   cd Alixyz-Scanner
