class hospital:

    ministry = "Ministry of Health"

    def __init__(self,name,location) -> None:
        self.name = name
        self.location = location


grandy = hospital("Grandy" , "Greenland")
print(f"The name of this hospital is {grandy.name} and is located at {grandy.location}.")
print(f"The hospital belongs to the {grandy.ministry}")
print(f"The hospital belongs to the {grandy.__class__.ministry}")