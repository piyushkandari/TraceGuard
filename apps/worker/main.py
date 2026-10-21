"""Worker process entrypoint."""
import time
import structlog

logger = structlog.get_logger()

def main() -> None:
    """Run the worker loop."""
    logger.info("worker_started")
    while True:
        logger.info("worker_polling", message="Waiting for jobs...")
        time.sleep(10)

if __name__ == "__main__":
    main()