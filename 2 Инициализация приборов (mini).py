import MOKO
import MOSC
import MGPH
import MFRT
import time

# Uin_PS = MOKO.Report("Uin_PS", "get", "string", "", "float")
# Iin_PS = MOKO.Report("Iin_PS", "get", "string", "", "float")
# Uout_EL = MOKO.Report("Uout_EL", "get", "string", "", "float")
# Iout_EL = MOKO.Report("Iout_EL", "get", "string", "", "float")


def InitDevice(name: str):
    MOKO.Driver(name, "init")
    # time.sleep(3)
    # MOKO.Driver(name, "Check")

    MOKO.Program('tree', 'set', 'chosen=passed')

#Region Инициализация
#description: Измеряемый \nпараметр;Диапазон \nизмерений; ID прибора;

MOKO.Program('tree', 'set', f'select = Инициализация DMM6500_04582450')
InitDevice("DMM6500_04582450")    #hesh Инициализация DMM6500_04582450: Uout; 0 - 20 VDC; ...450

MOKO.Program('tree', 'set', f'select = Инициализация Keysight66332A')
InitDevice("Keysight66332A")      #hesh Инициализация Keysight66332A:      Uout; 0 - 20 VDC; ...910

#EndRegion Инициализация





#Region Настройка параметров
#description: Уст. \nпараметр;Диапазон \nустановки; ID прибора;

#hesh Настройка DMM6500_04582450: VDC; 0 - 20 VDC; ...450

MOKO.Program('tree', 'set', f'select = Настройка DMM6500_04582450')

MOKO.Driver('DMM6500_04582450', 'set', 'Function = VDC')
time.sleep(1)
MOKO.Driver('DMM6500_04582450', 'set', 'Range = Auto')
time.sleep(1)

MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################

#hesh Настройка Keysight66332A: VDC; 0 - 20 VDC; ...545

MOKO.Program('tree', 'set', f'select = Настройка Keysight66332A')

MOKO.Driver('DMM6500_04625545', 'set', 'Function = VDC')
time.sleep(1)
MOKO.Driver('DMM6500_04625545', 'set', 'Range = Auto')
time.sleep(1)

MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################


#EndRegion Настройка параметров

MOKO.EndScript('passed')