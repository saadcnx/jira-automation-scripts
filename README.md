
# 🧠 JIRA Automation Suite (by Saad Khan)

Automating project management tasks using **Python** and the **Atlassian JIRA REST API**.  
This collection of scripts helps teams save time by automating repetitive operations like ticket creation, system monitoring, and support email notifications.

---

## 🚀 Overview

### 🎫 **Auto Ticket Creator**
A Python automation that connects to JIRA and:
- Creates new JIRA tickets programmatically  
- Adds formatted comments with timestamps  
- Fetches and displays complete issue details and discussion history  

**Use Case:** Streamlining ticket creation and updates for QA and project teams.

---

### 🧮 **Server Health Monitor**
A lightweight script that:
- Connects to remote servers via SSH (using Paramiko)  
- Monitors system memory usage in real-time  
- Automatically creates a **“High Priority JIRA Task”** if available memory drops below a defined threshold  

**Use Case:** DevOps and SRE teams can proactively detect and respond to server issues.

---

### 📧 **Automated Acknowledgment Mailer**
An intelligent automation that:
- Scans JIRA for **newly created unassigned issues** in the last 5 minutes  
- Sends a personalized acknowledgment email to the issue reporter  
- Notifies both the reporter and support team (via CC)  

**Use Case:** Customer support teams can instantly confirm issue receipt without manual effort.

---

## 🧰 Tech Stack

| Technology | Purpose |
|-------------|----------|
| **Python 3** | Core scripting language |
| **Atlassian JIRA API (jira library)** | JIRA automation & integration |
| **Paramiko** | SSH for remote server monitoring |
| **smtplib** | Email automation via Gmail SMTP |
| **datetime, os** | Time formatting & environment handling |

---

## ⚙️ Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/saadcnx/jira-automation-scripts.git
   cd jira-automation-suite


