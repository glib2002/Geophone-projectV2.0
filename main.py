

import time
import ADS1256
import FileReader
import RPi.GPIO as GPIO


try:
    
    ADC = ADS1256.ADS1256()
    
    ADC.ADS1256_init()
    print("RUNNING  :  "+time.ctime())
    print("=============================================================")
    Reader = FileReader.FileReader()
    file = Reader.openFile('geophone_file_test_'+time.ctime()+'.txt', 'w')

    file.write("first geophone " + "         "+"second geophone "+ '\n')

    file.flush()
    print("First geophone"+"                                 "+"Second geophone")
    start = time.time()
    while(1):


        ADC_Value = ADC.ADS1256_GetAll() 
        raw_1 =ADC_Value[2]
        raw_2 = ADC_Value[4]
        file.write(str(raw_1)+"                 "+ str(raw_2) +'\n')
        file.flush()
        print (("(1) binary code : "+ str(raw_1) +"   " + "Voltage :  "+str(raw_1*5.0/0x7fffff))+"   |||  " +"(2) binary code : "+ str(raw_2) +"   " + "Voltage :  "+str(raw_2*5.0/0x7fffff))
        operationalTime = time.time()
        if((operationalTime-start)>180):
            file.flush()
            file.close()
            break

except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
