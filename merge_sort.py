# UC5 – Apply Merge Sort on list of strings using lexicographical order

from typing import List


class MergeSort:
    """Class to implement Merge Sort for strings."""

    @staticmethod
    def sort(data: List[str]) -> List[str]:
        """
        Sorts a list of strings lexicographically.

        :param data: List of strings
        :return: Sorted list
        """
        if len(data) <= 1:
            return data

        mid: int = len(data) // 2
        left: List[str] = MergeSort.sort(data[:mid])
        right: List[str] = MergeSort.sort(data[mid:])

        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(left: List[str], right: List[str]) -> List[str]:
        """Merge two sorted string lists."""
        merged: List[str] = []
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


def main() -> None:
    """Main execution function."""
    data: List[str] = ["banana", "apple", "cherry", "date"]

    print("Original List:", data)
    sorted_data: List[str] = MergeSort.sort(data.copy())
    print("Sorted List:", sorted_data)


if __name__ == "__main__":
    main()