setlocal

set FLASK_APP=endorse\app.py
set ENDORSE_CFG=%cd%\config_local.cfg

flask run
