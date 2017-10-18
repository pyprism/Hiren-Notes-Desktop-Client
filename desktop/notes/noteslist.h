#ifndef NOTESLIST_H
#define NOTESLIST_H

#include <QDialog>

namespace Ui {
class NotesList;
}

class NotesList : public QDialog
{
    Q_OBJECT

public:
    explicit NotesList(QWidget *parent = 0);
    ~NotesList();

private:
    Ui::NotesList *ui;
};

#endif // NOTESLIST_H
