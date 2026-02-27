import MOKO
from MOSC import HeshStatus, hesh_passed, hesh_failed
import MGPH
from MFRT import *
import random
from datetime import datetime
import time


def VDC(voltage_value: (str | float | int), hesh: str, tolerance: float = 0.1) -> None:

    if HeshStatus(hesh):

        MOKO.Driver('Keysight66332A', 'set', f'VDC = {voltage_value}')
        measured_value_str = MOKO.Driver('DMM6500_04625545', 'get', 'read','float')
        measured_value = float(measured_value_str)
        target_voltage = float(voltage_value)
        deviation = target_voltage - measured_value
        if abs(deviation) <= tolerance:
            status = 'Успешно'
            hesh_passed()
        else:
            status = 'Ошибка'
            hesh_failed()

        # 6. Записываем результаты в отчет
        # Формат: хэш;заданное напряжение;измеренное напряжение;отклонение;статус
        MOKO.Report("Results", "set", "table",f"{hesh};{voltage_value};{measured_value:.3f};{deviation:.3f};{status}")



MOKO.Report("Results", "info", "table", "Номер \\nзамера#120;"
                                                             "Установленное \\n напряжение#120;"
                                                             "Измеренное \\n напряжение#120;"
                                                             "Отклонение \\nнапряжение#120;"
                                                             "Статус #90;")


#Region Ход измерений
#description: Входное \nнапряжение, В;Погрешность,%;Нагрузка, Ом;

MOKO.Driver('Keysight66332A', 'set', 'OUTPUT = ON')

VDC('1','Измерение 1')   #hesh Измерение 1: 1;10;30;
VDC('2','Измерение 2')   #hesh Измерение 2: 2;10;30;
VDC('3','Измерение 3')   #hesh Измерение 3: 3;10;30;
VDC('4','Измерение 4')   #hesh Измерение 4: 4;10;30;
VDC('5','Измерение 5')   #hesh Измерение 5: 5;10;30;
VDC('6','Измерение 6')   #hesh Измерение 6: 6;10;30;
VDC('7','Измерение 7')   #hesh Измерение 7: 7;10;30;
VDC('8','Измерение 8')   #hesh Измерение 8: 8;10;30;
VDC('9','Измерение 9')   #hesh Измерение 9: 9;10;30;
VDC('10','Измерение 10')  #hesh Измерение 10: 10;10;30;
VDC('11','Измерение 11')  #hesh Измерение 11: 11;10;30;
VDC('12','Измерение 12')  #hesh Измерение 12: 12;10;30;
VDC('13','Измерение 13')  #hesh Измерение 13: 13;10;30;
VDC('14','Измерение 14')  #hesh Измерение 14: 14;10;30;
VDC('15','Измерение 15')  #hesh Измерение 15: 15;10;30;

#EndRegion Ход измерений


MOKO.EndScript('passed')