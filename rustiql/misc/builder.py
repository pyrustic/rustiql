from rustiql.dao.main_dao import MainDao
from rustiql.host.main_host import MainHost
from rustiql.host.internal_data_manager import InternalDataManager
from rustiql.view.main_view import MainView
from rustiql.view.header import Header
from rustiql.view.tree import Tree
from rustiql.view.footer import Footer
from rustiql.view.editor import Editor
from rustiql.view.nodebar import Nodebar
from pyrustic.dao import Dao
from pyrustic.manager.misc import funcs


class MainDaoBuilder:
    def build(self, path):
        dao = Dao(path)
        return MainDao(dao)


class MainHostBuilder:
    def build(self):
        return MainHost(MainDaoBuilder())


class MainViewBuilder:
    def build(self, app):
        jasonix = funcs.get_manager_jasonix()
        target = jasonix.data["target"]
        main_host = MainHostBuilder().build()
        internal_data_manager = InternalDataManagerBuilder().build()
        return MainView(app, target, main_host, internal_data_manager,
                        HeaderBuilder(), TreeBuilder(), FooterBuilder())


class HeaderBuilder:
    def build(self, parent_view, host, internal_database_manager, target):
        header = Header(parent_view, host, internal_database_manager, target)
        header.build()
        return header


class TreeBuilder:
    def build(self, parent_view, box, host):
        tree = Tree(parent_view, box, NodebarBuilder(), host)
        tree.build()
        return tree


class FooterBuilder:
    def build(self, parent_view, main_host, target):
        footer = Footer(parent_view, main_host, EditorBuilder(target))
        footer.build()
        return footer


class EditorBuilder:
    def __init__(self, target):
        self._target = target

    def build(self, parent_view):
        editor = Editor(parent_view, self._target)
        editor.build_wait()


class InternalDataManagerBuilder:
    def build(self):
        manager_jasonix = funcs.get_manager_jasonix()
        sqleditor_jasonix = funcs.get_sqleditor_jasonix(False)
        return InternalDataManager(manager_jasonix, sqleditor_jasonix)


class NodebarBuilder:
    def build(self, parent_view, node_id,
              collapsable_frame, file, path,
              real_path, result, datatype,
              description):
        node = Nodebar(parent_view, node_id,
                       collapsable_frame, file, path, real_path,
                       result, datatype,
                       description)
        node.build()
        return node
