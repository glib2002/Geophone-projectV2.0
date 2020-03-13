class FileReader:


#    READING: 'r'  # opening for reading
    #   WRITING: 'w'  # opening for writing if dont exists creates new one
    #  EXCEPTION: 'x'  # opening for writing if dont exists throws exception
    #  REWRITE: '+a'  # opening for rewriting
    #  BINARY: 'b'  # opening in binary mode


    def openFile(self ,name ,filemode):
        file = open(name, filemode);
        return file

    def readFile(self ,file ,symbols):
        return file.read(symbols)

    def readAll(self ,file):
        str = file.read()
        return str

    def writeFile(self ,data ,file):
        file.write(str(data ) +'\n')


    def closeFile(self ,file):
        file.close()

    def getName(self ,file):
        return file.name

    def isClosed(self ,file):
        return file.closed

    def getMode(self ,file):
        return file.mode