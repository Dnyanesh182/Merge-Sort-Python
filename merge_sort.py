# UC6 – Sort custom objects using Merge Sort with key (e.g., sort by age)

from typing import List, Callable, TypeVar

T = TypeVar("T")


class Person:
    """Represents a person with name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"


class MergeSort:
    """Class to implement Merge Sort for custom objects."""

    @staticmethod
    def sort(data: List[T], key: Callable[[T], int]) -> List[T]:
        """
        Sorts objects using Merge Sort based on a key.

        :param data: List of objects
        :param key: Function to extract comparison key
        :return: Sorted list
        """
        if len(data) <= 1:
            return data

        mid: int = len(data) // 2
        left: List[T] = MergeSort.sort(data[:mid], key)
        right: List[T] = MergeSort.sort(data[mid:], key)

        return MergeSort._merge(left, right, key)

    @staticmethod
    def _merge(left: List[T], right: List[T], key: Callable[[T], int]) -> List[T]:
        """Merge two sorted lists using key."""
        merged: List[T] = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
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
    people: List[Person] = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 30),
        Person("David", 20),
    ]

    print("Original List:", people)

    sorted_people: List[Person] = MergeSort.sort(
        people.copy(), key=lambda person: person.age
    )

    print("Sorted List (by age):", sorted_people)


if __name__ == "__main__":
    main()