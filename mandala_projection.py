# mandala_projection.py
#
# This script:
# - Loads a GPT-2 model and tokenizer,
# - Extracts hidden state activations (sentence embeddings),
# - Projects the high-dimensional hidden states into 2D space using UMAP,
# - Provides simple visualization of the projected points ("Mandala view"),
# - Calculates basic symmetry metrics like radial density imbalance to detect fragile knowledge regions.
#
# This module supports:
# - Mandala visualization of model internal knowledge structures,
# - Symmetry analysis to identify weak or missing knowledge branches,
# - Preparation for detecting areas that may need healing.
#
# ---
# Part                         | What it does
# ------------------------------|--------------------------------------------------------
# load_model_and_tokenizer()    | Loads GPT-2 model and tokenizer (with hidden states enabled).
# get_sentence_embedding()      | Extracts mean hidden-state embedding for a given sentence.
# project_sentences()           | Projects multiple sentence embeddings into 2D space using UMAP.
# plot_projections()            | Draws a 2D scatter plot of projected knowledge points.
# radial_density_imbalance()    | Calculates asymmetry score to detect fragile regions.
# __main__ block                | Example usage: project and visualize sample sentences.

import torch
import numpy as np
import umap
import matplotlib.pyplot as plt
from transformers import GPT2Tokenizer, GPT2Model

def load_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2Model.from_pretrained('gpt2', output_hidden_states=True)
    model.eval()
    return model, tokenizer

def get_sentence_embedding(sentence, model, tokenizer, layer_index=-1):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    hidden_states = outputs.hidden_states
    embedding = hidden_states[layer_index].mean(dim=1).squeeze()
    return embedding.cpu().numpy()

def project_sentences(sentences, model, tokenizer, layer_index=-1, n_neighbors=10, min_dist=0.1):
    embeddings = []
    for sentence in sentences:
        emb = get_sentence_embedding(sentence, model, tokenizer, layer_index)
        embeddings.append(emb)
    embeddings = np.stack(embeddings)
    reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, metric='cosine')
    projections = reducer.fit_transform(embeddings)
    return projections

def plot_projections(points, labels=None, title="Mandala Projection"):
    plt.figure(figsize=(8, 8))
    if labels is not None:
        plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='Spectral', s=10)
    else:
        plt.scatter(points[:, 0], points[:, 1], s=10)
    plt.title(title)
    plt.axis('off')
    plt.show()

def radial_density_imbalance(points, sectors=8):
    angles = np.arctan2(points[:, 1], points[:, 0])  # [-π, π]
    counts, _ = np.histogram(angles, bins=sectors)
    imbalance = counts.std() / (counts.mean() + 1e-6)
    return imbalance

if __name__ == "__main__":
    # Example usage
    model, tokenizer = load_model_and_tokenizer()
    sample_sentences = [
        "What is the capital of France?",
        "Who discovered America?",
        "What is the chemical formula of water?",
        "Who wrote The Odyssey?",
        "Where is the Great Wall located?"
    ]
    projections = project_sentences(sample_sentences, model, tokenizer)
    plot_projections(projections)

    imbalance_score = radial_density_imbalance(projections)
    print(f"Radial Density Imbalance: {imbalance_score:.3f}")
