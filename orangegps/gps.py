import time


class GPS:
    def __init__(self, serial_connection):
        self.gps_serial = serial_connection

    def get(self) -> (float, float, str, str):
        while True:
            line = self.gps_serial.readline()
            buffer: str = line.decode()
            buffer = buffer.replace("\\r", "")
            buffer = buffer.replace("\\n", "")
            buffer = buffer.replace("\\", "")
            parts = buffer.split(',')
            gps_sattelite = parts[0][1:3]
            id_number = parts[0][3:]
            #print(gps_sattelite, parts[0][3:])
            if gps_sattelite not in ("GA", "GB", "GI", "GL", "GP", "GQ", "GN"):
                return None, None, None, None
            if id_number:
                #print(parts)
                latitude = self._convert_to_degree(parts[2])
                if parts[3] == 'S':
                    latitude = -latitude
                longitude = self._convert_to_degree(parts[4])
                if parts[5] == 'W':
                    longitude = -longitude
                satellites = parts[7]
                gps_time = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1]
                return latitude, longitude, satellites, gps_time
            time.sleep(1)

    def _convert_to_degree(self, raw_degrees):
        raw_as_float = float(raw_degrees)
        first_digits = int(raw_as_float / 100)
        next_two_digits = raw_as_float - float(first_digits * 100)

        converted = float(first_digits + next_two_digits / 60.0)
        converted = '{0:.6f}'.format(converted)
        return float(converted)