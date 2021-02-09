## 📸 BIO LINK TOOL 🔗

✨ *You can see the output of this webapp (tool) [here](https://bio-link.tr0ublesh00ter.repl.co).* ✨

*Instagram gives you one link. **ONE**. Sometimes you feel like Oliver Twist needing more.*
<br />![Oliver Twist needing more](https://i.pinimg.com/originals/a8/98/15/a89815aab925797337cffd5e685100d2.gif)

*That's why we got tools called **Bio Link Tool.***
*<br /> A famous example is [Linktree](https://linktr.ee/).*
*So I tried making one myself.*

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

I used [Python 3](https://www.python.org/) as for processes. [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework for linking the html pages and my current favourite [Bulma](https://bulma.io/) CSS framework for CSS. This webapp basically got 3 main pages:
- `tree.html` The main page that can be seen by everyone and contains all the links. Hosted at the domain name where this add is hosted. https://bio-link.tr0ublesh00ter.repl.co
- `login.html` For admin login which leads to a page where links are added or removed and is hosted at \<domain>/login. In my case it is https://bio-link.tr0ublesh00ter.repl.co/login
- `admin.html` The page where adding and removing of links takes place. It is hosted at \<domain>/login. In my case it is https://bio-link.tr0ublesh00ter.repl.co/admin. But it cannot be accessed directly. Yo have to pass through the login page.

All the necessary data is passed in `.env` file.Here is an example.
```env
user_name=username

_password=your_password_here

title=Your Title/ Name Here

avatar_link=https://i.pinimg.com/originals/aa/98/11/aa9811e6b484b35bedb46fa85359df61.png

tab_title=Main Tab's Title Here

organisation_name=Your Organisation's Name

page_icon=https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flat_tick_icon.svg/1200px-Flat_tick_icon.svg.png
```
Now let's see what each variable does.
- `user_name` Stores the username for admin login.
- `_password` Stores the password for admin login.
- `title` Stores the title that will be shown in the webpage.
- `avatar_link` Stores the link of the avatar that will be shown in the webpage.
- `tab_title` Stores the title of the webpage that is hown on the tab.
- `organisation_name` Stores the name of the organisation using the tool. It is displayed at the footer of every page.
- `page_icon` Stores the link of the icon that will be shown in the tab of every webpage.

#### Now, How to Run it on local host?
I would recomment creating a virtual environment.
<br />So let's see what we gotta write in our git bash terminal to run this.

Command to create virtual env
```console
$ python -m venv virtual
```

Command to activate virtual env
```console
$ source virtual/Scripts/activate
```

Command to setup developement mode
```console
$ export FLASK_ENV=development
$ export FLASK_APP=main.py
```

Command to run/host
```console
$ flask run
```

After runnging this command you'll see the link where the webapp is hosted. 

Command to deactivate virtual env
```console
$  deactivate
```
That's all hope you like it. 😀