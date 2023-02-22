import abc

class Duck(abc.ABC):
    def __init__(self):
        pass

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    def fly(self):
        return self.fly_behavior.fly()

    def quack(self):
        return self.quack_behavior.quack()

    def swim(self):
        return "All ducks float, even decoys!"

class FlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class QuackBehavior(abc.ABC):
    @abc.abstractmethod
    def quack(self):
        pass
