from pyrustic.app import App
from rustiql.misc.builder import MainViewBuilder
from rustiql.misc import my_theme


def main():
    # The App
    app = App()
    # Title
    app.title = "Rustiql"
    # Geometry
    app.geometry = "900x550+0+0"
    # Resizable
    app.resizable = (False, False)
    # Set theme
    app.theme = my_theme.get_theme()
    # Set view
    app.view = MainViewBuilder().build(app)
    # Center the window
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()
