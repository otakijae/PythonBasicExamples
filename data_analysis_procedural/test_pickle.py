import pickle

f = open("class_A.bin", "wb")

data = {"JaeHyuk Shin":100}
pickle.dump(data,f)

data = {"Wayne Rooney":78}
pickle.dump(data,f)

data = {"Paul Pogba":60}
pickle.dump(data,f)

data = {"Eden Hazard":95}
pickle.dump(data,f)

data = {"Mesut Ozil":10}
pickle.dump(data,f)

data = {"Harry Kane":50}
pickle.dump(data,f)

f.close()
