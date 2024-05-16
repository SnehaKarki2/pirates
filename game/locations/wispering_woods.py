from game import location
import game.config as config
from game.display import announce
from game.events import *
from game.items import Item
import random
import numpy
from game import event
from game.combat import Monster
import game.combat as combat
from game.display import menu


class WhisperingWoods(location.Location):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.name = "Whispering Woods"
        self.symbol = "W"
        self.visitable = True
        self.starting_location = MoonglowGlade(self)
        self.locations = {
            "moonglowglade": self.starting_location,
            "whisperingwillows": WhisperingWillows(self),
            "forgottenruins": ForgottenRuins(self),
            "enchantedsprings": EnchantedSprings(self),
            "shadowthornthicket": ShadowthornThicket(self),
        }

    def enter(self, ship):
        announce(
            "You arrive at the mysterious island of Whispering Woods. A dense forest looms before you, its trees swaying gently in the breeze, as if whispering secrets of old. The island is known for its enchanted groves, ancient ruins, and magical springs. Legends speak of powerful artifacts hidden within its depths, guarded by ancient puzzles and mythical creatures. Beware the magic that lingers, for it can be both a blessing and a curse."
        )

    def visit(self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()


class Puzzle:
    def __init__(self, description, solution):
        self.description = description
        self.solution = solution

    def solve(self, player_solution):
        return player_solution.lower() == self.solution.lower()


class MoonglowGlade(location.SubLocation):
    def __init__(self, mainlocation):
        super().__init__(mainlocation)
        self.name = "moonglowglade"
        self.verbs["north"] = self
        self.verbs["moonglowglade"] = self
        self.verbs["whisperingwillows"] = self
        self.verbs["forgottenruins"] = self
        self.verbs["enchantedsprings"] = self
        self.verbs["shadowthornthicket"] = self
        self.verbs["enter"] = self
        self.description_printed = False
        self.puzzle = Puzzle(
            "A mysterious inscription reads: 'What walks on four legs in the morning, two legs in the afternoon, and three legs in the evening?'",
            "human",
        )

        self.event_chance = 25
        self.events.append(seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(man_eating_monkeys.ManEatingMonkeys())

    def enter(self):
        if not self.description_printed:
            announce(
                "You enter the Moonglow Glade, a mystical clearing bathed in an ethereal light. The glade is said to hold the key to unlocking the secrets of the island."
            )
            self.puzzle_encounter()

        self.description_printed = True
        announce("You already completed exploring this location")

    def puzzle_encounter(self):
        announce(self.puzzle.description)
        player_solution = input("Enter your answer: ")
        if self.puzzle.solve(player_solution):
            announce(
                "Correct! The glade reveals its secrets to you. You find an ancient map that marks the locations of hidden treasures scattered throughout the island."
            )
        else:
            announce(
                "Incorrect. The glade remains silent, and its secrets remain hidden."
            )

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            announce("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False

        elif verb == "moonglowglade":
            config.the_player.next_loc = self.main_location.locations["moonglowglade"]

        elif verb == "whisperingwillows":
            config.the_player.next_loc = self.main_location.locations[
                "whisperingwillows"
            ]

        elif verb == "forgottenruins":
            config.the_player.next_loc = self.main_location.locations["forgottenruins"]

        elif verb == "enchantedsprings":
            config.the_player.next_loc = self.main_location.locations[
                "enchantedsprings"
            ]

        elif verb == "shadowthornthicket":
            config.the_player.next_loc = self.main_location.locations[
                "shadowthornthicket"
            ]


class WhisperingWillows(location.SubLocation):
    def __init__(self, mainlocation):
        super().__init__(mainlocation)
        self.name = "whisperingwillows"
        self.verbs["moonglowglade"] = self
        self.verbs["whisperingwillows"] = self
        self.verbs["forgottenruins"] = self
        self.verbs["enchantedsprings"] = self
        self.verbs["shadowthornthicket"] = self
        self.verbs["enter"] = self
        self.description_printed = False
        self.puzzle = Puzzle(
            "The willows whisper a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'",
            "echo",
        )

        self.event_chance = 25
        self.events.append(seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(man_eating_monkeys.ManEatingMonkeys())

    def enter(self):
        if not self.description_printed:
            announce(
                "You find yourself amidst the Whispering Willows, where the trees seem to murmur ancient secrets. It is said that those who decipher the willows' riddle gain insight into the island's past."
            )
            self.puzzle_encounter()

        self.description_printed = True
        announce("You already completed exploring this location")

    def puzzle_encounter(self):
        announce(self.puzzle.description)
        player_solution = input("Enter your answer: ")
        if self.puzzle.solve(player_solution):
            announce(
                "Correct! The willows reveal a piece of the island's history to you. You learn of an ancient civilization that once thrived here, possessing great knowledge and power."
            )
        else:
            announce(
                "Incorrect. The willows fall silent, and the island's past remains a mystery."
            )

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "moonglowglade":
            config.the_player.next_loc = self.main_location.locations["moonglowglade"]

        elif verb == "whisperingwillows":
            config.the_player.next_loc = self.main_location.locations[
                "whisperingwillows"
            ]

        elif verb == "forgottenruins":
            config.the_player.next_loc = self.main_location.locations["forgottenruins"]

        elif verb == "enchantedsprings":
            config.the_player.next_loc = self.main_location.locations[
                "enchantedsprings"
            ]

        elif verb == "shadowthornthicket":
            config.the_player.next_loc = self.main_location.locations[
                "shadowthornthicket"
            ]


class ForgottenRuins(location.SubLocation):
    def __init__(self, mainlocation):
        super().__init__(mainlocation)
        self.name = "forgottenruins"
        self.verbs["moonglowglade"] = self
        self.verbs["whisperingwillows"] = self
        self.verbs["forgottenruins"] = self
        self.verbs["enchantedsprings"] = self
        self.verbs["shadowthornthicket"] = self
        self.verbs["enter"] = self
        self.description_printed = False
        self.puzzle = Puzzle(
            "In the center of the ruins, you find an ancient mechanism with symbols. The inscription reads: 'Align the symbols in the order of the cycle of life: birth, growth, decay, and rebirth.'",
            "birth growth decay rebirth",
        )

        self.event_chance = 25
        self.events.append(seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(man_eating_monkeys.ManEatingMonkeys())

    def enter(self):
        if not self.description_printed:
            announce(
                "You stumble upon the Forgotten Ruins, the remnants of an ancient civilization. The crumbling structures hold secrets waiting to be uncovered."
            )
            self.puzzle_encounter()

        self.description_printed = True
        announce("You already completed exploring this location")

    def puzzle_encounter(self):
        announce(self.puzzle.description)
        player_solution = input(
            "Enter the correct order of symbols (separated by spaces): "
        )
        if self.puzzle.solve(player_solution):
            announce(
                "Correct! The mechanism clicks into place, revealing a hidden chamber. Inside, you find an ancient artifact imbued with powerful magic."
            )
        else:
            announce(
                "Incorrect. The mechanism remains locked, and the secrets of the ruins elude you."
            )

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "moonglowglade":
            config.the_player.next_loc = self.main_location.locations["moonglowglade"]

        elif verb == "whisperingwillows":
            config.the_player.next_loc = self.main_location.locations[
                "whisperingwillows"
            ]

        elif verb == "forgottenruins":
            config.the_player.next_loc = self.main_location.locations["forgottenruins"]

        elif verb == "enchantedsprings":
            config.the_player.next_loc = self.main_location.locations[
                "enchantedsprings"
            ]

        elif verb == "shadowthornthicket":
            config.the_player.next_loc = self.main_location.locations[
                "shadowthornthicket"
            ]


class EnchantedSprings(location.SubLocation):
    def __init__(self, mainlocation):
        super().__init__(mainlocation)
        self.name = "enchantedsprings"
        self.verbs["moonglowglade"] = self
        self.verbs["whisperingwillows"] = self
        self.verbs["forgottenruins"] = self
        self.verbs["enchantedsprings"] = self
        self.verbs["shadowthornthicket"] = self
        self.verbs["enter"] = self
        self.description_printed = False
        self.puzzle = Puzzle(
            "At the heart of the springs, a shimmering pool bears an inscription: 'Reflect on the virtues that bring balance: courage, wisdom, compassion, and humility. Choose the one that resonates with your spirit.'",
            "wisdom",
        )

        self.event_chance = 25
        self.events.append(seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(man_eating_monkeys.ManEatingMonkeys())

    def enter(self):
        if not self.description_printed:
            announce(
                "You come across the Enchanted Springs, a series of crystal-clear pools that radiate with magical energy. The springs are known to grant blessings to those who demonstrate virtue."
            )
            self.puzzle_encounter()

        self.description_printed = True
        announce("You already completed exploring this location")

    def puzzle_encounter(self):
        announce(self.puzzle.description)
        player_solution = input(
            "Enter your choice (courage/wisdom/compassion/humility): "
        )
        if self.puzzle.solve(player_solution):
            announce(
                "As you reflect on wisdom, the springs glow with a warm light. You feel a surge of mental clarity and insight, enhancing your ability to navigate the island's challenges."
            )
        else:
            announce(
                "The springs remain still, and no blessings are bestowed upon you."
            )

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "moonglowglade":
            config.the_player.next_loc = self.main_location.locations["moonglowglade"]

        elif verb == "whisperingwillows":
            config.the_player.next_loc = self.main_location.locations[
                "whisperingwillows"
            ]

        elif verb == "forgottenruins":
            config.the_player.next_loc = self.main_location.locations["forgottenruins"]

        elif verb == "enchantedsprings":
            config.the_player.next_loc = self.main_location.locations[
                "enchantedsprings"
            ]

        elif verb == "shadowthornthicket":
            config.the_player.next_loc = self.main_location.locations[
                "shadowthornthicket"
            ]


class ShadowthornThicket(location.SubLocation):
    def __init__(self, mainlocation):
        super().__init__(mainlocation)
        self.name = "shadowthornthicket"
        self.verbs["moonglowglade"] = self
        self.verbs["whisperingwillows"] = self
        self.verbs["forgottenruins"] = self
        self.verbs["enchantedsprings"] = self
        self.verbs["shadowthornthicket"] = self
        self.verbs["enter"] = self
        self.description_printed = False
        self.puzzle = Puzzle(
            "In the heart of the thicket, a twisted tree bears an enigmatic engraving: 'Embrace the shadow within, for it is a part of your destiny. Speak the words that acknowledge your inner darkness.'",
            "i embrace my shadow",
        )

        self.event_chance = 25
        self.events.append(seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())
        self.events.append(man_eating_monkeys.ManEatingMonkeys())

    def enter(self):
        if not self.description_printed:
            announce(
                "You venture into the Shadowthorn Thicket, a dense and foreboding area. The shadows seem to whisper, tempting you to delve deeper into the darkness."
            )
            self.puzzle_encounter()

        self.description_printed = True
        announce("You already completed exploring this location")

    def puzzle_encounter(self):
        announce(self.puzzle.description)
        player_solution = input("Speak the words: ")
        if self.puzzle.solve(player_solution):
            announce(
                "As you utter the words, the shadows swirl around you, revealing a hidden path. You feel a sense of clarity and purpose, ready to face the challenges that lie ahead."
            )
        else:
            announce(
                "The shadows remain silent, and the thicket's secrets remain unresolved."
            )

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "moonglowglade":
            config.the_player.next_loc = self.main_location.locations["moonglowglade"]

        elif verb == "whisperingwillows":
            config.the_player.next_loc = self.main_location.locations[
                "whisperingwillows"
            ]

        elif verb == "forgottenruins":
            config.the_player.next_loc = self.main_location.locations["forgottenruins"]

        elif verb == "enchantedsprings":
            config.the_player.next_loc = self.main_location.locations[
                "enchantedsprings"
            ]

        elif verb == "shadowthornthicket":
            config.the_player.next_loc = self.main_location.locations[
                "shadowthornthicket"
            ]