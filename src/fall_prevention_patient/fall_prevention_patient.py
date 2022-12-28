import json

class Patient():
    def __init__(self, name, id, age, weight, height, sex, floor, room, bed, doctor, nurse):
        self.sex_dict = None
        self.doctor_dict = None
        self.nurse_dict = None
    
        self.name = name
        self.id = id
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.floor = floor
        self.room = room
        self.bed = bed
        self.doctor = doctor
        self.nurse = nurse

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("Invalid Name!")
        self._name = name

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id) -> None:
        if not isinstance(id, int):
            raise TypeError("Invalid ID!")

        self._id = id

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, age) -> None:
        if not isinstance(age, int):
            raise TypeError("Invalid Age!")
        
        self._age = age
    
    @property
    def weight(self) -> int:
        return self._weight
    
    @weight.setter
    def weight(self, weight) -> None:
        if not isinstance(weight, int):
            raise TypeError("Invalid Weight!")
        
        self._weight = weight

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, height) -> None:
        if not isinstance(height, int):
            raise TypeError("Invalid Height!")
        
        self._height = height

    @property
    def sex(self) -> str:
        return self._sex
    
    @sex.setter
    def sex(self, sex) -> None:
        if not isinstance(sex, str):
            raise TypeError("Invalid Sex!")

        with open("fall_prevention_web/assets/json/sex.json") as f:
            json_dict = json.load(f)
            if sex not in json_dict:
                raise TypeError("Invalid Sex!")
            
            self.sex_dict = json_dict[sex]
        self._sex = sex
        
    @property
    def floor(self) -> int:
        return self._floor
    
    @floor.setter
    def floor(self, floor) -> None:
        if not isinstance(floor, int):
            raise TypeError("Invalid floor!")
        
        self._floor = floor

    @property
    def room(self) -> int:
        return self._room
    
    @room.setter
    def room(self, room) -> None:
        if not isinstance(room, int):
            raise TypeError("Invalid room!")
        
        self._room = room

    @property
    def bed(self) -> int:
        return self._bed
    
    @bed.setter
    def bed(self, bed) -> None:
        if not isinstance(bed, int):
            raise TypeError("Invalid bed!")
        
        self._bed = bed

    @property
    def doctor(self) -> str:
        return self._doctor
    
    @doctor.setter
    def doctor(self, doctor) -> None:
        if not isinstance(doctor, str):
            raise TypeError("Invalid doctor!")

        with open("fall_prevention_web/assets/json/doctor.json") as f:
            json_dict = json.load(f)
            if doctor not in json_dict:
                raise TypeError("Invalid doctor!")
            self.doctor_dict = json_dict[doctor]

        self._doctor = doctor

    @property
    def nurse(self) -> str:
        return self._nurse
    
    @nurse.setter
    def nurse(self, nurse) -> None:
        if not isinstance(nurse, str):
            raise TypeError("Invalid nurse!")

        with open("fall_prevention_web/assets/json/nurse.json") as f:
            json_dict = json.load(f)
            if nurse not in json_dict:
                raise TypeError("Invalid nurse!")
            self.nurse_dict = json_dict[nurse]

        self._nurse = nurse

    @staticmethod
    def readPatient(patient_dict: dict):
        return Patient(patient_dict["name"], patient_dict["id"], patient_dict["age"], patient_dict["weight"], patient_dict["height"],
        patient_dict["sex"], patient_dict["floor"], patient_dict["room"], patient_dict["bed"], patient_dict["doctor"], patient_dict["nurse"])

    @staticmethod
    def readPatientsJson(json_path: str) -> list:
        with open(json_path) as f:
            return [Patient.readPatient(patient) for patient in json.load(f).values()]

    def update(self, patient_dict: dict):
        self.name = patient_dict["name"]

if __name__ == '__main__':
    print("Fall Prevention Patient")
    a = Patient.readPatientsJson("fall_prevention_web/assets/json/patient.json")
    for p in a:
        for i, j in vars(p).items():
            print(f"{i}: {j}")
