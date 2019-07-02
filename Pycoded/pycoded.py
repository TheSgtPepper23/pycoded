from optparse import OptionParser
from classes import TextFile, ImageFile
from base64 import b64encode, b64decode

def initialize_parser():
    usage = "Usage: %prog [options] filename/text"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--decode", dest="decode", action="store_true",
                      help="Indicates that you want to decode the file (encode by default).", default=False)
    parser.add_option("-o", "--output", dest="output",
                      help="The name of the outputfile.(samename_pycoded.ext by default)", metavar="FILE")
    parser.add_option("-i", "--image", dest="image", action="store_true",
                      help="Indicate that the file is an image and not a text file.", default=False)
    parser.add_option("-t", "--text", dest="text", help="If you only like to encode text rather than a file",
                    default=False, action="store_true")

    return parser

def encoder(content):
    return b64encode(content)

def decoder(content):
    return b64decode(content)


if __name__ == "__main__":
    parser = initialize_parser()

    (options, args) = parser.parse_args()
    
    if options.text and options.output != None or options.text and options.image:
        parser.error("You are encoding/decoding text, the -i and -o options are only for files.")

    if len(args) != 1:
        parser.error("Wrong number of arguments.")

    if options.text:
        content = args[0]
        content = content.encode()

        if options.decode:
            print(decoder(content).decode())
        else:
            print(encoder(content).decode())
    else:
        filename = args[0]
        if options.image:
            file_object = ImageFile(filename)
            
        else:
            file_object = TextFile(filename)

        if options.decode:
            try:
                modified_content = decoder(file_object.readf())
            except FileNotFoundError:
                parser.error("No such file.")
        else:
            try:
                modified_content = encoder(file_object.readf())
            except FileNotFoundError:
                parser.error("No such file.")


        file_object.writef(modified_content, options.output)
