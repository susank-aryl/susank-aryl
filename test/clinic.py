from hospital import hospital

class clinic(hospital):
    """
    This class expresses the use and importance of inheritance. How it can be achieved
    """
    def __init__(self, name, location, ministry, clinic_name, clinic_revenew, clinic_patients) -> None:
        super().__init__(name = name, location = location, ministry = ministry,revenew = 0,patients = 0) 
        self.__clinic_name = clinic_name
        self.__clinic_revenew = clinic_revenew
        self.__clinic_patients = clinic_patients

    def __str__(self) -> str:
        """
        Information about the clinic class a child class of hospital.
        """
        return f"Child class of the hospital class with aditional attibutes.\nclinic_name : {self.__clinic_name} | clinic_revenew : {self.__clinic_revenew} | clinic_patients : {self.__clinic_patients}"

    def get_revenew(self):
        return self.__clinic_revenew

    def get_clinic_name(self):
        return self.__clinic_name

    def get_clinic_patients(self):
        return self.__clinic_patients

    def set_revenew(self, clinic_revenew):
        if self.__clinic_revenew < 75000:
            raise ValueError("Too less revenew")
        self.__clinic_revenew = clinic_revenew

    def set_clinic_name(self, clinic_name):
        self.__clinic_name = clinic_name

    def set_clinic_patients(self, clinic_patients):
        self.__clinic_patients = clinic_patients

    def avg_money_spent(self):
        if self.__clinic_patients == 0:
            raise ValueError("Number of patients cannot be 0.")
        return f"${self.__clinic_revenew / self.__clinic_patients:,.2f}k"
    
# norvic = clinic(name = "Grandy",location = "Kaldhara", ministry="Health", clinic_name="Norvic", clinic_patients= 150, clinic_revenew= 89000)

# print("=" * 75)
# print(f"The namme of the clinic is {norvic.get_clinic_name()} which is affielated with {norvic.name}")
# print(norvic)

# print("=" * 75)
# """
# What python OOP does is it always looks for method in parent class and then look for the same method if it exists or not in child class and if it does exist on child class the parent method gets overright.
# Like in this case the get_revenew and set_revenew is getting overright
# """

# print(f"Revenew from child class : {norvic.get_revenew()}")
# print (f"Revenew from parent class : {grandy.get_revenew()}")