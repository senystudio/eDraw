import atexit
import logging

__all__ = ("warn_section", )

logging.basicConfig(
    filename="log.log",
    format="{levelname:<8} {asctime} {name:<8} |> {message};",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    level=logging.INFO,
    force=True
)


def warn_section(text: str, label_width=35):
    logging.warning(f"#{'=' * (2 * label_width + len(text))}#")
    logging.warning(f"|{' ' * label_width}{text}{' ' * label_width}|")
    logging.warning(f"#{'=' * (2 * label_width + len(text))}#")


warn_section("APP STARTED")
atexit.register(lambda: warn_section("APP CLOSED"))
