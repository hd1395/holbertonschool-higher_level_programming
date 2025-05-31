#!/usr/bin/python3
""" Module CountedIterator that extends the built-in iterator obtained from the iter function """


class CountedIterator:
    """CountedIterator class

    Args:
        Nothing

    Returns:
        Iterator or item within iterator

    """

    iterator = iter([])
    count = 0

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count = self.count + 1
            return item
        except StopIteration as exc:
            raise StopIteration() from exc

    def get_count(self) -> int:
        """returns count value"""
        return self.count
