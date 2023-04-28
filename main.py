import discord
import random
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

truth_norm = [
  "What is a weird food that you love?",
  "What terrible movie or show is your guilty pleasure?",
  "What was your biggest childhood fear?",
  'What is the first letter of your crush’s name?',
  'What is the worst grade you received for a class in school/college?',
  'What is the biggest lie you’ve ever told?',
  'Have you ever accidentally hit something (or someone!) with your car?',
  'Have you ever broken an expensive item?',
  'What is one thing you’d change about your appearance if you could?',
  'If you suddenly had a million dollars, how would you spend it?',
  'Who is the best teacher you’ve ever had and why?',
  'What is the worst food you’ve ever tasted?',
  'What is the weirdest way you’ve met someone you now consider a close friend?',
  'What is the most embarrassing thing you’ve posted on social media?',
  'Who was your first celebrity crush?',
  'Have you ever revealed a friend’s secret to someone else?',
  'How many kids do you want to have one day (or how many did you want to have growing up)?',
  'If you could only eat one meal for the rest of your life, what would it be?',
  'What is a secret you had as a child that you never told your parents?',
  'What is your favorite book of all time?',
  'What is the last text message you sent your best friend?',
  'What is something you would do if you knew there were no consequences?',
  'What is the worst physical pain you’ve ever been in?',
  'Personality-wise, are you more like your mom or your dad?',
  'When is the last time you apologized (and what did you do)?',
  'Have you ever reported someone for doing something wrong (either to the police or at work/school)?',
  'If your house caught on fire and you could only save three things (besides people), what would they be?',
  'If you could pick one other player to take with you to a deserted island, who would it be?',
  "What sport or hobby do you wish you would’ve picked up as a child?"
]

dare_norm = [
  "Do a free-style rap for the next minute.",
  "Let another person post a status on your behalf.",
  "Hand over your phone to another player who can send a single text saying anything they want to anyone they want.",
  "Let the other players go through your phone for one minute.",
  "Smell another player's armpit.", "Smell another player's bare foot.",
  "Eat a bite of a banana peel.",
  "Do an impression of another player until someone can figure out who it is.",
  "Say pickles at the end of every sentence you say until it's your turn again.",
  "Imitate a YouTube star until another player guesses who you're portraying.",
  "Act like a chicken until your next turn.",
  "Talk in a British accent until your next turn.",
  "Call a friend, pretend it's their birthday, and sing them Happy Birthday to You.",
  "Name a famous person that looks like each player in the room.",
  "Show us your best dance moves.", "Eat a packet of hot sauce straight.",
  "Let another person draw a tattoo on your back with a permanent marker.",
  "Put on a blindfold and touch the other players' faces until you can figure out who's who.",
  "Serenade the person to your right for a full minute.", "Do 20 squats.",
  "Let the other players redo your hairstyle.", "Gulp down a raw egg.",
  "Dump out your purse, backpack, or pockets and do a show and tell of what's inside.",
  "Let the player to your right redo your makeup.",
  "Do a prank call on one of your family members.",
  "Let another player create a hat out of toilet paper — and you've got to wear it for the rest of the game.",
  "Do a plank for a full minute.", "Let someone give you a wedgie.",
  "Put five cubes in your mouth (you can't chew them, you just have to let them melt—brrr).",
  "Bark like a dog.",
  "Draw your favorite movie and have the other person guess it (Pictionary-style).",
  "Repeat everything the person to your right says until your next turn.",
  "Demonstrate how you style your hair in the mirror (without actually using the mirror).",
  "Play air guitar for one minute.",
  "Empty a glass of cold water onto your head outside.",
  "Lay on the floor and act like a sizzling piece of bacon.",
  "In the next ten minutes, find a way to scare another player and make it a surprise.",
  "Lick a bar of soap.", "Eat a teaspoon of mustard.",
  "Put an ice cube in your pocket until it melts.",
  "Try to chug a bottle of beer in less than 20 seconds.",
  "Take a shot of barbecue sauce.", "Eat half a teaspoon of wasabi.",
  "Go to the nearest fridge, pour a little bit of all the liquids found (not including medication) into a glass, stir it, and drink it all up.",
  "Pledge your undying love to the person directly across from you for a minute.",
  "Make an unflattering picture of yourself your Facebook profile picture for at least a day.",
  "Let someone spoon-feed you with both of you blindfolded for 2 minutes. Make it something messy like yogurt, applesauce, etc.",
  "Turn off your phone for the rest of the game.",
  "Let everyone in the room, dress you up, do your makeup, and your hair. Take a picture and make that your new social media profile picture for at least one day.",
  "Pick your nose in front of everyone.",
  "Let someone in the room write whatever they want from your Facebook account.",
  "Do the worm.", "Slap the person on the left.",
  "Spank the person on your right.",
  "Smell the foot of the person on your left.",
  "Use a pickup line on the person on your right.",
  "Serenade someone in the room.",
  "Wear someone else’s worn socks on your head for the rest of the game.",
  "Wear someone else’s shoes as mittens for the next 10 minutes.",
  "Put your toe in your mouth. If you cannot do that then you have to put someone else’s toe in your mouth.",
  "Do the robot", "Do 50 sit ups.",
  "Jog in place very slowly for the next 3 minutes.",
  "Say something very dirty to the person on your left.",
  "Speak in an accent for the rest of the game (examples of accents include British, Southern American, Caribbean, German, and Italian.)",
  "Pick up the person next to you.",
  "Carry the person next to you across the room.",
  "Swallow a tablespoon of ketchup, mustard, or something similar.",
  "Talk for 5 minutes without stopping.",
  "Put your underwear on top of your head.",
  "Lick the side of someone’s face.",
  "Perform a rap for everyone in the room.",
  "Try to put your foot behind your head.",
  "Speak in pig Latin for the rest of the game.",
  "Switch clothes with someone of the opposite gender for the rest of the game.",
  "Pretend to spin an imaginary hula hoop around your waist for the next 2 minutes.",
  "Send a love letter to someone on Facebook.",
  "Send someone a message that says, “I know what you did last summer.”",
  "Wear your underwear outside of your clothes.", "Streak across the room.",
  "Crack a raw egg on your head.",
  "Post a video of you singing and share it on your social media account.",
  "Ask the neighbors next door for a cup of sugar. If they do not have sugar or do not answer, try until you get someone.",
  "Say the alphabet backwards.",
  "Lay on the floor and pretend that you are swimming for two minutes.",
  "Speak in rhymes for the rest of the game.",
  "Instead of speaking, you have to sing everything that you want to say for the rest of the game.",
  "Blow a raspberry on the stomach of the person to your right.",
  "Prank call the number of someone that you do not know.",
  "Give an insult to every person in the room.",
  "Try to woo the person to your right.",
  "Chew gum that someone else has already chewed.",
  "Switch outfits with the person on your right.",
  "Do the moonwalk across the room.",
  "Go outside and try to hug the next person that walks by.",
  "may also like to check out these 19 boyfriend and girlfriend games.",
  "Go outside and sing Twinkle, Twinkle Little Star loudly.",
  "Call someone on your phone and talk to them for 5 minutes without telling them that you are playing Truth or Dare.",
  "Snort like a pig at the end of each sentence you say for the rest of the game.",
  "Sing a song for 2 minutes, but meow instead of singing the words.",
  "Strip down to your underwear and make an outfit for yourself using no more than 2 rolls of toilet paper.",
  "Sit on someone’s lap for 10 minutes.",
  "Slow dance with the person on your left for the duration of one song.",
  "Give a kiss to each player in the room. A peck on the lips is okay.",
  "Let everyone in the room give you a makeup makeover. Everyone gets to contribute.",
  "Let each person in the room paint your nails.",
  "Eat a piece of food off of someone’s face without using your hands.",
  "Do a belly dance for one minute for everyone in the room.",
  "Give a foot massage to the person on your left.",
  "Go outside and wrap a toilet paper around your neighbors tree.",
  "Let the person next to you give you a hair cut using only his/hers left hand.",
  "Go outside and do a chicken dance for  5 minutes.",
  "Cut 5 onions into little pieces.", "Eat couple cloves of raw garlic.",
  "Go outside and pretend that you are an airplane for 10 minutes.",
  "Go to your neighbors house and say you are sorry for hitting his/her dog.",
  "Go to your neighbors house and pretend to be Adele and sing “Hello” behind his/her door.",
  "Go and fart in front of your teacher or boss.", "Spit on someone.",
  "Take a coin out of your wallet and lick it.",
  "Do a crazy dance outside in a busy intersection.",
  "Touch your friends nose with your tongue only.",
  "Prank call someone and pretend she/he is your girlfriend/boyfriend and propose to him/her.",
  "Bark like a dog for 10 minutes.", "Wax your arms in front of everyone.",
  "Kiss the person in the room who is the same gender. Do it passionately.",
  "Stand or jump on one foot for 5 minutes.",
  "Go to your neighbors house and tell him/her a joke.",
  "Cry loudly in front of everyone.",
  "Try to do a stand up comedy in front of the other players.",
  "Imitate any animal of your choice for several minutes.",
  "Let the person on your left draw a mustache on your skin with a lipstick only.",
  "Let the person on your right put a make up on you blind folded.",
  "Show your whole browsing history to the players in the room.",
  "Disclose your girlfriend’s/boyfriend’s name online.",
  "Call your best friend and make him/her believe that you are a gay.",
  "Try to be a ballerina and dance for 5 minutes.",
  "Say “I love you” for 50 times.", "Take a shower with all your clothes on.",
  "Call your best friend make her believe that you hate her.",
  "Propose to the person on your left.",
  "Call your mom and cry on the phone telling her that you just got dumped.",
  "Pretend that you are an enemy with the person on your right.",
  "Don’t talk for the rest of the game.",
  "Don’t talk to anyone for 30 minutes.",
  "Do a seductive dance in front of everyone.",
  "Use a poetry form of talking for the rest of the game.",
  "Call your dad and tell him that you are going to elope in Vegas.",
  "Go on the street and wear your underwear over your pants for 10 minutes and yell to everyone who passes by that you are a superman.",
  "Go outside and bed for money.",
  "Prank call someone and make them believe that they have won the lottery.",
  "French kiss the person on your left.",
  "Prank call someone and tell them that you are horny.",
  "Be rude to your girlfriend/boyfriend for a day.",
  "Go outside and propose to the first person who passes by.",
  "Get your back hair waxed in front of the other players.",
  "Behave like a lesbian for the rest of the game.",
  "Repeat “I will do it” for 100 times.",
  "Try to drink 3 glasses of milk in 1 minute.",
  "Call your mom and ask her to cook the food that you hate the most.",
  "Try to laugh continuously for the rest of the game.",
  "Remove any of your 4 articles of clothing.",
  "Have a 5 minute conversation of any topic.",
  "Go to your neighbor and ask if they could give you a condom.",
  "Remove your pants/skirt for the rest of the game.",
  "Give a 20 minute lecture of safe sex.",
  "Try to touch your nose with your tongue.", "Do a belly dance.",
  "Join the Discord server https://discord.gg/mwaPKHypGF and ask for 5$."
  "Mimic the joker from a Batman movie.",
  "Call your closest friend and invite him/her for a threesome."
]


@bot.event
async def on_ready():
  print('TruthorDare bot is online!')
  await bot.change_presence(activity=discord.Game(''))


@bot.command()
async def truth(ctx):
  embed = discord.Embed(
    title=f"{ctx.author.name}, {random.choice(truth_norm)}",
    colour=discord.Colour.green())

  await ctx.send(embed=embed)


@bot.command()
async def dare(ctx):
  embed = discord.Embed(title=f"{ctx.author.name}, {random.choice(dare_norm)}",
                        colour=discord.Colour.red())

  await ctx.send(embed=embed)


@bot.command()
async def runit(ctx):
  for i in range(500):
    await ctx.send(i)


keep_alive()

bot.run('your token')
