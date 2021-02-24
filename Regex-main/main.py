from RegularExpressionGen.ParseTree import ParseTree
from RegularExpressionGen.Evaluate import evaluate

Ptree = ParseTree('( ( A * ) . ( C | B ) )') #Enter regular expression here

#Enter the number of strings you want to generate
numOut = int(input())
Outputs = []
for i in range(numOut):
    while True:
        out = evaluate(Ptree)
        if out not in Outputs:
            Outputs.append(out)
            break

for i in range(len(Outputs)):
    print(i + 1, ' : ', Outputs[i])
