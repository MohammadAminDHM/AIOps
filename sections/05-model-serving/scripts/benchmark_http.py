import argparse
import concurrent.futures
import statistics
import time
import urllib.request


def call(url: str) -> float:
    started = time.perf_counter()
    with urllib.request.urlopen(url, timeout=30) as response:
        response.read()
    return time.perf_counter() - started


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple HTTP latency benchmark for model-serving labs.")
    parser.add_argument("--url", default="http://localhost:8000/health")
    parser.add_argument("--requests", type=int, default=20)
    parser.add_argument("--concurrency", type=int, default=4)
    args = parser.parse_args()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        latencies = list(pool.map(lambda _: call(args.url), range(args.requests)))

    latencies_ms = [x * 1000 for x in latencies]
    print(f"requests={args.requests} concurrency={args.concurrency}")
    print(f"min_ms={min(latencies_ms):.2f}")
    print(f"mean_ms={statistics.mean(latencies_ms):.2f}")
    print(f"p95_ms={statistics.quantiles(latencies_ms, n=20)[18]:.2f}")
    print(f"max_ms={max(latencies_ms):.2f}")


if __name__ == "__main__":
    main()
