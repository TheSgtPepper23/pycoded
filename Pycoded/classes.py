from abc import ABC, abstractmethod
import os
import base64

class File(ABC):
    def __init__(self, filename):
        super().__init__()
        self.name, self.ext = os.path.splitext(filename)
        self.name_ext = filename

    @abstractmethod
    def readf(self):
        pass

    @abstractmethod
    def writef(self, content, output=None):
        pass
    

class TextFile(File):
    def __init__(self, filename):
        super().__init__(filename)

    def readf(self):
        content = ""
        with open(self.name_ext, "r") as file:
            content = file.read()

        return content.encode()
    
    def writef(self, content, output=None):
        content = content.decode()
        if output == None:
            full_name = self.name + "_pycoded" + self.ext
        else:
            full_name = output
        
        with open(full_name, "w") as file:
            file.write(content)


class ImageFile(File):
    def __init__(self, filename):
        super().__init__(filename)

    def readf(self):
        content = ""
        with open(self.name_ext, "rb") as file:
            content = file.read()
    
        return content

    def writef(self, content, output=None):
        if output == None:
            full_name = self.name + "_pycoded" + self.ext
        else:
            full_name = output

        with open(full_name, "wb") as file:
            file.write(content)

if __name__ == "__main__":
    text = ImageFile("leon.jpg")
    print(text.readf())
