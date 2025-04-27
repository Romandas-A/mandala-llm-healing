# gui_mandala_heal.py

import matplotlib.pyplot as plt
import numpy as np
import torch
from transformers import GPT2Model, GPT2Tokenizer
import umap
from mandala_projection import load_model_and_tokenizer, get_sentence_embedding, project_sentences

# Global Variables
selected_points = []
projection_points = None
sentences = []

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = event.xdata, event.ydata
        distances = np.linalg.norm(projection_points - np.array([x, y]), axis=1)
        idx = np.argmin(distances)
        if idx not in selected_points:
            selected_points.append(idx)
            print(f"Selected point {idx}: {sentences[idx]}")

def show_projection(points):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.scatter(points[:, 0], points[:, 1], s=10)
    ax.set_title("Mandala Projection (Click points to select for healing)")
    ax.axis('off')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

def simulate_healing(model, selected_indices):
    if not selected_indices:
        print("No points selected for healing.")
        return None

    hidden_size = model.config.n_embd
    delta = torch.zeros(hidden_size)

    for idx in selected_indices:
        delta += torch.randn(hidden_size) * 0.002  # Small noise for healing simulation

    delta /= len(selected_indices)
    print(f"Simulated healing delta generated for {len(selected_indices)} points.")
    return delta

if __name__ == "__main__":
    # Load model
    model, tokenizer = load_model_and_tokenizer()

    # Example sentences
    sentences = [
        "What is the capital of France?",
        "Who discovered America?",
        "What is the chemical formula of water?",
        "Who wrote The Odyssey?",
        "Where is the Great Wall located?",
        "What gas do plants absorb?",
        "What year did WW2 end?",
        "What is the boiling point of water?"
    ]

    # Project them
    projection_points = project_sentences(sentences, model, tokenizer)
    show_projection(projection_points)

    # After selection
    healing_delta = simulate_healing(model, selected_points)

    if healing_delta is not None:
        print("Healing delta ready. You can now apply it using permanent injection scripts.")
