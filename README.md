
# Shopping Mall System

A shopping mall system to manage customers and products and store the information in a PostgreSql database. You can add, remove or change informations in the database.


## Authors

- [Macan Mehri](https://github.com/macanMehri)


## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```
Change sample_settings.py file name to local_settings.py and compelet informations in the file like this
```bash
  DATABASE = {
    'name': 'database name',
    'user': 'database user',
    'password': 'database password',
    'host': 'database host maybe localhost',
    'port': 5432
}
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/macanMehri/ShoppingMallSystemWithDB.git
```

Go to the project directory

```bash
  cd ShoppingMallSystemWithDB
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```


## Features

- Ease of use
- You can see a chart of top five sales of a year
- You can see a chart of total number of sales in a year
- You can see a chart of total earnings in a year
- Easy analysis of income and sales
- Maintaining information in a coherent database


## FAQ

#### Why should I use this program

Many features that the program gives you, which you can see in section Features

#### What is the difference between this program and other programs?

Visualizing the information of a store for a better analysis

