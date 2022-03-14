import constants
import random
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        if self._keyboard_service.is_key_down('j') or self._keyboard_service.is_key_down('l') or self._keyboard_service.is_key_down('i') or self._keyboard_service.is_key_down('k'):
            snake = cast.get_first_actor("snakes")
            snake.turn_head(self._direction)
        
        if self._keyboard_service.is_key_down('a') or self._keyboard_service.is_key_down('s') or self._keyboard_service.is_key_down('d') or self._keyboard_service.is_key_down('w'):
            snake_2 = cast.get_first_actor("snakes_2")
            snake_2.turn_head(self._direction)

    # def execute_2(self, cast, script):
    #     """Executes the control actors action.

    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #         script (Script): The script of Actions in the game.
    #     """
    #     # left
    #     if self._keyboard_service.is_key_down('a'):
    #         self._direction = Point(-constants.CELL_SIZE, 0)
        
    #     # right
    #     if self._keyboard_service.is_key_down('d'):
    #         self._direction = Point(constants.CELL_SIZE, 0)
        
    #     # up
    #     if self._keyboard_service.is_key_down('w'):
    #         self._direction = Point(0, -constants.CELL_SIZE)
        
    #     # down
    #     if self._keyboard_service.is_key_down('s'):
    #         self._direction = Point(0, constants.CELL_SIZE)
        
    #     snake_2 = cast.get_first_actor("snakes_2")
    #     snake_2.turn_head(self._direction)