import os
import os.path
import tkinter as tk
from viewable import Viewable
from megawidget.scrollbox import ScrollBox
from rustiql.view.tree_hook import TreeHook


class MainView(Viewable):
    def __init__(self, app, project, main_host,
                 header_builder, tree_builder, nodebar_builder,
                 footer_builder):
        super().__init__()
        # args/kwargs
        self._app = app
        self._main_host = main_host
        self._project = project
        # builders
        self._header_builder = header_builder
        self._tree_builder = tree_builder
        self._nodebar_builder = nodebar_builder
        self._footer_builder = footer_builder
        # gui vars
        self._body = None
        self._header = None
        self._scrollbox = None
        self._tree = None
        self._footer = None
        # cache
        self._last_node_id = None

    def open_database(self, path):
        self._header.open_database(path)

    def notify_database_change(self):
        self._tree.clear(0)
        self._footer.push("tables", execute=True)

    def push_sql(self, sql, formatter, execute=False):
        self._footer.push(sql, formatter, execute)

    def notify_operation_execution(self, result, datatype, description, sql, formatter):
        file = "<NO FILE>"
        path = "<MEMORY>"
        real_path = ":memory:"
        if self._main_host.path != ":memory:":
            file = os.path.basename(self._main_host.path)
            path = self._main_host.path
            real_path = path
        data = {"type": datatype,
                "file": file,
                "path": path,
                "realpath": real_path,
                "result": result,
                "description": description,
                "formatter": formatter}
        # close the previous
        for node in self._tree.nodes:
            node_id = node["node_id"]
            if node_id != 0:
                self._tree.collapse(node_id)
        self._last_node_id = self._tree.insert(parent=0,
                          title=sql,
                          data=data,
                          index=0,
                          expand=True)
        self._scrollbox.yview_moveto(0)

    def leave_app(self):
        self._app.close()

    def _build(self):
        self._body = tk.Frame(self._app.root)
        self._body.columnconfigure(0, weight=1)
        self._body.rowconfigure(1, weight=1)
        # install header
        self._header = self._header_builder.build(self,
                                                  self._main_host,
                                                  self._project)
        self._header.body.grid(row=0, column=0, sticky="we",
                               padx=2)
        # install footer
        self._footer = self._footer_builder.build(self,
                                                  self._main_host,
                                                  self._project)
        self._footer.body.grid(row=2, column=0, sticky="we",
                               padx=2)
        # install scrollbox
        self._scrollbox = ScrollBox(self._body, orient="y")
        self._scrollbox.grid(row=1, column=0, sticky="nswe", pady=1)
        # install tree
        self._tree = self._tree_builder.build(self._scrollbox.box,
                                              spacing=20)
        self._tree.pack(expand=1, fill=tk.BOTH, padx=5)
        hook = (lambda self=self:
                TreeHook(self,
                         self._nodebar_builder, self._main_host))
        self._tree.hook = hook

    def _on_map(self):
        # insert root node
        node_id = self._tree.insert(expand=True)
        self._tree.ghost(node_id)

    def _on_destroy(self):
        pass
