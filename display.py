import snake

class Image:
    # Stores and displays console images.

    def __init__(self,width: int,height: int,defaultCharacter: str="#"):
        # Create a image of given width and height filled with default character.

        self.image: list[list[str]] = []
        self.width = width
        self.height = height

        # create 2d array of characters
        for __ in range(height):
            line = []
            for __ in range(width):
                line.append(defaultCharacter)
            self.image.append(line)
    
    def display(self, padding=" "):
        # Prints current image to console.

        for line in self.image:
            for character in line:
                print(padding + character, end="")
            print()

    def fill(self, character: str):
        # Fills whole image with single charcter

        # redo defualt image generation with new character
        self.image = []
        for __ in range(self.height):
            line = []
            for __ in range(self.width):
                line.append(character)
            self.image.append(line)
    
    def set(self, location: tuple[int], character: str):
        # Sets pixel character.

        x = location[0]
        y = location[1]
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            self.image[y][x] = character

    def drawSnake(self, snake: snake.Snake, character: str):
        # TODO: finish this function
        pass
