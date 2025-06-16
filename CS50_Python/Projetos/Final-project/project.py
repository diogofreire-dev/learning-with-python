#!/usr/bin/env python3
"""
Interactive Story Generator - CS50P Final Project
Author: [Your Name]
"""

import json
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table


def main():
    """Main program function"""
    console = Console()
    
    welcome_text = Text("INTERACTIVE STORY GENERATOR", style="bold magenta")
    console.print(Panel(welcome_text, border_style="bright_blue"))
    
    while True:
        menu_table = Table(show_header=False, box=None)
        menu_table.add_column("Option", style="cyan", width=3)
        menu_table.add_column("Description", style="white")
        
        menu_table.add_row("1.", "New Story")
        menu_table.add_row("2.", "Load Saved Story") 
        menu_table.add_row("3.", "Exit")
        
        console.print("\nMain Menu:", style="bold yellow")
        console.print(menu_table)
        
        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3"], default="1")
        
        if choice == "1":
            start_new_story(console)
        elif choice == "2":
            load_saved_story(console)
        elif choice == "3":
            console.print("Thanks for playing! See you next time!", style="bold green")
            break


def start_new_story(console):
    """Start a new interactive story"""
    console.print("\nStarting new story...", style="bold blue")
    
    # Initialize story data
    story_data = {
        "title": "The Enchanted Castle",
        "current_scene": "start",
        "player_name": "",
        "choices_made": [],
        "inventory": [],
        "start_time": datetime.now().isoformat()
    }
    
    # Get player name
    player_name = Prompt.ask("\nWhat is your name, adventurer?")
    if not player_name.strip():
        player_name = "Adventurer"
    
    story_data["player_name"] = player_name
    
    console.print(f"\nWelcome, [bold cyan]{player_name}[/]! Your adventure is about to begin...")
    
    # Begin the adventure
    play_scene(story_data, "start", console)


def play_scene(story_data, scene_id, console):
    """Execute a specific scene of the story"""
    scenes = get_story_scenes()
    
    if scene_id not in scenes:
        console.print("Error: Scene not found!", style="bold red")
        return
    
    scene = scenes[scene_id]
    player_name = story_data["player_name"]
    
    # Show scene description
    description = scene["description"].replace("{player_name}", player_name)
    console.print(Panel(description, title="Story", border_style="green"))
    
    # Check if it's an ending scene
    if scene.get("is_ending", False):
        console.print(Panel(scene.get("ending_text", "Your adventure ends here."), 
                          title="THE END", border_style="red"))
        
        # Ask if player wants to save this story
        if Confirm.ask("Would you like to save this completed story?"):
            save_story(story_data, console)
        
        Prompt.ask("Press Enter to return to main menu")
        return
    
    # Show choices
    if "choices" in scene:
        console.print("\nWhat do you want to do?", style="bold yellow")
        
        choices_table = Table(show_header=False, box=None)
        choices_table.add_column("Option", style="cyan", width=3)
        choices_table.add_column("Action", style="white")
        choices_table.add_column("Requirement", style="dim")
        
        available_choices = []
        for i, choice in enumerate(scene["choices"], 1):
            # Check if player has required item
            requirement = choice.get("requires_item", "")
            if not requirement or has_item(story_data, requirement):
                choices_table.add_row(f"{i}.", choice['text'], "")
                available_choices.append(str(i))
            else:
                choices_table.add_row(f"{i}.", f"[dim]{choice['text']} (Need: {requirement})[/]", f"Locked")
        
        choices_table.add_row("S.", "Save Game", "")
        choices_table.add_row("I.", "View Inventory", "")
        
        console.print(choices_table)
        
        # Get player choice
        all_choices = available_choices + ["S", "I", "s", "i"]
        choice = Prompt.ask("Choose", choices=all_choices)
        
        if choice.upper() == "S":
            save_story(story_data, console)
            play_scene(story_data, scene_id, console)
            return
        elif choice.upper() == "I":
            show_inventory(story_data, console)
            play_scene(story_data, scene_id, console)
            return
        
        # Process story choice
        choice_index = int(choice) - 1
        chosen_option = scene["choices"][choice_index]
        
        # Record the choice
        story_data["choices_made"].append({
            "scene": scene_id,
            "choice": chosen_option["text"],
            "timestamp": datetime.now().isoformat()
        })
        
        # Add item to inventory if specified
        if "gives_item" in chosen_option:
            add_to_inventory(story_data, chosen_option["gives_item"])
            console.print(f"You obtained: {chosen_option['gives_item']}", style="green")
        
        # Show result
        if 'result' in chosen_option:
            console.print(f"\n{chosen_option['result']}", style="italic bright_blue")
        
        # Continue to next scene
        next_scene = chosen_option["next_scene"]
        story_data["current_scene"] = next_scene
        
        Prompt.ask("\nPress Enter to continue", default="")
        console.clear()
        
        play_scene(story_data, next_scene, console)


def get_story_scenes():
    """Return dictionary of story scenes"""
    return {
        "start": {
            "description": """
Welcome {player_name} to the Enchanted Castle!

You stand before an ancient castle shrouded in mist. The massive wooden doors 
are slightly ajar, and you can hear strange sounds echoing from within. 
A rusty sign reads: 'Enter if you dare, but beware the guardian's test.'

To your left, you notice a small path leading to what appears to be a garden.
To your right, there's a narrow alley between the castle wall and some old stables.
            """,
            "choices": [
                {
                    "text": "Enter through the main doors",
                    "result": "You push open the heavy doors and step into the castle's grand hall.",
                    "next_scene": "great_hall"
                },
                {
                    "text": "Explore the garden path",
                    "result": "You follow the winding path through overgrown bushes and flowers.",
                    "next_scene": "garden"
                },
                {
                    "text": "Investigate the narrow alley",
                    "result": "You squeeze through the tight space and discover a hidden entrance.",
                    "next_scene": "secret_entrance"
                }
            ]
        },
        
        "great_hall": {
            "description": """
You find yourself in a magnificent great hall with high vaulted ceilings.
Ancient tapestries hang on the walls, and a grand staircase curves upward
to the second floor. 

In the center of the room, there's an ornate pedestal with a golden key
resting on top. However, you notice that touching it might trigger some
kind of mechanism - there are strange symbols glowing around the base.

To your left, you see a doorway leading to what looks like a library.
To your right, another door opens to what appears to be a dining hall.
            """,
            "choices": [
                {
                    "text": "Take the golden key from the pedestal",
                    "result": "You carefully take the key. The symbols stop glowing and you hear a distant door unlock.",
                    "gives_item": "golden_key",
                    "next_scene": "library"
                },
                {
                    "text": "Go to the library",
                    "result": "You enter a vast library filled with dusty tomes and ancient scrolls.",
                    "next_scene": "library"
                },
                {
                    "text": "Enter the dining hall",
                    "result": "You walk into an elegant dining room with a long table set for a feast.",
                    "next_scene": "dining_hall"
                },
                {
                    "text": "Climb the grand staircase",
                    "result": "You ascend the stairs to explore the upper floors of the castle.",
                    "next_scene": "upper_floor"
                }
            ]
        },
        
        "garden": {
            "description": """
You enter a magical garden where flowers glow with an ethereal light.
In the center stands an ancient well with a bucket and rope.
A wise-looking owl perches on a nearby branch, watching you intently.

The owl speaks: 'Brave traveler, if you seek the castle's treasure,
you must first prove your worth. Will you help me recover my lost amulet
from the bottom of this well?'
            """,
            "choices": [
                {
                    "text": "Agree to help the owl and lower the bucket into the well",
                    "result": "You retrieve a beautiful silver amulet. The owl is delighted and gives you a magic potion.",
                    "gives_item": "healing_potion",
                    "next_scene": "garden_reward"
                },
                {
                    "text": "Politely decline and head back to the castle",
                    "result": "The owl looks disappointed but nods understanding. You head back to explore other areas.",
                    "next_scene": "great_hall"
                },
                {
                    "text": "Ask the owl about the castle's history",
                    "result": "The owl tells you about secret passages and warns you about the castle's guardian.",
                    "next_scene": "owl_wisdom"
                }
            ]
        },
        
        "secret_entrance": {
            "description": """
You discover a hidden door in the castle wall that leads directly to the treasury!
The room is filled with gold coins, precious gems, and magical artifacts.
However, you notice that everything is protected by a magical barrier.

A note on the wall reads: 'Only those who possess the golden key may 
claim these treasures. Beware - taking anything without the key will 
curse you to wander these halls forever.'
            """,
            "choices": [
                {
                    "text": "Try to take some gold despite the warning",
                    "result": "As you reach for the gold, you feel a strange tingling. Perhaps this wasn't wise...",
                    "next_scene": "cursed_ending"
                },
                {
                    "text": "Leave the treasury and enter the castle properly",
                    "result": "Wisdom prevails. You decide to explore the castle and find the key first.",
                    "next_scene": "great_hall"
                },
                {
                    "text": "Look for clues about where to find the golden key",
                    "requires_item": "golden_key",
                    "result": "You already have the golden key! You can claim the treasure safely.",
                    "next_scene": "treasure_ending"
                }
            ]
        },
        
        "library": {
            "description": """
The library is vast and filled with knowledge from ages past.
You find a book titled 'Secrets of the Enchanted Castle' lying open
on a reading table. As you read, you learn about a powerful guardian
that protects the castle's greatest treasure.

The book mentions that the guardian can be defeated with the right 
combination of courage, wisdom, and magical aid.
            """,
            "choices": [
                {
                    "text": "Continue reading to learn more",
                    "result": "You discover the location of the guardian's chamber in the castle's highest tower.",
                    "next_scene": "upper_floor"
                },
                {
                    "text": "Take the book with you",
                    "result": "The book disappears in a flash of light, but the knowledge remains in your mind.",
                    "gives_item": "ancient_knowledge",
                    "next_scene": "dining_hall"
                },
                {
                    "text": "Search for other useful books",
                    "result": "You find a spell book that teaches you a protection charm.",
                    "gives_item": "protection_spell",
                    "next_scene": "upper_floor"
                }
            ]
        },
        
        "upper_floor": {
            "description": """
You reach the upper floor of the castle and find yourself in a circular chamber.
At the center stands a magnificent dragon, but it doesn't seem hostile.
Instead, it speaks to you in a gentle voice:

'Greetings, brave adventurer. I am the Guardian of this castle.
Many have tried to claim the treasure, but few have shown the wisdom
and courage you possess. I offer you a choice that will determine your fate.'
            """,
            "choices": [
                {
                    "text": "Challenge the dragon to combat",
                    "result": "The dragon looks sad but prepares for battle. This was not the wise choice...",
                    "next_scene": "battle_ending"
                },
                {
                    "text": "Ask the dragon about the castle's purpose",
                    "result": "The dragon is impressed by your curiosity and wisdom.",
                    "next_scene": "wisdom_ending"
                },
                {
                    "text": "Offer to help the dragon with whatever it needs",
                    "requires_item": "healing_potion",
                    "result": "You offer your healing potion to the injured dragon. It is deeply moved by your kindness.",
                    "next_scene": "compassion_ending"
                }
            ]
        },
        
        # Ending scenes
        "treasure_ending": {
            "description": """
With the golden key in hand, you successfully claim the castle's treasure!
You've gathered immense wealth and magical artifacts.
As you leave the castle, you realize that the real treasure was the 
wisdom and experience you gained on this adventure.

Congratulations, {player_name}! You have achieved the Treasure Hunter ending!
            """,
            "is_ending": True,
            "ending_text": "You have successfully completed your quest and claimed the castle's treasure!"
        },
        
        "wisdom_ending": {
            "description": """
The dragon reveals that this castle is actually a test for worthy heroes.
Your wisdom and curiosity have proven that you are meant for greater things.
The dragon grants you the title of 'Guardian of Wisdom' and offers you
a place as protector of magical knowledge.

Congratulations, {player_name}! You have achieved the Wisdom ending!
            """,
            "is_ending": True,
            "ending_text": "Your wisdom has earned you a place among the castle's eternal guardians!"
        },
        
        "compassion_ending": {
            "description": """
Your act of kindness touches the dragon's heart deeply.
It reveals that it has been lonely for centuries, waiting for someone
who would show compassion rather than greed.
The dragon offers to share all its knowledge and treasures with you,
and asks if you would like to stay and become its companion.

Congratulations, {player_name}! You have achieved the Compassion ending!
            """,
            "is_ending": True,
            "ending_text": "Your kindness has forged an eternal friendship with the dragon guardian!"
        },
        
        "cursed_ending": {
            "description": """
Your greed has triggered the castle's ancient curse!
You find yourself trapped within these walls, doomed to wander
as a ghost for eternity, warning future adventurers about the
dangers of taking what doesn't belong to them.

Perhaps in your next adventure, you'll choose wisdom over greed...

This is the Cursed ending. Better luck next time, {player_name}!
            """,
            "is_ending": True,
            "ending_text": "Your greed has sealed your fate. You are now part of the castle's curse."
        }
    }


def save_story(story_data, console):
    """Save the story progress"""
    # Create saves directory if it doesn't exist
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"saves/{story_data['player_name']}_{timestamp}.json"
    
    # Save data
    try:
        with open(filename, 'w') as f:
            json.dump(story_data, f, indent=2)
        console.print(f"Game saved successfully as {filename}", style="green")
    except Exception as e:
        console.print(f"Error saving game: {e}", style="red")


def load_saved_story(console):
    """Load a saved story"""
    if not os.path.exists("saves"):
        console.print("\nNo saved stories found!", style="yellow")
        return
    
    save_files = [f for f in os.listdir("saves") if f.endswith('.json')]
    
    if not save_files:
        console.print("\nNo saved stories found!", style="yellow")
        return
    
    # Show available saves
    console.print("\nAvailable saved stories:", style="bold yellow")
    
    saves_table = Table()
    saves_table.add_column("ID", style="cyan", width=3)
    saves_table.add_column("Player Name", style="magenta")
    saves_table.add_column("Date Saved", style="green")
    saves_table.add_column("Current Scene", style="blue")
    
    valid_saves = []
    for i, filename in enumerate(save_files, 1):
        try:
            with open(f"saves/{filename}", 'r') as f:
                save_data = json.load(f)
            
            # Extract info from filename and data
            date_str = filename.split('_')[1].replace('.json', '')
            date_formatted = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]} {date_str[9:11]}:{date_str[11:13]}"
            
            saves_table.add_row(
                str(i),
                save_data.get('player_name', 'Unknown'),
                date_formatted,
                save_data.get('current_scene', 'Unknown')
            )
            valid_saves.append((str(i), filename, save_data))
            
        except Exception as e:
            console.print(f"Error reading save file {filename}: {e}", style="red")
    
    if not valid_saves:
        console.print("No valid save files found!", style="red")
        return
    
    console.print(saves_table)
    
    # Get user choice
    choice_options = [save[0] for save in valid_saves]
    choice = Prompt.ask("Choose save to load", choices=choice_options + ["cancel"], default="cancel")
    
    if choice == "cancel":
        return
    
    # Load the chosen save
    for save_id, filename, save_data in valid_saves:
        if save_id == choice:
            console.print(f"Loading story for {save_data['player_name']}...", style="green")
            console.clear()
            play_scene(save_data, save_data['current_scene'], console)
            break


def add_to_inventory(story_data, item):
    """Add an item to player's inventory"""
    if item not in story_data["inventory"]:
        story_data["inventory"].append(item)


def has_item(story_data, item):
    """Check if player has a specific item"""
    return item in story_data["inventory"]


def remove_from_inventory(story_data, item):
    """Remove an item from player's inventory"""
    if item in story_data["inventory"]:
        story_data["inventory"].remove(item)


def show_inventory(story_data, console):
    """Display player's inventory"""
    inventory = story_data.get("inventory", [])
    
    if not inventory:
        console.print("\nYour inventory is empty.", style="yellow")
        return
    
    console.print("\nYour Inventory:", style="bold cyan")
    inventory_table = Table(show_header=False, box=None)
    inventory_table.add_column("Item", style="green")
    
    for item in inventory:
        inventory_table.add_row(f"• {item}")
    
    console.print(inventory_table)
    Prompt.ask("Press Enter to continue", default="")


if __name__ == "__main__":
    main()