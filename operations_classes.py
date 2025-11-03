from datetime import datetime
from base_classes import LogMessage


class Operations:
    @classmethod
    def parse_log_message(cls, log_message):
        if log_message[0] == '*':
            log_message = log_message[1:]
        message_list = log_message.split(': ')
        date_time_str = message_list[0]
        date_time = datetime.strptime(date_time_str, "%b %d %Y %H:%M:%S.%f")
        facility = message_list[1].split('-')[0][1:]
        severity = int(message_list[1].split('-')[1])
        event_type = message_list[1].split('-')[2]
        if len(message_list) > 3:
            message = ' '.join(message_list[2:])
        else:
            message = message_list[2]
        return LogMessage(
            date_time=date_time,
            facility=facility,
            severity=severity,
            event_type=event_type,
            message=message
            )

    @classmethod
    def parse_log_file(cls, filename):
        log_message_objs = []
        with open(filename, 'r') as file:
            for line in file:
                log_message = cls.parse_log_message(line)
                log_message_objs.append(log_message)
        return log_message_objs