class LogMessage:
    def __init__(self, date_time, facility, severity, mnemonic, message):
        self._date_time = date_time
        self._facility = facility
        self._severity = severity
        self._mnemonic = mnemonic
        self._message = message

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        self._date_time = value

    @property
    def facility(self):
        return self._facility

    @facility.setter
    def facility(self, value):
        self._facility = value

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, value):
        if value < 0 or value > 7:
            raise ValueError("Severity ranges from 0 to 7")
        self._severity = value

    @property
    def mnemonic(self):
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, value):
        self._mnemonic = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def __str__(self):
        return f"{self.date_time}: %{self.facility}-{self.severity}-{self.mnemonic}: {self.message}"

    def old_message(self):
        pass

    def new_message(self):
        pass

    def is_critical(self):
        return self.severity >= 5


