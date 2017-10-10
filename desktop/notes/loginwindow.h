#ifndef LOGINWINDOW_H
#define LOGINWINDOW_H

#include <QMainWindow>
#include <QSettings>

class QByteArray;
class QNetworkAccessManager;
class QNetworkReply;

namespace Ui {
class LoginWindow;
}

class LoginWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit LoginWindow(QWidget *parent = 0);
    ~LoginWindow();

    void BuildLogin();
private slots:
    void on_login_pushButton_clicked();
    void OnResponseReadyToRead();
    void OnResponseReadFinished();

private:
    Ui::LoginWindow *ui;
    void NetworkCleanup();
    QNetworkAccessManager * mNetMan;
    QNetworkReply * mNetReply;
    QByteArray * mDataBuffer;
};

#endif // LOGINWINDOW_H
