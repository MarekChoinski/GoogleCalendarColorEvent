# Coloring of the JSOS-imported events
## For Google Calendar

Colour the plan you've imported from JSOS to your Google Calendar so that the events colors reflect the type of the activities yadda yadda

# Howto
```bash
git clone https://github.com/MarekChoinski/GoogleCalendarColorEvent.git
cd GoogleCalendarColorEvent

# Maybe create a virtualenv or something now

# Install deps
pip install -r requirements.txt

# Create the authentication credentials on
# https://console.developers.google.com/apis/credentials
# And save them in the repo root under `credentials.json`

# Open up `config.py` and set the `calendar_id` variable
# (which is your email address)
vim config.py # for masochists like @Wint3rmute

# Optionally, change the colors for lectures, labs, etc
#   - also located in the `config.py` file

# Finally
python main.py

# And let it happen
```



