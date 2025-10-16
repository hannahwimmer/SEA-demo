import numpy as np


def coffee_fitness_4d(roast: int, blend: int, grind: int, brew_time: float) -> float:
    """
    Fictional 4D coffee quality fitness function
    (ChatGPT-generated - sorry about that.. was just looking for a quick 4D dummy
    function...)
    ---------------------------------------------
    Parameters:
        roast (int):  [0, 20]
        blend (int):  [0, 50]
        grind (int):  [0, 10]
        brew_time (float): [0.0, 5.0] (minutes)

    Returns:
        float: quality score in [0, 100]

    The function is intentionally multimodal, with many local optima and
    a clear global optimum region around ideal values.
    """

    # --- normalize inputs to [0, 1] ---
    R = np.clip(roast / 20.0, 0, 1)
    B = np.clip(blend / 100.0, 0, 1)
    G = np.clip(grind / 10.0, 0, 1)
    T = np.clip(brew_time / 5.0, 0, 1)

    # --- sinusoidal landscape for local optima ---
    base_pattern = (
        np.sin(6 * np.pi * R) * np.cos(4 * np.pi * B) +
        np.sin(5 * np.pi * G) * np.cos(3 * np.pi * T) +
        0.5 * np.sin(2 * np.pi * (R + B + G + T))
    )

    # --- smooth "global optimum" Gaussian region ---
    # Ideal combination: medium roast, balanced blend, mid grind, moderate brew
    ideal = np.exp(
        -((R - 0.6)**2 / 0.015)
        -((B - 0.5)**2 / 0.02)
        -((G - 0.5)**2 / 0.02)
        -((T - 0.55)**2 / 0.015)
    )

    # --- cross-interaction term to couple dimensions (non-separable landscape) ---
    interactions = 0.2 * np.sin(3 * np.pi * R * B) + 0.15 * np.cos(4 * np.pi * G * T)

    # --- combine components ---
    score = 0.6 * ideal + 0.3 * base_pattern + interactions

    # --- add a small asymmetry (e.g., bitterness penalty) ---
    bitterness = 0.6 * R + 0.4 * T
    if bitterness > 0.7:
        score -= 0.2 * (bitterness - 0.7) ** 2

    # --- scale and clip to [0, 100] ---
    quality = np.clip(50 + 50 * score, 0, 100)

    return float(quality)
