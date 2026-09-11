"""
Inference layer — this file is the single seam between your API and the
ML model, matching the "inference layer mock ml" box in the Desease
Detector API Flow diagram.

Right now it's a mock: random class + confidence, with a fake delay to
simulate real inference. Frontend can build against this today.

When Data Science hands you the trained model, you only change
`run_inference()` below — nothing in views.py, serializers.py, or urls.py
needs to change, because the contract (input: image path, output: dict)
stays the same.
"""
import random
import time

from diseases.models import Disease

# Fallback labels used only if the diseases table hasn't been seeded yet.
FALLBACK_LABELS = ["healthy", "tungro", "brown-spot", "blast", "blight", "scald"]


def run_inference(image_path: str) -> dict:
    """
    Contract:
      input:  path to the uploaded image on disk
      output: {"label": <disease slug str>, "confidence": <float 0-100>, "inference_time_ms": <int>}

    --- Swapping in the real model later ---
    import torch
    from PIL import Image

    _model = torch.load("path/to/model.pt")
    _model.eval()

    def run_inference(image_path):
        start = time.time()
        img = Image.open(image_path).convert("RGB")
        tensor = preprocess(img)  # your transforms
        with torch.no_grad():
            logits = _model(tensor.unsqueeze(0))
            probs = torch.softmax(logits, dim=1)[0]
        idx = int(torch.argmax(probs))
        label = CLASS_NAMES[idx]  # ordered to match model's output layer
        confidence = float(probs[idx]) * 100
        inference_time_ms = int((time.time() - start) * 1000)
        return {"label": label, "confidence": confidence, "inference_time_ms": inference_time_ms}
    """
    start = time.time()

    labels = list(Disease.objects.values_list("slug", flat=True)) or FALLBACK_LABELS
    label = random.choice(labels)
    confidence = round(random.uniform(75.0, 99.9), 2)

    # simulate realistic inference latency, like the "22070ms" seen in the mockup
    time.sleep(random.uniform(0.3, 0.8))
    inference_time_ms = int((time.time() - start) * 1000)

    return {"label": label, "confidence": confidence, "inference_time_ms": inference_time_ms}
