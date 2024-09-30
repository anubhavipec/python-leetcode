from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
class CarSize(Enum):
    SMALL="Small"
    MEIDUM="Medium"
    LARGE="Large"
    
@dataclass
class Car:
    size:str
    color:str
    brand:str
    
    def __str__(self) -> str:
        return f"{self.size} {self.color} {self.brand}"

@dataclass
class ParkingSpot:
   
   
    def __init__(self) -> None:
       self.parked_car: Optional[Car] = None
    
    def park(self,car:Car) -> bool:
        if self.parked_car:
            return False
        else:
            self.parked_car = car
            return True
        
    def remove(self) -> bool:
        if self.parked_car:
            self.parked_car = None
            return True
        return False

    def __str__(self) -> str:
        if self.parked_car:
            return str(self.parked_car)
        return "Empty"
    
        
    
@dataclass
class ParkingLot:
    def __init__(self,size:int) -> None:
        self.parking_spots:List[ParkingSpot] = []
        self.__size = size
        self.__free_spots = size
        for _ in range(size):
            self.parking_spots.append(ParkingSpot())
    
    
    
    def get_free_spots(self) -> int:
        return self.__free_spots

    def park_vehicle(self,instruction:str) -> bool:
        car = get_car_desc(instruction)
        prefrred_spot = instruction[1]
        if self.get_free_spots() == 0:
            return
        
        for spot in range(int(prefrred_spot,self.__size)):
            if  self.parking_spots[spot].park(car=car):
                self.__free_spots -= 1
                return True
        for spot in range(int(prefrred_spot)):
            if self.parking_spots[spot].park(car=car):
                self.__free_spots -= 1
                return True
        return False
                
                
    def leave(self,instruction:str) -> None:
        remove_idx:int = instruction[1]
        if self.parking_spots[remove_idx].remove():
            self.__free_spots += 1
    




def get_car_desc(instruction:List[str]) -> Car:
    car_detail_arr = instruction[2].split(" ")
    return Car(car_detail_arr[0],car_detail_arr[1],car_detail_arr[2])

         
def parking_system(n: int, instructions: List[List[str]]) -> List[str]:
    res:List[str] = []
    parking_lot = initialize_parking_lot(n)
    parking_lot_state:List[str] = []
    for instruction in instructions:
        if instruction[0] == "park":
            parking_lot.park_vehicle(instruction)
        elif instruction[0] == "print":
            res.append(str(parking_lot.parking_spots[int(instruction[1])-1]))
        elif instruction[0] == "remove":
            parking_lot.leave( instruction=instruction)
        elif instruction[0] == "print_free_spots":
            res.append(parking_lot.get_free_spots())
        else:
            print("Bad Instruction")
    return res

def initialize_parking_lot(n:int) -> ParkingLot:
    parking_lot = ParkingLot(n)

    return parking_lot
    '''
4          
5
park 1 Small Silver BMW
print 1
print 2
print 3
print_free_spots
    '''
    

if __name__ == "__main__":
    # n = int(input())
    # instructions = [input().split() for _ in range(int(input()))]
    n = 4
    instructions = [["park", "1", "Small Silver BMW"],["print","1"],["print", "2"],["print","3"],["print_free_spots"]]
    res = parking_system(n, instructions)
    for line in res:
        print(line)