import pandas as pd
def toSmallDf(df):
	dfTemp=pd.DataFrame(columns=['fullNumber', 'sex','country', 'id'])
	dfTemp['fullNumber']=df.iloc[:,0]
	dfTemp['sex']=dfTemp.apply(lambda x: x.fullNumber[0], axis=1)
	dfTemp['country']=dfTemp.apply(lambda x: x.fullNumber[1:4], axis=1)
	dfTemp['id']=dfTemp.apply(lambda x: x.fullNumber[4:], axis=1)
	return dfTemp

def splitID(fullNumber):
	sex = fullNumber[0]
	countryCode = fullNumber[1:4]
	id=fullNumber[4:]
	return sex, countryCode, id
