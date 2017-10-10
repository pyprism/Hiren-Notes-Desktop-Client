#include "loginwindow.h"
#include "ui_loginwindow.h"
#include <QDebug>
#include <QByteArray>

#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonValue>

#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <QUrl>
#include <QUrlQuery>
#include <QJsonValue>
#include <QJsonObject>


LoginWindow::LoginWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LoginWindow),
    mNetMan(new QNetworkAccessManager(this)),
    mNetReply(nullptr),
    mDataBuffer(new QByteArray)
{
    ui->setupUi(this);
    BuildLogin();
}

void LoginWindow::BuildLogin(){
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

void LoginWindow::NetworkCleanup (){
    mNetReply->deleteLater ();
    mNetReply = nullptr;
    mDataBuffer->clear ();
}

void LoginWindow::on_login_pushButton_clicked()
{
    ui->statusBar->clearMessage();
    QSettings settings;
    const QString url = ui->server_lineEdit->text ();
    const QString username = ui->username_lineEdit->text ();
    const QString password = ui->password_lineEdit->text ();
    const QString encryption = ui->encrytion_lineEdit->text ();
    settings.setValue ("url", url);
    settings.setValue ("username", username);

    const QUrl URL(url + "/api/auth/");
    QNetworkRequest req(URL);
    req.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");

//    QUrlQuery urlQuery;
//    urlQuery.addQueryItem ("username", username);
//    urlQuery.addQueryItem ("password", password);
//    QUrl params;
//    params.setQuery (urlQuery);

    QByteArray postData;
    postData.append("username=" + username + "&password=" + password);

    mNetReply = mNetMan->post(req, postData);

    connect(mNetReply, &QIODevice::readyRead, this, &LoginWindow::OnResponseReadyToRead);
    connect(mNetReply, &QNetworkReply::finished, this, &LoginWindow::OnResponseReadFinished);


//    connect (reply, &QNetworkReply::readyRead, [reply]() {
//        qDebug()  << "Ready to read from reply";
//    });
//    connect (reply, &QNetworkReply::sslErrors, [this] (QList<QSslError> error) {
//        qWarning () << "Ssl error: " << error;
//    });

}

void LoginWindow::OnResponseReadyToRead()
{
    mDataBuffer->append (mNetReply->readAll ());
}

void LoginWindow::OnResponseReadFinished()
{
    QJsonDocument doc = QJsonDocument::fromJson (*mDataBuffer);
    QJsonObject object = doc.object ();

    QJsonValue token = object.value ("token");
    QJsonValue err = object.value ("error");

    if(token.isUndefined()) {
        ui->statusBar->setStyleSheet("color: red");
        ui->statusBar->showMessage("Username/Password is not valid");
    } else {
        QSettings settings;
        settings.setValue("token", token.toString());
    }

    NetworkCleanup();
}




