import django_filters
from django_filters import CharFilter,ChoiceFilter
from django.contrib.auth.models import User
from .models import Employee


class search_user(django_filters.FilterSet):
    class Meta:
        model=User
        fields = ['username']
        


class search_doctor(django_filters.FilterSet):
    Address=CharFilter(field_name='address',lookup_expr='icontains',label='Address')

    class Meta:
        model=Employee
        fields = ['user','Address']
        
        
    def __init__(self, *args, **kwargs):
        super(search_doctor, self).__init__(*args, **kwargs)
        self.filters['user'].extra.update(
            {'empty_label': 'choose Doctor to consult'})
        self.filters['user'].label='Doctors'