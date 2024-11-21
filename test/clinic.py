import hospital

class clinic(hospital):
    def __init__(self, name, location, ministry, clinic_name, clinic_revenew, clinic_patients) -> None:
        super().__init__(name = "No Name", location = "No Location", ministry = "No Ministry")
        self.__clinic_name = clinic_name
        self.__clinic_revenew = clinic_revenew
        self.__clinic_patients = clinic_patients

    def __str__(self) -> str:
        """
        Information about the clinic class a child class of hospital.
        """
        return f"Child class of the hospital class with aditional attibutes.\nclinic_name : {self.__clinic_name} | clinic_revenew : {self.__clinic_revenew} | clinic_patients : {self.__clinic_patients}"

    def get_clinic_revenew(self):
        return self.__clinic_revenew

    def get_clinic_name(self):
        return self.__clinic_name

    def get_clinic_patients(self):
        return self.__clinic_patients

    def set_clinic_revenew(self):
        if self.__clinic_revenew < 75000:
            raise ValueError("Too less revenew")
        self.__clinic_revenew = clinic_revenew

    def set_clinic_name(self):
        self.__clinic_name = clinic_name

    def set_clinic_patients(self):
        self.__clinic_patients = clinic_patients

    def avg_money_spent(self):
        return f"${self.__clinic_revenew / self.__clinic_patients:,.2f}k"
    
norvic = clinic("Grandy","Kaldhara", "Health", clinic_name="Norvic", clinic_patients= 150, clinic_revenew= 89000)

print(f"The namme of the clinic is {norvic.get_clinic_name} which is affielated with {norvic.get_name}")