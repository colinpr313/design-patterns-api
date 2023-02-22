from design_patterns_api.strategy_pattern.base_classes import FlyBehavior

class Fly(FlyBehavior):
    def fly(self):
        return "I'm flying!"

class FlyNoWay(FlyBehavior):
    def fly(self):
        return "I can't fly :("

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        return "I'm flying with a rocket!"

