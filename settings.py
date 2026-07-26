import os
from pathlib import Path

# Application Metadata
APP_NAME = "Security Scanner & Monitor"
APP_VERSION = "1.0.0"

# Directories
BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Risk Weight Definitions
RISK_THRESHOLDS = {
    "HIGH": 70,
    "MEDIUM": 40,
    "LOW": 0
}

# Suspicious file extensions for scanning
SUSPICIOUS_EXTENSIONS = {".exe", ".bat", ".cmd", ".vbs", ".ps1", ".scr", ".dll"}