Back to [Modules overview](https://github.com/pyrustic/rustiql/blob/master/docs/modules/README.md)
  
# Module documentation
>## rustiql.view.nodebar
No description
<br>
[classes (1)](https://github.com/pyrustic/rustiql/blob/master/docs/modules/content/rustiql.view.nodebar/classes.md)


## Classes
```python
class Nodebar(viewable.Viewable):
    """
    Subclass this if you are going to create a view.
    
    Lifecycle of a view:
        1- you instantiate the view
        2- '__init__()' is implicitly called
        3- you call the method '.build()'
        4- '_build()' is implicitly called
        5- '_on_map()' is implicitly called once the widget is mapped
        6- '_on_destroy()' is implicitly called when the widget is destroyed/closed
    
    The rules to create your view is simple:
    - You need to subclass Viewable.
    - You need to implement the methods '_build()', and optionally
        implement '_on_map()' and '_on_destroy()'.
    - You need to set an instance variable '_body' with either a tk.Frame or tk.Toplevel
        in the method '_on_build()'
    That's all ! Of course, when you are ready to use the view, just call the 'build()' method.
    Calling the 'build()' method will return the body of the view. The one that you assigned
    to the instance variable '_body'. The same body can be retrieved with the property 'body'.
    The 'build()' method should be called once. Calling it more than once will still return
    the body object, but the view won't be built again.
    You can't re-build your same view instance after destroying its body.
    You can destroy the body directly, by calling the conventional tkinter destruction method
     on the view's body. But it's recommended to destroy the view by calling the view's method
     'destroy()' inherited from the class Viewable.
    The difference between these two ways of destruction is that when u call the Viewable's
     'destroy()' method, the method '_on_destroy()' will be called BEFORE the effective
     destruction of the body. If u call directly 'destroy' conventionally on the tkinter
     object (the body), the method '_on_destroy()' will be called AFTER the beginning
      of destruction of the body.
    
      By the way, you can use convenience methods "build_pack", "build_grid", "build_place"
      to build and pack/grid/place your widget in the master !!
      Use "build_wait" for toplevels if you want the app to wait till the window closes
    """

    def __init__(self, parent_view, node_id, collapsable_frame, file, path, real_path, result, datatype, description):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
        """

    def old_install_db_schema(self, master, result):
        """
        
        """

    def _build(self):
        """
        Build the view here by defining the _body instance
        """

    def _content_table_mask(self, index, data):
        """
        
        """

    def _fill_request_result_frame(self, master):
        """
        
        """

    def _fill_result_frame(self, frame):
        """
        
        """

    def _fill_text(self, text):
        """
        
        """

    def _install_db_schema(self, master, result, i=0, table_info=None):
        """
        
        """

    def _install_result_table(self, master, result):
        """
        
        """

    def _on_click_drop(self, name):
        """
        
        """

    def _on_click_explore(self, name):
        """
        
        """

    def _on_click_open(self):
        """
        
        """

    def _on_click_truncate(self, name):
        """
        
        """

    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

    def _schema_table_mask(self, index, data):
        """
        
        """

```

