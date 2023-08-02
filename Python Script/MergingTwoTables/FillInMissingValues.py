import pandas as pd



def filling_missing_values(filepath):

#Converting the csv to a dataframe
    df = pd.read_csv(filepath)
    
#Extracting the dataframe where the item description is null
    df1 = df[df['item_description'].isnull()]
    
#Extracting the dataframe where the item description is not null
    df2 = df[df['item_description'].notnull()]
    i = len(df1)
    
#Storing the values item description to a list 
    item_description1 = df2['item_description']
    item_description = item_description1[:i]
    
# item number   
    item_number1= df2['Item_Number']
    item_number = item_number1[:i]
    
# material number   
    material_number1= df2['Material_Number']
    material_number = material_number1[:i]
    
#Adding the values of extracted item description to the original table where it was null
    df1.iloc[0:i+1,df1.columns.get_loc('item_description')]=item_description
    df1.iloc[0:i+1,df1.columns.get_loc('Item_Number')]=item_number
    df1.iloc[0:i+1,df1.columns.get_loc('Material_Number')]=material_number
  
#Generating a storing the new result to a new CSV
    df1.to_csv(filepath+"output.csv",index=False)
        


