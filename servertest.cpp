
#include "server.h"

#include <QObject>
#include <QDebug>

int main(int argc, char** argv)
{
    Server server;
    auto m2 = server.call2();
    if (m2->metaObject()->className() == QStringLiteral("Method2")) {
        qDebug() << "PASS";
        return 0;
    }
    qDebug() << "FAIL";
    return 1;
}
