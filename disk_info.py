
import shutil

def disk_percent_usage(directory):
        '''
        Return percent usage of disk where directory resides
        '''
        disk_info = shutil.disk_usage(directory)
        return round(disk_info.used * 100 / disk_info.total, 2)


