from pyrustic.app import App
from rustiql.misc.builder import MainViewBuilder
from rustiql.misc import my_theme


def main():
    app = App(__package__)
    app.root.title("Rustiql - Pyrustic SQL Editor")
    app.theme = my_theme.get_theme()
    app.view = MainViewBuilder().build(app)
    app.center()
    app.start()


if __name__ == "__main__":
    main()
