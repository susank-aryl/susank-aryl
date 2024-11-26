class hospital:
    #class attribute
    ministry = "Ministry of Health"

    # class Constructer
    def __init__(self,name,location,ministry, revenew, patients) -> None: #This function doesnot return anything
    # Initializing Parameters   
        self.name = name
        self.location = location
        self.ministry = ministry
        self.__revenew = revenew #private attribute
        self.__patients = patients #private attribute

    def __str__(self) -> str:
        """
        Used to provide infomation about the class. It is called when print(object) is passed.
        """
        return f"Name : {self.name} | Location : {self.location} | Ministry : {self.ministry}"
    
    def get_revenew(self):
        """
        Getter method to access the private attribute.
        """
        if self.__revenew < 100000:
            raise ValueError("Too small revenew")
        return self.__revenew
    
    def get_patients(self):
        """
        Getter method to access the private attribute patient
        """
        return self.__patients
    
    def set_revenew(self, revenew):
        """
        Setter method to update the private attribute.
        Always use setter to update the private attribute
        """
        if self.__revenew < 100000:
            raise ValueError("Too small revenew")
        self.__revenew = revenew
    
    def set_patients(self, patients):
        """
        Setter method to update the private attribute.
        """
        self.__patients = patients

    def avg_money_spent(self):
        # Avg money spent can only be accessed throught a method
        return f"${self.__revenew / self.__patients:,.2f}K"
    
    def facilities(self, beds):
        """
        This will create or update an instance attribute, 
        store the value of bed inside of object making it part of object's status.
        """
        self.beds = beds
        print("The object instance attribute has been updated + object.beds.")   

    def complaints(self, message):
        """
        This method uses message parameter temporarily during method execution.
        Do not temper with the object, message is just a local variable of the method used for the duration of method call.
        """
        print(f"The most common comment for {self.name} is {message}")

# grandy = hospital("Grandy" , "Greenland", "DepHealth", 120000, 40000) #Creating object instance

# print(f"The name of this hospital is {grandy.name} and is located at {grandy.location}.")

# print(f"The hospital belongs to the {grandy.ministry}") #Gives object's instance output.

# print(f"The hospital belongs to the {grandy.__class__.ministry}") #Gives class attribute by the name of ministry.

# print ('=' * 75)

# #Initializing the bed parameter for failities method
# grandy.facilities(42)
# print(f"The number of beds in {grandy.name} is {grandy.beds}.")

# print("=" * 75)

# #Initialing message parameter fir complaint method
# grandy.complaints("too expensive")
# # grandy.message() # Error AttributeError : Has no attribute message

# print(f"The revenew of the hospital is {grandy.get_revenew()} with total patients being {grandy.get_patients()} and avg being {grandy.avg_money_spent()}.") #the private element can only be accessed using getter

# print("=" * 75)

# # Using Getter and Setter
# grandy.set_patients(44700)
# grandy.set_revenew(125000)
# print(f"Past year the total patients were {grandy.get_patients()} and the total revenew was {grandy.get_revenew()}")
# print(f"Same year the average money spent was {grandy.avg_money_spent()}")

# print("=" * 75)
# # Getting the class description "runs __str__ method"
# print(grandy)