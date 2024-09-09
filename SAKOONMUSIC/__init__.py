from SAKOONMUSIC.core.bot import sakoon
from SAKOONMUSIC.core.dir import dirr
from SAKOONMUSIC.core.git import git
from SAKOONMUSIC.core.userbot import Userbot
from SAKOONMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = sakoon()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
