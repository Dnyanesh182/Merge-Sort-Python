# UC7 – Analyze time and space complexity of Merge Sort with different input sizes

from typing import List, Tuple
import time
import random
import sys


class MergeSort:
    """Class to implement Merge Sort."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data

        mid: int = len(data) // 2
        left: List[int] = MergeSort.sort(data[:mid])
        right: List[int] = MergeSort.sort(data[mid:])

        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        merged: List[int] = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


def analyze_performance(sizes: List[int]) -> None:
    """Analyze time and space for Merge Sort."""
    for size in sizes:
        data: List[int] = [random.randint(1, 1000) for _ in range(size)]

        # Time measurement
        start_time: float = time.time()
        MergeSort.sort(data.copy())
        end_time: float = time.time()

        # Space estimation (approx)
        space_usage: int = sys.getsizeof(data)

        print(
            f"Input Size: {size}, Time: {end_time - start_time:.6f}s, Space: {space_usage} bytes"
        )


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 1000, 5000]

    print("Merge Sort Complexity Analysis:")
    analyze_performance(sizes)


if __name__ == "__main__":
    main()