from process_monitor import ProcessMonitor
from file_scanner import FileScanner
from startup_checker import StartupChecker
from risk_engine import RiskEngine

class SystemScanner:
    """Unified engine to run complete system checks."""

    def run_full_scan(self, target_folder: str = "."):
        processes = ProcessMonitor.get_running_processes()
        files = FileScanner.scan_directory(target_folder)
        startup_items = StartupChecker.get_startup_items()
        
        risk_summary = RiskEngine.evaluate_risk(processes, files, startup_items)

        return {
            "processes": processes,
            "files": files,
            "startup_items": startup_items,
            "risk_summary": risk_summary
        }