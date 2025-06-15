import pytest
import os
from rich.console import Console
from project import get_story_scenes, save_story, play_scene


def test_get_story_scenes():
    """Testa se as cenas da história são carregadas corretamente"""
    scenes = get_story_scenes()
    
    # Verifica se retorna um dicionário
    assert isinstance(scenes, dict)
    
    # Verifica se tem a cena inicial
    assert "inicio" in scenes
    
    # Verifica se a cena inicial tem os campos necessários
    inicio_scene = scenes["inicio"]
    assert "description" in inicio_scene
    assert "choices" in inicio_scene
    
    # Verifica se as escolhas têm os campos necessários
    for choice in inicio_scene["choices"]:
        assert "text" in choice
        assert "next_scene" in choice


def test_save_story():
    """Testa se consegue guardar uma história"""
    # Dados de teste
    test_story = {
        "title": "Teste",
        "player_name": "TestPlayer",
        "current_scene": "inicio",
        "choices_made": [],
        "start_time": "2024-01-01T10:00:00"
    }
    
    # Console para o teste
    console = Console()
    
    # Guarda a história
    save_story(test_story, console)
    
    # Verifica se a pasta saves foi criada
    assert os.path.exists("saves")
    
    # Verifica se existe pelo menos um ficheiro de save
    save_files = [f for f in os.listdir("saves") if f.startswith("TestPlayer")]
    assert len(save_files) > 0
    
    # Limpa o ficheiro de teste
    for save_file in save_files:
        os.remove(f"saves/{save_file}")


def test_list_available_stories():
    """Testa se a função de listar histórias funciona"""
    # Esta função apenas imprime por agora, então vamos testar se existe
    from project import list_available_stories
    
    # Verifica se a função existe e é chamável
    assert callable(list_available_stories)


# Função auxiliar para limpar ficheiros de teste
def cleanup_test_files():
    """Remove ficheiros de teste criados durante os testes"""
    if os.path.exists("saves"):
        test_files = [f for f in os.listdir("saves") if f.startswith("TestPlayer")]
        for test_file in test_files:
            os.remove(f"saves/{test_file}")


if __name__ == "__main__":
    # Executa os testes
    pytest.main([__file__])