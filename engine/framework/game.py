"""
configurations = {
    "size": int,
    "intensity": float,
    "configs": {
        # for 2P games
        "R" : float,
        "S" : float,
        "T" : float,
        "P" : float
    }
}
"""


class Game:
    def __init__(self, game_configurations):
        self.Z = game_configurations["size"]
        self.configs = game_configurations["configs"]

    def fitnessC(self):
        pass

    def fitnessD(self):
        return

    def Gradient(self):
        return self.fitnessC() - self.fitnessD()


class Game2P(Game):
    def __init__(self, game_configurations):
        super().__init__(game_configurations)
        self.R = self.configs["R"]
        self.S = self.configs["S"]
        self.T = self.configs["T"]
        self.P = self.configs["P"]

    def fitnessC(self):
        pass

    def fitnessD(self):
        pass

    def fitnessCD(self):
        pass


class HarmonyGame(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class PrisonersDilemma(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class SnowdriftGame(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class StagHunt(Game2P):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class GameNP(Game):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class NSnowdriftGame(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class NStagHunt(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class PublicGoodGames(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)


class CollectiveRiskDilemma(GameNP):
    def __init__(self, game_specs):
        super().__init__(game_specs)
