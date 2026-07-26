import os
import sys

class StartupChecker:
    """Checks startup items across OS environments."""

    @staticmethod
    def get_startup_items():
        items = []
        if sys.platform == "win32":
            import winreg
            keys = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
            ]
            for root, key_path in keys:
                try:
                    with winreg.OpenKey(root, key_path, 0, winreg.KEY_READ) as key:
                        idx = 0
                        while True:
                            name, value, _ = winreg.EnumValue(key, idx)
                            items.append({"name": name, "path": value, "source": "Registry"})
                            idx += 1
                except OSError:
                    pass
        else:
            # Fallback mock for non-Windows platforms (macOS/Linux user startup paths)
            startup_path = Path.home() / ".config" / "autostart"
            if startup_path.exists():
                for f in startup_path.glob("*.desktop"):
                    items.append({"name": f.stem, "path": str(f), "source": "Autostart Folder"})

        return items