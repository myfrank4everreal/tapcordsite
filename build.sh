pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate 


# creating admin user on render
# added this to my environment variable list on render dashboard: 
# Key = Value
# -----------------
# CREATE_SUPERUSER = True
# DJANGO_SUPERUSER_EMAIL = <...>
# DJANGO_SUPERUSER_PASSWORD = <...>
# DJANGO_SUPERUSER_USERNAME =<...>
# this is the code snipet to run django admin on render on free plan

# this should actually be added to the environment variables of the render dashboard

# CREATE_SUPERUSER = True
# DJANGO_SUPERUSER_EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL")
# DJANGO_SUPERUSER_PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD")
# DJANGO_SUPERUSER_USERNAME = os.getenv("USER_USERNAME")

# if [[ $CREATE_SUPERUSER ]];
# then
#   python world_champ_2022/manage.py createsuperuser --no-input
# fi

if [[ $CREATE_SUPERUSER ]];
then
  python tapcordsite/manage.py createsuperuser --no-input
fi





