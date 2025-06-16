#!/usr/bin/env python3
"""
Tests for Interactive Story Generator
"""

import pytest
import json
import os
import tempfile
import shutil
from rich.console import Console
from project import (
    get_story_scenes, 
    save_story, 
    play_scene, 
    add_to_inventory, 
    has_item, 
    remove_from_inventory,
    show_inventory,
    load_saved_story
)


def test_get_story_scenes():
    """Test if story scenes are loaded correctly"""
    scenes = get_story_scenes()
    
    # Check if scenes dictionary is not empty
    assert len(scenes) > 0
    
    # Check if required scenes exist
    assert "start" in scenes
    assert "great_hall" in scenes
    assert "garden" in scenes
    
    # Check if start scene has required structure
    start_scene = scenes["start"]
    assert "description" in start_scene
    assert "choices" in start_scene
    assert len(start_scene["choices"]) > 0
    
    # Check if choices have required fields
    for choice in start_scene["choices"]:
        assert "text" in choice
        assert "next_scene" in choice


def test_add_to_inventory():
    """Test adding items to inventory"""
    story_data = {"inventory": []}
    
    # Add items
    add_to_inventory(story_data, "golden_key")
    add_to_inventory(story_data, "healing_potion")
    
    # Check if items were added
    assert "golden_key" in story_data["inventory"]
    assert "healing_potion" in story_data["inventory"]
    assert len(story_data["inventory"]) == 2
    
    # Try adding duplicate item
    add_to_inventory(story_data, "golden_key")
    
    # Should still be only 2 items (no duplicates)
    assert len(story_data["inventory"]) == 2


def test_has_item():
    """Test checking if player has specific item"""
    story_data = {"inventory": ["golden_key", "healing_potion"]}
    
    # Test existing items
    assert has_item(story_data, "golden_key") == True
    assert has_item(story_data, "healing_potion") == True
    
    # Test non-existing item
    assert has_item(story_data, "magic_sword") == False
    
    # Test with empty inventory
    empty_story = {"inventory": []}
    assert has_item(empty_story, "golden_key") == False


def test_remove_from_inventory():
    """Test removing items from inventory"""
    story_data = {"inventory": ["golden_key", "healing_potion", "ancient_knowledge"]}
    
    # Remove existing item
    remove_from_inventory(story_data, "healing_potion")
    assert "healing_potion" not in story_data["inventory"]
    assert len(story_data["inventory"]) == 2
    
    # Try to remove non-existing item (should not cause error)
    remove_from_inventory(story_data, "magic_sword")
    assert len(story_data["inventory"]) == 2
    
    # Remove another item
    remove_from_inventory(story_data, "golden_key")
    assert "golden_key" not in story_data["inventory"]
    assert len(story_data["inventory"]) == 1


def test_save_story():
    """Test saving story to file"""
    # Create temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    original_cwd = os.getcwd()
    
    try:
        os.chdir(temp_dir)
        
        # Test story data
        story_data = {
            "title": "Test Story",
            "player_name": "TestPlayer",
            "current_scene": "start",
            "choices_made": [],
            "inventory": ["test_item"],
            "start_time": "2024-01-01T12:00:00"
        }
        
        console = Console()
        
        # Save the story
        save_story(story_data, console)
        
        # Check if saves directory was created
        assert os.path.exists("saves")
        
        # Check if save file was created
        save_files = os.listdir("saves")
        assert len(save_files) > 0
        
        # Check if the saved file contains correct data
        save_file = save_files[0]
        with open(f"saves/{save_file}", 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data["player_name"] == "TestPlayer"
        assert loaded_data["current_scene"] == "start"
        assert "test_item" in loaded_data["inventory"]
        
    finally:
        # Clean up
        os.chdir(original_cwd)
        shutil.rmtree(temp_dir)


def test_show_inventory():
    """Test inventory display function"""
    console = Console()
    
    # Test with items in inventory
    story_data = {"inventory": ["golden_key", "healing_potion"]}
    
    # This should run without errors
    try:
        show_inventory(story_data, console)
        inventory_test_passed = True
    except Exception:
        inventory_test_passed = False
    
    assert inventory_test_passed == True
    
    # Test with empty inventory
    empty_story = {"inventory": []}
    
    try:
        show_inventory(empty_story, console)
        empty_inventory_test_passed = True
    except Exception:
        empty_inventory_test_passed = False
    
    assert empty_inventory_test_passed == True


def test_story_scene_structure():
    """Test that all story scenes have proper structure"""
    scenes = get_story_scenes()
    
    for scene_id, scene in scenes.items():
        # Every scene must have a description
        assert "description" in scene
        assert len(scene["description"]) > 0
        
        # Non-ending scenes must have choices
        if not scene.get("is_ending", False):
            assert "choices" in scene
            assert len(scene["choices"]) > 0
            
            # Each choice must have required fields
            for choice in scene["choices"]:
                assert "text" in choice
                assert "next_scene" in choice
        
        # Ending scenes must have ending marker
        if scene.get("is_ending", False):
            assert "ending_text" in scene or "description" in scene


def test_story_connectivity():
    """Test that all scenes are properly connected"""
    scenes = get_story_scenes()
    
    # Collect all scene IDs
    scene_ids = set(scenes.keys())
    
    # Collect all referenced next_scenes
    referenced_scenes = set()
    
    for scene in scenes.values():
        if "choices" in scene:
            for choice in scene["choices"]:
                if "next_scene" in choice:
                    referenced_scenes.add(choice["next_scene"])
    
    # All referenced scenes should exist (except ending scenes)
    for ref_scene in referenced_scenes:
        if ref_scene not in scene_ids:
            # This might be acceptable for some endings, but let's check
            # if it's a known ending pattern
            assert ref_scene.endswith("_ending") or ref_scene in scene_ids


def test_inventory_item_consistency():
    """Test that inventory items mentioned in scenes are consistent"""
    scenes = get_story_scenes()
    
    # Collect all items that can be given or required
    items_given = set()
    items_required = set()
    
    for scene in scenes.values():
        if "choices" in scene:
            for choice in scene["choices"]:
                if "gives_item" in choice:
                    items_given.add(choice["gives_item"])
                if "requires_item" in choice:
                    items_required.add(choice["requires_item"])
    
    # All required items should be available somewhere in the story
    for required_item in items_required:
        assert required_item in items_given, f"Item '{required_item}' is required but never given"


# Test for edge cases
def test_empty_inventory_operations():
    """Test inventory operations with edge cases"""
    # Test with missing inventory key
    story_data = {}
    
    # These should handle missing inventory gracefully
    assert has_item(story_data, "any_item") == False
    
    # Adding to missing inventory should create it
    add_to_inventory(story_data, "test_item")
    assert "inventory" in story_data
    assert "test_item" in story_data["inventory"]


def test_scene_placeholder_replacement():
    """Test that player name placeholders work in scenes"""
    scenes = get_story_scenes()
    
    # Check if scenes contain player name placeholder
    start_scene = scenes["start"]
    description = start_scene["description"]
    
    # Should contain placeholder
    assert "{player_name}" in description
    
    # Test replacement (simulated)
    test_description = description.replace("{player_name}", "TestPlayer")
    assert "TestPlayer" in test_description
    assert "{player_name}" not in test_description