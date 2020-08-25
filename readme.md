<h4>Install Dependencies</h4>

```
$ pip install -r requirements.txt
```

<h4> Create File for storing DB Info</h4>

```
$ touch med_reminder/cred_vals/db.py
```

<h4> Update <strong>cred_vals/db.py</strong></h4>

```
DBURL = "<YOUR_MONGO_CONN_URI>"
```

<h4>Export App Vals</h4>

```
$ export FLASK_APP=server.py && export FLASK_ENV=development && export FLASK_DEBUG=1
```
---------------------
<h4>Start App (Dev Mode)</h4>

```
$ flask run --host=127.0.0.1 --port=6000
```
