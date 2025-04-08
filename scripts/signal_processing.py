import numpy as np
from scipy.signal import find_peaks, welch

def get_ppg_peaks(ppg_signal, distance=50):
    peaks, _ = find_peaks(ppg_signal, distance=distance)
    return peaks

def get_ibi(peaks):
    return np.diff(peaks)

def pnn50(ibi):
    diff_ibi = np.abs(np.diff(ibi))
    return 100.0 * np.sum(diff_ibi > 50) / len(diff_ibi)

def frequency_domain_features(ibi, fs=4):
    if len(ibi) < 2:
        return {'HRV_LF': 0, 'HRV_HF': 0, 'LF_HF_ratio': 0}
    fxx, pxx = welch(ibi, fs=fs)
    lf_band = (fxx >= 0.04) & (fxx <= 0.15)
    hf_band = (fxx >= 0.15) & (fxx <= 0.4)
    lf = np.trapz(pxx[lf_band], fxx[lf_band])
    hf = np.trapz(pxx[hf_band], fxx[hf_band])
    return {
        'HRV_LF': lf,
        'HRV_HF': hf,
        'LF_HF_ratio': lf / hf if hf != 0 else 0
    }
