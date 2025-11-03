from base_classes import LogMessage
from operations_classes import Operations
from datetime import datetime, timedelta

def main():
    log_message_objs = Operations.parse_log_file("log_messages.txt")
    for obj in log_message_objs:
        if obj.is_critical():
            print(obj.message.strip())

if __name__ == "__main__":
    main()