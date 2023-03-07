from importer import json, urllib, pd, np, Pipeline, SimpleImputer, OneHotEncoder, StandardScaler, ColumnTransformer, joblib, FieldStorage, cgitb , cgi 
from function1 import is_uniprot 

UniProtID=  input("Enter in the uniprot ID name \n") 

var=is_uniprot(UniProtID)
if var== False: 
    print("Enter in Proper UniProtID") 
    exit()
else:
    print("You are good to go")
  

url_old="https://rest.uniprot.org/uniprotkb/"
url= url_old+UniProtID
data=json.load(urllib.request.urlopen(url))

organism=data['organism']['scientificName']
name=data['proteinDescription']['recommendedName']['fullName']['value']

print("Your protein selected is from organism :",organism)
print("The name of your protein/enzyme selected is:",name)

seq=data['sequence']['value'] #Array1

seq=list(seq)
l=len(seq)
pos=list(range(1,l+1)) #Array2
UniID=[]
for i in range(0,l):
    UniID.append(UniProtID)
    
d= {"UniProt":UniID, "AA":seq, "Position":pos}
df2=pd.DataFrame.from_dict(d)

file1=open("./data/Expasy_AA_scales.txt",'r+')
with file1 as f:
    t=f.readlines()

new_list=[]
for i in range(0,len(t)):
    q=t[i]
    q=q.split("\t")
    new_list.append(q)

df1=pd.DataFrame(new_list)
df1.columns=df1.iloc[0]
df1=df1[1:] #cleans up the dataframe and gets the values into a dataframe that can be used for parameter reading
df1.rename(columns= {'Hphob_Rf_mobility\n':'Hphob_Rf_mobility'}, inplace=True)
df1['Hphob_Rf_mobility'] = df1['Hphob_Rf_mobility'].str.replace('\n', '')

df_set1= df2.merge(df1)
df_raw=df_set1
#PreProcessing
df_raw.drop_duplicates(inplace=True)
df_raw.sort_values(by=['UniProt','Position'], inplace=True)
df_raw.reset_index(inplace=True)
df_preprep= df_raw.drop(columns=['index'])

df_cat= ["UniProt","AA"] #Categorical Variable

df_num=[]

for col in df_preprep:
    df_num.append(col)
    
unwanted_indices=[0,1]
for ele in sorted(unwanted_indices, reverse = True):
    del df_num[ele]



protein_array=['A','R','L','M','K','Q','E','I','W','S','Y','F','H','V','N','T','C'] #AA commonly found
df_prep=df_preprep[df_preprep["AA"].isin(protein_array)]

df_news= df_prep[['Position','alpha_helix_Deleage_Roux','alpha_helix_Chou_Fasman', 'alpha_helix_Levitt',
       'beta_turn_Chou_Fasman', 'beta_turn_Levitt',
       'beta_turn_Deleage_Roux', 'Average_area_buried', 'Refractivity',
       'HPLC_TFA_retention', 'Hphob_HPLC_Parker', 'Hphob_Miyazawa',
       'HPLC_HFBA_retention', 'Hphob_OMH_Sweet', 'Hphob_Rf_mobility',
       'beta_sheet_Chou_Fasman','Hphob_Rose','Bulkiness']]

df_news2=df_news.columns #the numerical variables for the model 
df_news2=list(df_news2)

df_news.astype({'Position': 'object'}).dtypes


onehot_encoder = OneHotEncoder()
num_pipeline = Pipeline([ ('imputer', SimpleImputer(strategy="median")),('std_scaler', StandardScaler()) ])
full_pipeline = ColumnTransformer([("num", num_pipeline, df_news2),("cat", OneHotEncoder(), df_cat),])

Data_new = full_pipeline.fit_transform(df_prep)


print("The dimensions of your data are: ",Data_new.shape) 


print("Your model is now gonna show you the values: enjoy")

final_model2 = joblib.load("final_model.pkl") #loads the ML Model


a=final_model2.predict(Data_new)

array_count=['UniProt','Position','AA']
df_final= df_preprep[array_count]
a=list(a) #makes the ml predictor into a list
b=len(a) #length of predicted model
r=len(df_final) #length of amino acids
for i in range(0,r):
    if df_final.iloc[i,2] not in protein_array:
        a.insert(i,'0')

df_final["is_alpha_helix_or_not"]=a

print(df_final.to_string())

#if you want to see al

    
    


