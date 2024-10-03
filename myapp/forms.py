from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    options=(
        ("fiction","fiction"),
        ("Action","Action"),
        ("comedy","comedy"),
        ("Horror","Horror")
    )

    genre=forms.ChoiceField(choices=options)

    language=forms.CharField()

    year=forms.CharField()

    runtime=forms.IntegerField()
    
    directer=forms.CharField()

    def clean(self):

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        if int(year)<1990:

            error_message="year should be greater than 1990"

            self.add_error("year",error_message)

    def clean(self):

        cleaned_data=super().clean()

        runtime=cleaned_data.get("runtime")

        if int(runtime)>210 or int(runtime)<60:

            error_message="runtime should be in the range of 60 and 210"

            self.add_error("runtime",error_message)