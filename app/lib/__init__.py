import sys
import math

sys.path.append("../")
from app.lib.input import Input
from app.lib.logsys import Log

def main():
    Log.info('------------------')
    Log.info('Split task Starts')
    Log.info('------------------')
    inputArgs = sys.argv
    args = inputArgs[1:]
    filePath, fileName = Input.getValues(args)
    Log.info('Path:')
    Log.info(filePath)
    Log.info('File name:')
    Log.info(fileName)
    try:
        with open(filePath) as f:
            lines = sum(1 for _ in f)
    except  EnvironmentError as e:
        Log.error('Input file error:')
        Log.error(e)
        Log.exit()
    Log.info('Number of sequences:')
    Log.info(lines/2)
    Log.info('The dataset is being splittted in files of 50 sequences.')
    Log.info('Total files:')
    filesNumber = math.ceil(lines/100)
    Log.info(filesNumber)
    filesList = []
    count = 0
    Log.info('File names:')
    Log.info('---------------------')
    Log.info('Split task Completes')
    Log.info('---------------------')

if __name__ == "__main__":
    main()
