from pathlib import Path
from settings import SUSPICIOUS_EXTENSIONS

class FileScanner:
    """Scans files in a target directory for high-risk attributes."""

    @staticmethod
    def scan_directory(target_dir: str):
        findings = []
        path = Path(target_dir)

        if not path.exists() or not path.is_dir():
            return findings

        for item in path.rglob("*"):
            try:
                if item.is_file():
                    ext = item.suffix.lower()
                    size_mb = item.stat().st_size / (1024 * 1024)
                    
                    is_suspicious = ext in SUSPICIOUS_EXTENSIONS
                    
                    findings.append({
                        "path": str(item),
                        "name": item.name,
                        "size_mb": round(size_mb, 2),
                        "extension": ext,
                        "is_suspicious": is_suspicious
                    })
            except PermissionError:
                continue
        return findings