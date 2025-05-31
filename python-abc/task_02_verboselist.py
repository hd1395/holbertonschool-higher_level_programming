#!/usr/bin/python3
""" Module for extending python List """


class VerboseList(list):
    """VerboseList class

    Args:
        list

    Returns:
        Nothing

    """

    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        count = sum(1 for _ in items)
        print("Extended the list with {} items.".format(count))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed {} from the list.".format(item))
        except ValueError as exc:
            print("Attempted to remove value {} from the list.".format(item))
            print("Specified value does not exist. Nothing changed. Raising ValueError")
            raise ValueError() from exc

    def pop(self, index = None):
        if index is None:
            index = len(self) - 1

        try:
            print("Popped {} from the list.".format(self[index]))
            item = super().pop(index)
        except IndexError as exc:
            print("Attempted to pop index {0} from the list.".format(index))
            print("Specified index is out of range. Nothing changed. Raising IndexError")
            raise IndexError() from exc

        return item
