import time
import os
import sys

class Logger(object):

    def __init__(self, stream=sys.stdout):
        output_dir = "log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H-%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    sys.stdout = Logger(sys.stdout)  #  将输出记录到log
    sys.stderr = Logger(sys.stderr)  # 将错误信息记录到log
    i = 0
    while True:
        time.sleep(5)
        i+=1
        print("loger ",i)
