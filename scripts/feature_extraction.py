import numpy as np
from scipy.signal import find_peaks

def extract_eda_features(eda_signal):
    eda_mean = np.mean(eda_signal)
    eda_std = np.std(eda_signal)
    eda_max = np.max(eda_signal)
    eda_min = np.min(eda_signal)
    eda_peaks, props = find_peaks(eda_signal, distance=50, prominence=0.02)
    scr_count = len(eda_peaks)
    scr_mean_amp = np.mean(props["prominences"]) if scr_count > 0 else 0

    return {
        'eda_mean': eda_mean,
        'eda_std': eda_std,
        'eda_max': eda_max,
        'eda_min': eda_min,
        'eda_scr_count': scr_count,
        'eda_scr_mean_amp': scr_mean_amp
    }
