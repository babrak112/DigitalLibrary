import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, NumberInput, DateField

from DigitalLibrary.settings import DEBUG
from library.models import Country, Author, Genre, Book


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    date_of_birth = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))
    date_of_death = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        initial_name = cleaned_data['first_name']
        initial_surname = cleaned_data['surname']
        if DEBUG:
            print(f"Initial name: '{initial_name}', "
                  f"Initial surname: '{initial_surname}'")
        if not initial_name or not initial_surname:
            raise ValidationError("Please enter both initial_name and initial_surname")

        initial_date_of_birth = cleaned_data['date_of_birth']
        initial_date_of_death = cleaned_data['date_of_death']
        if initial_date_of_birth and initial_date_of_death and initial_date_of_death <= initial_date_of_birth:
            raise ValidationError("Date of death cannot be before birth")

        return cleaned_data


    def clean_first_name(self):
        initial = self.cleaned_data['first_name']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

    def clean_surname(self):
        initial = self.cleaned_data['surname']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        if DEBUG:
            print(f"Initial date of birth: {initial}")
        if initial and initial > date.today():
            raise ValidationError("Date of birth must be in the past")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        if DEBUG:
            print(f"initial date of death: {initial}")
        if initial and initial > date.today():
            raise ValidationError("Date of death must be in the past")
        return initial

    def clean_biography(self):
        initial = self.cleaned_data['biography']
        if DEBUG:
            print(f"Initial biography: {initial}")
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)



class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title_orig(self):
        initial = self.cleaned_data['title_orig']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

    def clean_title_cz(self):
        initial = self.cleaned_data['title_cz']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

    def clean_publisher(self):
        initial = self.cleaned_data['publisher']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

    def clean_description(self):
        initial = self.cleaned_data['description']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def clean_name(self):
        initial = self.cleaned_data['name']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result

class CountryModelForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def clean_country_name(self):
        initial = self.cleaned_data['name']
        print(f"initial: {initial}")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result = {result}")
        return result