#include "loginwindow.h"
#include "ui_loginwindow.h"
#include <QDebug>
#include <QNetworkRequest>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QUrlQuery>
#include <QUrl>


LoginWindow::LoginWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LoginWindow)
{
    ui->setupUi(this);
    ui->password_lineEdit->setEchoMode(QLineEdit::Password);
    ui->encrytion_lineEdit->setEchoMode(QLineEdit::Password);
    ui->login_pushButton->setIcon (QIcon(":/new/img/login.svg"));
    this->setWindowTitle ("Login");

    QSettings settings;
    ui->server_lineEdit->setText (QVariant(settings.value ("url")).toString ());
    ui->username_lineEdit->setText (QVariant(settings.value ("username")).toString ());
}

LoginWindow::~LoginWindow()
{
    delete ui;
}

void LoginWindow::on_login_pushButton_clicked()
{
    QSettings settings;
    const QString url = ui->server_lineEdit->text ();
    const QString username = ui->username_lineEdit->text ();
    const QString password = ui->password_lineEdit->text ();
    const QString encrytion = ui->encrytion_lineEdit->text ();
    settings.setValue ("url", url);
    settings.setValue ("username", username);

    QNetworkAccessManager mAccessManager;
    QNetworkRequest request(QUrl(url + "/api/auth/"));

    QUrlQuery urlQuery;
    urlQuery.addQueryItem ("username", username);
    urlQuery.addQueryItem ("password", password);

    QUrl params;
    params.setQuery (urlQuery);

    QNetworkReply* reply = mAccessManager.post (request, params.toEncoded ());

    connect (reply, &QNetworkReply::readyRead, [reply]() {
        qDebug()  << "Ready to read from reply";
    });
    connect (reply, &QNetworkReply::sslErrors, [this] (QList<QSslError> error) {
        qWarning () << "Ssl error: " << error;
    });

}




