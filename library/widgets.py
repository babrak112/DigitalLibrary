from django_addanother.widgets import AddAnotherWidgetWrapper

class SafeAddAnotherWidgetWrapper(AddAnotherWidgetWrapper):
    @property
    def choices(self):
        return self.widget.choices

    @choices.setter
    def choices(self, value):
        self.widget.choices = value
