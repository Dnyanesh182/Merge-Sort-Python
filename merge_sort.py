# UC10 – Refactor Merge Sort implementation using clean code practices and reusable functions

from typing import List, TypeVar, Callable, Optional

T = TypeVar("T")


class MergeSort:
    """Refactored, generic Merge Sort implementation."""

    @staticmethod
    def sort(
        data: List[T],
        key: Optional[Callable[[T], int]] = None,
        reverse: bool = False,
    ) -> List[T]:
        """
        Generic Merge Sort with key and reverse support.

        :param data: List of elements
        :param key: Optional key function
        :param reverse: Sort descending if True
        :return: Sorted list
        """
        if len(data) <= 1:
            return data

        key_func: Callable[[T], int] = key if key else lambda x: x

        mid: int = len(data) // 2
        left: List[T] = MergeSort.sort(data[:mid], key_func, reverse)
        right: List[T] = MergeSort.sort(data[mid:], key_func, reverse)

        return MergeSort._merge(left, right, key_func, reverse)

    @staticmethod
    def _merge(
        left: List[T],
        right: List[T],
        key: Callable[[T], int],
        reverse: bool,
    ) -> List[T]:
        """Reusable merge logic."""
        merged: List[T] = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            left_val = key(left[i])
            right_val = key(right[j])

            should_take_left: bool = (
                left_val <= right_val if not reverse else left_val >= right_val
            )

            if should_take_left:
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

    asc_sorted = MergeSort.sort(data.copy())
    desc_sorted = MergeSort.sort(data.copy(), reverse=True)

    print("Ascending:", asc_sorted)
    print("Descending:", desc_sorted)


if __name__ == "__main__":
    main()