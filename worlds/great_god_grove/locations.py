from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import GreatGodGroveWorld

LOCATION_NAME_TO_ID = {
    #######NEW GAME#######
    "Flotsam": 1,
    "Junk": 2,
    "Trash": 3,
    "Jetsam": 4,

    #######CHAPTER 1#######
    "P HERE!": 5,
    "Tiny weak little bug.": 6,
    "BARKBARKBARKBARK": 7,
    "Love Letter": 8,
    "I got a BIG OL' crush on you.": 9,
    "Get ready for pets, cutie pie!": 10,
    "IT'S MEGAPON!": 11,
    "GET TO WORK, YOU LAZY PUP!": 12,
    "God and human, we can solve this mystery TOGETHA!": 13,
    "Lay off and take a snack break! That's an order.": 14,
    "GOODY JOB ON THE GOODY WORK!": 15,
    "Plank": 16,
    "Toys": 17,
    "DON'T WORRY MISSY! INSPEKTA WILL SAVE THE DAY!": 18,
    "I miss what my eloquent KING had to say!": 19,
    "With the power of communication, I can bring the gods together!": 20,
    "I AM GOING TO EAT YOU.": 21,

    #######CHAPTER 2#######
    "I thought this place had barbeque. WHERE'S THE SMOKED HOG?": 22,
    "Bork...": 23,
    "Yip... yiyip": 24,
    "ROUGHFFF!!!": 25,
    "Wherf!!!": 26,
    "Meow.": 27,
    "WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???": 28,
    "Oh Bayker... I LOVE IT!": 38,
    "If you ask me, Saul's just misunderstood.": 50,
    "That'll happen when pigs fly.": 51,
    "Cornelius": 48,
    "Extra Crow": 49,
    "Godpoke, go tell RAZZMA to draw something HEROIC for once.": 42,
    "TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!": 45,

    #######Chapter 2 Field#######
    "Like for example, what if they had edible lipstick?": 29,
    "I think edible lipstick would be the Bee's Cheese.": 30,
    "I... HATE that shaggy little man!": 31,
    "BUT SAUL WILL SAVE US ALL!": 32,
    "Hey there, handsome stranger!": 33,
    "Oh Cappy, can I please have my name back?": 34,
    "Hey vaquerito, go tell that DUMB BURRO Capochin to get a MOVE on!": 35,
    "-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS.": 44,

    "Marmaline": 46,
    "Gramma Boogie": 47,

    "You know, I used to make milldreadberry jam for the whole town!": 57,

    #######Chapter 2 Bayker House#######
    "HAAAACHHOOOOOOOOO!!!": 36,
    "Lipstick Pie": 37,
    "I thwear it on my life!!": 39,
    "Pappy Pumpkin": 40,

    "Milldreadberry Jam": 58,

    #######Chapter 2 Cobigail#######
    "BOO!": 41,

    #######Chapter 2 School#######
    "GET A HAIRCUT!": 43,

    #######Chapter 2 Underground#######
    "The snacks are made of friendliness; the drinks are filled with glee.": 52,
    "Milldread Berry": 56,

    #######Chapter 2 Hide and Seek#######
    "Our differences will bring us close, and Milldread we shall be.": 53,
    "Join your hands with anyone, sing in any key.": 54,
    "A bonfire in the evening breeze; an Autumn jubilee.": 55,

    #######Chapter 2 Fight#######
    "Pumpkin": 59,
    "mmmphWORTHLESS mphIDIOT!": 60,

    #######Chapter Select Unlocks#######
    "New Game Select": 150,
    "Chapter 1 Select": 151,
    "Chapter 2 Select": 152,
    "Chapter 3 Select": 153


}


class GreatGodGroveLocation(Location):
    game = "Great God Grove"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: GreatGodGroveWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: GreatGodGroveWorld) -> None:
    new_game = world.get_region("New Game")
    new_game_locations = (get_location_names_with_ids(
        [
            "Flotsam",
            "Junk",
            "Trash",
            "Jetsam",
        ]
    ))
    new_game.add_locations(new_game_locations, GreatGodGroveLocation)

    chapter_1_start = world.get_region("Chapter 1 Start")
    chapter_1_start_locations = (get_location_names_with_ids(
        [
            "P HERE!",
            "Tiny weak little bug.",
            "BARKBARKBARKBARK",
            "Love Letter",
            "I got a BIG OL' crush on you.",
            "Get ready for pets, cutie pie!",
        ]

    ))
    chapter_1_start.add_locations(chapter_1_start_locations, GreatGodGroveLocation)

    chapter_1_bizzyboys = world.get_region("Chapter 1 Bizzyboys")
    chapter_1_bizzyboys_locations = get_location_names_with_ids(
        [
            "IT'S MEGAPON!",
            "GET TO WORK, YOU LAZY PUP!"
        ]
    )
    chapter_1_bizzyboys.add_locations(chapter_1_bizzyboys_locations, GreatGodGroveLocation)

    chapter_1_inspekta = world.get_region("Chapter 1 Inspekta")
    chapter_1_inspekta_locations = (get_location_names_with_ids(
        [
            "God and human, we can solve this mystery TOGETHA!",
            "Lay off and take a snack break! That's an order.",
            "GOODY JOB ON THE GOODY WORK!"
        ]
    ))
    chapter_1_inspekta.add_locations(chapter_1_inspekta_locations, GreatGodGroveLocation)
    #todo: write a method for this, are you nuts

    chapter_1_miss_mitternacht = world.get_region("Chapter 1 Miss Mitternacht")
    chapter_1_miss_mitternacht_locations = get_location_names_with_ids(
        [
            "Plank",
            "Toys",
            "DON'T WORRY MISSY! INSPEKTA WILL SAVE THE DAY!",
            "I miss what my eloquent KING had to say!",

        ]
    )
    chapter_1_miss_mitternacht.add_locations(chapter_1_miss_mitternacht_locations)

    chapter_1_razzma = world.get_region("Chapter 1 Razzma")
    chapter_1_razzma_locations = get_location_names_with_ids(
        [
            "With the power of communication, I can bring the gods together!",
            "I AM GOING TO EAT YOU."
        ]
    )
    chapter_1_razzma.add_locations(chapter_1_razzma_locations)


    chapter_2_start = world.get_region("Chapter 2 Start")
    chapter_2_start_locations = get_location_names_with_ids(
        [
            "I thought this place had barbeque. WHERE'S THE SMOKED HOG?",
            "Bork...",
            "Yip... yiyip",
            "ROUGHFFF!!!",
            "Wherf!!!",
            "Meow.",
            "WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???",
            "Oh Bayker... I LOVE IT!",
            "Godpoke, go tell RAZZMA to draw something HEROIC for once.",
            "TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!",
            "If you ask me, Saul's just misunderstood.",
            "That'll happen when pigs fly.",
            "Cornelius",
            "Extra Crow",
            "Godpoke, go tell RAZZMA to draw something HEROIC for once.",
            "TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!"
        ]
    )
    chapter_2_start.add_locations(chapter_2_start_locations)

    chapter_2_field = world.get_region("Chapter 2 Field")
    chapter_2_field_locations = get_location_names_with_ids(
        [
            "Like for example, what if they had edible lipstick?",
            "I think edible lipstick would be the Bee's Cheese.",
            "I... HATE that shaggy little man!",
            "BUT SAUL WILL SAVE US ALL!",
            "Hey there, handsome stranger!",
            "Oh Cappy, can I please have my name back?",
            "Hey vaquerito, go tell that DUMB BURRO Capochin to get a MOVE on!",
            "-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS.",
            "Marmaline",
            "Gramma Boogie",
            "You know, I used to make milldreadberry jam for the whole town!"
        ]
    )
    chapter_2_field.add_locations(chapter_2_field_locations)

    chapter_2_bayker = world.get_region("Chapter 2 Bayker")
    chapter_2_bayker_locations = get_location_names_with_ids(
        [
            "HAAAACHHOOOOOOOOO!!!",
            "Lipstick Pie",
            "I thwear it on my life!!",
            "Pappy Pumpkin",
            "Milldreadberry Jam"
        ]
    )
    chapter_2_bayker.add_locations(chapter_2_bayker_locations)

    chapter_2_underground = world.get_region("Chapter 2 Underground")
    chapter_2_underground_locations = get_location_names_with_ids(
        [
            "The snacks are made of friendliness; the drinks are filled with glee.",
            "Milldread Berry"
        ]
    )
    chapter_2_underground.add_locations(chapter_2_underground_locations)

    chapter_2_school = world.get_region("Chapter 2 School")
    chapter_2_school_locations = get_location_names_with_ids(
        [
            "GET A HAIRCUT!"
        ]
    )
    chapter_2_school.add_locations(chapter_2_school_locations)

    chapter_2_cobigail = world.get_region("Chapter 2 Cobigail")
    chapter_2_cobigail_locations = get_location_names_with_ids(
        [
            "BOO!"
        ]
    )
    chapter_2_cobigail.add_locations(chapter_2_cobigail_locations)

    chapter_2_hide_and_seek = world.get_region("Chapter 2 Hide and Seek")
    chapter_2_hide_and_seek_locations = get_location_names_with_ids(
        [
            "Our differences will bring us close, and Milldread we shall be.",
            "Join your hands with anyone, sing in any key.",
            "A bonfire in the evening breeze; an Autumn jubilee."
        ]
    )
    chapter_2_hide_and_seek.add_locations(chapter_2_hide_and_seek_locations)

    chapter_2_fight = world.get_region("Chapter 2 Fight")
    chapter_2_fight_locations = get_location_names_with_ids(
        [
            "Pumpkin",
            "mmmphWORTHLESS mphIDIOT!"
        ]
    )
    chapter_2_fight.add_locations(chapter_2_fight_locations)

    chapter_3_start = world.get_region("Chapter 3 Start")

    if world.options.chapter_shuffle:

        new_game.add_locations(get_location_names_with_ids(
            [
            "New Game Select"
            ]
        ))

        chapter_1_start.add_locations(get_location_names_with_ids(
            [
            "Chapter 1 Select"
            ]
        ))

        chapter_2_start.add_locations(get_location_names_with_ids(
            [
                "Chapter 2 Select"
            ]
        ))

        chapter_3_start.add_locations(get_location_names_with_ids(
            [
                "Chapter 3 Select"
            ]
        ))


def create_events(world: GreatGodGroveWorld) -> None:
    chapter_3_start = world.get_region("Chapter 3 Start")

    chapter_3_start.add_event(
        "FINISH", "Victory", location_type=GreatGodGroveLocation, item_type=items.GreatGodGroveItem
    )
