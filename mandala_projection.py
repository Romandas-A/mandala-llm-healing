# mandala_projection.py

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
