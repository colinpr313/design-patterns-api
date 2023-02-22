from design_patterns_api.strategy_pattern.base_classes import Duck
import design_patterns_api.strategy_pattern.fly_classes as fb
import design_patterns_api.strategy_pattern.quack_class as qb

class MallardDuck(Duck):
    def __init__(self):
        self.name = "mallard duck"

        fly_instance = fb.Fly()
        quack_instance = qb.Quack()

        self.set_fly_behavior(fly_instance)
        self.set_quack_behavior(quack_instance)

class ModelDuck(Duck):
    def __init__(self):
        self.name ="model duck"

        fly_instance = fb.FlyNoWay()
        quack_instance = qb.SqueakQuack()

        self.set_fly_behavior(fly_instance)
        self.set_quack_behavior(quack_instance)

class DecoyDuck(Duck):
    def __init__(self):
        self.name = "decoy duck"

        fly_instance = fb.FlyRocketPowered()
        quack_instance = qb.MuteQuack()

        self.set_fly_behavior(fly_instance)
        self.set_quack_behavior(quack_instance)


