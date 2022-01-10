# Django Based Settings Manager

An experiment to see if using the Django Tools as a settings manager makes sense.

## installation

```bash
> python3 -m venv venv
> bash venv/bin/activate
> pip install -r requirements.txt
```

Once things are installed, you'll need to run some base configurations.
The following presume you're running python and scripts inside of the virtualenv.
If you like, you can `activate` the virtualenv by running

```bash
> exec venv/bin/activate
```

### set up the local files

See https://django-admin-tools.readthedocs.io/en/latest/configuration.html

```bash
> python settings_mgr/manage.py migrate
```

*NOTE* I've already included the 'static' files into the git repo. This may or may not be correct. The command to generate them is ```collectstatic```, but note that this does not bring in the template files.

## create the superuser

```bash
> python settings_mgr/manage.py createsuperuser
```

## Running the server

Check that `settings.py` is configured the way you want it.

```bash
> python settings_mgr/manage.py runserver
```

You should be able to go to `http://SERVER:8000/admin/` and get the admin login page.

TODO:

* JSON argument reader
* Object editor for each setting / value
* setting validator
* GCP storage reader/writer
