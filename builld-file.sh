echo "Build Start"
python3.6 -m pip install -r requirements.txt
python3.6 manage.py collectstatic --noinput --clear
echo "Build End"