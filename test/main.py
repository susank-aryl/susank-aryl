from hospital import hospital
from clinic import clinic

class main():
    def run_clinic(self, norvic, grandy):
        print("=" * 75)
        print(f"The namme of the clinic is {norvic.get_clinic_name()} which is affielated with {norvic.name}")
        print(norvic)

        print("=" * 75)
        """
        What python OOP does is it always looks for method in parent class and then look for the same method if it exists or not in child class and if it does exist on child class the parent method gets overright.
        Like in this case the get_revenew and set_revenew is getting overright
        """
        print(f"Revenew from child class : {norvic.get_revenew()}")
        print (f"Revenew from parent class : {grandy.get_revenew()}")
    
    
    def run_hospital(self,grandy):

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

        print(f"The revenew of the hospital is {grandy.get_revenew()} with total patients being {grandy.get_patients()} and avg being {grandy.avg_money_spent()}.") #the private element can only be accessed using getter

        print("=" * 75)

        # Using Getter and Setter
        grandy.set_patients(44700)
        grandy.set_revenew(125000)
        print(f"Past year the total patients were {grandy.get_patients()} and the total revenew was {grandy.get_revenew()}")
        print(f"Same year the average money spent was {grandy.avg_money_spent()}")

        print("=" * 75)
        # Getting the class description "runs __str__ method"
        print(grandy)
            
if __name__ == '__main__':
    grandy = hospital("Grandy" , "Greenland", "DepHealth", 120000, 40000) #Creating object instance
    norvic = clinic(name = "Grandy",location = "Kaldhara", ministry="Health", clinic_name="Norvic", clinic_patients= 150, clinic_revenew= 89000)
    main().run_hospital(grandy)
    main().run_clinic(norvic, grandy)

    print("\nCalling the method of Parent Class with child object.")
    norvic.complaints(message="Over-priced")