# UC8 – Compare Merge Sort performance with Bubble Sort and Selection Sort

from typing import List
import time
import random


class MergeSort:
    @staticmethod
    def sort(data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = MergeSort.sort(data[:mid])
        right = MergeSort.sort(data[mid:])
        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        merged: List[int] = []
        i = j = 0
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


class BubbleSort:
    @staticmethod
    def sort(data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break
        return data


class SelectionSort:
    @staticmethod
    def sort(data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if data[j] < data[min_index]:
                    min_index = j
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        return data


def compare(size: int) -> None:
    """Compare performance of sorting algorithms."""
    data: List[int] = [random.randint(1, 1000) for _ in range(size)]

    # Merge Sort
    start = time.time()
    MergeSort.sort(data.copy())
    merge_time = time.time() - start

    # Bubble Sort
    start = time.time()
    BubbleSort.sort(data.copy())
    bubble_time = time.time() - start

    # Selection Sort
    start = time.time()
    SelectionSort.sort(data.copy())
    selection_time = time.time() - start

    print(f"Input Size: {size}")
    print(f"Merge Sort: {merge_time:.6f}s")
    print(f"Bubble Sort: {bubble_time:.6f}s")
    print(f"Selection Sort: {selection_time:.6f}s")
    print("-" * 40)


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [100, 500, 1000]

    print("Performance Comparison of Sorting Algorithms:")
    for size in sizes:
        compare(size)


if __name__ == "__main__":
    main()