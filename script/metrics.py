from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
import time

exporter = OTLPMetricExporter(
    endpoint="http://localhost:4318/v1/metrics"
)

reader = PeriodicExportingMetricReader(
    exporter,
    export_interval_millis=5000
)

provider = MeterProvider(
    metric_readers=[reader]
)

metrics.set_meter_provider(provider)

meter = metrics.get_meter("python-demo")

counter = meter.create_counter(
    "app.requests",
    description="Number of application requests"
)

while True:
    counter.add(1)
    print("Metric recorded")
    time.sleep(1)