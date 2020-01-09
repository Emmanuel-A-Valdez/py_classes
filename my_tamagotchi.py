import random


class Pet:
    hunger_threshold = 10
    boredom_threshold = 5
    hunger_decrement = 4
    boredom_decrement = 6
    sounds = ["Mrrp"]
    # known_words = []

    def __init__(self, name="Kitkat"):
        self.name = name
        self.hunger = random.randrange(self.hunger_threshold)
        self.boredom = random.randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    def mood(self):
        if self.boredom > self.boredom_threshold:
            return "bored"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "happy"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def hi(self):
        print(self.sounds[random.randrange(len(self.sounds))])
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


# import sys

# sys.setExecutionLimit(60000)


def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None  # no pet matched


def play():
    animals = []

    # option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback += "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()


play()
