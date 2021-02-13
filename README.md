# salaryy

> It has two y's, so it must be good

`salaryy` is a simple app that helps you manage your income, expenses and the salaries of your employees.

Keep in mind that this is merely a practice project, so maybe it won't have many real world applications.

## Features

As of right now, `salaryy` pretty much has no features.

...Hovever, here's a list of things it will once be able to do:

- manage a list of employees and their salary
- store monthly raises for each employee
- calculate each employee's salary for this month
- calculate your monthly income and expenses

## Installing

In order to install `salaryy`, you need Python 3

### Using a POSIX-compliant shell (such as `bash`)

First, clone this repository.

```shell
$ git clone https://github.com/bvpav/salaryy
$ cd salaryy
```

#### Create a virtual environment (optional, but recommended)

```shell
$ python -m venv venv
$ . venv/bin/activate
(venv) $
```
#### Install the package for development

```shell
(venv) $ pip install --editable .
```

## Running

### Run the web interface

Given that you've installed the package and all it's dependencies, you can simply run the following:

```shell
$ export FLASK_APP=salaryy/web
$ export FLASK_ENV=development
$ flask init-db # Initialize the database
$ flask run
```

> Note that if you're on windows, you have to use `set` instead of `export`

When the server is running, simply open a web browser and visit [http://localhost:5000/](http://localhost:5000/) to see the webapp.

## License

`salaryy` is licensed under the GNU General Public License version 3

See [LICENSE](./LICENSE) for more details.
