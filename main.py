from control import *
from inputClass import *

hostname = 'localhost'
username = 'root'
password = ''
database = 'hoteldb'



input1 = Input()



controlPanel = Control()
controlPanel.controlInput(input1,input1.userInput("enter 1-search, 2-show table, 3-input --> "))




