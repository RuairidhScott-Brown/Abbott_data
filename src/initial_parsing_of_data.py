import pprint
import re
import matplotlib.pyplot as plt
import scipy.interpolate
import numpy as np
import copy

demo = "C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/203.ALL"



class aerofoil:

    def __init__(self, file_location):
        self.__file_location = file_location
        with open(self.__file_location, 'r') as file:
            self.__lines = file.readlines()

        self.__data = {"CL_vs_alpha": {
                        "3x10^6": { 
                            "alpha": [],
                            "CL": []
                        },
                        "6x10^6": {
                            "alpha": [],
                            "CL": []
                        }, 
                        "9x10^6": {
                            "alpha": [],
                            "CL": []
                        }, 
                        "6x10^6-rough": {
                            "alpha": [],
                            "CL": []
                        }, 
                        "flap1": {
                            "alpha": [],
                            "CL": []
                        }, 
                        "flap2": {
                            "alpha": [],
                            "CL": []
                        }
        },
        "CM_vs_alpha": {
                        "3x10^6": { 
                            "alpha": [],
                            "CM": []
                        },
                        "6x10^6": {
                            "alpha": [],
                            "CM": []
                        }, 
                        "9x10^6": {
                            "alpha": [],
                            "CM": []
                        }, 
                        "6x10^6-rough": {
                            "alpha": [],
                            "CM": []
                        }, 
                        "flap1": {
                            "alpha": [],
                            "CM": []
                        }, 
                        "flap2": {
                            "alpha": [],
                            "CM": []
                        }

        },
        "CL_vs_CD": {
                        "3x10^6": { 
                            "CD": [],
                            "CL": []
                        },
                        "6x10^6": {
                            "CD": [],
                            "CL": []
                        }, 
                        "9x10^6": {
                            "CD": [],
                            "CL": []
                        }, 
                        "6x10^6-rough": {
                            "CD": [],
                            "CL": []
                        }, 
                        "flap1": {
                            "CD": [],
                            "CL": []
                        }, 
                        "flap2": {
                            "CD": [],
                            "CL": []
                        }

        },
        "CL_vs_CM": {
                        "3x10^6": { 
                            "CM": [],
                            "CL": []
                        },
                        "6x10^6": {
                            "CM": [],
                            "CL": []
                        }, 
                        "9x10^6": {
                            "CM": [],
                            "CL": []
                        }, 
                        "6x10^6-rough": {
                            "CM": [],
                            "CL": []
                        }, 
                        "flap1": {
                            "CM": [],
                            "CL": []
                        }, 
                        "flap2": {
                            "CM": [],
                            "CL": []
                        }

        }
                        
                        }

    def print_file(self):
        print(self.__file_location)

    def clean(self):
        flag = True
        while flag == True:
            flag = False
            for line_number, line in enumerate(self.__lines):
                if re.search("[a-zA-Z]", line):
                    flag = True
                    self.__lines.remove(line)
        self.remove_newline()
        self.convert_to_float()

    def remove_newline(self):
        for line_number, line in enumerate(self.__lines):
            self.__lines[line_number] = line.replace('\n', '')

    def convert_to_float(self):
        for line_number, line in enumerate(self.__lines):
            string_list = line.split()
            for index, string in enumerate(string_list):
                string_list[index] = float(string)
            self.__lines[line_number] = string_list

    def create_dict(self):
        counter = 0
        counter_2 = 0
        for index, array in enumerate(self.__lines):
            if len(array) == 3:
                break  
            if len(array) == 1:
                temp = array[0]
                if counter < temp:
                    counter = array[0]
                elif counter > temp:
                    counter_2 = 1
                    counter = array[0]
                else:
                    break

                continue
            if counter == 1 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["3x10^6"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["3x10^6"]["CL"].append(array[1])
            elif counter == 2 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["6x10^6"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["6x10^6"]["CL"].append(array[1])
            elif counter == 3 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["9x10^6"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["9x10^6"]["CL"].append(array[1])
            elif counter == 4 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["6x10^6-rough"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["6x10^6-rough"]["CL"].append(array[1])
            elif counter == 5 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["flap1"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["flap1"]["CL"].append(array[1])
            elif counter == 6 and counter_2 == 0:
                self.__data["CL_vs_alpha"]["flap2"]["alpha"].append(array[0])
                self.__data["CL_vs_alpha"]["flap2"]["CL"].append(array[1])
            
            elif counter == 7 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["3x10^6"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["3x10^6"]["CM"].append(array[1])
            elif counter == 8 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["6x10^6"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["6x10^6"]["CM"].append(array[1])
            elif counter == 9 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["9x10^6"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["9x10^6"]["CM"].append(array[1])
            elif counter == 10 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["6x10^6-rough"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["6x10^6-rough"]["CM"].append(array[1])
            elif counter == 11 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["flap1"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["flap1"]["CM"].append(array[1])
            elif counter == 12 and counter_2 == 0:
                self.__data["CM_vs_alpha"]["flap2"]["alpha"].append(array[0])
                self.__data["CM_vs_alpha"]["flap2"]["CM"].append(array[1])

            elif counter == 1 and counter_2 == 1:
                self.__data["CL_vs_CD"]["3x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["3x10^6"]["CD"].append(array[1])
            elif counter == 2 and counter_2 == 1:
                self.__data["CL_vs_CD"]["6x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["6x10^6"]["CD"].append(array[1])
            elif counter == 3 and counter_2 == 1:
                self.__data["CL_vs_CD"]["9x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["9x10^6"]["CD"].append(array[1])
            elif counter == 4 and counter_2 == 1:
                self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"].append(array[1])
            elif counter == 5 and counter_2 == 1:
                self.__data["CL_vs_CD"]["flap1"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["flap1"]["CD"].append(array[1])
            elif counter == 6 and counter_2 == 1:
                self.__data["CL_vs_CD"]["flap2"]["CL"].append(array[0])
                self.__data["CL_vs_CD"]["flap2"]["CD"].append(array[1])

            elif counter == 7 and counter_2 == 1:
                self.__data["CL_vs_CM"]["3x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["3x10^6"]["CM"].append(array[1])
            elif counter == 8 and counter_2 == 1:
                self.__data["CL_vs_CM"]["6x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["6x10^6"]["CM"].append(array[1])
            elif counter == 9 and counter_2 == 1:
                self.__data["CL_vs_CM"]["9x10^6"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["9x10^6"]["CM"].append(array[1])
            elif counter == 10 and counter_2 == 1:
                self.__data["CL_vs_CM"]["6x10^6-rough"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["6x10^6-rough"]["CM"].append(array[1])
            elif counter == 11 and counter_2 == 1:
                self.__data["CL_vs_CM"]["flap1"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["flap1"]["CM"].append(array[1])
            elif counter == 12 and counter_2 == 1:
                self.__data["CL_vs_CM"]["flap2"]["CL"].append(array[0])
                self.__data["CL_vs_CM"]["flap2"]["CM"].append(array[1])
            
    def find_the_LD_max(self,x,y):
        if len(x) == 0:
            return 0
        grad = []
        for i in range(len(x)):
            grad.append((y[i] - 0) / (x[i] - 0))
        index_grad = grad.index(max(grad))
        return y[index_grad]
        #fig, axes = plt.subplots(1,2)
        #axes[0].plot(x, y, "o-")
        #axes[0].plot([0,x[index_grad]], [0,y[index_grad]])
        #axes[1].plot(self.__data["CL_vs_CD"]["3x10^6"]["CD"],self.__data["CL_vs_CD"]["3x10^6"]["CL"], "o-")
        #axes[1].plot([0,x[index_grad]], [0,y[index_grad]])
        #plt.show()

    def find_LD_in_range(self, Cl, Cd, min, max):
        Cl = np.array(Cl)
        Cd = np.array(Cd)
        LD = Cl/Cd
        LD_in_range = []
        for index, i in enumerate(Cl):
            if i > min and i < max:
                LD_in_range.append(LD[index])
        return LD_in_range


    def find_LD(self, mini, maxi):
        Re3_LD = self.find_LD_in_range(self.__data["CL_vs_CD"]["3x10^6"]["CL"],self.__data["CL_vs_CD"]["3x10^6"]["CD"], mini, maxi)
        Re6_LD = self.find_LD_in_range(self.__data["CL_vs_CD"]["6x10^6"]["CL"],self.__data["CL_vs_CD"]["6x10^6"]["CD"], mini, maxi)
        Re9_LD = self.find_LD_in_range(self.__data["CL_vs_CD"]["9x10^6"]["CL"],self.__data["CL_vs_CD"]["9x10^6"]["CD"], mini, maxi)
        Re6_LD_rough = self.find_LD_in_range(self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"],self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"], mini, maxi)
        #flap_1 = self.find_LD_in_range(self.__data["CL_vs_CD"]["flap_1"]["CL"],self.__data["CL_vs_CD"]["flap_1"]["CD"], mini, maxi)
        #flap_2 = self.find_LD_in_range(self.__data["CL_vs_CD"]["flap_2"]["CL"],self.__data["CL_vs_CD"]["flap_2"]["CD"], mini, maxi)

        return {"3x10^6_LD": Re3_LD, "6x10^6_LD": Re6_LD, "9x10^6_LD": Re9_LD, "6x10^6_rough_LD": Re6_LD_rough}


    def print_LD(self):

        Re3_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["3x10^6"]["CD"], self.__data["CL_vs_CD"]["3x10^6"]["CL"])
        Re3_LD_CD_index = self.__data["CL_vs_CD"]["3x10^6"]["CL"].index(Re3_LD)
        Re3_LD_CD = self.__data["CL_vs_CD"]["3x10^6"]["CD"][Re3_LD_CD_index]

        Re6_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["6x10^6"]["CD"], self.__data["CL_vs_CD"]["6x10^6"]["CL"])
        Re6_LD_CD_index = self.__data["CL_vs_CD"]["6x10^6"]["CL"].index(Re6_LD)
        Re6_LD_CD = self.__data["CL_vs_CD"]["6x10^6"]["CD"][Re6_LD_CD_index]

        Re9_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["9x10^6"]["CD"], self.__data["CL_vs_CD"]["9x10^6"]["CL"])
        Re9_LD_CD_index = self.__data["CL_vs_CD"]["9x10^6"]["CL"].index(Re9_LD)
        Re9_LD_CD = self.__data["CL_vs_CD"]["9x10^6"]["CD"][Re9_LD_CD_index]

        Re6_LD_rough = self.find_the_LD_max(self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"], self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"])
        Re6_LD_rough_CD_index = self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"].index(Re6_LD_rough)
        Re6_LD_rough_CD = self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"][Re6_LD_rough_CD_index]

        #flap1_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["flap1"]["CD"], self.__data["CL_vs_CD"]["flap1"]["CL"])
        #flap1_LD_CD_index = self.__data["CL_vs_CD"]["flap1"]["CL"].index(flap1_LD)
        #flap1_LD_CD = self.__data["CL_vs_CD"]["3x10^6"]["CD"][flap1_LD_CD_index]

        #flap2_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["flap2"]["CD"], self.__data["CL_vs_CD"]["flap2"]["CL"])
        #flap_2_LD_CD_index = self.__data["CL_vs_CD"]["flap2"]["CL"].index(flap2_LD)
        #flap_2_LD_CD = self.__data["CL_vs_CD"]["flap2"]["CD"][flap_2_LD_CD_index]

        fig, axes = plt.subplots(2,2)
        axes[0,0].plot(self.__data["CL_vs_CD"]["3x10^6"]["CL"], self.__data["CL_vs_CD"]["3x10^6"]["CD"])
        axes[0,0].plot([0, Re3_LD], [0, Re3_LD_CD])
        axes[0,1].plot(self.__data["CL_vs_CD"]["6x10^6"]["CL"], self.__data["CL_vs_CD"]["6x10^6"]["CD"])
        axes[0,1].plot([0, Re6_LD], [0, Re6_LD_CD])
        axes[1,0].plot(self.__data["CL_vs_CD"]["9x10^6"]["CL"], self.__data["CL_vs_CD"]["9x10^6"]["CD"])
        axes[1,0].plot([0, Re9_LD], [0, Re9_LD_CD])
        axes[1,1].plot(self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"], self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"])
        #axes[2,0].plot(self.__data["CL_vs_CD"]["flap1"]["CL"], self.__data["CL_vs_CD"]["flap1"]["CD"])
        #axes[2,1].plot(self.__data["CL_vs_CD"]["flap2"]["CL"], self.__data["CL_vs_CD"]["flap2"]["CD"])

        #plt.show()
            
    def LD_analysis(self):

        Re3_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["3x10^6"]["CD"], self.__data["CL_vs_CD"]["3x10^6"]["CL"])
        Re6_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["6x10^6"]["CD"], self.__data["CL_vs_CD"]["6x10^6"]["CL"])
        Re9_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["9x10^6"]["CD"], self.__data["CL_vs_CD"]["9x10^6"]["CL"])
        Re6_LD_rough = self.find_the_LD_max(self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"], self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"])
        flap1_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["flap1"]["CD"], self.__data["CL_vs_CD"]["flap1"]["CL"])
        flap2_LD = self.find_the_LD_max(self.__data["CL_vs_CD"]["flap2"]["CD"], self.__data["CL_vs_CD"]["flap2"]["CL"])        
        return {"3x10^6_LD": Re3_LD, "6x10^6_LD": Re6_LD, "9x10^6_LD": Re9_LD, "6x10^6_rough_LD": Re6_LD_rough, "flap1_LD": flap1_LD, "flap2_LD": flap2_LD}

        """
        lift_over_drag = list(Re3_range_y / Re3_range_x)
        max_lift_over_drag = max(lift_over_drag)
        print(max_lift_over_drag)
        index_LD_max = lift_over_drag.index(max_lift_over_drag)
        print(index_LD_max)
        print(Re3_range_y[index_LD_max])
        
        Re6 = scipy.interpolate.interp1d(self.__data["CL_vs_CD"]["6x10^6"]["CD"], self.__data["CL_vs_CD"]["6x10^6"]["CL"])
        Re9 = scipy.interpolate.interp1d(self.__data["CL_vs_CD"]["9x10^6"]["CD"], self.__data["CL_vs_CD"]["9x10^6"]["CL"])
        Re6_rough = scipy.interpolate.interp1d(self.__data["CL_vs_CD"]["6x10^6_rough"]["CD"], self.__data["CL_vs_CD"]["6x10^6_rough"]["CL"])
        Flap1 = scipy.interpolate.interp1d(self.__data["CL_vs_CD"]["flap1"]["CD"], self.__data["CL_vs_CD"]["flap1"]["CL"])
        Flap2 = scipy.interpolate.interp1d(self.__data["CL_vs_CD"]["flap2"]["CD"], self.__data["CL_vs_CD"]["flap2"]["CL"])
        """

    def plot_all_data(self):
        fig, axes = plt.subplots(2,2)
        axes[0,0].plot(self.__data["CL_vs_alpha"]["3x10^6"]["alpha"], self.__data["CL_vs_alpha"]["3x10^6"]["CL"])
        axes[0,0].plot(self.__data["CL_vs_alpha"]["6x10^6"]["alpha"], self.__data["CL_vs_alpha"]["6x10^6"]["CL"])
        axes[0,0].plot(self.__data["CL_vs_alpha"]["9x10^6"]["alpha"], self.__data["CL_vs_alpha"]["9x10^6"]["CL"])
        axes[0,0].plot(self.__data["CL_vs_alpha"]["6x10^6-rough"]["alpha"], self.__data["CL_vs_alpha"]["6x10^6-rough"]["CL"])
        axes[0,0].plot(self.__data["CL_vs_alpha"]["flap1"]["alpha"], self.__data["CL_vs_alpha"]["flap1"]["CL"])
        axes[0,0].plot(self.__data["CL_vs_alpha"]["flap2"]["alpha"], self.__data["CL_vs_alpha"]["flap2"]["CL"])

        axes[0,1].plot(self.__data["CM_vs_alpha"]["3x10^6"]["alpha"], self.__data["CM_vs_alpha"]["3x10^6"]["CM"])
        axes[0,1].plot(self.__data["CM_vs_alpha"]["6x10^6"]["alpha"], self.__data["CM_vs_alpha"]["6x10^6"]["CM"])
        axes[0,1].plot(self.__data["CM_vs_alpha"]["9x10^6"]["alpha"], self.__data["CM_vs_alpha"]["9x10^6"]["CM"])
        axes[0,1].plot(self.__data["CM_vs_alpha"]["6x10^6-rough"]["alpha"], self.__data["CM_vs_alpha"]["6x10^6-rough"]["CM"])
        axes[0,1].plot(self.__data["CM_vs_alpha"]["flap1"]["alpha"], self.__data["CM_vs_alpha"]["flap1"]["CM"])
        axes[0,1].plot(self.__data["CM_vs_alpha"]["flap2"]["alpha"], self.__data["CM_vs_alpha"]["flap2"]["CM"])

        axes[1,0].plot(self.__data["CL_vs_CD"]["3x10^6"]["CL"], self.__data["CL_vs_CD"]["3x10^6"]["CD"])
        axes[1,0].plot(self.__data["CL_vs_CD"]["6x10^6"]["CL"], self.__data["CL_vs_CD"]["6x10^6"]["CD"])
        axes[1,0].plot(self.__data["CL_vs_CD"]["9x10^6"]["CL"], self.__data["CL_vs_CD"]["9x10^6"]["CD"])
        axes[1,0].plot(self.__data["CL_vs_CD"]["6x10^6-rough"]["CL"], self.__data["CL_vs_CD"]["6x10^6-rough"]["CD"])
        axes[1,0].plot(self.__data["CL_vs_CD"]["flap1"]["CL"], self.__data["CL_vs_CD"]["flap1"]["CD"])
        axes[1,0].plot(self.__data["CL_vs_CD"]["flap2"]["CL"], self.__data["CL_vs_CD"]["flap2"]["CD"])

        axes[1,1].plot(self.__data["CL_vs_CM"]["3x10^6"]["CL"], self.__data["CL_vs_CM"]["3x10^6"]["CM"])
        axes[1,1].plot(self.__data["CL_vs_CM"]["6x10^6"]["CL"], self.__data["CL_vs_CM"]["6x10^6"]["CM"])
        axes[1,1].plot(self.__data["CL_vs_CM"]["9x10^6"]["CL"], self.__data["CL_vs_CM"]["9x10^6"]["CM"])
        axes[1,1].plot(self.__data["CL_vs_CM"]["6x10^6-rough"]["CL"], self.__data["CL_vs_CM"]["6x10^6-rough"]["CM"])
        axes[1,1].plot(self.__data["CL_vs_CM"]["flap1"]["CL"], self.__data["CL_vs_CM"]["flap1"]["CM"])
        axes[1,1].plot(self.__data["CL_vs_CM"]["flap2"]["CL"], self.__data["CL_vs_CM"]["flap2"]["CM"])

        #plt.show()
        #pprint.pprint(self.__data)

    @property
    def data(self):
        return self.__data



file_location = "C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/"
all_aero_foils = []
Cl_stuff_3 = []
Cl_stuff_6 = []
Cl_stuff_9 = []
counter  = 131
for page_number in range(131,264):
    file = f"{file_location}{page_number}.ALL"
    try:
        NACA = aerofoil(file)
    except:
        continue
    NACA.clean()
    NACA.create_dict()
    Cl_stuff_3.append(NACA.find_LD(0.25, 0.4)["3x10^6_LD"])
    Cl_stuff_6.append(NACA.find_LD(0.2, 0.4)["6x10^6_LD"])
    Cl_stuff_9.append(NACA.find_LD(0.2, 0.4)["9x10^6_LD"])
    all_aero_foils.append(NACA)


for index, value in enumerate(Cl_stuff_3):
    three = np.average(value)
    six = np.average(Cl_stuff_6[index])
    nine = np.average(Cl_stuff_9[index])
    avg = (six + nine + three) / 3
    print(f"{index}     {three}     {six}      {nine}     {avg}")

aero = all_aero_foils[111]
Cl_max = aero.data[""]


N = all_aero_foils[111]
N.print_file()
N.plot_all_data()

e = 0.9
CL = 0.3
AR = np.arange(5, 10, 0.1)
induced_drag = CL / (e * np.pi *AR)
weight = AR**(0.5)

CL__ = np.array(N.data["CL_vs_alpha"]["6x10^6"]["CL"])
alpha__ = np.array(N.data["CL_vs_alpha"]["6x10^6"]["alpha"])

alpha_ = np.array([])
CL_ = np.array([])

for index, value in enumerate(alpha__):
    if value > -5 and value < 5:
        print(value)
        alpha_ = np.append(alpha_, value)
        CL_ = np.append(CL_, CL__[index])

print(CL_)
print(alpha_)

X = np.append(alpha_.reshape(len(alpha_), 1), np.ones((len(alpha_), 1)), axis=1)

theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(CL_)
print(f'The parameters of the line: {theta}')
y_line = X.dot(theta)

Cl_ascpect_5 = CL__ / (1 + (CL__) / (e* np.pi *5))
Cl_ascpect_6 = CL__ / (1 + (CL__) / (e* np.pi *6))
Cl_ascpect_7 = CL__ / (1 + (CL__) / (e* np.pi *7.5))
Cl_ascpect_8 = CL__ / (1 + (CL__) / (e* np.pi *8))
Cl_ascpect_9 = CL__ / (1 + (CL__) / (e* np.pi *9))
Cl_ascpect_10 = CL__ / (1 + (CL__) / (e* np.pi *10))

a_5 = theta[1] / ((1 + 57.3*theta[1] )/(np.pi * e * 5))
a_6 = theta[1]  / ((1 + 57.3*theta[1] )/(np.pi * e * 6))
a_7 = theta[1]  / ((1 + 57.3*theta[1] )/(np.pi * e * 7.5))
a_8 = theta[1]  / ((1 + 57.3*theta[1] )/(np.pi * e * 8))
a_9 = theta[1]  / ((1 + 57.3*theta[1] )/(np.pi * e * 9))
a_10 = theta[1]  / ((1 + 57.3*theta[1] )/(np.pi * e * 10))

theta_5 = copy.copy(theta)
theta_5[0] = a_5
theta_6 = copy.copy(theta)
theta_6[0] = a_6
theta_7 = copy.copy(theta)
theta_7[0] = a_7
theta_8 = copy.copy(theta)
theta_8[0] = a_8
theta_9 = copy.copy(theta)
theta_9[0] = a_9
theta_10 = copy.copy(theta)
theta_10[0] = a_10


x_alpha = np.linspace(-20,60,1000)

fig, axs = plt.subplots(1, 3)
print(f'The parameters of the line: {theta_10}')
axs[0].plot(AR, weight)
axs[0].set_xlabel(r'$AR$', fontsize=20)
axs[0].set_ylabel(r'$AW~(N)$', fontsize=20)
axs[0].axvspan(7, 8, facecolor='#2ca02c', alpha=0.5)
axs[0].axvline(x=7.5, color='black', linestyle='--', label = "Chosen AR = 7.5")
axs[0].legend(loc = 3)
axs[1].plot(AR,induced_drag)
axs[1].set_xlabel(r'$AR$', fontsize=20)
axs[1].set_ylabel(r'$C_{Di}$', fontsize=20)
axs[1].axvspan(7, 8, facecolor='#2ca02c', alpha=0.5)
axs[1].axvline(x=7.5, color='black', linestyle='--', label = "Chosen AR = 7.5")
axs[1].axvline(x=9, color='purple', linestyle='-.', label = "AR with winglets = 7.5")
axs[1].legend(loc = 3)
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], N.data["CL_vs_alpha"]["6x10^6"]["CL"])
#axs[2].plot(alpha_, CL_)
#axs[2].plot(alpha_, y_line)
axs[2].plot(alpha_, X.dot(theta_5), 'o-', label="AR = 5")
axs[2].plot(alpha_, X.dot(theta_6), 'v-', label="AR = 6")
axs[2].plot(alpha_, X.dot(theta_7),'^-', label="AR = 7.5")
axs[2].plot(alpha_, X.dot(theta_8), '<-', label="AR = 8")
axs[2].plot(alpha_, X.dot(theta_9), '>-', label="AR = 9")
axs[2].plot(alpha_, X.dot(theta_10), label="AR = 10")
axs[2].set_xlabel(r'$AoA ~(^\circ)$', fontsize=20)
axs[2].set_ylabel(r'$C_L$', fontsize=20)
axs[2].grid()
axs[2].legend(loc=4)



axs[0].grid()
axs[1].grid()
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], Cl_ascpect_6)
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], Cl_ascpect_7)
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], Cl_ascpect_8)
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], Cl_ascpect_9)
#axs[2].plot(N.data["CL_vs_alpha"]["6x10^6"]["alpha"], Cl_ascpect_10)

plt.show()
#N.print_LD()