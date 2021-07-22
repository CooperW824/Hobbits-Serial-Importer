
import serial
import subprocess

class reader():

    port = ""
    baudrate = 0
    timeout = 0
    numBytes = 0
    car_and_NL = False
    nf_cr = False
    __returnbytes = bytearray()
    __dataRead = bytes
    __dataList = []


    def __init__(self, port:str, baudrate:int, timeout:int, bytesNum:int, nf_cr:bool,cariage_and_NL:bool):
        """
        Initialize the reader with the necessary information, serial port address, baudrate, timeout duration,
        and the number of bytes to read, and check if the timeout is 0, and if it is then set the timeout to None.

        Caveats:
            The serial reader will read until one of two possible conditions are met, either the timeout duration 
            (set by timeout) is reached, or until the maximum nuber of bytes to read (set by bytesNum) is reached

        Args:
            port (str): [The serial port to read from, ex: /dev/ttyACM0]
            baudrate (int): [The baudrate that the serial port/device is working on, baudrate describes the maximum number of bits transfered per second]
            timeout (int): [How long for the reader to read from the serial port before stopping, set to 0 for no timeout]
            bytesNum (int): [How many bytes (not bits) for the serial reader to read in befor stopping]
            nf_cr (bool): [Should hobbits create a new frame on a carriage return or not]
            cariage_and_NL (bool): [Should the Cariage Return and Newline Symbols be included in the output, Set False to remove items]
        """

        self.port = port
        self.baudrate = baudrate
        self.numBytes = bytesNum
        self.car_and_NL = cariage_and_NL
        self.nf_cr = nf_cr

        if timeout == 0:
            self.timeout = None
        else:
            self.timeout = timeout


    def check_port(self):

        """
        Checks to see if the port selected is a valid and active port, raises a PortError exception if the port is invalid.

        Raises:
            PortError: [Raised if the port selected is not a valid or active port, alerts the user to the issue and gives troubleshooting suggestions.]
        """

        match = False

        ports  = subprocess.check_output(["python3", "-m", "serial.tools.list_ports"]) #gets a list of active ports using the tools provided by the pyserial module

        ports  = str(ports) # convert bytes to string 
        ports = ports[2:len(ports)-1] #getting rid of extra stuff
        ports = ports.split('\\n') # spliting on each different active port

        for i in range(0, len(ports)): # for each port in the list ports, check if the port is equal to the one the user entered
           ports[i] = ports[i].replace(" ", "") # removes trailing whitespace from getting the port list
           if ports[i] == self.port: # if it matches
               match = True # set match to true

        if match == False: # if no matches are found alert the user
            errorstr = "\n\nCould not find " + self.port + " Please check that the device is plugged in and you are using the correct port name. Active Ports:\n"
            for i in ports:
                errorstr += i +"\n" 
            raise PortError(errorstr)

    def read_serial(self):

        """
        Reads the serial data comming off the serial port the user selected, 
        at the baudrate the user selected, for the timeout the user selected, 
        and the number of bytes the user selected then closes the Serial object. 

        Caveats:
            The serial reader will read until one of two possible conditions are met, either the timeout duration 
            (set by timeout) is reached, or until the maximum nuber of bytes to read (set by bytesNum) is reached.
        """

        serial_reader = serial.Serial(self.port, self.baudrate, timeout=self.timeout) # setup the serial reader
        self.__dataRead = serial_reader.read(self.numBytes) # start reading upto 100 bytes, store the data into __dataRead
        serial_reader.close() # close after reading 

    
    def format_data(self):

        """
        Formats the serial data so that it can have \r\n removed, and formated back to binary.
        """
        if self.nf_cr:
            self.__dataRead = self.__dataRead.decode()
            self.__dataList = self.__dataRead.split("\r\n")
            for i in range(0, len(self.__dataList)):
                if self.car_and_NL:
                    self.__dataList[i]+="\r\n"
                
                
        if self.car_and_NL == False:
            self.__dataRead = self.__dataRead.decode()
            self.__dataRead = self.__dataRead.replace("\r\n", "")
            self.__returnbytes = bytearray(self.__dataRead, encoding="utf-8")
        else:
            self.__returnbytes = self.__dataRead
            
       


    def get_bytes(self):

        """
        Return the byte array that is found at the private var __returnbytes

        Returns:
            [bytes]: [Value of __returnbytes]
        """

        return self.__returnbytes

    
    def get_string(self):

        """
        Returns the value of __dataRead after formatting 

        Returns:
            [bytes | str]: [value of __dataRead]
        """

        return self.__dataRead


class PortError(Exception):

    """
    Custom Exception for the reader.check_port() method used to alert the user that the port inputed is invalid.
    """

    pass