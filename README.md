<h2 align='center'>☎ Discord Phone Call Bot with IFTTT</h2>

[![discord.py](https://img.shields.io/badge/discord-py-red.svg)](https://github.com/Rapptz/discord.py/tree/rewrite)
[![python 3.6](https://img.shields.io/badge/python-3.8-red.svg)](https://www.python.org/)
<br>

<h3 align='center'>🤖📞 A discord bot that can call your actual phone via a Discord command using IFTTT and Python. Easy to set up and customize. Uses IFTT's VOIP applet (not an actual phone number).</h3>
<br>

___

<h2 align='center'>ℹ Disclaimer:</h2>
<h5 align='center'>Many people are confused about what this does, so please read the following before continuing

<br><br>

⚠ No, this does not call your phone with an actual phone number. It uses IFTTT'S VOIP applet, <a href='https://ifttt.com/voip_calls>'><i>click here for more info</i></a>.</h5> 

___

<h2 align=center>💡 Setup</h2>

- This program was made with Python 3.8. Newer or slightly older versions should work, but use at your own risk.
- Ensure you have [IFTTT](https://ifttt.com/about), which needs to be installed on your mobile device.

<h2 align=center>✅ Install the requirements</h2>

```shell
pip install -r requirements.txt
```

> Also, make sure you have a Discord Bot, you can make one [here](https://discordapp.com/developers/applications/). You'll need the bot token which can be found in the *bot* section of your application

___

<h2 align=center>⚙ Configuiring IFTTT</h2>

Go to [IFTTT](https://ifttt.com/create) and create a new Applet.

For the first part, make a webhook. Name the *event name* whatever you want, but remember it.

For the second part, make a *VoIP calls* thing. **Important: Make the** ***Voice message field*** **(essentially what the robot voice calling you will say) the following:**

```python
{{Value1}} {{Value2}}
```

Next, go to https://ifttt.com/services/maker_webhooks/settings and grab the token in the **URL** section (will look something like https://maker.ifttt.com/use/zvicdsCSDdSuDXkODmKllkOWZ1do (only the key at the end of the url is important)

Now go to the **config.json** file and fill in the required information. Here's what each piece means (found in config.json):

```json

"prefix": Used to "talk to" your bot. You can also mention the bot by default to run commands, but you also need a prefix.
"callCoolDown": Set a cooldown between how long users can use the call command. I recommend 30 seconds or more (this is per user)
"eventName": The event name from your webhook
"IFTTTkey": The IFTTT key that you got from the webhook settings URL thingy
"discordToken": Your bot token from the Discord developer portal in the bot section (NOT client secret/client ID)
```

___

<h2 align=center>🎉 Hosting and running the bot on Docker<h2>

#### First download [Docker Desktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module) which should enable the Docker CLI.
#### After you've configured your bot and IFTTT app and installed Docker (making sure the docker command works), run the following commands in your shell:

```shell
docker build --tag phone-bot .
```

```shell
docker run --name Phone-Bot phone-bot:latest
```

___

<h2 align=center>🤝 Contributing and other notes</h2>

⭐Please star the repo, or even join my [Discord server](https://discord.gg/cFC7FDtTYp)

If you have any problems open an issue or join the server and I'll gladly help!

If you'd like to contribute, go ahead!

<br>

___

<h3 align=center>This project was built under the GNU Public License. See <a href='LICENSE'>LICENSE</a> for more details.</h3>