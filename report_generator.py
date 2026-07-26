import json
from datetime import datetime
from settings import REPORTS_DIR

class ReportGenerator:
    """Handles reporting output formatting and export."""

    @staticmethod
    def save_json_report(scan_results: dict):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = REPORTS_DIR / f"scan_report_{timestamp}.json"
        
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(scan_results, f, indent=4)

        return str(report_file)