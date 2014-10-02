backup-rotate
=============

Backups rotate script

Command line script for save only important dumps.

Example for parameters
======================
<pre>
$ python ./backup-rotate.py -h 
usage: backup-rotate.py [-h] [-d daily] [-w daily] [-m monthly]
                        [--really-remove-files] [--silent]
                        &lt;path&gt;
 
Rotate old backup files by date.
 
positional arguments:
 &lt;path&gt;                path to backups dir

optional arguments:
  -h, --help            show this help message and exit
  -d daily              how many backups save with delta time 1 day (= 10)
  -w daily              how many backups save with delta time 1 week (= 10)
  -m monthly            how many backups save with delta time 1 month (= inf)
  --really-remove-files
                        really remove too old files (by default just print)
  --silent              don`t print save/remove table
</pre>


Example how it work
===================
<pre>
$ python ./backup-rotate.py --really-remove-files /root/backup/archive/
0 file(s) for del
+ | 114 dago | Wed Jun 11 01:54:40 2014 | /root/backup/archive/dump-2014-06-11.7z
+ |  31 days | Sat Jul 12 02:18:34 2014 | /root/backup/archive/dump-2014-07-12.7z
+ |   4 days | Wed Jul 16 02:22:20 2014 | /root/backup/archive/dump-2014-07-16.7z
+ |   7 days | Wed Jul 23 02:32:36 2014 | /root/backup/archive/dump-2014-07-23.7z
+ |   7 days | Wed Jul 30 02:29:42 2014 | /root/backup/archive/dump-2014-07-30.7z
+ |   8 days | Thu Aug  7 02:06:20 2014 | /root/backup/archive/dump-2014-08-07.7z
+ |   7 days | Thu Aug 14 02:06:19 2014 | /root/backup/archive/dump-2014-08-14.7z
+ |   7 days | Thu Aug 21 02:36:06 2014 | /root/backup/archive/dump-2014-08-21.7z
+ |   7 days | Thu Aug 28 02:13:30 2014 | /root/backup/archive/dump-2014-08-28.7z
+ |   7 days | Thu Sep  4 01:48:51 2014 | /root/backup/archive/dump-2014-09-04.7z
+ |   8 days | Fri Sep 12 01:46:59 2014 | /root/backup/archive/dump-2014-09-12.7z
+ |   1 days | Sat Sep 13 01:47:08 2014 | /root/backup/archive/dump-2014-09-13.7z
+ |   6 days | Fri Sep 19 01:48:16 2014 | /root/backup/archive/dump-2014-09-19.7z
+ |   2 days | Sun Sep 21 01:49:19 2014 | /root/backup/archive/dump-2014-09-21.7z
+ |   1 days | Mon Sep 22 01:47:54 2014 | /root/backup/archive/dump-2014-09-22.7z
+ |   2 days | Wed Sep 24 01:48:51 2014 | /root/backup/archive/dump-2014-09-24.7z
+ |   1 days | Thu Sep 25 01:48:24 2014 | /root/backup/archive/dump-2014-09-25.7z
+ |   1 days | Fri Sep 26 01:49:00 2014 | /root/backup/archive/dump-2014-09-26.7z
+ |   1 days | Sat Sep 27 01:48:16 2014 | /root/backup/archive/dump-2014-09-27.7z
+ |   1 days | Sun Sep 28 01:48:58 2014 | /root/backup/archive/dump-2014-09-28.7z
+ |   2 days | Tue Sep 30 01:48:24 2014 | /root/backup/archive/dump-2014-09-30.7z
+ |   1 days | Wed Oct  1 01:48:51 2014 | /root/backup/archive/dump-2014-10-01.7z
+ |   1 days | Thu Oct  2 01:49:05 2014 | /root/backup/archive/dump-2014-10-02.7z
</pre>
