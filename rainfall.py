
import pandas as pd

#task 1

data = {'Month':pd.Series(['January','Febuary','March','April','May','June','July','August','September','October','Noveember','December']),
    'Rainfall':pd.Series([1.65,1.25,1.94,2.75,3.14,3.65,5.05,1.50,1.33,0.07,0.50,2.30]),

}


#create data frame
#df=pd.DataFrame(data)
#dfc=pd.read_csv(r'./rain.csv')
df=pd.read_json(r'./rain.json')

print("Our Data Frrame : ")
print(df,"\n")

#fill in missing values with 0
"""

dfzeroes =df.fillna(0)

print("Our new Data Frrame : ")
print(dfzeroes,"\n")
"""

#removes rows with the missing values

dfclean = df.dropna(0);
print("New data = \n",dfclean)


#create a count of all rows that contain nan

count = 0
for i ,row in df.iterrows():
    if any(row.isnull()):
        count = count +1
print("\n Number of rows with nan : "+str(count))

print(" Mean : ",dfclean.mean())

print("\n Median : ",dfclean.median())

print("\n Standard Deviation : ",dfclean.std())

#print the rainfall and ean for first few months

rainfall = dfclean['Rainfall'][0:3]
print(rainfall,"\n")
print("RAinfall mean for first 3 months " ,rainfall.mean(),"\n")

#print just rainfall and temperature

dfTempRain = (dfclean[['Temperature','Rainfall']])
print(dfTempRain)
print("Mean : \n",dfTempRain.mean())

index=dfclean['Month']
dfIndexed= dfclean.set_index(index)

#requires a properly indexed dataframe
print(" Finds a row by value \n",dfIndexed.loc['March'])















