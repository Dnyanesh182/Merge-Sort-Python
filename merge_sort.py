# UC2 – Modify Merge Sort to sort array in descending order

from typing import List


class MergeSort:
    """Class to implement Merge Sort in descending order."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list in descending order using Merge Sort.

        :param data: List of integers
        :return: Sorted list
        """
        if len(data) <= 1:
            return data

        mid: int = len(data) // 2
        left: List[int] = MergeSort.sort(data[:mid])
        right: List[int] = MergeSort.sort(data[mid:])

        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """Merges two sorted lists in descending order."""
        merged: List[int] = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:  # descending comparison
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)
    sorted_data: List[int] = MergeSort.sort(data.copy())
    print("Sorted List (Descending):", sorted_data)


if __name__ == "__main__":
    main()