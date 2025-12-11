from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class ChapterShuffle(Toggle):
    """
    Shuffles chapters from the chapter select into the pool as AP Items.
    Reaching each chapter is a location.
    You still unlock a chapter's chapter select by reaching it normally.
    """

    display_name = "Chapter Shuffle"

class StartingChapter(Choice):
    """
    The starting chapter for playing the game. Only matters with chapter shuffle enabled.
    """

    display_name = "Starting Chapter"

    option_new_game = 0
    option_chapter_1 = 1
    option_chapter_2 = 2
    #chapter_3 = 3
    #chapter_4 = 4
    #chapter_5 = 5

    # Choice options must define an explicit default value.
    default = option_new_game




@dataclass
class GreatGodGroveOptions(PerGameCommonOptions):
    chapter_shuffle: ChapterShuffle
    starting_chapter: StartingChapter