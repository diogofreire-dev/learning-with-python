#!/usr/bin/env python3
"""
Gerador de Histórias Interativas - CS50P Final Project
Autor: [Teu Nome]
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
    """Função principal do programa"""
    console = Console()
    
    # Banner de boas-vindas
    welcome_text = Text("GERADOR DE HISTÓRIAS INTERATIVAS", style="bold magenta")
    console.print(Panel(welcome_text, border_style="bright_blue"))
    
    while True:
        # Menu principal com estilo
        menu_table = Table(show_header=False, box=None)
        menu_table.add_column("Opção", style="cyan", width=3)
        menu_table.add_column("Descrição", style="white")
        
        menu_table.add_row("1.", "Nova História")
        menu_table.add_row("2.", "Carregar História Guardada") 
        menu_table.add_row("3.", "Ver Histórias Disponíveis")
        menu_table.add_row("4.", "Sair")
        
        console.print("\nMenu Principal:", style="bold yellow")
        console.print(menu_table)
        
        choice = Prompt.ask("\nEscolhe uma opção", choices=["1", "2", "3", "4"], default="1")
        
        if choice == "1":
            start_new_story(console)
        elif choice == "2":
            load_saved_story(console)
        elif choice == "3":
            list_available_stories(console)
        elif choice == "4":
            console.print("Obrigado por jogares!", style="bold green")
            break


def start_new_story(console):
    """Inicia uma nova história interativa"""
    console.print("\nA iniciar nova história...", style="bold blue")
    
    # Por agora, vamos começar com uma história simples
    story_data = {
        "title": "A Aventura do Castelo Misterioso",
        "current_scene": "inicio",
        "player_name": "",
        "choices_made": [],
        "start_time": datetime.now().isoformat()
    }
    
    # Pergunta o nome do jogador
    player_name = Prompt.ask("\nQual é o teu nome, aventureiro?")
    if not player_name.strip():
        player_name = "Aventureiro"
    
    story_data["player_name"] = player_name
    
    console.print(f"\nBem-vindo, [bold cyan]{player_name}[/]! A tua aventura está prestes a começar...")
    
    # Começar a história
    play_scene(story_data, "inicio", console)


def play_scene(story_data, scene_id, console):
    """Executa uma cena específica da história"""
    scenes = get_story_scenes()
    
    if scene_id not in scenes:
        console.print("Erro: Cena não encontrada!", style="bold red")
        return
    
    scene = scenes[scene_id]
    player_name = story_data["player_name"]
    
    # Mostrar a descrição da cena
    description = scene["description"].replace("{player_name}", player_name)
    console.print(Panel(description, title="História", border_style="green"))
    
    # Se é uma cena final, mostrar final e terminar
    if scene.get("is_ending", False):
        ending_panel = Panel(
            f"{scene['ending_message']}", 
            title="🎉 Final da História",
            border_style="gold1"
        )
        console.print(ending_panel)
        
        # Perguntar se quer guardar
        if Confirm.ask("\nQueres guardar esta história?"):
            save_story(story_data, console)
        return
    
    # Mostrar opções
    if "choices" in scene:
        console.print("\nO que queres fazer?", style="bold yellow")
        
        choices_table = Table(show_header=False, box=None)
        choices_table.add_column("Opção", style="cyan", width=3)
        choices_table.add_column("Ação", style="white")
        
        for i, choice in enumerate(scene["choices"], 1):
            choices_table.add_row(f"{i}.", choice['text'])
        
        console.print(choices_table)
        
        # Obter escolha do jogador
        valid_choices = [str(i) for i in range(1, len(scene["choices"]) + 1)]
        choice_num = int(Prompt.ask("Escolhe", choices=valid_choices))
        
        chosen_option = scene["choices"][choice_num - 1]
        
        # Registar a escolha
        story_data["choices_made"].append({
            "scene": scene_id,
            "choice": chosen_option["text"],
            "timestamp": datetime.now().isoformat()
        })
        
        # Ir para a próxima cena
        next_scene = chosen_option["next_scene"]
        story_data["current_scene"] = next_scene
        
        result_text = chosen_option.get('result', 'Continuas a tua jornada...')
        console.print(f"\n➡️ {result_text}", style="italic bright_blue")
        
        Prompt.ask("\nPressiona Enter para continuar", default="")
        
        play_scene(story_data, next_scene, console)


def get_story_scenes():
    """Retorna o dicionário com todas as cenas da história"""
    # Por agora, vamos criar uma história simples hardcoded
    # Mais tarde vamos mover isto para ficheiros JSON
    
    scenes = {
        "inicio": {
            "description": """
{player_name}, encontras-te em frente a um castelo antigo e misterioso.
As torres elevam-se contra o céu escuro, e uma luz fraca pisca numa das janelas.
O portão principal está entreaberto, rangendo suavemente com o vento.
À tua esquerda, vês um caminho que contorna o castelo.
            """,
            "choices": [
                {
                    "text": "Entrar pelo portão principal",
                    "next_scene": "portao_principal",
                    "result": "Empurras o portão e entras no pátio do castelo..."
                },
                {
                    "text": "Seguir o caminho lateral",
                    "next_scene": "caminho_lateral", 
                    "result": "Decides explorar os arredores primeiro..."
                },
                {
                    "text": "Observar o castelo mais atentamente",
                    "next_scene": "observar_castelo",
                    "result": "Paras para examinar melhor a estrutura..."
                }
            ]
        },
        
        "portao_principal": {
            "description": """
Entras no pátio do castelo. O chão está coberto de pedras antigas e musgo.
No centro há uma fonte seca com uma estátua de um cavaleiro.
Vês duas portas: uma grande porta de madeira ornamentada que deve levar ao salão principal,
e uma porta mais pequena que parece dar acesso às cozinhas.
            """,
            "choices": [
                {
                    "text": "Ir para o salão principal",
                    "next_scene": "salao_principal",
                    "result": "Diriges-te para a imponente porta principal..."
                },
                {
                    "text": "Explorar as cozinhas",
                    "next_scene": "cozinhas",
                    "result": "Optas por explorar a área de serviço..."
                }
            ]
        },
        
        "salao_principal": {
            "description": """
Entras num salão majestoso com um teto altíssimo. Candelabros cobertos de teias de aranha
pendem do teto, e retratos antigos observam-te das paredes.
No fundo do salão, vês um trono dourado. Algo brilha no assento do trono.
            """,
            "choices": [
                {
                    "text": "Aproximar-te do trono",
                    "next_scene": "final_tesouro",
                    "result": "Caminhas cuidadosamente em direção ao trono..."
                },
                {
                    "text": "Examinar os retratos",
                    "next_scene": "final_misterio",
                    "result": "Os retratos parecem contar uma história..."
                }
            ]
        },
        
        "final_tesouro": {
            "description": """
Aproximas-te do trono e descobres uma coroa de ouro cravejada de pedras preciosas!
Ao tocares na coroa, o castelo começa a brilhar com uma luz dourada.
És coroado como o novo guardião do castelo misterioso!
            """,
            "is_ending": True,
            "ending_message": "Parabéns! Encontraste o tesouro e tornaste-te o guardião do castelo!"
        },
        
        "final_misterio": {
            "description": """
Os retratos começam a mover-se e contar-te a história do castelo.
Descobres que és o descendente perdido da família real que construiu este lugar.
O castelo reconhece o teu sangue real e as portas secretas abrem-se para ti!
            """,
            "is_ending": True,
            "ending_message": "Incrível! Descobriste a tua verdadeira identidade real!"
        },
        
        # Vamos adicionar as outras cenas gradualmente...
        "caminho_lateral": {
            "description": "Segues o caminho e encontras uma entrada secreta...",
            "choices": [
                {
                    "text": "Entrar pela entrada secreta",
                    "next_scene": "final_tesouro",
                    "result": "A entrada secreta leva-te diretamente ao tesouro!"
                }
            ]
        },
        
        "observar_castelo": {
            "description": "Ao observares atentamente, notas símbolos estranhos na parede...",
            "choices": [
                {
                    "text": "Investigar os símbolos",
                    "next_scene": "final_misterio", 
                    "result": "Os símbolos revelam o segredo da tua linhagem!"
                }
            ]
        }
    }
    
    return scenes


def save_story(story_data, console):
    """Guarda o progresso da história"""
    # Criar diretório de saves se não existir
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    # Nome do ficheiro baseado no nome do jogador e timestamp
    filename = f"saves/{story_data['player_name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(story_data, f, ensure_ascii=False, indent=2)
        console.print(f"História guardada como: [green]{filename}[/]")
    except Exception as e:
        console.print(f"Erro ao guardar: {e}", style="bold red")


def load_saved_story(console):
    """Carrega uma história guardada"""
    console.print("\nFuncionalidade de carregar ainda não implementada...", style="yellow")
    console.print("Será adicionada na próxima versão!")


def list_available_stories(console):
    """Lista as histórias disponíveis"""
    stories_table = Table(title="Histórias Disponíveis")
    stories_table.add_column("Nº", style="cyan", width=3)
    stories_table.add_column("Título", style="magenta")
    stories_table.add_column("Estado", style="green")
    
    stories_table.add_row("1", "A Aventura do Castelo Misterioso", "✅ Disponível")
    stories_table.add_row("2", "A Floresta Encantada", "🔄 Em breve...")
    stories_table.add_row("3", "A Cidade Perdida", "🔄 Em breve...")
    
    console.print(stories_table)


if __name__ == "__main__":
    main()