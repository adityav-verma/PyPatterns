class Buffer:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.buffer = [''] * (self.height * self.width)

    def write(self, text):
        self.buffer.append(text)

    def __getitem__(self, item):
        return self.buffer[item]


class ViewPort:
    def __init__(self, buffer: Buffer):
        self.buffer = buffer
        self.offset = 0

    def append(self, text):
        self.buffer.write(text)

    def get_char_at(self, index):
        return self.buffer[index + self.offset]


# A facade over the above complex components

class Console:
    def __init__(self):
        buffer = Buffer
        view_port = ViewPort(buffer)
        self.buffers = [buffer]
        self.current_view_port = view_port
        self.view_ports = [self.current_view_port]

    # A high level API
    def write(self, text):
        self.current_view_port.buffer.write(text)

    # A low level API
    def get_char_at(self, index):
        return self.current_view_port.get_char_at(index)


if __name__ == '__main__':
    # As we can see here, a facade is Providing a very simple interface
    c = Console()
    c.write('Hello world')