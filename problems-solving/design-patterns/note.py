class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print_ingredients(self):
        print(self.ingredients)


class BurgerFactory:
    def creteCheeseBurger(self):
        ingridients = ["cheese", "meat", "bread"]
        return Burger(ingridients)

    def createVeggieBurger(self):
        ingridients = ["tomato", "cucumber", "bread"]
        return Burger(ingridients)

    def createFishBurger(self):
        ingridients = ["fish", "bread"]
        return Burger(ingridients)


if __name__ == "__main__":
    burger_factory = BurgerFactory()
    cheese_burger = burger_factory.creteCheeseBurger()
    cheese_burger.print_ingredients()


class Burger:
    def __init__(self, ingredients):
        self.buns = None
        self.patties = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatties(self, patties):
        self.patties = patties

    def setCheese(self, cheese):
        self.cheese = cheese


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addPatties(self, patties):
        self.burger.setPatties(patties)
        return self

    def addCheese(self, cheese):
        self.burger.setCheese(cheese)
        return self

    def build(self):
        return self.burger


if __name__ == "__main__":
    burger_builder = BurgerBuilder()
    burger = (
        burger_builder.addBuns("sesame")
        .addPatties("chicken")
        .addCheese("cheddar")
        .build()
    )


class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if ApplicationState.instance == None:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)
appState2 = ApplicationState.getAppState()
appState2.isLoggedIn = True

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)
