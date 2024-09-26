# Guestbook with Python3 | Flask

This is just a little poorly written experiment of what could be guest book visiting my house in Turin

### Features

This program allows you to leave a name, a comment and above all a photo that the program will render on the homepage of the site.

At the moment the html file is absolutely rubbish, the implementation has only the jinja2 part needed to send data to the webserver, the UI is oversimplistic and visibly awful.

### Repo

Inside this [repo](https://github.com/filippo-ferrando/quelli-silenziosi) you can find all the code used, from the webserver to the HTML

### Screenshot of the homepage with an example

<img src="https://gist.github.com/filippo-ferrando/bb3e9bcb958f82265936250a1e998309/raw/2c225cccd9b74d941e13e6a157db96d3dd615ff5/guestbook.png" alt="guestbook"></img>

#### Structure
```bash
.
├── static
│   └── img
│       └── images..
├── templates
│   └── index.html
├── app.py
└── entries.txt
```
