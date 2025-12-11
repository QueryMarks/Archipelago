from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import GreatGodGroveWorld


def create_and_connect_regions(world: GreatGodGroveWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: GreatGodGroveWorld) -> None:

    chapter_select = Region("Chapter Select", world.player, world.multiworld)

    new_game = Region("New Game", world.player, world.multiworld)
    chapter_1_start = Region("Chapter 1 Start", world.player, world.multiworld)
    chapter_1_bizzyboys = Region("Chapter 1 Bizzyboys", world.player, world.multiworld)
    chapter_1_inspekta = Region("Chapter 1 Inspekta", world.player, world.multiworld)
    chapter_1_miss_mitternacht = Region("Chapter 1 Miss Mitternacht", world.player, world.multiworld)
    chapter_1_razzma = Region("Chapter 1 Razzma", world.player, world.multiworld)

    chapter_2_start = Region("Chapter 2 Start", world.player, world.multiworld)
    chapter_2_field = Region("Chapter 2 Field", world.player, world.multiworld)
    chapter_2_bayker = Region("Chapter 2 Bayker", world.player, world.multiworld)
    chapter_2_school = Region("Chapter 2 School", world.player, world.multiworld)
    chapter_2_cobigail = Region("Chapter 2 Cobigail", world.player, world.multiworld)
    chapter_2_underground = Region("Chapter 2 Underground", world.player, world.multiworld)
    chapter_2_hide_and_seek = Region("Chapter 2 Hide and Seek", world.player, world.multiworld)
    chapter_2_fight = Region("Chapter 2 Fight", world.player, world.multiworld)

    chapter_3_start = Region("Chapter 3 Start", world.player, world.multiworld)

    regions = [
        chapter_select,
        new_game,
        chapter_1_start,
        chapter_1_bizzyboys,
        chapter_1_inspekta,
        chapter_1_miss_mitternacht,
        chapter_1_razzma,
        chapter_2_start,
        chapter_2_field,
        chapter_2_bayker,
        chapter_2_school,
        chapter_2_cobigail,
        chapter_2_underground,
        chapter_2_hide_and_seek,
        chapter_2_fight,
        chapter_3_start
    ]

    world.multiworld.regions += regions

def connect_regions(world: GreatGodGroveWorld) -> None:

    chapter_select = world.get_region("Chapter Select")


    new_game = world.get_region("New Game")
    chapter_1_start = world.get_region("Chapter 1 Start")
    chapter_1_bizzyboys = world.get_region("Chapter 1 Bizzyboys")
    chapter_1_inspekta = world.get_region("Chapter 1 Inspekta")
    chapter_1_miss_mitternacht = world.get_region("Chapter 1 Miss Mitternacht")
    chapter_1_razzma = world.get_region("Chapter 1 Razzma")

    chapter_2_start = world.get_region("Chapter 2 Start")
    chapter_2_field = world.get_region("Chapter 2 Field")
    chapter_2_bayker = world.get_region("Chapter 2 Bayker")
    chapter_2_school = world.get_region("Chapter 2 School")
    chapter_2_cobigail = world.get_region("Chapter 2 Cobigail")
    chapter_2_underground = world.get_region("Chapter 2 Underground")
    chapter_2_hide_and_seek = world.get_region("Chapter 2 Hide and Seek")
    chapter_2_fight = world.get_region("Chapter 2 Fight")

    chapter_3_start = world.get_region("Chapter 3 Start")

    #connect regions below

    chapter_select.connect(
        new_game,
        "Chapter Select to New Game",
        lambda state: state.has("New Game Select", world.player)
    )

    chapter_select.connect(
        chapter_1_start,
        "Chapter Select to Chapter 1 Start",
        lambda state: state.has("Chapter 1 Select", world.player)
    )

    chapter_select.connect(
        chapter_2_start,
        "Chapter Select to Chapter 2 Start",
        lambda state: state.has("Chapter 2 Select", world.player)
    )

    chapter_select.connect(
        chapter_3_start,
        "Chapter Select to Chapter 3 Start",
        lambda state: state.has("Chapter 3 Select", world.player)
    )




    new_game.connect(chapter_1_start, "New Game to Chapter 1 Start")
    chapter_1_start.connect(
        chapter_1_bizzyboys,
        "Chapter 1 Start to Chapter 1 Bizzyboys",
        lambda state: state.has("I got a BIG OL' crush on you.", world.player)
    )
    chapter_1_bizzyboys.connect(
        chapter_1_inspekta,
        "Chapter 1 Bizzyboys to Chapter 1 Inspekta",
        lambda state: (
                state.has("IT'S MEGAPON!", world.player)
        )
    )

    chapter_1_bizzyboys.connect(
        chapter_1_miss_mitternacht,
        "Chapter 1 Bizzyboys to Chapter 1 Miss Mitternacht",
        lambda state: (
            state.has("Lay off and take a snack break! That's an order.", world.player)
        )
    )

    chapter_1_miss_mitternacht.connect(
        chapter_1_razzma,
        "Chapter 1 Miss Mitternacht to Chapter 1 Razzma",
        lambda state: (
            state.has("Plank", world.player)
        )
    )

    chapter_1_miss_mitternacht.connect(
        chapter_2_start,
        "Chapter 1 Miss Mitternacht to Chapter 2 Start",
        lambda state: (
            state.has("God and human, we can solve this mystery TOGETHA!", world.player)
            and
            state.has("With the power of communication, I can bring the gods together!", world.player)
        )
    )

    chapter_2_start.connect(
        chapter_2_field,
        "Chapter 2 Start to Chapter 2 Field",
        lambda state: (
            state.has("ROUGHFFF!!!", world.player)
        )
    )

    chapter_2_field.connect(chapter_2_bayker, "Chapter 2 Field to Chapter 2 Bayker")

    chapter_2_start.connect(
        chapter_2_school,
        "Chapter 2 Start to Chapter 2 School",
        lambda state: (
            state.has("Pappy Pumpkin", world.player)
        )
    )

    chapter_2_school.connect(chapter_2_cobigail, "Chapter 2 School to Chapter 2 Cobigail")

    chapter_2_field.connect(
        chapter_2_underground,
        "Chapter 2 Field to Chapter 2 Underground",
        lambda state:
        (
            state.has("Cornelius", world.player)
            or state.has("Marmaline", world.player)
            or state.has("Gramma Boogie", world.player)
            or state.has("Extra Crow", world.player)
        )
    )

    chapter_2_underground.connect(
        chapter_2_hide_and_seek,
    "Chapter 2 Underground to Chapter 2 Hide and Seek"
    )

    chapter_2_hide_and_seek.connect(
        chapter_2_fight,
        "Chapter 2 Hide and Seek to Chapter 2 Fight",
        lambda state:
        (
            state.has("Pappy Pumpkin", world.player)
            and state.has("Milldreadberry Jam", world.player)
        )
    )

    chapter_2_fight.connect(
        chapter_3_start,
        "Chapter 2 Fight to Chapter 3 Start",
        lambda state:
        (
            state.has("Mildreadberry Jam", world.player)
        )
    )


