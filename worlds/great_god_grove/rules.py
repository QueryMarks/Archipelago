from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import GreatGodGroveWorld


def set_all_rules(world: GreatGodGroveWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: GreatGodGroveWorld) -> None:
    new_game_to_chapter_1_start = world.get_entrance("New Game to Chapter 1 Start")

    def can_start_game(state: CollectionState) -> bool:
        return True

    set_rule(new_game_to_chapter_1_start, can_start_game)

def set_all_location_rules(world: GreatGodGroveWorld) -> None:

    big_ol_crush = world.get_location("I got a BIG OL' crush on you.")

    add_rule(
        big_ol_crush,
        lambda state: (
            state.has("Love Letter", world.player)
        )
    )

    ready_for_pets = world.get_location("Get ready for pets, cutie pie!")
    add_rule(
        ready_for_pets,
        lambda state: (
            state.has("Love Letter", world.player)
        )
    )

    snack_break = world.get_location("Lay off and take a snack break! That's an order.")
    add_rule(
        snack_break,
        lambda state: (
            state.has("God and human, we can solve this mystery TOGETHA!", world.player)
        )
    )

    good_job = world.get_location("GOODY JOB ON THE GOODY WORK!")
    add_rule(
        good_job,
        lambda state: (
            state.has("God and human, we can solve this mystery TOGETHA!", world.player)
        )
    )

    eat_you = world.get_location("I AM GOING TO EAT YOU.")
    add_rule(
        eat_you,
        lambda state: (
            state.has("I miss what my eloquent KING had to say!", world.player)
        )
    )

    #######CHAPTER 2 RULES##############

    #######Chapter 2 Start#######
    wantsToWorkWithBayker = world.get_location("Oh Bayker... I LOVE IT!")
    add_rule(
        wantsToWorkWithBayker,
        lambda state: (
            state.has("Lipstick Pie", world.player)
        )
    )

    saulComplimentGoody = world.get_location("If you ask me, Saul's just misunderstood.")
    add_rule(
        saulComplimentGoody,
        lambda state: (
            state.has("ROUGHFFF!!!", world.player)
            and
            (
                state.has("Cornelius", world.player)
                or state.has("Marmaline", world.player)
                or state.has("Gramma Boogie", world.player)
                or state.has("Extra Crow", world.player)
            )
        )
    )

    pigsFly = world.get_location("That'll happen when pigs fly.")
    add_rule(
        pigsFly,
        lambda state: (
                state.has("ROUGHFFF!!!", world.player)
                and
                (
                        state.has("Cornelius", world.player)
                        or state.has("Marmaline", world.player)
                        or state.has("Gramma Boogie", world.player)
                        or state.has("Extra Crow", world.player)
                )
                and state.has("Lipstick Pie", world.player)
        )
    )



    cornelius = world.get_location("Cornelius")
    add_rule(
        cornelius,
        lambda state: (
            state.has("BOO!", world.player)
        )
    )

    extra_crow = world.get_location("Extra Crow")
    add_rule(
        extra_crow,
        lambda state: (
            state.has("BOO!", world.player)
        )
    )

    #######Chapter 2 Field#######
    razz_insult_2 = world.get_location("-TELL CAPO HE'S AS HEROIC AS KING'S TOENAIL CLIPPINGS.")
    add_rule(
        razz_insult_2,
        lambda state: (
            state.has("Godpoke, go tell RAZZMA to draw something HEROIC for once.", world.player)
        )
    )
    marmaline = world.get_location("Marmaline")
    add_rule(
        marmaline,
        lambda state: (
            state.has("BOO!", world.player)
        )
    )

    gramma_boogie = world.get_location("Gramma Boogie")
    add_rule(
        gramma_boogie,
        lambda state: (
            state.has("BOO!", world.player)
        )
    )

    used_to_make_jam = world.get_location("You know, I used to make milldreadberry jam for the whole town!")
    add_rule(
        used_to_make_jam,
        lambda state: (
            state.has("Milldread Berry", world.player)
        )
    )

    #######Chapter 2 Bayker#######
    lipstick_pie = world.get_location("Lipstick Pie")
    add_rule(
        lipstick_pie,
        lambda state: (
            state.has("Like for example, what if they had edible lipstick?", world.player)
            and
            state.has("WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???", world.player)
        )
    )

    promise = world.get_location("I thwear it on my life!!")
    add_rule(
        promise,
        lambda state: (
            state.has("Oh Bayker... I LOVE IT!", world.player)
            and
            state.has("Like for example, what if they had edible lipstick?", world.player)
            and
            state.has("WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???", world.player)
        )
    )
    pappy_pumpkin = world.get_location("Pappy Pumpkin")
    add_rule(
        pappy_pumpkin,
        lambda state: (
            state.has("Oh Bayker... I LOVE IT!", world.player)
            and state.has("Like for example, what if they had edible lipstick?", world.player)
            and state.has("WON'T SOMEONE SMASH THE SCHOOL DOOR WITH THE HEAVIEST THING THEY GOT???", world.player)
        )
    )

    milldreadberry_jam = world.get_location("Milldreadberry Jam")
    add_rule(
        milldreadberry_jam,
        lambda state: (
            state.has("Milldread Berry", world.player)
            and state.has("You know, I used to make milldreadberry jam for the whole town!", world.player)
        )
    )

    #######no checks require rules in school or cobigail#######

    #######Chapter 2 Underground#######
    milldread_berry = world.get_location("Milldread Berry")
    add_rule(
        milldread_berry,
        lambda state: (
            state.has("The snacks are made of friendliness; the drinks are filled with glee.", world.player)
            and state.has("Our differences will bring us close, and Milldread we shall be.", world.player)
            and state.has("Join your hands with anyone, sing in any key.", world.player)
            and state.has("A bonfire in the evening breeze; an Autumn jubilee.", world.player)
        )
    )

    #######no checks require rules in hide and seek#######

    #######Chapter 2 Fight#######
    goon_insult = world.get_location("mmmphWORTHLESS mphIDIOT!")
    add_rule(
        goon_insult,
        lambda state: (
            state.has("Pumpkin", world.player)
            #or state.has("Bonky Rock", world.player)
        )
    )



    finish = world.get_location("FINISH")

    add_rule(
        finish,
        lambda state: (
            state.has("With the power of communication, I can bring the gods together!", world.player)
            and state.has("God and human, we can solve this mystery TOGETHA!", world.player)
            and state.has("Milldreadberry Jam", world.player)
        )
    )

def set_completion_condition(world: GreatGodGroveWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)