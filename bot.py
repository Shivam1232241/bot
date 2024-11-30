from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext 
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, JobQueue
import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.constants import ParseMode  # Correct import for version 20.x and above
from telegram import InputMediaPhoto
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from telegram.constants import ParseMode



# Add this function to handle user profile initialization if the user doesn't exist
def initialize_user_profile(user_id):
    if user_id not in user_profiles:
        user_profiles[user_id] = {'badges': []}  # Empty badges list for new users
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your own user ID and Gym Leaders' IDs
YOUR_USER_ID = 6977793872  # Replace with your Telegram user ID
GYM_LEADER_USER_IDS = [6977793872, 112233445]  # Replace with Gym Leader IDs

# Example user profiles, make sure to structure this properly in your bot
user_profiles = {
    6977793872: {'badges': []},  # Example user profile for a challenger
}

# Function to initialize user profile
def initialize_user_profile(user_id):
    if user_id not in user_profiles:
        user_profiles[user_id] = {'badges': []}  # Empty badges list for new users

async def give_badge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only the bot owner or Gym Leaders can give badges
    if update.message.from_user.id not in [YOUR_USER_ID] + GYM_LEADER_USER_IDS:
        await update.message.reply_text("You don't have permission to give badges.")
        return
    
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /give <challenger_id> <badge_name>")
        return
    
    challenger_id = int(context.args[0])
    badge_name = context.args[1]
    
    # List of valid badges
    valid_badges = ["Ghost", "Fire", "Water", "Thunder", "Rock", "Ice", "Steel", "Dragon", "Dark", "Fighting", "Psychic"]
    
    # Initialize user profile if the challenger doesn't exist
    initialize_user_profile(challenger_id)
    
    # Check if the provided badge is valid
    if badge_name not in valid_badges:
        await update.message.reply_text(f"Invalid badge. Available badges: {', '.join(valid_badges)}.")
        return
    
    # Add badge to the user's profile
    user_profiles[challenger_id]['badges'].append(badge_name)
    
    # Send a confirmation message
    await update.message.reply_text(f"Badge '{badge_name}' has been successfully given to challenger {challenger_id}.")



# Function to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the Gym Badges Bot!")

# Sample user profile data storage
# Sample user profile data storage
user_profiles = {}

# Your user ID (replace with your actual Telegram user ID)
OWNER_ID = 6977793872  # Replace with your actual Telegram user ID

# List of allowed gym badges
ALLOWED_BADGES = [
    'Ghost', 'Fire', 'Water', 'Thunder', 'Rock', 'Ice', 
    'Steel', 'Dragon', 'Dark', 'Fighting', 'Psychic'
]

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id

    # Initialize user's profile if not already
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            'badges': [],
            'total_matches': 0,
            'wins': 0,
            'losses': 0,
            'profile_picture': None,
            'name': user.full_name,
            'user_id': user.id
        }

    # Fetch user's profile photo (if exists)
    profile_picture = None
    photos = await user.get_profile_photos()  # Await the coroutine
    if photos.total_count > 0:
        profile_picture = photos.photos[0][-1].file_id  # Get the highest resolution photo

    # Update profile picture in user profile
    user_profiles[user_id]['profile_picture'] = profile_picture

    # User profile data
    profile_data = user_profiles[user_id]
    badges = ", ".join(profile_data['badges']) if profile_data['badges'] else "No badges"

    # Prepare message to show user's profile information
    message = (
        f"𝓤𝓼𝓮𝓻: {profile_data['name']}\n"
        "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
        f"𝓤𝓼𝓮𝓻 𝓘𝓓: {profile_data['user_id']}\n"
        "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
        f"𝓑𝓪𝓭𝓰𝓮𝓼: {badges}\n"
        "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
        f"𝓣𝓸𝓽𝓪𝓵 𝓜𝓪𝓽𝓬𝓱𝓮𝓼: {profile_data['total_matches']}\n"
        "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
        f"𝓦𝓲𝓷𝓼: {profile_data['wins']}\n"
        "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
        f"𝓛𝓸𝓼𝓼𝓮𝓼: {profile_data['losses']}\n"
    )

    # Send user profile info with profile picture
    if profile_picture:
        await update.message.reply_photo(profile_picture, caption=message)
    else:
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)


# Handler for /addbadge command to add a badge
async def add_badge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id

    # Ensure only the bot owner can assign badges
    if user_id != OWNER_ID:
        await update.message.reply_text("You don't have permission to assign badges.")
        return

    # Check if the command is properly formatted
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /addbadge <user_id> <badge_name>")
        return

    target_user_id = int(context.args[0])  # User ID to which badge will be assigned
    badge_name = context.args[1]  # Badge name to assign

    # Check if the badge name is valid
    if badge_name not in ALLOWED_BADGES:
        await update.message.reply_text(f"Invalid badge. Valid badges are: {', '.join(ALLOWED_BADGES)}.")
        return

    # Initialize target user's profile if not already
    if target_user_id not in user_profiles:
        user_profiles[target_user_id] = {
            'badges': [],
            'total_matches': 0,
            'wins': 0,
            'losses': 0,
            'profile_picture': None,
            'name': "Unknown",
            'user_id': target_user_id
        }

    # Add the badge to the target user's profile
    user_profiles[target_user_id]['badges'].append(badge_name)

    # Send confirmation message
    await update.message.reply_text(f"Badge '{badge_name}' has been added to user {target_user_id}'s profile.")

# Handler to add wins
async def add_win(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id

    # Initialize user's profile if not already
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            'badges': [],
            'total_matches': 0,
            'wins': 0,
            'losses': 0,
            'profile_picture': user.profile_photo.get_small_file() if user.profile_photo else None,
            'name': user.full_name,
            'user_id': user.id
        }

    # Increment win count
    user_profiles[user_id]['wins'] += 1
    user_profiles[user_id]['total_matches'] += 1

    # Send confirmation message
    await update.message.reply_text(f"Win added! Total Wins: {user_profiles[user_id]['wins']}")

# Handler to add losses
async def add_loss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id

    # Initialize user's profile if not already
    if user_id not in user_profiles:
        user_profiles[user_id] = {
            'badges': [],
            'total_matches': 0,
            'wins': 0,
            'losses': 0,
            'profile_picture': user.profile_photo.get_small_file() if user.profile_photo else None,
            'name': user.full_name,
            'user_id': user.id
        }

    # Increment loss count
    user_profiles[user_id]['losses'] += 1
    user_profiles[user_id]['total_matches'] += 1

    # Send confirmation message
    await update.message.reply_text(f"Loss added! Total Losses: {user_profiles[user_id]['losses']}")

# Store the target group chat ID
target_group_chat_id = 1002342573806

# Command to set the target group chat
async def set_target_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global target_group_chat_id
    chat_id = update.effective_chat.id

    if update.effective_chat.type in ["group", "supergroup"]:
        target_group_chat_id = chat_id
        await update.message.reply_text(f"Target group chat set to: {chat_id}")
    else:
        await update.message.reply_text("Please use this command in a group chat.")

# Command to send a message to the target group chat
async def send_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global target_group_chat_id

    if target_group_chat_id is None:
        await update.message.reply_text("No target group chat has been set. Use /setgroup in a group first.")
        return

    if not context.args:
        await update.message.reply_text("Please provide a message to send to the group.")
        return

    message = " ".join(context.args)

    try:
        await context.bot.send_message(chat_id=target_group_chat_id, text=message)
        await update.message.reply_text("Message sent to the group!")
    except Exception as e:
        await update.message.reply_text(f"Failed to send message: {e}")

# Store tournament participants and tournament state
participants = []
matches = []
current_round = 1

# Define the tournament rewards
rewards = {
    "1st": "1000 PokéDollars 💰 and a Rare Pokémon!",
    "2nd": "500 PokéDollars 💰 and a Rare Candy 🍬",
    "3rd": "200 PokéDollars 💰"
}

# Function to start the tournament registration
async def register_tournament(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    if user.username not in participants:
        participants.append(user.username)
        await update.message.reply_text(f"You're now registered for the tournament, {user.first_name}!")
    else:
        await update.message.reply_text(f"You are already registered, {user.first_name}.")

# Function to start the tournament
async def start_tournament(update: Update, context: CallbackContext) -> None:
    global current_round
    if len(participants) < 2:
        await update.message.reply_text("Not enough participants to start the tournament!")
        return

    random.shuffle(participants)  # Shuffle participants randomly
    # Generate the first round of matches
    matches.clear()
    for i in range(0, len(participants), 2):
        if i + 1 < len(participants):
            matches.append([participants[i], participants[i+1]])

    current_round = 1
    await update.message.reply_text(f"Tournament started! Round {current_round}:\n" + format_matches())

# Function to format and display the current matches
def format_matches():
    match_str = ""
    for idx, match in enumerate(matches, start=1):
        match_str += f"Match {idx}: {match[0]} vs {match[1]}\n"
    return match_str

# Function to report results of a match
async def report_result(update: Update, context: CallbackContext) -> None:
    global current_round
    if len(context.args) < 2:
        await update.message.reply_text("Please provide the winner and loser. Format: /result <winner> <loser>")
        return

    winner, loser = context.args[0], context.args[1]

    # Check if the match exists
    match_found = False
    for match in matches:
        if (winner in match) and (loser in match):
            match_found = True
            # Remove the loser from the match
            match.remove(loser)
            await update.message.reply_text(f"Match result: {winner} wins!")
            break
    
    if not match_found:
        await update.message.reply_text("Invalid match result.")

    # Proceed to next round if all matches are reported
    if all(len(match) == 1 for match in matches):
        current_round += 1
        await update.message.reply_text(f"Round {current_round} is starting!")
        # Prepare the next round
        advance_winners_to_next_round()

# Function to advance the winners to the next round
def advance_winners_to_next_round():
    global matches
    winners = [match[0] for match in matches]
    matches.clear()
    random.shuffle(winners)
    for i in range(0, len(winners), 2):
        if i + 1 < len(winners):
            matches.append([winners[i], winners[i + 1]])

# Function to announce the tournament winner
async def announce_winner(update: Update, context: CallbackContext) -> None:
    if len(matches) == 1:  # Only one match should be left in the final
        winner = matches[0][0]
        await update.message.reply_text(f"Congratulations {winner}! You have won the tournament! 🎉\n\n"
                                       f"1st Place: {rewards['1st']}")
    else:
        await update.message.reply_text("The tournament has not finished yet.")

# Function to list the current participants
async def list_participants(update: Update, context: CallbackContext) -> None:
    if participants:
        await update.message.reply_text("Current Tournament Participants:\n" + "\n".join(participants))
    else:
        await update.message.reply_text("No participants yet.")

# Function to display the current round and matches
async def current_round_info(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Current Round: {current_round}\n" + format_matches())




# Define the leader command handler
async def leader(update: Update, context: CallbackContext) -> None:
    # Define the gym leaders and badges in a formatted way
    response = (
        "┊BADGES                     |             LEADERS   ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Ghost┊👻┊              〄         ┊Royal👻  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Fire┊🐦‍🔥┊              〄        ┊Sosuke Azien🐦‍🔥  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Water┊🌊┊             〄           ┊None🌊  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Thunder┊⚡┊           〄            ┊None⚡  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Rock┊🪨┊              〄          ┊None🪨  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Ice┊🧊┊               〄        ┊None🧊  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Steel┊🛡️┊             〄         ┊Kevin🛡️  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Dragon┊🐉┊            〄            ┊Om Naik🐉  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Dark┊🌑┊              〄       ┊Ryuga🌑  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Fighting┊🤛┊          〄       ┊None🤛  ┊\n"
        "┊﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉┊\n"
        "┊Psychic┊🔮┊            〄            ┊Tanya🔮  ┊\n"
        "﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉"
    )

    # Send the formatted response to the user
    await update.message.reply_text(response)



# Gym Badge Mapping with images
GYM_BADGES = {
    "Leaf": {"name": "Leaf Badge", "image_url": "https://static.wikia.nocookie.net/pokemon/images/0/00/Grass_Badge.png/revision/latest?cb=20191124174202"},
    "Fire": {"name": "Flame Badge", "image_url": "https://archives.bulbagarden.net/media/upload/c/cc/Fire_Badge.png?download"},
    "Water": {"name": "Wave Badge", "image_url": "https://static.wikia.nocookie.net/pokemon/images/7/7a/Water_Badge.png/revision/latest?cb=20191124174225"},
    "Thunder": {"name": "Thunder Badge", "image_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/18087af6-9cff-463c-8216-a29d1bad80b9/d3afia5-b348f9e0-2c52-4145-b919-0824fc4364d5.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE4MDg3YWY2LTljZmYtNDYzYy04MjE2LWEyOWQxYmFkODBiOVwvZDNhZmlhNS1iMzQ4ZjllMC0yYzUyLTQxNDUtYjkxOS0wODI0ZmM0MzY0ZDUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.v8-IcH4hJwUFiPQDb-GbnrgozuBwf7w_HyWzLAmBlvA"},
    "Rock": {"name": "Rock Badge", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQbP_16twozhb0Fn74ctQupamjsHsWFQZ57A&s"},
    "Ice": {"name": "Glacier Badge", "image_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e8ddc4da-23dd-4502-b65b-378c9cfe5efa/dffvkm5-d5b70ee9-1441-4dd5-84e0-6cdf408ba840.png/v1/fill/w_1280,h_1280/ice_badge_by_jormxdos_dffvkm5-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2U4ZGRjNGRhLTIzZGQtNDUwMi1iNjViLTM3OGM5Y2ZlNWVmYVwvZGZmdmttNS1kNWI3MGVlOS0xNDQxLTRkZDUtODRlMC02Y2RmNDA4YmE4NDAucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.20GUCAP6KIZtEkXxceUnD6-pV5MdsjRdVql6pnUni50"},
    "Steel": {"name": "Iron Badge", "image_url": "https://png.pngitem.com/pimgs/s/20-208531_pokemon-platinum-mine-badge-hd-png-download.png"},
    "Dragon": {"name": "Dragon Badge", "image_url": "https://archives.bulbagarden.net/media/upload/2/27/Dragon_Badge.png?download"}
}

async def badges(update: Update, context: CallbackContext) -> None:
    for badge_key, badge_info in GYM_BADGES.items():
        await update.message.reply_photo(
            photo=badge_info["image_url"],
            caption=f"🏅 **{badge_info['name']}**",
            parse_mode="Markdown"
        )

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name

    keyboard = [
        [InlineKeyboardButton("Start Journey", callback_data="start_journey")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.ytimg.com/vi/26mTZ6BtMqc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBf4Ee3rsq5un5vK8mt4rYXafxMKw",  # Replace with an actual image URL
        caption=f"Welcome to the Pokémon Gym Challenge, {user_name}!\n"
                "Are you ready to embark on your journey to become the Champion?",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.message.caption:
        await query.edit_message_caption(
            caption="Your journey has begun! Challenge Gym Leaders and collect 8 badges to face the Champion.\n"
                    "Defeat the Champion to become the ultimate Pokémon Trainer!"
        )
    else:
        await query.edit_message_text(
            text="Your journey has begun! Challenge Gym Leaders and collect 8 badges to face the Champion.\n"
                 "Defeat the Champion to become the ultimate Pokémon Trainer!"
        )

    await query.message.reply_text(
        "1. Use /challenge <gym_name> to challenge a Gym Leader.\n"
        "2. Earn badges by defeating Gym Leaders.\n"
        "3. Collect all 8 badges and face the Champion, who is a real player!\n"
        "Good luck!"
    )

async def challenge(update: Update, context: CallbackContext) -> None:
    # Ensure that the gym name and user tag are provided
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /challenge <gym_name> @username")
        return

    gym_name, user_tag = context.args[0], context.args[1]

    # Ensure the gym exists
    if gym_name not in GYM_BADGES:
        await update.message.reply_text("This gym doesn't exist!")
        return

    # Challenge Logic (For now, assuming user can challenge only if gym exists)
    await update.message.reply_text(
        f"Your challenge has been sent to {user_tag} The {gym_name} Gym Leader. Please wait for them to accept!"
    )

async def profile(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name

    keyboard = [
        [InlineKeyboardButton("View Badges", callback_data="view_badges")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://static.wikia.nocookie.net/pokemon/images/e/ed/Player_card_Violet_Scarlet.png/revision/latest?cb=20221130230512",
        caption=f"Trainer Profile: {user_name}\n"
                "Your journey status is:\n"
                "Badges: 0/8\n"  # Update this logic dynamically
                "Challenges: Pending...",
        reply_markup=reply_markup
    )




# Define the challenge command handler
async def challenge(update: Update, context: CallbackContext) -> None:
    # Check if the user provided both the gym name and the username
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /challenge <gym_name> @username")
        return

    # Extract the gym name and the username
    gym_name, user_tag = context.args[0], context.args[1]

    # Send the custom response to the user
    await update.message.reply_text(f"Your challenge has been sent to {user_tag} The {gym_name} Gym Leader. Please wait for them to accept!")


def main() -> None:
    application = Application.builder().token("7636503804:AAEzHsrE6XtrlY6efjglfmokQTyP_LpLkyA").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("badges", badges))
    application.add_handler(CallbackQueryHandler(button_click))
    application.add_handler(CommandHandler("challenge", challenge))
    application.add_handler(CommandHandler("leader", leader))
    application.add_handler(CommandHandler("register_tournament", register_tournament))
    application.add_handler(CommandHandler("start_tournament", start_tournament))
    application.add_handler(CommandHandler("result", report_result))
    application.add_handler(CommandHandler("winner", announce_winner))
    application.add_handler(CommandHandler("list_participants", list_participants))
    application.add_handler(CommandHandler("current_round", current_round_info))
    application.add_handler(CommandHandler("setgroup", set_target_group))
    application.add_handler(CommandHandler("send", send_to_group))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("addbadge", add_badge))
    application.add_handler(CommandHandler("addwin", add_win))
    application.add_handler(CommandHandler("addloss", add_loss))
    application.add_handler(CommandHandler("give", give_badge))
    application.run_polling()

if __name__ == '__main__':
    main()
import sqlite3
