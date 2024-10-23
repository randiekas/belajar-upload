
python3 -m venv .venv
source .venv/bin/activate

authbind --deep python server.py
python server.py
pip freeze > requirements.txt

screen yarn start --a 0.0.0.0 --port 80

streamlit run app.py