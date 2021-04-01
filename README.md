# Book details store using [pyhton-tkinter](https://docs.python.org/3/library/tkinter.html)

It is a simple GUI which stores the book information and perform some operations.

I use python-sqlite3 for database, which is used tp store details and and help to perform operations. When first time we run our program it creates a database file inside working directory (like book.db) where data will store.
## A program shows following book information:
>Title

>Author

>Year

>ISBN

## User can do following operations:
>view all records

>search 

>add

>update

>delete

>close
## Installation

Tkinter comes with python installer, we just need to install python

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
[sqlite3](https://docs.python.org/3/library/sqlite3.html)
```bash
pip install sqlite3
```