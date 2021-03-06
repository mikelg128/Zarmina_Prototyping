import tcod
import event_handling


class Engine:
    def __init__(self):
        self.WIDTH = 80
        self.HEIGHT = 60

        # Load font as tileset:
        self.tileset = tcod.tileset.load_tilesheet('assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
        self.console = tcod.Console(self.WIDTH, self.HEIGHT, order='F')
        self.event_dispatch = event_handling.State()

    def play_game(self):
        with tcod.context.new_terminal(columns=self.console.width, rows=self.console.height, tileset=self.tileset) \
                as context:
            while True:
                self.console.clear()
                self.console.print(x=0, y=0, string="Hello World")
                context.present(self.console)

                for event in tcod.event.wait():
                    context.convert_event(event)
                    print(event)
                    self.event_dispatch.dispatch(event)


def main() -> None:
    zarmina = Engine()
    zarmina.play_game()


if __name__ == "__main__":
    main()
