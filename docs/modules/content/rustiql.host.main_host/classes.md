Back to [Modules overview](https://github.com/pyrustic/rustiql/blob/master/docs/modules/README.md)
  
# Module documentation
>## rustiql.host.main\_host
No description
<br>
[classes (1)](https://github.com/pyrustic/rustiql/blob/master/docs/modules/content/rustiql.host.main_host/classes.md)


## Classes
```python
class MainHost(object):
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

    def _open(self, path):
        """
        
        """

    def _setup(self):
        """
        
        """

```

