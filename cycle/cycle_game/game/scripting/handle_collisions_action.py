import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0
        self.num = 0
        self.num2 = 10

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        snake_2 = cast.get_first_actor("snakes_2")
        head_2 = snake_2.get_segments()[0]
        segments_2 = snake_2.get_segments()[1:]
        
        self.num += 1
        if self.num >= self.num2:
            snake.grow_tail(1)
            snake_2.grow_tail(1)
            self.num2 += 25

        for segment in segments:
            if head_2.get_position().close_enough(segment.get_position()):
                self._is_game_over = True
                self._winner = 2
        
        for segment in segments_2:
            if head.get_position().close_enough(segment.get_position()):
                self._is_game_over = True
                self._winner = 1
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            snake_2 = cast.get_first_actor("snakes_2")
            segments = snake.get_segments()
            segments_2 = snake_2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            if self._winner == 1:
                message = Actor()
                message.set_text("Game Over! Red wins")
                message.set_position(position)
                cast.add_actor("messages", message)
                for segment in segments:
                    segment.set_color(constants.WHITE)

            if self._winner == 2:
                message = Actor()
                message.set_text("Game Over! Green wins")
                message.set_position(position)
                cast.add_actor("messages", message)
                for segment in segments_2:
                    segment.set_color(constants.WHITE)

