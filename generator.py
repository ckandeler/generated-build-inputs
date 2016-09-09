#!/usr/bin/env python

import os, sys

if len(sys.argv) == 4 and sys.argv[1] == "--list":
    outPath = sys.argv[2]
    numFiles = int(sys.argv[3])

    print(os.path.join(outPath, "server.h"))

    for num in range(numFiles):
        print(os.path.join(outPath, "method%s.h" % num))

    sys.exit(0)

if len(sys.argv) == 3:
    outPath = sys.argv[1]
    numFiles = int(sys.argv[2])

    if not os.path.exists(outPath):
        os.makedirs(outPath)
else:
    print("Incorrect args. Use ./generator.py [--list] /path/to/output numFiles")

with open(os.path.join(outPath, "server.h"), "w") as serverFile:

    for num in range(numFiles):
        serverFile.write('#include "method%s.h"\n' % num)

    serverFile.write("""
class Server {
public:
""")

    for num in range(numFiles):
        serverFile.write('    Method%s* call%s() { return new Method%s; }\n' % (num, num, num))

    serverFile.write("""};

""")

for num in range(numFiles):
    with open(os.path.join(outPath, "method%s.h" % num), "w") as methodFile:
        methodFile.write("""
#include <QObject>

class Method%s : public QObject {
  Q_OBJECT
};
""" % num)
