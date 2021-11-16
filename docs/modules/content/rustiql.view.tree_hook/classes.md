Back to [Modules overview](https://github.com/pyrustic/rustiql/blob/master/docs/modules/README.md)
  
# Module documentation
>## rustiql.view.tree\_hook
No description
<br>
[classes (1)](https://github.com/pyrustic/rustiql/blob/master/docs/modules/content/rustiql.view.tree_hook/classes.md)


## Classes
```python
class TreeHook(megawidget.tree.Hook):
    """
    
    """

    def __init__(self, parent_view, nodebar_builder, host):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def build_node(self, tree, node, frame):
        """
        
        """

    # inherited from megawidget.tree.Hook
    def on_build_node(self, tree, node, frame):
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

    def _on_click_edit(self, tree, node_id):
        """
        
        """

    def _on_click_sql(self, tree, node_id):
        """
        
        """

```

