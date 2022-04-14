from dataclasses import dataclass, field
import datetime
import uuid


@dataclass
class ArrayFIFO:
    
    _elements: list = field(default_factory=list, repr=False)
    _element_by_key: dict = field(default_factory=dict, repr=False)
    _key_by_date: dict = field(default_factory=dict, repr=False)

    @staticmethod
    def _get_uuid() -> int:
        return uuid.uuid1().int

    def push(self, new_element) -> object:
        """
        Add an element to the class
        :param new_element:
        """
        key = self._get_uuid()
        self._element_by_key[new_element] = key
        self._elements.append(new_element)
        self._key_by_date[key] = datetime.datetime.now()
        return new_element

    def pop(self) -> object:
        """
        Get and remove the oldest element
        :return:
        """
        try:
            element = self._elements.pop(0)
            key = self._element_by_key.get(element)
            self._key_by_date.pop(key)

        except IndexError as ex:
            raise IndexError(f'There was an error: {ex}')
        return element

    def size(self) -> int:
        """
        Get the number of elements
        :return: int
        """
        return len(self._elements)

    @property
    def _last_element(self) -> object:
        """
        Return last element of array
        :return:
        """
        if self._elements:
            return self._elements[-1]

    def addition_time(self, element=None) -> datetime:
        """
        Get the datetime when any element present on the FIFO was added.
        If no position is specified by default return last element addition.
        :param element: optional
        :return: datetime
        """
        if element is None:
            key = self._element_by_key.get(self._last_element)
            element_date = self._key_by_date.get(key)
            return element_date
        if element in self._elements:
            key = self._element_by_key.get(element)
            element_date = self._key_by_date.get(key)
            return element_date
        else:
            raise ValueError(f'Element {element} does not exist')
