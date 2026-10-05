import time
import random

from opentelemetry import _logs
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter



exporter = OTLPLogExporter(
    endpoint="http://localhost:4318/v1/logs"
)


logger_provider = LoggerProvider()

logger_provider.add_log_record_processor(
    BatchLogRecordProcessor(exporter)
)

_logs.set_logger_provider(logger_provider)

logger = _logs.get_logger("log-demo")


while True:

    event = random.choice([
        "user_login",
        "payment_success",
        "payment_failed",
        "database_error",
        "request_completed"
    ])

    if event == "user_login":

        logger.emit(
            severity_text="INFO",
            body="User logged in"
        )

    elif event == "payment_success":

        logger.emit(
            severity_text="INFO",
            body="Payment completed successfully"
        )

    elif event == "payment_failed":

        logger.emit(
            severity_text="WARN",
            body="Payment failed"
        )

    elif event == "database_error":

        logger.emit(
            severity_text="ERROR",
            body="Database connection failed"
        )

    elif event == "request_completed":

        logger.emit(
            severity_text="INFO",
            body="Request completed"
        )

    time.sleep(2)