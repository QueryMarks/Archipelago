from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import GreatGodGroveWorld

ITEM_NAME_TO_ID = {
    "Flotsam": 1,
    "Junk" : 2,
    "Trash": 3,
    "Jetsam" : 4,
    "P HERE!" : 5,
    "Tiny weak little bug." : 6,
    "BARKBARKBARKBARK" : 7,
    "Love Letter" : 8,
    "I got a BIG OL' crush on you." : 9,
    "Get ready for pets, cutie pie!" : 10,
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
    "If you ask me, Saul's just misunderstood." : 50,
    "That'll happen when pigs fly." : 51,
    "Cornelius" : 48,
    "Extra Crow" : 49,
    "Godpoke, go tell RAZZMA to draw something HEROIC for once." : 42,
    "TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!" : 45,


    #######Chapter 2 Field#######
    "Like for example, what if they had edible lipstick?" : 29,
    "I think edible lipstick would be the Bee's Cheese." : 30,
    "I... HATE that shaggy little man!" : 31,
    "BUT SAUL WILL SAVE US ALL!" : 32,
    "Hey there, handsome stranger!" : 33,
    "Oh Cappy, can I please have my name back?" : 34,
    "Hey vaquerito, go tell that DUMB BURRO Capochin to get a MOVE on!" : 35,
    "-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS." : 44,

    "Marmaline": 46,
    "Gramma Boogie": 47,

    "You know, I used to make milldreadberry jam for the whole town!" : 57,



    #######Chapter 2 Bayker House#######
    "HAAAACHHOOOOOOOOO!!!" : 36,
    "Lipstick Pie" : 37,
    "I thwear it on my life!!" : 39,
    "Pappy Pumpkin" : 40,

    "Milldreadberry Jam" : 58,

    #######Chapter 2 Cobigail#######
    "BOO!" : 41,

    #######Chapter 2 School#######
    "GET A HAIRCUT!" : 43,


    #######Chapter 2 Underground#######
    "The snacks are made of friendliness; the drinks are filled with glee." : 52,
    "Milldread Berry" : 56,

    #######Chapter 2 Hide and Seek#######
    "Our differences will bring us close, and Milldread we shall be." : 53,
    "Join your hands with anyone, sing in any key." : 54,
    "A bonfire in the evening breeze; an Autumn jubilee." : 55,

    #######Chapter 2 Fight#######
    "Pumpkin" : 59,
    "mmmphWORTHLESS mphIDIOT!" : 60,

    #######Chapter Select Unlocks#######
    "New Game Select" : 150,
    "Chapter 1 Select" : 151,
    "Chapter 2 Select" : 152,
    "Chapter 3 Select" : 153
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Flotsam": ItemClassification.filler,
    "Junk": ItemClassification.filler,
    "Trash": ItemClassification.filler,
    "Jetsam": ItemClassification.filler,
    "P HERE!": ItemClassification.filler,
    "Tiny weak little bug.": ItemClassification.filler,
    "BARKBARKBARKBARK": ItemClassification.filler,
    "Love Letter": ItemClassification.progression,
    "I got a BIG OL' crush on you.": ItemClassification.progression,
    "Get ready for pets, cutie pie!": ItemClassification.filler,
    "IT'S MEGAPON!": ItemClassification.progression,
    "GET TO WORK, YOU LAZY PUP!": ItemClassification.filler,
    "God and human, we can solve this mystery TOGETHA!": ItemClassification.progression,
    "Lay off and take a snack break! That's an order.": ItemClassification.progression,
    "GOODY JOB ON THE GOODY WORK!": ItemClassification.filler,
    "Plank": ItemClassification.progression,
    "Toys": ItemClassification.filler,
    "DON'T WORRY MISSY! INSPEKTA WILL SAVE THE DAY!": ItemClassification.filler,
    "I miss what my eloquent KING had to say!": ItemClassification.progression,
    "With the power of communication, I can bring the gods together!": ItemClassification.progression,
    "I AM GOING TO EAT YOU.": ItemClassification.filler,

    #######CHAPTER 2#######
    "I thought this place had barbeque. WHERE'S THE SMOKED HOG?": ItemClassification.filler,
    "Bork...": ItemClassification.filler,
    "Yip... yiyip": ItemClassification.filler,
    "ROUGHFFF!!!": ItemClassification.progression,
    "Wherf!!!": ItemClassification.filler,
    "Meow.": ItemClassification.filler,
    "WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???": ItemClassification.progression,
    "Oh Bayker... I LOVE IT!": ItemClassification.progression,
    "If you ask me, Saul's just misunderstood.": ItemClassification.filler,
    "That'll happen when pigs fly.": ItemClassification.filler,
    "Cornelius": ItemClassification.progression,
    "Extra Crow": ItemClassification.progression,
    "Godpoke, go tell RAZZMA to draw something HEROIC for once.": ItemClassification.progression,
    "TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!": ItemClassification.filler,


    #######Chapter 2 Field#######
    "Like for example, what if they had edible lipstick?" : ItemClassification.progression,
    "I think edible lipstick would be the Bee's Cheese." : ItemClassification.filler,
    "I... HATE that shaggy little man!" : ItemClassification.progression,
    "BUT SAUL WILL SAVE US ALL!" : ItemClassification.filler,
    "Hey there, handsome stranger!" : ItemClassification.filler,
    "Oh Cappy, can I please have my name back?" : ItemClassification.filler,
    "Hey vaquerito, go tell that DUMB BURRO Capochin to get a MOVE on!" : ItemClassification.progression,
    "-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS.":ItemClassification.progression,

    "Marmaline": ItemClassification.progression,
    "Gramma Boogie": ItemClassification.progression,
    
    "You know, I used to make milldreadberry jam for the whole town!": ItemClassification.progression,

    #######Chapter 2 Bayker House#######
    "HAAAACHHOOOOOOOOO!!!" : ItemClassification.filler,
    "Lipstick Pie" : ItemClassification.progression,
    "I thwear it on my life!!": ItemClassification.progression,
    "Pappy Pumpkin": ItemClassification.progression,

    "Milldreadberry Jam": ItemClassification.progression,

    #######Chapter 2 Cobigail#######
    "BOO!": ItemClassification.progression,

    #######Chapter 2 School#######
    "GET A HAIRCUT!": ItemClassification.progression,

    #######Chapter 2 Underground#######
    "The snacks are made of friendliness; the drinks are filled with glee.": ItemClassification.progression,
    "Milldread Berry": ItemClassification.progression,

    #######Chapter 2 Hide and Seek#######
    "Our differences will bring us close, and Milldread we shall be.": ItemClassification.progression,
    "Join your hands with anyone, sing in any key.": ItemClassification.progression,
    "A bonfire in the evening breeze; an Autumn jubilee.": ItemClassification.progression,

    #######Chapter 2 Fight#######
    "Pumpkin": ItemClassification.progression,
    "mmmphWORTHLESS mphIDIOT!": ItemClassification.progression,

    #######Chapter Select Unlocks######
    "New Game Select" : ItemClassification.progression,
    "Chapter 1 Select" : ItemClassification.progression,
    "Chapter 2 Select" : ItemClassification.progression,
    "Chapter 3 Select" : ItemClassification.progression

}

class GreatGodGroveItem(Item):
    game = "Great God Grove"

def get_random_filler_item_name(world: GreatGodGroveWorld) -> str:
    filler_array = ["Flotsam", "Junk", "Trash", "Jetsam", "P HERE!", "Tiny weak little bug.", "BARKBARKBARKBARK"]
    return "Flotsam"

def create_item_with_correct_classification(world: GreatGodGroveWorld, name: str) -> GreatGodGroveItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return GreatGodGroveItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: GreatGodGroveWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Flotsam"),
        world.create_item("Junk"),
        world.create_item("Trash"),
        world.create_item("Jetsam"),
        world.create_item("Love Letter"),
        world.create_item("Tiny weak little bug."),
        world.create_item("BARKBARKBARKBARK"),
        world.create_item("P HERE!"),
        world.create_item("I got a BIG OL' crush on you."),
        world.create_item("Get ready for pets, cutie pie!"),
        world.create_item("IT'S MEGAPON!"),
        world.create_item("GET TO WORK, YOU LAZY PUP!"),
        world.create_item("God and human, we can solve this mystery TOGETHA!"),
        world.create_item("Lay off and take a snack break! That's an order."),
        world.create_item("GOODY JOB ON THE GOODY WORK!"),
        world.create_item("Plank"),
        world.create_item("Toys"),
        world.create_item("DON'T WORRY MISSY! INSPEKTA WILL SAVE THE DAY!"),
        world.create_item("I miss what my eloquent KING had to say!"),
        world.create_item("With the power of communication, I can bring the gods together!"),
        world.create_item("I AM GOING TO EAT YOU."),

        #######CHAPTER 2#######
        world.create_item("I thought this place had barbeque. WHERE'S THE SMOKED HOG?"),
        world.create_item("Bork..."),
        world.create_item("Yip... yiyip"),
        world.create_item("ROUGHFFF!!!"),
        world.create_item("Wherf!!!"),
        world.create_item("Meow."),
        world.create_item("WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???"),
        world.create_item("Oh Bayker... I LOVE IT!"),
        world.create_item("If you ask me, Saul's just misunderstood."),
        world.create_item("That'll happen when pigs fly."),
        world.create_item("Cornelius"),
        world.create_item("Extra Crow"),
        world.create_item("Godpoke, go tell RAZZMA to draw something HEROIC for once."),
        world.create_item("TELL RAZZMA SHE'LL FOREVER LIVE IN THE SHADOW OF AN EVIL TYRANT!"),

        #######Chapter 2 Field#######
        world.create_item("Like for example, what if they had edible lipstick?"),
        world.create_item("I think edible lipstick would be the Bee's Cheese."),
        world.create_item("I... HATE that shaggy little man!"),
        world.create_item("BUT SAUL WILL SAVE US ALL!"),
        world.create_item("Hey there, handsome stranger!"),
        world.create_item("Oh Cappy, can I please have my name back?"),
        world.create_item("Hey vaquerito, go tell that DUMB BURRO Capochin to get a MOVE on!"),
        world.create_item("-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS."),

        world.create_item("Marmaline"),
        world.create_item("Gramma Boogie"),

        world.create_item("You know, I used to make milldreadberry jam for the whole town!"),

        #######Chapter 2 Bayker House#######
        world.create_item("HAAAACHHOOOOOOOOO!!!"),
        world.create_item("Lipstick Pie"),
        world.create_item("I thwear it on my life!!"),
        world.create_item("Pappy Pumpkin"),

        world.create_item("Milldreadberry Jam"),

        #######Chapter 2 Cobigail#######
        world.create_item("BOO!"),

        #######Chapter 2 School#######
        world.create_item("GET A HAIRCUT!"),

        #######Chapter 2 Underground#######
        world.create_item("The snacks are made of friendliness; the drinks are filled with glee."),
        world.create_item("Milldread Berry"),

        #######Chapter 2 Hide and Seek#######
        world.create_item("Our differences will bring us close, and Milldread we shall be."),
        world.create_item("Join your hands with anyone, sing in any key."),
        world.create_item("A bonfire in the evening breeze; an Autumn jubilee."),

        #######Chapter 2 Fight#######
        world.create_item("Pumpkin"),
        world.create_item("mmmphWORTHLESS mphIDIOT!"),

        #######Chapter Select Unlocks#######
        world.create_item("New Game Select"),
        world.create_item("Chapter 1 Select"),
        world.create_item("Chapter 2 Select"),
        world.create_item("Chapter 3 Select")



    ]

    if world.options.chapter_shuffle:
        chapter_items = [
            #######Chapter Select Unlocks#######
            world.create_item("New Game Select"),
            world.create_item("Chapter 1 Select"),
            world.create_item("Chapter 2 Select"),
            world.create_item("Chapter 3 Select")
        ]
        itempool += chapter_items

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]


    world.multiworld.itempool += itempool

    if world.options.chapter_shuffle:
        starting_chapter = "New Game Select"
        match world.options.starting_chapter:
            #case 0:
                #nothing needed here
            case 1:
                starting_chapter = "Chapter 1 Select"
            case 2:
                starting_chapter = "Chapter 2 Select"
            #case 3:
                #starting_chapter = "Chapter 3 Select"
        world.push_precollected(world.create_item(starting_chapter))
