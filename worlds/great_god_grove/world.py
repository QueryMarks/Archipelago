from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules

class GreatGodGroveWorld(World):
    """
    Great God Grove APWorld.
    Suck up dialogue and get some checks!
    """
    game = "Great God Grove"

    options_dataclass = options.GreatGodGroveOptions
    options: options.GreatGodGroveOptions


    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID


    origin_region_name = "Chapter Select"


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.GreatGodGroveItem:
        return items.create_item_with_correct_classification(self, name)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "chapter_shuffle",
            "starting_chapter"
        )