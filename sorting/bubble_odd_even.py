
from concurrent.futures import ThreadPoolExecutor


def _compare_and_swap(args):
    arr, j = args
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return True
    return False


def odd_even_transpose_sort(arr, mode="sequential", workers=None):
    if mode not in {"sequential", "threaded"}:
        raise ValueError("mode must be 'sequential' or 'threaded'")

    n = len(arr)
    if n < 2:
        return

    quiet_phases = 0
    if mode == "threaded":
        executor = ThreadPoolExecutor(max_workers=workers)
    else:
        executor = None

    try:
        for phase in range(n):
            start = phase % 2
            if executor is None:
                swapped = False
                for j in range(start, n - 1, 2):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
            else:
                pairs = ((arr, j) for j in range(start, n - 1, 2))
                swapped = any(list(executor.map(_compare_and_swap, pairs)))

            quiet_phases = 0 if swapped else quiet_phases + 1
            if quiet_phases == 2:
                break
    finally:
        if executor is not None:
            executor.shutdown()


if __name__ == "__main__":
    arr = [5, 82, 1, 91, 2, 3, 7, 4, 23, 8, 86, 6, 2, 3, 11, 12, 9]
    odd_even_transpose_sort(arr, mode="sequential")
    print(arr)