import utils
import webbrowser

from pystray import Icon, Menu, MenuItem
from configuration import ConfigFile, ConfigNode


class ZoomerApp:
    def __init__(self, app_name='Zoomer'):
        self.config = ConfigFile(name='ZoomLinks')
        self.icon = Icon(app_name, icon=utils.create_image(), menu=self.make_menu())
        self.state = False

    def make_menu(self):
        links_dict = self.config.get_dict_node(ConfigNode.LINKS)
        menus = ()
        for key in links_dict:
            menus = menus + (MenuItem(
                key,
                self.make_action(key, links_dict[key]),
                checked=None
            ),)
        menus = menus + (MenuItem(
            'Quit',
            self.quit_app,
            checked=None
        ),)
        menu = Menu(*menus)
        return menu

    def quit_app(self):
        self.icon.stop()

    def start(self):
        self.icon.run()

    @staticmethod
    def make_action(title='title', link='link'):
        def action():
            ZoomerApp.open_link(link)
        return action

    @staticmethod
    def open_link(link):
        if link is not None:
            webbrowser.open(link, new=2)


if __name__ == '__main__':
    app = ZoomerApp()
    app.start()
