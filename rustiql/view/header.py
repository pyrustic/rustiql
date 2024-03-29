import os
import os.path
import tkinter as tk
from viewable import Viewable
from megawidget.toast import Toast
from tkinter import filedialog


class Header(Viewable):
    def __init__(self, parent_view, host, project):
        super().__init__()
        self._parent_view = parent_view
        self._host = host
        self._project = project
        self._body = None
        # stringvar
        self._stringvar_entry_database = tk.StringVar()
        self._stringvar_entry_path = tk.StringVar()

    def open_database(self, path):
        self._open(path)

    def _build(self):
        self._body = tk.Frame(self._parent_view.body, class_="HeaderBar")
        self._body.columnconfigure(1, weight=2, uniform=1)
        self._body.columnconfigure(3, weight=3, uniform=1)
        # label database
        label_database = tk.Label(self._body, text="FILE:")
        # entry Database
        entry_database = tk.Entry(self._body,
                                  textvariable=self._stringvar_entry_database,
                                  state="readonly",
                                  width=1)
        # label path
        label_path = tk.Label(self._body, text="PATH:")
        # entry Path
        entry_path = tk.Entry(self._body,
                              textvariable=self._stringvar_entry_path,
                              state="readonly",
                              width=1)
        # button Open
        button_open = tk.Button(self._body,
                                text="Open",
                                command=self._on_click_open)
        # button New
        button_new = tk.Button(self._body,
                               text="New",
                               command=self._on_click_new)
        # button In-Memory
        button_in_memory = tk.Button(self._body,
                                     text="In-memory",
                                     command=self._on_click_in_memory)
        # install
        label_database.grid(row=0, column=0, sticky="we", ipadx=3)
        entry_database.grid(row=0, column=1, sticky="we", padx=(0, 0))
        label_path.grid(row=0, column=2, sticky="we", ipadx=3)
        entry_path.grid(row=0, column=3, sticky="we", padx=(0, 3))
        button_open.grid(row=0, column=4, padx=(0, 3), pady=2)
        button_new.grid(row=0, column=5, padx=(0, 3), pady=2)
        button_in_memory.grid(row=0, column=6, padx=(0, 0), pady=2)

    def _on_map(self):
        pass

    def _on_destroy(self):
        pass

    def _on_click_open(self):
        filename = filedialog.askopenfilename(initialdir=self._project,
                                              title="Select a database file")
        if not isinstance(filename, str) or not filename:
            return
        self._open(filename)

    def _on_click_new(self):
        filename = filedialog.asksaveasfilename(initialdir=self._project,
                                              title="Create a database file")
        if not isinstance(filename, str) or not filename:
            return
        if os.path.exists(filename):
            os.unlink(filename)
        self._open(filename)

    def _on_click_in_memory(self):
        self._open(":memory:")

    def _open(self, filename):
        # try to open the database
        if not self._host.open(filename):
            Toast(self._body, message="Invalid database !", duration=2000)
            return
        self._parent_view.notify_database_change()
        self._fill_form(filename)
        # store path

    def _fill_form(self, filename):
        database = "<NO FILE>"
        path = "<MEMORY>"
        if filename != ":memory:":
            database = os.path.basename(filename)
            path = os.path.normpath(filename)
        self._stringvar_entry_database.set(database)
        self._stringvar_entry_path.set(path)
