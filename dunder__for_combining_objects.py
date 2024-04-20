# from typing import Self

class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name 
        self.grams = grams
    
    def __format__(self, format_spec: str) -> str:
        """for using with {fruit_inst: "kg"}"""
        match format_spec:
            case "kg":
                return f"{self.grams / 1000}"
            case "lb":
                return f"{self.grams / 453.5924}"
            case "desc":
                return f"{self.grams}g of {self.name}"
            case _:
                raise ValueError("that value is not a valid weight unit string")
    
    def __or__(self, other: "Fruit"):
        new_name: str = f"{self.name} & {other.name}"
        new_grams: float = self.grams + other.grams

        return Fruit(name=new_name, grams=new_grams)
    
    def __repr__(self):
        """gives a representation like a dataclass would"""
        return f"Fruit(name={self.name}, grams={self.grams})"


def main():
    apple: Fruit = Fruit(name="Apple", grams=2500)
    orange = Fruit(name="orange", grams=100)
    banana = Fruit(name="Banana", grams=5000)

    combined = apple | orange | banana
    print(combined)

if __name__ == "__main__":
    main()



        