class GamingConsole:

    def __init__(self, name="Example", color="white"):
        self.color = "white"

        self.name = name


class PlayStation(GamingConsole):

    def __init__(self, version="4", newGames=True):
        self.new_games = newGames

        self.version = version

    def play(self):
        print("The game has started")


gaming_console = GamingConsole("Nintendo")

print(gaming_console.color)

print(gaming_console.name)

ps5 = PlayStation("5")

print(ps5.version)

print(ps5.play())
