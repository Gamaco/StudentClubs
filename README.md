# studentclubs
Instructions to setup this repository.

Once you copy it to your vc code do the following:

1. Install Python if you don't have it installed yet.
  go to vs code extensions > python
  
2. Delete the virtual environment file that was my bad for not adding it in .gitignore file initially.
  Then re-install it by running this command.
  python -m venv venv-name
  
3. Activate it by pressing F1 > Select interpreter > your venv-name and reopen the terminal.

4. install django.
   pip install django
   
5. In the settings.py file, configure the database to which ever you're using, in this case I'm using postgresql,
   if you don't have it, download it and setup the credentials.
   
6. Migrate tables to the database by running this command:
   python manage.py migrate website
   
7. Run the project.
   python manage.py runserver 3000

