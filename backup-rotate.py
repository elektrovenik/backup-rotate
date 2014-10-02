# coding=utf-8
from dircache import listdir
import time
import argparse
import os.path
from os.path import isfile, join
import math

__author__ = 'kid'

parser = argparse.ArgumentParser(description='Rotate old backup files by date.')
parser.add_argument('path', metavar='<path>', type=str, nargs=1, help='path to backups dir')
parser.add_argument('-d', metavar='daily', type=int, nargs=1, default=10,
                    help='how many backups save with delta time 1 day (= 10)')
parser.add_argument('-w', metavar='daily', type=int, nargs=1, default=10,
                    help='how many backups save with delta time 1 week (= 10)')
parser.add_argument('-m', metavar='monthly', type=int, nargs=1, default=max,
                    help='how many backups save with delta time 1 month (= inf)')
parser.add_argument('--really-remove-files', action='store_true', default=False,
                    help='really remove too old files (by default just print)')
parser.add_argument('--silent', action='store_true', default=False,
                    help='don`t print save/remove table')

args = parser.parse_args()

backupsDirectory = args.path[0]
rotateSettings = {30: args.m, 7: args.w, 1: args.d}


# ищем файлы
files = []
for filename in listdir(backupsDirectory):
    fn = join(backupsDirectory, filename)
    if isfile(fn):
        files.insert(-1, [fn, os.path.getmtime(fn) if isfile(fn) else os.path.getctime(fn)])
    # print "file found: %s" % fn


# сортируем по возрастанию даты
def reverse_numeric(x, y):
    return 1 if (y[1] < x[1]) else -1

files = sorted(files, cmp=reverse_numeric)
lastFile = files[-1]

allFiles = files[:]

# фильтруем что удалять а что сохранить
allSavedFiles = []
for rotate in sorted(rotateSettings.keys(), reverse=False):
    # print rotate
    savedFiles = []
    lastTime = 0
    for (fileInfo) in files:
        days = round((fileInfo[1] - lastTime) / 3600 / 24)
        if days >= rotate:
            # print "last modified of %s (%s), %s days: %s" % (time.ctime(fileInfo[1]), fileInfo[1], days, fileInfo[0])
            lastTime = fileInfo[1]
            savedFiles.append(fileInfo)

    # больше чем надо
    if savedFiles.__len__() > rotateSettings[rotate]:
        ss = (savedFiles.__len__() - rotateSettings[rotate])
        savedFiles = savedFiles[ss:]

    # убираем сохраненные файлы из списка на удаление
    for ff in savedFiles:
        if ff in files:
            files.remove(ff)

    allSavedFiles.extend(savedFiles)

# всегда сохранять последний файл
if lastFile not in allSavedFiles:
    allSavedFiles.extend([lastFile])

# убираем сохраненные файлы из списка на удаление
for ff in allSavedFiles:
    if ff in files:
        files.remove(ff)

# if not args.really_remove_files
# print allSavedFiles.__len__()
# for ff in allSavedFiles:
#     print ff[0]

if not args.silent:
    print "%s file(s) for del" % files.__len__()


def get_max_days_digits(all_files):
    _dd = 0
    max_days = 0
    for _f1 in all_files:
        max_days = max(max_days, int(round((_f1[1] - _dd) / 3600 / 24)))
        _dd = _f1[1]

    return str(int(max(1, math.ceil(math.log(max_days, 10)))))

maxDaysDigs = get_max_days_digits(allFiles)

dd = 0
for f1 in allFiles:
    days = int(round((f1[1] - dd) / 3600 / 24))

    if not args.silent:
        print "%s | %s days | %s | %s" % ('+' if f1 in allSavedFiles else '-',
                                          ('{0:' + maxDaysDigs + 'd}').format(days), time.ctime(f1[1]), f1[0])
    dd = f1[1]

    # удаляем файл
    if args.really_remove_files:
        if f1 not in allSavedFiles:
            os.remove(f1[0])
