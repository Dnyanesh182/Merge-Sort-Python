# UC9 – Implement in-place Merge Sort optimization (reduce extra space usage)

from typing import List


class MergeSort:
    """Class to implement in-place Merge Sort."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts list using in-place Merge Sort.

        :param data: List of integers
        :return: Sorted list
        """
        if len(data) <= 1:
            return data

        MergeSort._merge_sort(data, 0, len(data) - 1)
        return data

    @staticmethod
    def _merge_sort(data: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        mid: int = (left + right) // 2

        MergeSort._merge_sort(data, left, mid)
        MergeSort._merge_sort(data, mid + 1, right)
        MergeSort._merge(data, left, mid, right)

    @staticmethod
    def _merge(data: List[int], left: int, mid: int, right: int) -> None:
        """Merge using temporary buffer within bounds."""
        temp: List[int] = []
        i: int = left
        j: int = mid + 1

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp.append(data[i])
                i += 1
            else:
                temp.append(data[j])
                j += 1

        while i <= mid:
            temp.append(data[i])
            i += 1

        while j <= right:
            temp.append(data[j])
            j += 1

        # Copy back to original array
        for idx, val in enumerate(temp):
            data[left + idx] = val


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)

    sorted_data: List[int] = MergeSort.sort(data.copy())

    print("Sorted List:", sorted_data)


if __name__ == "__main__":
    main()