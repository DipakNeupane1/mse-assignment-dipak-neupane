import numpy as np

def calculateTemperature(temperatureData):
  highestTemp=0;
  lowestTemp=0;
  i=0
  for temp in temperatureData:
    fahrenheitValue=temp * 9/5+32
    print(f"Fahrenheit value is :: ", fahrenheitValue)
    if(temp>20.0):
        print(f"Temperature which crossed the 20°C is :: {temp} at index :: {i}")
    elif(temp>highestTemp):
      highestTemp=temp
    elif(lowestTemp<temp):
      lowestTemp=temp
    i+=1
  print(f"Highest recorded temperature is :: {highestTemp}")
  print(f"Lowest recorded temperature is :: {lowestTemp}")
  averageTemp= np.mean(temperatureData)
  return np.round(averageTemp, 2)

if __name__ == "__main__":
  roomTemperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9], float)
  print(f"Average temperature for the week is {calculateTemperature(roomTemperatures)}")