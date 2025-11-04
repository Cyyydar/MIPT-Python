from datetime import datetime
import os
import random


class LogManager:

    def __init__(self, filename="Log.txt", user="anonymous"):
        self.filename = filename
        self.user = user

        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("=== LOG FILE CREATED ===\n")

    def _generate_event_id(self):
        return f"EVT-{random.randint(100000, 999999)}"

    def _write_log(self, level, source, message, extra_info=None):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_id = self._generate_event_id()

        log_entry = (
            f"[{time_str}] "
            f"[{level}] "
            f"[{source}] "
            f"[User: {self.user}] "
            f"[EventID: {event_id}] "
            f"Message: {message}"
        )

        if extra_info:
            log_entry += f"\n  Extra: {extra_info}"

        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    def info(self, source, message, extra_info=None):
        self._write_log("INFO", source, message, extra_info)

    def debug(self, source, message, extra_info=None):
        self._write_log("DEBUG", source, message, extra_info)

    def warn(self, source, message, extra_info=None):
        self._write_log("WARN", source, message, extra_info)

    def error(self, source, message, extra_info=None):
        self._write_log("ERROR", source, message, extra_info)

    def fatal(self, source, message, extra_info=None):
        self._write_log("FATAL", source, message, extra_info)