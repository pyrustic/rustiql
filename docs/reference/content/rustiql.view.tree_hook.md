
Back to [Reference Overview](https://github.com/pyrustic/rustiql/blob/master/docs/reference/README.md#readme)

# rustiql.view.tree\_hook



<br>


```python

class TreeHook:
    """
    
    """

    def __init__(self, parent_view, nodebar_builder, host):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def build_node(self, tree, node, frame):
        """
        
        """

    def on_change_database(self, path):
        """
        
        """

    def on_click_drop(self, table):
        """
        
        """

    def on_click_explore(self, table):
        """
        
        """

    def on_click_truncate(self, table):
        """
        
        """

    def on_collapse_node(self, tree, node):
        """
        
        """

    def on_destroy_node(self, tree, node):
        """
        
        """

    def on_expand_node(self, tree, node):
        """
        
        """

    def on_feed_node(self, tree, node, *args, **kwargs):
        """
        
        """

    def on_map_node(self, tree, node):
        """
        
        """

```

