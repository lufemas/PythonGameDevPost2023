
from enum import Enum

class Game:
    class State(Enum):
      NONE      = 0
      MAINMENU  = 1
      PAUSE     = 2
      DEV       = 9
      TEST      = 10

    stateStack = [State.NONE, State.DEV]

    @staticmethod
    def popState():
      print('Finished State: ', Game.currentState());
      Game.stateStack.pop();
      print('Current State: ', Game.currentState());

    @staticmethod
    def appendState(state):
      print('Appeding State: ', state);
      Game.stateStack.append(state);
      print('Current State: ', Game.currentState());

    @staticmethod
    def currentState():
      return Game.stateStack[-1]
