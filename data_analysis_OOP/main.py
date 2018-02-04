from DataHandlerClass import *
from EvaluateClass import *

dh = DataHandler("class_A.bin", "2-3")

dh.GetEvaluation()

print(dh.WhoIsTheLowest())
print(dh.WhoIsTheHighest())
print("\n")
print(dh.GetStandardDeviation())
print(dh.GetVariance())
print(dh.GetAverage())

#how to use static function/method
print("\n")
print(DataHandler.GetItemsFromFile("class_A.bin"))

#how to use object function/method
evaluator = Evaluate()
evaluator.evaluateClass(dh.GetAverage(), dh.GetStandardDeviation())
