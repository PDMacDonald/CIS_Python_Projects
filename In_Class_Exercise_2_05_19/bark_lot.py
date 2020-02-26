

__author__ = "Preston MacDonald"
__copyright__ = "2019 MacDonald"
__credits__ = ""
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonald"
__email__ = "macdonaldpd@appstate.edu"
__status__ = ""

#Constants for dog daycare pricing
dog_wgroup_1 = 55
dog_wgroup_2 = 75
dog_wgroup_3 = 105
dog_wgroup_4 = 125


#input

owner_id = input("Enter owner ID: ")
dog_name = input("Enter dog's name: ")
dog_breed = input("Enter dog's breed: ")
dog_age = input("Enter dog's age: ")
dog_weight_lbs = float(input("Enter dog's weight in lbs: "))

#Process
if(dog_weight_lbs < 15):
    fee = dog_wgroup_1
elif(dog_weight_lbs < 30):
    fee = dog_wgroup_2
elif(dog_weight_lbs < 80):
    fee = dog_wgroup_3
else:
    fee = dog_wgroup_4
#Output


print("\n")
print("Owner id: {}".format(owner_id))
print("Dog's name: {}".format(dog_name))
print("Dog's breed: {}".format(dog_breed))
print("Dog's age: {}".format(dog_age))
print("Dog's weight: {}".format(dog_weight_lbs))
print("Fee: {}".format(fee))
print("\n")


print("Press and key to End Program")
input()

#End of program
