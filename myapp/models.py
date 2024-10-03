from django.db import models

# class GenreChoices(models.TextChoices):

    # Action='Action','Action'

    # Fiction='Fiction','Fiction'

    # Thriller='Thriller','Thriller'

Genre_Choice=[('Action','Action'),

                ('Fiction','Fiction'),

                ('Thriller','Thriller')
                ]

class movies(models.Model):

    title=models.CharField(max_length=200, null=True)

    # genre=models.CharField(max_length=200, null=True,choices=GenreChoices.choices)

    genre=models.CharField(max_length=200, null=True,choices=Genre_Choice)

    language=models.CharField(max_length=200 ,null=True)

    year=models.CharField(max_length=200, null=True)

    runtime=models.PositiveIntegerField(null=True)
    
    directer=models.CharField(max_length=200, null=True)


# class student(models.Model):

#     name=models.CharField(max_length=200, null=True)

#     # genre=models.CharField(max_length=200, null=True,choices=GenreChoices.choices)

    
#     classs=models.CharField(max_length=200 ,null=True,choices=Classs_Choice.choices)

#     div=models.CharField(max_length=200, null=True,choices=Div_Choice.choices)

#     contact=models.IntegerField(max_length=200, null=True)

#     about_me=models.TextField(null=True)

#     img=models.ImageField(null=True)

#     url=models.URLField(null=True)

# class Classs_Choice(models.IntegerChoices):
#     one=1,1
#     two=2,2
#     three=3,3
#     four=4,4
#     five=5,5
#     six=6,6
#     seven=7,7
#     eight=8,8
#     nine=9,9
#     ten=10,10
# class Div_Choice(models.TextChoices):
#     div1='A','A'
#     div2='B','B'
#     div3='C','C'
#     div4='D','D'


# class Car(models.Model):

    # name=models.CharField(max_length=200,null=True)

    # model=models.CharField(max_length=200,null=True)

    # year=models.DateField(null=True)

    # seat=models.IntegerField(max_length=200,null=True)

    # fueltype=models.CharField(max_length=200,null=True,choices=Fuel_Choice.choices)

    # perfomance=models.CharField(max_length=200,null=True)

    # img=models.ImageField(null=True)

    # instock=models.CharField(null=True)

    # release_date=models.DateField()


#  class Fuel_Choice(models.TextChoices):
    # petrol='petrol','petrol'
    # diesel='diesel','diesel'
    # ev='ev','ev'

  
# class customer(models.model):

    # name=models.CharField(max_length=200,null=False)

    # lastname=models.CharField(max_length=200,null=False)
    
    # adress=models.CharField(max_length=200,null=False)

    # street_address=models.CharField(max_length=200,null=True)

    # city=models.CharField(max_length=200,null=True)

    # state=models.CharField(max_length=200,null=true)

    # zip_code=models.IntegerField(null=False)

    # phone_number=models.IntegerField(null=False)

    # email=models.EmailField(null=True)

    # aboutus=models.CharField(max_length=200,null=false)

    # feedback=models.CharField(max_length=200,null=True)

    # suggestions=models.CharField(max_length=200, null=True)

    # recomentation=models.CharField(null=True)

    

    



    

