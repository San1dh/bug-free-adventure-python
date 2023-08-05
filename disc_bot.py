import discord
import random
from replit import db

intents = discord.Intents().all()
client = discord.Client(command_prefix = ".", intents=intents)

danger_words = ["gun", "bomb", "kill", "harm", "die", "blood", "gunshot"]

starter_encouragements = ["Don't say that ", "That's dangerous "]

if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  #command id = 1053989495986454568
  #now = datetime.now()  #follows utc time
  #current_min = now.strftime("%M:%S")
  #if (current_min == "21:00"):
  while (1):
    await client.change_presence(activity=discord.Game('-help'))

    channel = client.get_channel(1053989495986454568)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith('-help'):

    cmds = "commands are [ -list ]"
    await message.reply(cmds)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options.extend(db["encouragements"])

  if any(word in msg for word in danger_words):
    
    channel = client.get_channel(1053989495986454568)
    
    # Find the message to delete
    message = await channel.fetch_message(message.id)

    # Send positive message
    await channel.send(random.choice(options) + message.author.mention + "!")

  if any(word in msg for word in danger_words):
    
    channel = client.get_channel(1053989495986454568)
    
    # Find the message to delete
    message = await channel.fetch_message(message.id)

    # Delete the message
    await message.delete()

  if msg.startswith("-responding"):
    value = msg.split("-responding ", 1)[1]

    if value.lower() == "on":
      db["responding"] = True
      await message.reply("Responding is on.")
    else:
      db["responding"] = False
      await message.reply("Responding is off.")

#my_secret = os.getenv('TOKEN')
#client.run(my_secret)
#client.run(os.getenv('TOKEN'))
client.run(API_KEY)
#my_secret = os.environ['TOKEN']
