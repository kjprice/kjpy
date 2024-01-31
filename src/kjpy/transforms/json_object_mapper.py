from typing import Callable, List, Optional, Union
from enum import Enum


def _ensure_list(items) -> List[str]:
    if type(items) == list:
        return items
    return [items]


def _split_keys(item: str) -> List[str]:
    return item.split(".")


class CustomHandler(Enum):
    PERSON = "is_person_field"
    PUBLISHER = "is_publisher_field"
    VARIATIONS = "is_variations_field"
    VARIATION_OF = "is_variation_of_field"


class JsonObjectMapper:
    def __init__(
        self,
        return_field_names: Union[str, List[str]],
        clean_fn: Optional[Callable] = None,
        custom_handler: Optional[CustomHandler] = None,
    ):
        self.return_fields: List[str] = _ensure_list(return_field_names)
        self.return_fields_keys: List[List[str]] = [
            _split_keys(f) for f in self.return_fields
        ]
        self.clean_fn = clean_fn
        self.custom_handler = custom_handler

    def get(self, value):
        if self.clean_fn:
            return self.clean_fn(value)

        return value