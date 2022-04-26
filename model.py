from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UnbiasedCoderTable(Model):
    class Meta:
        host = 'http://localhost:8000'
        table_name = 'unbiased_coder_table'

    name = UnicodeAttribute(hash_key=True)
    surname = UnicodeAttribute(range_key=True)
    twittername = UnicodeAttribute(null=True)
    
