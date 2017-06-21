#include "loginwindow.h"
#include "ui_loginwindow.h"
#include <QDebug>

LoginWindow::LoginWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LoginWindow)
{
    ui->setupUi(this);
    ui->password_lineEdit->setEchoMode(QLineEdit::Password);
    ui->encrytion_lineEdit->setEchoMode(QLineEdit::Password);
    this->setWindowTitle ("Login");

    //QSettings settings;
    //ui->server_lineEdit->setText (settings.value ("url"));
}

LoginWindow::~LoginWindow()
{
    delete ui;
}

void LoginWindow::on_login_pushButton_clicked()
{
    QSettings settings;
    qDebug() <<  settings.value ("url", "");
    const QString url = ui->server_lineEdit->text ();
    const QString username = ui->username_lineEdit->text ();
    const QString password = ui->password_lineEdit->text ();
    const QString encrytion = ui->encrytion_lineEdit->text ();
    settings.setValue ("url", url);
    settings.setValue ("username", username);
}
