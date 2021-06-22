import tkinter as tk
from megawidget.tree import Hook


class TreeHook(Hook):
    def __init__(self, parent_view, nodebar_builder, host):
        self._parent_view = parent_view
        self._nodebar_builder = nodebar_builder
        self._host = host
        self._stringvar_expander = tk.StringVar()
        self._stringvar_title = tk.StringVar()
        self._collapsable_frame = None
        self._nodebar = None
        self._formatter = None

    def on_change_database(self, path):
        self._parent_view.open_database(path)

    def on_click_truncate(self, table):
        sql = "DELETE FROM {}".format(table)
        formatter = "inline"
        self._parent_view.push_sql(sql, formatter, execute=True)

    def on_click_drop(self, table):
        sql = "DROP TABLE {}".format(table)
        formatter = "inline"
        self._parent_view.push_sql(sql, formatter, execute=True)

    def on_click_explore(self, table):
        sql = "SELECT * FROM {}".format(table)
        formatter = "inline"
        self._parent_view.push_sql(sql, formatter, execute=True)

    def build_node(self, tree, node, frame):
        node_id = node["node_id"]
        if node_id == 0:
            return
        # some vars
        title = node["title"]
        result = node["data"]["result"]
        datatype = node["data"]["type"]
        description = node["data"]["description"]
        file = node["data"]["file"]
        path = node["data"]["path"]
        real_path = node["data"]["realpath"]
        self._formatter = node["data"]["formatter"]
        # Populate stringvars
        self._stringvar_expander.set("-" if node["expanded"] else "+")
        self._stringvar_title.set(title)
        # config header frame
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=0)
        frame.columnconfigure(2, weight=1)
        # Fill titlebar
        # - button expander
        command = (lambda tree=tree, node_id=node_id:
                   tree.collexp(node_id))
        button_expander = tk.Button(frame,
                                    name="treeExpanderButton",
                                    textvariable=self._stringvar_expander,
                                    command=command)
        # - button edit
        button_edit = tk.Button(frame,
                                text="edit",
                                name="buttonEdit",
                                command=lambda self=self,
                                               node_id=node_id,
                                               tree=tree:
                                    self._on_click_edit(tree, node_id))
        # - entry title
        entry_title = tk.Entry(frame, name="treeTitle",
                               state="readonly",
                               textvariable=self._stringvar_title)
        entry_title.bind("<Button-1>",
                         lambda e, self=self,
                                node_id=node_id,
                                tree=tree:
                            self._on_click_sql(tree, node_id))
        # - install
        button_expander.grid(row=0, column=0, padx=(0, 5), sticky="w")
        button_edit.grid(row=0, column=1, padx=(0, 5), sticky="w")
        entry_title.grid(row=0, column=2, sticky="nswe")
        # collapsable_frame
        self._collapsable_frame = tk.Frame(frame, class_="CollapsableFrame")
        self._collapsable_frame.columnconfigure(0, weight=1)
        # - install
        self._collapsable_frame.grid(row=1, column=2, sticky="w", padx=(0, 20))
        # Fill collapsable frame
        self._nodebar = self._nodebar_builder.build(self, node_id,
                                    self._collapsable_frame,
                                    file, path, real_path, result,
                                    datatype, description)

    def on_map_node(self, tree, node):
        pass

    def on_destroy_node(self, tree, node):
        pass

    def on_feed_node(self, tree, node, *args, **kwargs):
        pass

    def on_expand_node(self, tree, node):
        node_id = node["node_id"]
        if node_id == 0:
            return
        self._stringvar_expander.set("-")
        self._collapsable_frame.grid()

    def on_collapse_node(self, tree, node):
        node_id = node["node_id"]
        if node_id == 0:
            return
        self._stringvar_expander.set("+")
        self._collapsable_frame.grid_remove()

    def _on_click_sql(self, tree, node_id):
        tree.collexp(node_id)

    def _on_click_edit(self, tree, node_id):
        sql = self._stringvar_title.get()
        self._parent_view.push_sql(sql, self._formatter)
