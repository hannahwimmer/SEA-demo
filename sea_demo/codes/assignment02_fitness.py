import numpy as np


def fitness_function(roast: int, blend: int, grind: int, brew_time: int) -> float:
    """
    a fictional coffee quality function with multiple local optima
    (sorry from my side - the function below's been generated with ChatGPT)
    ------------------------------------------
    inputs: basic properties in range 0..100, each
    output: quality score in range 0..100
    """

    # normalize the inputs
    R = roast / 100.0
    B = blend / 100.0
    G = grind / 100.0
    T = brew_time / 100.0

    # generate some base attributes
    acidity    = 1 - R
    bitterness = 0.6*R + 0.4*T
    body       = 0.5*B + 0.3*G + 0.2*T
    aroma      = 0.7*R + 0.2*B + 0.1*T
    sweetness  = 1 - 0.5*B - 0.5*T

    # introduce some nonlinearities / local optima
    bumps = (
        0.1*np.sin(5*np.pi*R)*np.sin(5*np.pi*G) + 
        0.1*np.cos(4*np.pi*B)*np.cos(3*np.pi*T)
    )

    # combine to an overall quality score
    quality_score = (
        0.3*aroma + 0.2*sweetness + 0.2*body + 0.2*acidity + 0.1*bitterness
    )
    quality_score = quality_score * 100 + bumps*50

    # penalize excessive bitterness (because why not...)
    if bitterness*100 > 60:
        quality_score -= 25*((bitterness*100 - 60)/60)**2

    # return a score between 0 and 100
    return max(0, min(100, quality_score))
