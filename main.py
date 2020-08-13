import pandas as pd
import numpy as np
from tqdm import tqdm

print('reading')
eur_usd = pd.read_excel (r'EUR:USD.xlsx')
print('eur_usd')

#usd_cad = pd.read_excel (r'USD:CAD.xlsx')
#print('usd_cad')

#aud_usd = pd.read_excel (r'AUD:USD.xlsx')
#print('aud_usd')

#gbp_usd = pd.read_excel (r'GBP:USD.xlsx')
#print('gbp_usd')

#usd_jpy = pd.read_excel (r'USD:JPY.xlsx')
#print('usd_jpy')

class data:
    def __init__(self, df):
        self.normal = df
        self.ma6 = prices.rolling(window=6).mean()
        self.ma14 = prices.rolling(window=14).mean()
        self.ma26 = prices.rolling(window=26).mean()

    def cross(self, rng):
        l1, l2, l3 = list(self.ma6[rng[0]:rng[1]]), list(self.ma14[rng[0]:rng[1]]), list(self.ma26[rng[0]:rng[1]])
        dif = []
        put = []
        call = []
        if len(l1)!=len(l2)and len(l1)!=len(l2):
            raise NameError("not ==")
        print("makng dif")
        for i in tqdm(range(len(l1))):
            dif = dif+[l1[i]-l2[i]]
        print("runnign algorithm")
        for j in tqdm(range(len(dif))):
            temp = l1[j], dif[j]>=0, l3[j]
            if j>0:
                if temp[1]!=lastn[1]:
                    if lastn[0]<temp[0]<l3[j]:
                        call = call+[j]
                    elif lastn[0]>temp[0] and l3[j]<lastn[0]:
                        put = put+[j]
            lastn = temp
        put = np.array(put)+365120
        call = np.array(call)+365120
        return(call, put)

    def check(self, d, t):
        cs, ps = d[0], d[1]
        price = self.normal
        good = 0
        bad = 0
        print("testing calls")
        for c in range(len(cs)):
            if price[c+t]> price[c]:
                good = good+1
            elif price[c+t]< price[c]:
                bad = bad+1
        print("testing puts")
        for p in range(len(ps)):
            if price[p+t]< price[p]:
                good = good+1
            elif price[p+t]> price[p]:
                bad = bad+1

            ans = str(str((good/(good+bad))*100)+"%")
            return(ans)
            
        
eur_usd = data(eur_usd["close"])
#usd_cad = data(usd_cad["close"])
#aud_usd = data(aud_usd["close"])
#gbp_usd = data(gbp_usd["close"])
#usd_jpy = data(usd_jpy["close"])

DTeur_usd = values.cross([60, len(eur_usd.normal)])

print(values.check([calls, puts], 2))