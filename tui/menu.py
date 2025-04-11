from rich.console import Console
from rich.prompt import Prompt
import torch
from models.protbert_embedder import get_prot_bert_embedding
from utils.fasta_loader import load_fasta

console = Console()

def predict_ppi():
    console.rule("[bold green]Protein–Protein Interaction Prediction")
    seq1 = Prompt.ask("Enter first protein sequence")
    seq2 = Prompt.ask("Enter second protein sequence")

    emb1 = get_prot_bert_embedding(seq1)
    emb2 = get_prot_bert_embedding(seq2)

    score = torch.nn.functional.cosine_similarity(emb1, emb2)
    console.print(f"\n[bold yellow]Predicted Interaction Score:[/bold yellow] {score.item():.4f}\n")

def show_recent_papers():
    console.rule("[bold cyan]Recent Advances in Deep Learning for PPI")
    try:
        with open("papers/recent_papers.txt", "r") as file:
            papers = file.readlines()
            for idx, paper in enumerate(papers, 1):
                console.print(f"{idx}. {paper.strip()}")
    except FileNotFoundError:
        console.print("[red]Papers file not found.[/red]")

def menu():
    while True:
        console.rule("[bold magenta]PPI TUI Menu")
        console.print("[1] Predict PPI")
        console.print("[2] Show Recent Papers")
        console.print("[3] Exit")
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"])

        if choice == "1":
            predict_ppi()
        elif choice == "2":
            show_recent_papers()
        elif choice == "3":
            console.print("[bold green]Exiting the app. Goodbye![/bold green]")
            break
