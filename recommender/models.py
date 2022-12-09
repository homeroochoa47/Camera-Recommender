from django.db import models

# Create your models here.
class Camera(models.Model):
    CAMERA_TYPES = [
        ('RA', 'Rangefinder'),
        ('SL', 'Single Lens Reflex (SLR)'),
        ('PS', 'Point and Shoot')
    ]
    OPERATION_TYPE = [
        ('ME', 'Mechanical Operation'),
        ('BA', 'Battery Operation'),
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    camera_type = models.CharField(choices=CAMERA_TYPES, max_length=200)
    operation_type = models.CharField(choices=OPERATION_TYPE, max_length=200)
    use_description = models.TextField()
    
'''
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, type, mech_or_batt, uses ):
        self.name = name
        self.price = price
        self.type = type #rangefinder, slr, point and shoot
        self.mech_or_batt = mech_or_batt
        self.uses = uses

    #adding __repr__ to provide an option to retrieve some more details about the camera
    def __repr__(self): #need to figure out conditionals for final format
        return "The {camera} is a {type} camera which is {mech_or_batt}. It is best used for {uses} and can be bought for about ${price}.".format(camera = self.name, type = self.type, mech_or_batt = self.mech_or_batt, uses = self.uses, price = self.price)
        
    #method to ask user if they want more info about their suggested camera
    def more_info(self):
        answer = input("Would you like to learn more about this camera? \n")
        if "y" in answer:
            print(self)
        elif "n" in answer:
            print ("Happy buying!")
        else:
            print ("Enter yes or no")
            return more_info(self)
'''