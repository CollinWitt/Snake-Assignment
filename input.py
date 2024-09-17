import threading
import readchar

class InputHandler:
    # Handles console inputs using readchar. 
    # Any character typed into the console will be stored without enter being pressed.

    def __init__(self) -> None:
        self._lastCharacter = ""
        self._running = False

    def _handleInputs(self):
        while self._running:
            self._lastCharacter = readchar.readchar()
        
    def start(self):
        # Starts listening for inputs.
        inputThread = threading.Thread(target=self._handleInputs)
        self._running = True
        inputThread.start()

    def stop(self):
        # Stops listening for inputs.
        self._running = False

    def isRunning(self):
        # Returns if the handler is running.
        return self._running

    def getLastKeyPress(self):
        # Returns the last character the user typed into the console.
        return self._lastCharacter

    