

import sys
import tkinter as tk
from gui import SecurityAppGUI
from scanner import SystemScanner
from report_generator import ReportGenerator


def run_cli():
    """Runs a quick security scan directly in the command line."""
    print("=" * 50)
    print("      SYSTEM SECURITY SCANNER - CLI MODE      ")
    print("=" * 50)
    print("Starting system assessment...\n")

    scanner = SystemScanner()
    results = scanner.run_full_scan(target_folder=".")
    
    report_path = ReportGenerator.save_json_report(results)
    summary = results["risk_summary"]

    print("--- SCAN RESULTS ---")
    print(f"Risk Level : {summary['level']}")
    print(f"Risk Score : {summary['score']} / 100")
    print(f"Processes  : {len(results['processes'])} analyzed ({summary['high_cpu_proc_count']} high CPU)")
    print(f"Files      : {len(results['files'])} scanned ({summary['suspicious_files_count']} suspicious)")
    print(f"Startups   : {summary['startup_count']} entry items checked")
    print("-" * 50)
    print(f"Report saved to: {report_path}\n")


def run_gui():
    """Launches the Tkinter Graphical User Interface."""
    root = tk.Tk()
    
    # Prevent window scaling/crispness issues on Windows displays
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    app = SecurityAppGUI(root)
    root.mainloop()


def main():
    """Entry point check for CLI flags or GUI launch."""
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--cli", "-c"]:
        run_cli()
    else:
        run_gui()


if __name__ == "__main__":
    main()