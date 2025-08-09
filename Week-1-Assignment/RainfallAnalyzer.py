import numpy as np

def rainfallAnalyzer(rainfall):
  roundedValue = np.round(np.sum(rainfall),2)
  daysWithNoRain = np.sum(rainfall<=0)
  print(f"Total rainfall is:: {roundedValue}")
  print(f"Days with no rainfall is:: {daysWithNoRain}")
  indexes = np.where(rainfall > 5)[0] # Fetching the index of rainfall more than 5 mm.
  for i in indexes: # Iterating through each indexes(days) where rainfall was more than 5 mm.
    print(f"At the day :: {i}, rainfall was :: {rainfall[i]}")
        
        
if __name__ == "__main__":
  rainfallSamples = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5], float)
  print(f"Rainfall samples are :: {rainfallSamples}")
  rainfallAnalyzer(rainfallSamples)