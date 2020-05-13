from shell import FtpShell
from ftp_core import FileService
from ftp_core import LocalFtpClient


if __name__ == '__main__':
    file_service = FileService('../data')
    ft_client = LocalFtpClient(file_service)
    FtpShell(ft_client).cmdloop()
