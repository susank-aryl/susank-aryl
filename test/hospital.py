class hospital:
    #class attribute
    ministry = "Ministry of Health"

    # class Constructer
    def __init__(self,name,location,ministry) -> None: #This function doesnot return anything
    # Initializing Parameters   
        self.name = name
        self.location = location
        self.ministry = ministry

    def facilities(self, beds):
        """
        This will create or update an instance attribute, 
        store the value of bed inside of object making it part of object's status.
        """
        self.beds = beds
        print("\nThe object instance attribute has been updated + object.beds.")   

    def complaints(self, message):
        """
        This method uses message parameter temporarily during method execution.
        Do not temper with the object, message is just a local variable of the method used for the duration of method call.
        """
        print(f"The most common comment for {self.name} is {message}")

grandy = hospital("Grandy" , "Greenland", "DepHealth") #Creating object instance

print(f"The name of this hospital is {grandy.name} and is located at {grandy.location}.")

print(f"The hospital belongs to the {grandy.ministry}") #Gives object's instance output.

print(f"The hospital belongs to the {grandy.__class__.ministry}") #Gives class attribute by the name of ministry.

print ('=' * 75)

#Initializing the bed parameter for failities method
grandy.facilities(42)
print(f"The number of beds in {grandy.name} is {grandy.beds}.")

print("=" * 75)

#Initialing message parameter fir complaint method
grandy.complaints("too expensive")
# grandy.message() # Error AttributeError : Has no attribute message
