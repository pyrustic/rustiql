
Back to [Reference Overview](https://github.com/pyrustic/rustiql/blob/master/docs/reference/README.md)

# rustiql.host.main\_host



<br>


```python

class MainHost:
    """
    
    """

    def __init__(self, dao_builder):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def path(self):
        """
        
        """

    def close(self):
        """
        
        """

    def columns(self, name):
        """
        
        """

    def db_schema(self):
        """
        
        """

    def exec_edit_request(self, sql):
        """
        
        """

    def exec_query_request(self, sql):
        """
        
        """

    def exec_script(self, script, is_file=False):
        """
        
        """

    def is_data_query_language(self, sql):
        """
        
        """

    def open(self, path):
        """
        
        """

    def table_content(self, name):
        """
        
        """

    def tables(self):
        """
        
        """

```

