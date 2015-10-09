import re
import time

class Tail(object):
    line_delimiters = ('\r\n', '\r', '\n')

    def __init__(self, file, read_size=1024):
        self.read_size = read_size
        self.file = file

    def __del__(self):
        self.close()

    def close(self):
        self.file.close()

    def seek_end(self):
        # go to the end
        self.seek(0, 2)

    def seek(self, pos, whence=0):
        self.file.seek(pos, whence)

    def seek_line(self):
        pos = end_pos = self.file.tell()

        read_size = self.read_size
        if pos > read_size:
            pos -= read_size
        else:
            pos = 0
            read_size = end_pos

        self.seek(pos)

        bytes_read, read_str = self.read(read_size)

        if bytes_read and read_str[-1] in self.line_delimiters:
            # The last character is a line delimiter, don't count this one
            bytes_read -= 1

            if read_str[-2:] == '\r\n' and '\r\n' in self.line_delimiters:
                # found carriage return and newlines
                bytes_read -= 1

        while bytes_read > 0:          
            # Scan backward, counting the newlines in this bufferpool
            i = bytes_read - 1
            while i >= 0:
                if read_str[i] in self.line_delimiters:
                    self.seek(pos + i + 1)
                    return self.file.tell()
                i -= 1

            if pos == 0 or pos - self.read_size < 0:
                # Not enought lines in the buffer, send the whole file
                self.seek(0)
                return None

            pos -= self.read_size
            self.seek(pos)

            bytes_read, read_str = self.read(self.read_size)

        return None

    def read(self, read_size=None):
        if read_size:
            read_str = self.file.read(read_size)
        else:
            read_str = self.file.read()

        return len(read_str), read_str

    def tail(self, lines=10):
        self.seek_end()
        end_pos = self.file.tell()

        for i in range(lines):
            if not self.seek_line():
                break

        data = self.file.read(end_pos - self.file.tell() - 1)
        if data:
            return self.split(data)
        else:
            return []

    def follow(self, delay=1.0):
        trailing = True       
        
        while 1:
            where = self.file.tell()
            line = self.file.readline()
            if line:    
                if trailing and line in self.line_delimiters:
                    # This is just the line delimiter added to the end of the file
                    # before a new line, ignore.
                    trailing = False
                    continue

                if line[-1] in self.line_delimiters:
                    line = line[:-1]
                    if line[-1:] == '\r\n' and '\r\n' in self.line_delimiters:
                        # found crlf
                        line = line[:-1]

                trailing = False
                yield line
            else:
                trailing = True
                self.seek(where)
                time.sleep(delay)

    def split(self, data):
        return re.split("|".join(self.line_delimiters), data)

