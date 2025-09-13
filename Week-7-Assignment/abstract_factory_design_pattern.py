from abc import ABC, abstractmethod

#Week 7 - Activity 3 (part 3): Factory design pattern - Update code
#Update code in Week7 - activity 3 (part2) with adding one more shape, "Triangle" to your code. 
#Then explain the difference between using the Factory Design Pattern and not using it,
#to demonstrate the value of the pattern. Include notes on which lines you added to your code and why. Share your GitHub link.
 
# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass


# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"
    
class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"
    
    
# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle
    }

    @classmethod
    def register(cls, name: str, shape_cls: type[Shape]) -> None:
        """Optionally register new shapes without modifying factory code."""
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())  
    
    triangle = factory.create("Triangle")
    print(triangle.draw())
    
    # My understanding into this code --->
   # Here, ABC is nothing but a abstract base class that is like interface/ in java, here the role of Shape(ABC) 
   # is all subclasses of Shape have to implement its method abstractmethod draw() and then factory is registering each subclasses
   # with key as shape string and when create() method of shape class is created, it is just fetching the instance of subclass from
   # registry of map, later we are drawing a shape from an object of subclass.