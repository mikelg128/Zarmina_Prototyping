import tcod

MOVE_KEYS = {  # key_symbol: (x, y)
    # Arrow keys.
    tcod.event.K_LEFT: (-1, 0),
    tcod.event.K_RIGHT: (1, 0),
    tcod.event.K_UP: (0, -1),
    tcod.event.K_DOWN: (0, 1),
    tcod.event.K_HOME: (-1, -1),
    tcod.event.K_END: (-1, 1),
    tcod.event.K_PAGEUP: (1, -1),
    tcod.event.K_PAGEDOWN: (1, 1),
    tcod.event.K_PERIOD: (0, 0),
    # Numpad keys.
    tcod.event.K_KP_1: (-1, 1),
    tcod.event.K_KP_2: (0, 1),
    tcod.event.K_KP_3: (1, 1),
    tcod.event.K_KP_4: (-1, 0),
    tcod.event.K_KP_5: (0, 0),
    tcod.event.K_KP_6: (1, 0),
    tcod.event.K_KP_7: (-1, -1),
    tcod.event.K_KP_8: (0, -1),
    tcod.event.K_KP_9: (1, -1),
    tcod.event.K_CLEAR: (0, 0),  # Numpad `clear` key.
    # Vi Keys.
    tcod.event.K_h: (-1, 0),
    tcod.event.K_j: (0, 1),
    tcod.event.K_k: (0, -1),
    tcod.event.K_l: (1, 0),
    tcod.event.K_y: (-1, -1),
    tcod.event.K_u: (1, -1),
    tcod.event.K_b: (-1, 1),
    tcod.event.K_n: (1, 1),
}


class State(tcod.event.EventDispatch[None]):
    """A state-based superclass that converts `events` into `commands`.

    The configuration used to convert events to commands are hard-coded
    in this example, but could be modified to be user controlled.

    Subclasses will override the `cmd_*` methods with their own
    functionality.  There could be a subclass for every individual state
    of your game.
    """

    def ev_quit(self, event: tcod.event.Quit) -> None:
        """The window close button was clicked or Alt+F$ was pressed."""
        print(event)
        self.cmd_quit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        """A key was pressed."""
        print(event)
        if event.sym in MOVE_KEYS:
            # Send movement keys to the cmd_move method with parameters.
            self.cmd_move(*MOVE_KEYS[event.sym])
        elif event.sym == tcod.event.K_ESCAPE:
            self.cmd_escape()

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> None:
        """The window was clicked."""
        print(event)

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        """The mouse has moved within the window."""
        print(event)

    def cmd_move(self, x: int, y: int) -> None:
        """Intent to move: `x` and `y` is the direction, both may be 0."""
        print("Command move: " + str((x, y)))

    def cmd_escape(self) -> None:
        """Intent to exit this state."""
        print("Command escape.")
        self.cmd_quit()

    def cmd_quit(self) -> None:
        """Intent to exit the game."""
        print("Command quit.")
        raise SystemExit()