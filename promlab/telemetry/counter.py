from prometheus_client import Counter, registry


http_requests_user_list_counter = Counter(
    'http_requests_', 'Number of requests to user list route'
)
