#include "noteslist.h"
#include "ui_noteslist.h"

NotesList::NotesList(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::NotesList)
{
    ui->setupUi(this);
}

NotesList::~NotesList()
{
    delete ui;
}
