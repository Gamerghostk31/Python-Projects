class Animal:
    
    def __init__(self, name, type, sound, size):
        self.name = name
        self.type = type
        self.sound = sound
        self.size = size
    
    def __repr__(self) -> str:
        description = f"""
This is {self.name}, it is a {self.type}. The sound that {self.name} makes is {self.sound}. {self.name} is a {self.size} {self.type}
        """
        return description

def main():
    fido = Animal("Fido", "dog", "woof", "large")
    print(fido)

if __name__ == '__main__':
    main()
