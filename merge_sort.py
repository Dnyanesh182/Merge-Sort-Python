# UC3 – Count number of comparisons performed during merging process

from typing import List, Tuple


class MergeSort:
    """Class to implement Merge Sort with comparison counting."""

    @staticmethod
    def sort(data: List[int]) -> Tuple[List[int], int]:
        """
        Sorts a list and counts comparisons.

        :param data: List of integers
        :return: Tuple of (sorted list, comparison count)
        """
        if len(data) <= 1:
            return data, 0

        mid: int = len(data) // 2
        left, left_count = MergeSort.sort(data[:mid])
        right, right_count = MergeSort.sort(data[mid:])

        merged, merge_count = MergeSort._merge(left, right)

        total_count: int = left_count + right_count + merge_count
        return merged, total_count

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> Tuple[List[int], int]:
        """Merges two sorted lists and counts comparisons."""
        merged: List[int] = []
        i: int = 0
        j: int = 0
        comparisons: int = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, comparisons


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)

    sorted_data, comparisons = MergeSort.sort(data.copy())

    print("Sorted List:", sorted_data)
    print("Total Comparisons:", comparisons)


if __name__ == "__main__":
    main()