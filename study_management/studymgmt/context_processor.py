from .models import Study
from .shared_data import field_names

# This get_fields contains the fields of the column or (modles in django terms)
# which will be avaiable for all the templates, so no need to pass it to the templates. (DRY)

def get_fields(request):
     # will be used for display column names in templates
    return {'fields':field_names}

def get_fields_names():  # for sharing with other modules
    return field_names