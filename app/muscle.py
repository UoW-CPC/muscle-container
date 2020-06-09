#!/usr/bin/python
import sys
from random import choice
from string import ascii_uppercase

sys.path.append("../")
from app.lib.input import Input
from app.lib.logsys import Log
from app.lib.system import System

def main():

    log = Log(''.join(choice(ascii_uppercase) for i in range(12)))
    Log.info('------------------------------')
    Log.info('MUSCLE Process Starts')
    Log.info('------------------------------')
    inputArgs = sys.argv
    args = inputArgs[1:]
    filePath, fileName = Input.getValues(args)
    Log.info('Path:')
    Log.info(filePath)
    Log.info('Filename:')
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
    outputFilePath = filePath.replace('in', 'out')
    outputFilePath = outputFilePath.replace('fas', 'afas')
    Log.info('Starting MUSCLE..')
    print(filePath, outputFilePath)
    (ret, out, err) = muscle(filePath,outputFilePath)
    Log.info("return, {}".format(ret))
    Log.info("output, {}".format(out))
    Log.error("error, {}".format(err))
    Log.info('------------------------')
    Log.info('MUSCLE Process Completes')
    Log.info('------------------------')

def muscle(input, output):
    (ret, out, err) = System.command(
        ['bin/muscle',
         '-in', input,
         '-out', output])
    return ret,out,err

if __name__ == "__main__":
    main()