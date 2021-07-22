import SerialLib.SerialLib as SerialLib

def import_bits(imported_bits, imported_bit_info, port:str, baudrate:int, timeout:int, numBytes:int, nf_cr:bool, c_nl:bool, progress):
    
    reader = SerialLib.reader(port, baudrate, timeout, numBytes, nf_cr, c_nl) # initialize the reader object

    reader.check_port() # check the users port

    reader.read_serial() # init the transfer

    reader.format_data() # format data as desired

    imported_bits.set_bytes(0, reader.get_bytes()) # import the bits from the serial reader

    imported_bit_info.set_metadata("Port", port)
    imported_bit_info.set_metadata("Baudrate", str(baudrate))
    imported_bit_info.set_metadata("Timeout", str(timeout))
    imported_bit_info.set_metadata("Number of Bytes", str(numBytes))
    imported_bit_info.set_metadata("Cariage and Newline", str(c_nl))

    progress.set_progress(1,1)