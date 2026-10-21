def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    if not samples:
        return []

    n = len(samples)
    counts = {}
    for val in samples:
        counts[val] = counts.get(val, 0) + 1

    return [(val, counts[val] / n) for val in sorted(counts.keys())]