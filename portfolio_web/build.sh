source .pw-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d portfolio_web/public
rm -f frontend.zip
deactivate