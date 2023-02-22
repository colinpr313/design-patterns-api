from design_patterns_api.strategy_pattern.base_classes import QuackBehavior

class Quack(QuackBehavior):
    def quack(self):
        return "Quack"

class MuteQuack(QuackBehavior):
    def quack(self):
        return "<<Silence>>"

class SqueakQuack(QuackBehavior):
    def quack(self):
        return "Squeak"