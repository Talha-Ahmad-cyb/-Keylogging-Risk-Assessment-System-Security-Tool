class RiskEngine:
    """Evaluates scan data and generates a calculated risk score."""

    @staticmethod
    def evaluate_risk(processes, files, startup_items):
        score = 0

        # Process Risk Factors
        high_cpu_procs = [p for p in processes if p.get('cpu', 0) > 80.0]
        score += len(high_cpu_procs) * 15

        # File Risk Factors
        suspicious_files = [f for f in files if f.get('is_suspicious')]
        score += len(suspicious_files) * 20

        # Startup Risk Factors
        score += len(startup_items) * 5

        # Clamp score to 100 max
        final_score = min(score, 100)

        if final_score >= 70:
            level = "HIGH"
        elif final_score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "score": final_score,
            "level": level,
            "suspicious_files_count": len(suspicious_files),
            "high_cpu_proc_count": len(high_cpu_procs),
            "startup_count": len(startup_items)
        }