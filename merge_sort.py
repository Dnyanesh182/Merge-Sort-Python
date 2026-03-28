# UC4 – Handle sorting of duplicate elements correctly while maintaining stability

from typing import List, Tuple


class MergeSort:
    """Class to implement stable Merge Sort."""

    @staticmethod
    def sort(data: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
        """
        Sorts list of tuples based on first element while maintaining stability.

        :param data: List of tuples (value, identifier)
        :return: Stable sorted list
        """
        if len(data) <= 1:
            return data

        mid: int = len(data) // 2
        left: List[Tuple[int, str]] = MergeSort.sort(data[:mid])
        right: List[Tuple[int, str]] = MergeSort.sort(data[mid:])

        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(
        left: List[Tuple[int, str]],
        right: List[Tuple[int, str]]
    ) -> List[Tuple[int, str]]:
        """Merge step preserving stability."""
        merged: List[Tuple[int, str]] = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            # Stable: pick left when equal
            if left[i][0] <= right[j][0]:
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
    data: List[Tuple[int, str]] = [
        (5, "A"),
        (3, "B"),
        (5, "C"),
        (2, "D"),
        (3, "E"),
    ]

    print("Original List:", data)

    sorted_data: List[Tuple[int, str]] = MergeSort.sort(data.copy())

    print("Sorted List (Stable):", sorted_data)


if __name__ == "__main__":
    main()