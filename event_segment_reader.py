import struct
import os
import event_pb2


class EventSegmentReader:

    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError('File does not exist')
        self.path = path

    def read_event(self, event_number):
        if event_number < 0:
            raise ValueError('Event number must be positive')

        count = 0
        for event in self.read_events():
            if count == event_number:
                return event
            count += 1

    def read_events(self):
        with open(self.path, 'rb') as f:
            # first 5 bytes are skipped
            f.seek(5)

            while not self._is_eof(f):
                yield from self._read_transaction(f)

    def _read_transaction(self, f):
        size = struct.unpack('>i', f.read(4))

        version = struct.unpack('>b', f.read(1))
        number_of_messages = struct.unpack('>h', f.read(2))

        for message in range(number_of_messages[0]):
            yield from self._read_event(f)

        f.read(4)

    def _read_event(self, f):
        size = struct.unpack('>i', f.read(4))

        event_data = f.read(size[0])
        event = event_pb2.Event()

        event.ParseFromString(event_data)
        yield event

    def _is_eof(self, f):
        current_position = f.tell()
        size = struct.unpack('>i', f.read(4))
        f.seek(current_position)
        return size[0] == -1 or size[0] == 0
