from src.utils import normalize_title
from src.types_example import get_value_types
from src.greetings import greet

if __name__ == "__main__": 

    print(f"What TaskMate – Hello, {normalize_title('world')}!")


    for value, typ in get_value_types():
        print(value, typ)
        


    print(greet("world"))    
