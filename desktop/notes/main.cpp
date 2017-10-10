#include "loginwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    app.setOrganizationName ("pyprism");
    app.setOrganizationDomain("pyprism.me");
    app.setApplicationName ("Hiren_Notes");
    app.setApplicationDisplayName ("Hiren Notes");
    app.setWindowIcon(QIcon(":/new/img/text_editor.svg"));
    LoginWindow w;
    w.show();

    return app.exec();
}
