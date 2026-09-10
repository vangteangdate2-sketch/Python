import pandas as pd
import numpy as np
from scipy.stats import zscore

np.random.seed(0)
normal_iq = np.random.normal(100, 5, 100)
outliers = [30, 250]

iq_data = np.concatenate([normal_iq, outliers])

df = pd.DataFrame({"IQ": iq_data})
df["Z_Score"] = zscore(df["IQ"])

outliers_z = df[np.abs(df["Z_Score"]) > 3]
print(outliers_z)