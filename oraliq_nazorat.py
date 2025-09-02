import numpy as np

matritsa = np.random.randint(0, 101, size=(5, 4))
print(matritsa)

dic = {}

for i in range(5):
    baholar = []
    baholar_np = matritsa[i]
    
    for baho in baholar_np:
        baholar.append(int(baho))
        
    ortacha = np.mean(baholar)
    dic["talaba" + str(i+1)] = {"baholar": baholar, "ortacha": ortacha}

for talaba, bahosi in dic.items():
    print(f"{talaba} ning baholari: {bahosi["baholar"]}, ortacha: {bahosi["ortacha"]}")
    
    
