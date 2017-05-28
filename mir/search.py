from opal.core.search.queries import DatabaseQuery
from django.db.models import Q
from mir.models import RegisterIncident


class QueryBackend(DatabaseQuery):
    def fuzzy_query(self):
        """
        Fuzzy queries break apart the query string by spaces and search a
        number of fields based on the underlying tokens.

        We then search hospital number, first name and surname by those fields
        and order by the occurances

        so if you put in Anna Lisa, even though this is a first name split
        becasuse Anna and Lisa will both be found, this will rank higher
        than an Anna or a Lisa, although both of those will also be found
        """
        some_query = self.query
        qs = RegisterIncident.objects.filter(
            Q(incident_name__icontains=some_query) | Q(countries__name__icontains=some_query)
        ).distinct()
        return [i.to_dict(None) for i in qs]
