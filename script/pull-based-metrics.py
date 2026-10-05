from prometheus_client import start_http_server, Counter, Gauge, Histogram
import time
import random

# Counter
requests = Counter(
    "app_requests_total",
    "Total number of application requests"
)

# Gauge
active_users = Gauge(
    "app_active_users",
    "Number of active users"
)

# Histogram
request_duration = Histogram(
    "app_request_duration_seconds",
    "Request duration in seconds"
)

# Expose /metrics on port 8000
start_http_server(8000)

while True:

    # Simulate request
    requests.inc()

    # Simulate active users
    active_users.set(random.randint(1, 100))

    # Simulate request duration
    duration = random.uniform(0.05, 1.5)
    request_duration.observe(duration)

    print(
        f"Request recorded | "
        f"Active Users: {int(active_users._value.get())} | "
        f"Duration: {duration:.2f}s"
    )

    time.sleep(1)