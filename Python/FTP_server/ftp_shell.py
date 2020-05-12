import cmd
import os
from local_ftp_client import LocalFtpClient


class FtpShell(cmd.Cmd):
    prompt = "$ "
    intro = "Welcome to MAMA-FT Server\nEnter a command: (?) for help"

    def __init__(self, client: LocalFtpClient):
        super().__init__(completekey='tab')
        self.ft_client = client

    # Save options
    def do_save(self, inp):
        src, out = inp.split()

        try:
            self.ft_client.save_file(src, out)
        except FileNotFoundError:
            print(f"The file can't be found or doesnt exist: {src}")

    @staticmethod
    def help_save():
        print("Saves a file onto the ft server")
        print("save [file source] [file output]")

    # General utilities
    @staticmethod
    def do_exit(self):
        print("Exiting, See you soon")
        return True

    @staticmethod
    def help_exit(self):
        print("exit the application. Shorthand: 'exit', 'Ctrl-D'.")

    @staticmethod
    def do_cls(self):
        os.system('clear')

    @staticmethod
    def help_cls():
        print("Clears the screen")

    def default(self, line):
        if line == 'q' or line == ':q':
            return self.do_exit(line)
        elif line == 'cls':
            return os.system('clear')

