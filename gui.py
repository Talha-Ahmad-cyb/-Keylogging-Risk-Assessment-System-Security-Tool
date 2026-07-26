import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from scanner import SystemScanner
from report_generator import ReportGenerator

class SecurityAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("System Security Scanner")
        self.root.geometry("550x400")

        self.scanner = SystemScanner()
        self.selected_directory = "."

        # UI Setup
        ttk.Label(root, text="System Security & Risk Assessment", font=("Helvetica", 14, "bold")).pack(pady=10)

        self.dir_frame = ttk.Frame(root)
        self.dir_frame.pack(fill="x", padx=20, pady=5)

        self.dir_label = ttk.Label(self.dir_frame, text="Scan Target: [ Current Directory ]")
        self.dir_label.pack(side="left")

        ttk.Button(self.dir_frame, text="Select Folder", command=self.select_folder).pack(side="right")

        self.scan_btn = ttk.Button(root, text="Run Full System Scan", command=self.run_scan)
        self.scan_btn.pack(pady=15)

        self.results_text = tk.Text(root, height=12, width=60)
        self.results_text.pack(padx=20, pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_directory = folder
            self.dir_label.config(text=f"Scan Target: {folder}")

    def run_scan(self):
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "Scanning system... Please wait...\n")
        self.root.update()

        try:
            results = self.scanner.run_full_scan(self.selected_directory)
            report_path = ReportGenerator.save_json_report(results)

            summary = results["risk_summary"]
            output = (
                f"--- SCAN COMPLETE ---\n"
                f"Overall Risk Level: {summary['level']}\n"
                f"Risk Score: {summary['score']}/100\n\n"
                f"Processes Inspected: {len(results['processes'])}\n"
                f"Files Scanned: {len(results['files'])}\n"
                f"Suspicious Files Found: {summary['suspicious_files_count']}\n"
                f"Startup Entries: {summary['startup_count']}\n\n"
                f"Report saved to:\n{report_path}"
            )
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, output)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during scanning:\n{str(e)}")