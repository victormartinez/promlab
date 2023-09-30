from prometheus_client import Counter, registry


http_requests_counter = Counter('http_requests', 'Number of requests processed')
