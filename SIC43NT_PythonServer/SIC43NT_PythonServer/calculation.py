from SIC43NT_PythonServer.utils.keystream import Keystream

class Calculate():
    uid = ''
    key = ''

    flag_tamper = ''
    time_stamp = ''
    time_stamp_int = 0
    rolling_code = ''

    flag_tamper_from_server = 'N/A'
    time_stamp_from_server = 'N/A'
    rolling_code_from_server = 'N/A'

    flag_tamper_decision = 'N/A'
    time_stamp_decision = 'N/A'
    rolling_code_decision = 'N/A'

    def get_updated_data(self, raw_data):
        if len(raw_data) == 32:
            self.uid = raw_data[0:14]
            self.key = 'FFFFFF' + self.uid
            self.flag_tamper = raw_data[14:16]
            self.time_stamp = raw_data[16:24]
            self.time_stamp_int = int(self.time_stamp, 16)
            self.rolling_code = raw_data[24:32]
            keystream = Keystream()
            self.rolling_code_from_server = keystream.stream(self.key, self.time_stamp, 4).upper()
        
            if self.rolling_code == self.rolling_code_from_server:
                self.rolling_code_decision = 'Correct'
            else:
                self.rolling_code_decision = 'Incorrect'
