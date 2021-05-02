from .models import *
import django_filters
from django_filters import DateRangeFilter, DateFilter


INDUSTRY = (
    ("Accountancy", "Accountancy"),
    ("Business", "Business"),
    ("Charity and Voluntary Work", "Charity and Voluntary Work"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Energy and Utilities", "Energy and Utilities"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Engineering and Manufacturing", "Engineering and Manufacturing"),
    ("Environment and Agriculture", "Environment and Agriculture"),
    ("Healthcare", "Healthcare"),
    ("Hospitality and Event Management", "Hospitality and Event Management"),
    ("Information Technology", "Information Technology"),
    ("Law", "Law"),
    ("Leisure, Sports, and Tourism", "Leisure, Sports, and Tourism"),
    ("Marketing, Advertising, and PR", "Marketing, Advertising, and PR"),
    ("Media and Internet", "Media and Internet"),
    ("Property and Consultation", "Property and Consultation"),
    ("Public Services and Administration", "Public Services and Administration"),
    ("Recruitment and HR", "Recruitment and HR"),
    ("Retail", "Retail"),
    ("Sales", "Sales"),
    ("Science and Pharmaceuticals", "Science and Pharmaceuticals"),
    ("Social Care", "Social Care"),
    ("Teacher Training and Education", "Teacher Training and Education"),
    ("Transport and Logistics", "Transport and Logistics"),
)


class ViewJobFilter(django_filters.FilterSet):
    applied = django_filters.BooleanFilter()
    saved = django_filters.BooleanFilter()
    date = DateRangeFilter()

    class Meta:
        model = JobSeeker
        fields = ['applied', 'saved', 'date']


class CategoriesFilter(django_filters.FilterSet):
    # category = django_filters.ChoiceFilter(choices=INDUSTRY)
    date = DateRangeFilter()

    class Meta:
        model = JobRecruiter
        fields = ['industry', 'job_title', 'location', 'experience', 'date']
