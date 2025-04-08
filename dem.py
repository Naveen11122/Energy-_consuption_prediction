import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats             
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naveen@123",
    database="electricity"
)
mycur = mydb.cursor()
mycur1 = mydb.cursor()
mycur2 = mydb.cursor()



# Load the dataset
# dt = pd.read_csv(r"D:\\electrycitydata4.csv")  # Use raw string for the file path
# print("Original DataFrame:")
# print(dt)

# # Display the first few rows  
# print("\nFirst 5 Rows of the DataFrame:")
# print(dt.head())

# # Display DataFrame info
# print("\nDataFrame Info:")
# dt.info()

# # Print the shape of the DataFrame
# print("\nShape of the DataFrame:")
# print(dt.shape)

# # Drop duplicates
# dt = dt.drop_duplicates()
# print("\nDataFrame after dropping duplicates:")
# print(dt)

# # Check for null values percentage
# null_percentage = dt.isnull().sum() / dt.shape[0] * 100
# print("\nPercentage of Null Values in Each Column:")
# print(null_percentage)

# # Remove rows with missing data
# dt.dropna(inplace=True)
# print("\nDataFrame after removing missing data:")
# print(dt)

# # Clean the specified columns by removing alphabets and non-numeric characters
# columns_to_clean = [
#     "Oil_Consumption_EJ",
#     "Gas_Consumption_EJ",
#     "Coal_Consumption_EJ",
#     "Hydro_Consumption_EJ",
#     "Nuclear_Consumption_EJ",
#     "Coconj"
# ]

# for col in columns_to_clean:
#     if col in dt.columns:
#         print(f"Cleaning alphabets and other non-numeric characters from '{col}':")
#         dt[col] = dt[col].astype(str).str.replace(r'[a-zA-Z]', '', regex=True)
#         dt[col] = dt[col].astype(str).str.replace(r'[^0-9.]', '', regex=True)  # Keep only numbers and decimal
#         dt[col] = pd.to_numeric(dt[col], errors='coerce')  # Convert to numeric and handle errors
#         dt[col].fillna(0, inplace=True)  # Replace NaN with 0

# print("\nInvalid Datet Values:")
# print(dt[dt["Datet"].isnull()])  # Check rows with NaN in the `Datet` column

# # Parse "Datet" column and extract Month/Year
# if "Datet" in dt.columns:
#     dt["Datet"] = pd.to_datetime(dt["Datet"], errors='coerce')
#     dt["Month"] = dt["Datet"].dt.month
#     dt["Year"] = dt["Datet"].dt.year
#     dt["Month"] = dt["Month"].fillna(0).astype(int)  # Fill NaN with 0 before converting to integer
#     dt["Year"] = dt["Year"].fillna(0).astype(int)
#     dt = dt.dropna(subset=["Datet"])  # Drop rows where `Datet` is NaN
# else:
#     print("'Datet' column not found in DataFrame.")
# yr1=dt["Datet"]
# # Display the updated DataFrame
# print("\nUpdated DataFrame:")
# for yr in range(2010,2020):
#      d1=[]
     
#      d1.append(yr)
#      if "Year" in dt.columns:
#     #   for yr in range(2010, 2020):
#         print(f"\nYear: {yr}")
#         dt_year = dt[dt["Year"] == yr]
#         if len(dt_year) > 0:
#             columns1 = [
#                 "Oil_Consumption_EJ" 
#     #             # "Gas_Consumption_EJ"
#             ]       
#             dt_year[ columns1] = dt_year[columns1].apply(pd.to_numeric, errors='coerce') 
#             print("year") 
#             dt_year['Year']=dt_year['Year']

#             # print(dt)
#             # v=str(yr)
#             print("Total consuption") 
#             dt1=(dt_year[columns1].sum() )  
#             print(dt1) 
#             v1=str(float(dt1.values))
#             dt2= dt_year[columns1].mean()       
#             print(dt2)
#             v2=str(float(dt2.values))
#             dt3= dt_year[columns1].median()       
#             print(dt3)
#             v3=str(float(dt3.values))
#             print("Variance:")
#             dt4= dt_year[columns1].var()       
#             print(dt4)
#             v4=str(float(dt4.values))
#             print("Standard Deviation:")
#             dt5= dt_year[columns1].std()       
#             print(dt5)
#             v5=str(float(dt5.values))
#             d1.append(v1)
#             d1.append(v2)
#             d1.append(v3)
#             # d1.append(v4)
#             d1.append(v4)
#             d1.append(v5)
#             print("total=",d1)
#         if len(dt_year) > 0:
#             column2 = [    "Gas_Consumption_EJ"
#             ]
#             dt_year[ column2] = dt_year[column2].apply(pd.to_numeric, errors='coerce') 
#             print("year") 
#             dt_year['Year']=dt_year['Year']
#             print(dt)
#             v=str(yr)
#             print("Total consuption") 
#             dt_gas1=(dt_year[column2].sum() )  
#             print(dt_gas1) 
#             v_gas1=str(float(dt_gas1.values))
#             dt_gas2= dt_year[column2].mean()       
#             print(dt_gas2)
#             v_gas2=str(float(dt_gas2.values))
#             dt_gas3= dt_year[column2].median()       
#             print(dt_gas3)
#             v_gas3=str(float(dt_gas3.values))
#             print("Variance:")
#             dt_gas4= dt_year[column2].var()       
#             print(dt_gas4)
#             v_gas4=str(float(dt_gas4.values))

#             print("Standard Deviation:")
#             dt_gas5= dt_year[column2].std()       
#             print(dt_gas5)
#             v_gas5=str(float(dt_gas4.values))
#             d1.append(v_gas1)
#             d1.append(v_gas2)
#             d1.append(v_gas3)
#             d1.append(v_gas4)
#             d1.append(v_gas5)
#             print("append=",d1)
#         if len(dt_year) > 0:
#             column3 = [ "Coal_Consumption_EJ"
#             ]            
#             dt_year[ column3] = dt_year[column3].apply(pd.to_numeric, errors='coerce') 
#             print("Total consuption") 
#             dt_col1=(dt_year[column3].sum() )  
#             print(dt_col1) 
#             v_col1=str(float(dt_col1.values))
#             dt_col2= dt_year[column3].mean()       
#             print(dt_col2)
#             v_col2=str(float(dt_col2.values))
#             dt_col3= dt_year[column3].median()       
#             print(dt_col3)
#             v_col3=str(float(dt_col3.values))
#             print("Variance:")
#             dt_col4= dt_year[column3].var()       
#             print(dt_col4)
#             v_col4=str(float(dt_col4.values))
#             print("Standard Deviation:")
#             dt_col5= dt_year[column3].std()       
#             print(dt_col5)
#             v_col5=str(float(dt_col5.values))
#             d1.append(v_col1)
#             d1.append(v_col2)
#             d1.append(v_col3)
#             # d1.append(v4)
#             d1.append(v_col4)
#             d1.append(v_col5)
#             print("append=",d1) 
#         if len(dt_year) > 0:
#             column4 = [ "Hydro_Consumption_EJ"
#             ]            
#             dt_year[ column4] = dt_year[column4].apply(pd.to_numeric, errors='coerce') 
#             # print("year") 
#             # dt_year['Year']=dt_year['Year']
#             # print(dt)
#             # v=str(yr)
#             print("Total consuption") 
#             dt_hy1=(dt_year[column4].sum() )  
#             print(dt_hy1) 
#             v_hy1=str(float(dt_hy1.values))
#             dt_hy2= dt_year[column4].mean()       
#             print(dt_hy2)
#             v_hy2=str(float(dt_hy2.values))
#             dt_hy3= dt_year[column4].median()       
#             print(dt_hy3)
#             v_hy3=str(float(dt_hy3.values))
#             # dt4 = dt_year[columns].mode()
#             # print(dt4)
#             # v4=str(dt4.values)
#             print("Variance:")
#             dt_hy4= dt_year[column4].var()       
#             print(dt_hy4)
#             v_hy4=str(float(dt_hy4.values))
#             print("Standard Deviation:")
#             dt_hy5= dt_year[column4].std()       
#             print(dt_hy5)
#             v_hy5=str(float(dt_hy5.values))
#             d1.append(v_hy1)
#             d1.append(v_hy2)
#             d1.append(v_hy3)
#             # d1.append(v4)
#             d1.append(v_hy4)
#             d1.append(v_hy5)
#             print("append=",d1)    

#         if len(dt_year) > 0:
#             column5 = [ "Nuclear_Consumption_EJ"
#             ]            
#             dt_year[ column5] = dt_year[column5].apply(pd.to_numeric, errors='coerce') 
#             print("Total consuption") 
#             dt_nc1=(dt_year[column5].sum() )  
#             print(dt_nc1) 
#             v_nc1=str(float(dt_nc1.values))
#             dt_nc2= dt_year[column5].mean()       
#             print(dt_nc2)
#             v_nc2=str(float(dt_nc2.values))
#             dt_nc3= dt_year[column5].median()       
#             print(dt_nc3)
#             v_nc3=str(float(dt_nc3.values))
#             print("Variance:")
#             dt_nc4= dt_year[column5].var()       
#             print(dt_nc4)
#             v_nc4=str(float(dt_nc4.values))
#             print("Standard Deviation:")
#             dt_nc5= dt_year[column5].std()       
#             print(dt_nc5)
#             v_nc5=str(float(dt_nc5.values))
#             d1.append(v_nc1)
#             d1.append(v_nc2)
#             d1.append(v_nc3)
#             # d1.append(v4)
#             d1.append(v_nc4)
#             d1.append(v_nc5)
#             print("append=",d1)  
#         if len(dt_year) > 0:
#             column6 = [ "Coconj"
#             ]            
#             dt_year[ column6] = dt_year[column6].apply(pd.to_numeric, errors='coerce') 
#             print("Total consuption") 
#             dt_co1=(dt_year[column6].sum() )  
#             print(dt_co1) 
#             v_co1=str(float(dt_nc1.values))
#             dt_co2= dt_year[column6].mean()       
#             print(dt_co2)
#             v_co2=str(float(dt_co2.values))
#             dt_co3= dt_year[column6].median()       
#             print(dt_co3)
#             v_co3=str(float(dt_co3.values))
#             print("Variance:")
#             dt_co4= dt_year[column6].var()       
#             print(dt_co4)
#             v_co4=str(float(dt_co4.values))
#             print("Standard Deviation:")
#             dt_co5= dt_year[column6].std()     
#             print(dt_co5)
#             v_co5=str(float(dt_co5))
#             print("value of co5=",v_co5)
#             d1.append(v_co1)
#             d1.append(v_co2)
#             d1.append(v_co3)
#             d1.append(v_co4)
#             d1.append(v_co5)
#             print("append=",d1)   
#             # #Insert the total oil consumption into the database
#             ## SQL statement to insert data
#             # mycur.execute("create table electricity_consptionsssssn(yr varchar(50),total_Oil_Consumption_EJ FLOAT,Mean_oil FLOAT,Medan_oil FLOAT,var_oil FLOAT,std_oil FLOAT,total_Gas_Consumption_EJ FLOAT,Mean_gas FLOAT,Medan_gas FLOAT,var_gas FLOAT,std_gas FLOAT,total_Coal_Consumption_EJ FLOAT,Mean_coal FLOAT,Medan_coal FLOAT,var_coal FLOAT,std_coal FLOAT,total_Hydro_Consumption_EJ FLOAT,Mean_hydro FLOAT,Medan_hydro FLOAT,var_hydro FLOAT,std_hydro FLOAT,total_Nuclear_Consumption_EJ FLOAT,Mean_Nuclear FLOAT,Medan_Nuclear FLOAT,var_Nuclear FLOAT,std_Nuclear FLOAT,total_Coconj FLOAT,mean_co FLOAT,medan_co FLOAT,vr_co FLOAT,st_co FLOAT)")
#             # mycur.ex#ecute("create table electricity_consptionssss(yr varchar(50),total_Oil_Consumption_EJ varchar(50),Mean_oil varchar(50),Medan_oil varchar(50),var_oil varchar(50),std_oil varchar(50),total_Gas_Consumption_EJ varchar(50),Mean_gas varchar(50),Medan_gas varchar(50),var_gas varchar(50),std_gas varchar(50),total_Coal_Consumption_EJ varchar(50),Mean_coal varchar(50),Medan_coal varchar(50),var_coal varchar(50),std_coal varchar(50),total_Hydro_Consumption_EJ varchar(50),Mean_hydro varchar(50),Medan_hydro varchar(50),var_hydro varchar(50),std_hydro varchar(50),total_Nuclear_Consumption_EJ varchar(50),Mean_Nuclear varchar(50),Medan_Nuclear varchar(50),var_Nuclear varchar(50),std_Nuclear varchar(50),total_Coconj varchar(50),mean_co varchar(50),medan_co varchar(50),vr_co varchar(50),st_co varchar(50))")    
#             sql="insert into electricity_consptionsssssn(yr,total_Oil_Consumption_EJ,Mean_oil,Medan_oil,var_oil,std_oil,total_Gas_Consumption_EJ,Mean_gas,Medan_gas,var_gas,std_gas,total_Coal_Consumption_EJ,Mean_coal,Medan_coal,var_coal,std_coal,total_Hydro_Consumption_EJ,Mean_hydro,Medan_hydro,var_hydro,std_hydro,total_Nuclear_Consumption_EJ,Mean_Nuclear,Medan_Nuclear,var_Nuclear,std_Nuclear,total_Coconj,mean_co,medan_co,vr_co,st_co) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             # sql="insert into electricity_consptionss(yr) values(%s)"
#             mycur.execute(sql,d1)
#             ###mydb.commit()
#             print(mycur.rowcount, "record inserted.")
#             mycur.execute("select * from electricity_consptionsssssn")
#             result = mycur.fetchall()
#             print(result)
# # # User input
while True:

    print("press 1 for total oil consuptios")
    print("press 2 for total gas consuptions")
    print("press 3 for total coal consuption")
    print("press 4 for total hydro consption")
    print("press 5 for total nucliar")
    print("press 6 for total co2 consption")
    print("press 7 for avraage with extra load of[oil,gas,coal,hydro,nucleyer,co2]")
    print("perss 8 for exite any kye to continue")

    num = int(input("Enter num="))
    if num == 1:
        mycur.execute("SELECT yr, min(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn GROUP BY yr")
        result = mycur.fetchall()
        if result:
           years = [row[0] for row in result]
           consumptions = [row[1] for row in result]
           years = np.array(years)
           consumptions = np.array(consumptions)

        # Plotting
           fig = plt.figure(figsize=(10, 5))
           plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
           plt.xlabel("Year")
           plt.ylabel("Total oil Consumption (EJ)")
           plt.title("Yearly Oil Consumption")
           plt.show()
           dr=[]
           mycur.execute(
           "SELECT AVG(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Oil_Consumption_EJ NOT IN (SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Oil_Consumption_EJ NOT IN (SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn)"
           )


           result = mycur.fetchall()[0][0]  # Extract the numeric value
           dr.append(result)
        # Query for the minimum value
           mycur.execute("SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
           result2 = mycur.fetchall()[0][0]  # Extract the numeric value
           dr.append(result2)

           # Query for the maximum value
           mycur.execute("SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
           result3 = mycur.fetchall()[0][0]  # Extract the numeric value
           dr.append(result3)

           # Prepare data for the plot
           values = [result, result2, result3]
           labels = ["Average", "Minimum", "Maximum"]

           # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric")
           plt.ylabel("Total Oil Consumption (EJ)")
           plt.title("Oil Consumption Metrics")
           plt.show()



           table= "electricity_consptionsssssn"  # Replace with the correct name:

           # Fetch all data at once
           mycur.execute(f"SELECT total_Oil_Consumption_EJ FROM {table}")
           results = mycur.fetchall()

    #       Ensure sufficient data is available
           if len(results) < 10:
                print("Not enough data in the table.")
           else:
    # Extract the first 10 results
               dt2 = [row[0] for row in results[:10]]

    # Calculate differences (dt3)
               dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
    # Calculate the average of the differences
               s = sum(dt3) / len(dt3)
               dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
               mx1=max(dt4)
               mn1=min(dt4)
               newload_avg1=sum(dt4)/len(dt4)



        #    entry=int(input("after 2019 load_capacity="))
        #    mycur.execute(
        #    "SELECT AVG(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Oil_Consumption_EJ NOT IN (SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Oil_Consumption_EJ NOT IN (SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn)"
        #    )

        #    result = mycur.fetchall()[0][0] 
        #    new_conection22=entry+result

        #    mycur.execute("SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
        #    result2 = mycur.fetchall()[0][0]  # Extract the numeric value

        #    new_conection33=entry+result2

        #    mycur.execute("SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
        #    result3 = mycur.fetchall()[0][0]  # Extract the numeric value
        #    new_conection44=entry+result3

           values = [newload_avg1, mn1,mx1]
           labels = ["Average", "Minimum", "Maximum"]


            # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric with new conection")
           plt.ylabel("Total Oil Consumption with new conection (EJ)")
           plt.title("Oil Consumption Metrics with new conection")
           plt.show()
        else:
           print("No data found in the database.")

    elif num == 2:
        mycur.execute("SELECT yr, min(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn GROUP BY yr")
        result = mycur.fetchall()

        if result:
           years = [row[0] for row in result]
           consumptions = [row[1] for row in result]
           years = np.array(years)
           consumptions = np.array(consumptions)

        # Plotting
           fig = plt.figure(figsize=(10, 5))
           plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
           plt.xlabel("Year")
           plt.ylabel("Total Gas Consumption (EJ)")
           plt.title("Yearly Gas Consumption")
           plt.show()
           mycur.execute(
           "SELECT AVG(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Gas_Consumption_EJ NOT IN (SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Gas_Consumption_EJ NOT IN (SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn)"
           )


           result = mycur.fetchall()[0][0]  # Extract the numeric value
           # Query for the minimum value
           mycur.execute("SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
           result2 = mycur.fetchall()[0][0]  # Extract the numeric value

           # Query for the maximum value
           mycur.execute("SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
           result3 = mycur.fetchall()[0][0]  # Extract the numeric value
           # Prepare data for the plot
           values = [result, result2, result3]
           labels = ["Average", "Minimum", "Maximum"]

           # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric")
           plt.ylabel("Total gas Consumption (EJ)")
           plt.title("gas Consumption Metrics")
           plt.show()
           table_name = "electricity_consptionsssssn"  # Replace with the correct name

# Fetch all data at once
           mycur.execute(f"SELECT total_Gas_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()

# Ensure sufficient data is available
           if len(results) < 10:
               print("Not enough data in the table.")
           else:
    # Extract the first 10 results
              dt2 = [row[0] for row in results[:10]]

              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]

    # Calculate the average of the differences
              s = sum(dt3) / len(dt3)

              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]

              mx2=max(dt4)
              mn2=min(dt4)

              newload_avg2=sum(dt4)/len(dt4)
#            entry=int(input("after 2019 load_capacity="))
#            mycur.execute(
#            "SELECT AVG(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Gas_Consumption_EJ NOT IN (SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Gas_Consumption_EJ NOT IN (SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn)"
#             )
#            result = mycur.fetchall()[0][0] 
#            new_conection1=entry+result
#            mycur.execute("SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
#            result2 = mycur.fetchall()[0][0]  # Extract the numeric value
#            new_conection2=entry+result2


#            mycur.execute("SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
#            result3 = mycur.fetchall()[0][0]  # Extract the numeric value
#            new_conection3=entry+result3


           values = [newload_avg2, mn2, mx2]
           labels = ["Average", "Minimum", "Maximum"]

           # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric with new conection")
           plt.ylabel("Total gas Consumption with new conection (EJ)")
           plt.title("Gas Consumption Metrics with new conection")
           plt.show()
        else:
            print("No data found in the database.")


    elif num == 3:
        # Corrected query with aggregation
       mycur.execute("SELECT yr, min(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn GROUP BY yr")
       result = mycur.fetchall()

       if result:
           years = [row[0] for row in result]
           consumptions = [row[1] for row in result]
           years = np.array(years)
           consumptions = np.array(consumptions)
           # Plotting
           fig = plt.figure(figsize=(10, 5))
           plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
           plt.xlabel("Year")
           plt.ylabel("Total Coal Consumption (EJ)")
           plt.title("Yearly Coal Consumption")
           plt.show()
           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Coal_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()


           if len(results) < 10:
               print("Not enough data in the table.")
           else:
    # Extract the first 10 results
              dt2 = [row[0] for row in results[:10]]

    # Calculate differences (dt3)
              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]


              s = sum(dt3) / len(dt3)

              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
              mx3=max(dt4)
              mn3=min(dt4)
              newload_avg3=sum(dt4)/len(dt4)
#            entry=int(input("after 2019 load_capacity="))
#            mycur.execute(
#            "SELECT AVG(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Coal_Consumption_EJ NOT IN (SELECT MAX(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Coal_Consumption_EJ NOT IN (SELECT MIN(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn)"
#              )
#            result = mycur.fetchall()[0][0] 
#            new_conection4=entry+result

#            mycur.execute("SELECT MIN(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn")
#            result2 = mycur.fetchall()[0][0]  # Extract the numeric value

#            new_conection5=entry+result2


#            mycur.execute("SELECT MAX(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn")
#            result3 = mycur.fetchall()[0][0]  # Extract the numeric value
#            new_conection6=entry+result3

           values = [newload_avg3, mn3, mx3]
           labels = ["Average", "Minimum", "Maximum"]

#         # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric with new conection")
           plt.ylabel("Total Coal Consumption with new conection (EJ)")
           plt.title("Coal Consumption Metrics with new conection")
           plt.show()
       else:
          print("No data found in the database.")

# # hydro consuption
    elif num == 4:
       mycur.execute("SELECT yr, min(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn GROUP BY yr")
       result = mycur.fetchall()

       if result:
           years = [row[0] for row in result]
           consumptions = [row[1] for row in result]
           years = np.array(years)
           consumptions = np.array(consumptions)

           # Plotting
           fig = plt.figure(figsize=(10, 5))
           plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
           plt.xlabel("Year")
           plt.ylabel("Total hydro Consumption (EJ)")
           plt.title("Yearly hydro Consumption")
           plt.show()
           mycur.execute(
           "SELECT AVG(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Hydro_Consumption_EJ NOT IN (SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Hydro_Consumption_EJ NOT IN (SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn)"
           )


           result = mycur.fetchall()[0][0]  # Extract the numeric value
        # Query for the minimum value
           mycur.execute("SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
           result2 = mycur.fetchall()[0][0]  # Extract the numeric value

        # Query for the maximum value
           mycur.execute("SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
           result3 = mycur.fetchall()[0][0]  # Extract the numeric value
        # Prepare data for the plot
           values = [result, result2, result3]
           labels = ["Average", "Minimum", "Maximum"]

         # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric")
           plt.ylabel("total_Hydro_Consumption_EJ")
           plt.title("Hydro Consumption")
           plt.show()
           
           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Hydro_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()


           if len(results) < 10:
               print("Not enough data in the table.")
           else:
    # Extract the first 10 results
              dt2 = [row[0] for row in results[:10]]

    # Print the fetched results

    # Calculate differences (dt3)
              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]


              s = sum(dt3) / len(dt3)

              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
              mx4=max(dt4)
              mn4=min(dt4)
              newload_avg4=sum(dt4)/len(dt4)

#            entry=int(input("after 2019 load_capacity="))
#            mycur.execute(
#            "SELECT AVG(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Hydro_Consumption_EJ NOT IN (SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Hydro_Consumption_EJ NOT IN (SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn)"
#            ) 
#            result = mycur.fetchall()[0][0] 
#            new_conection7=entry+result

#            mycur.execute("SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
#            result2 = mycur.fetchall()[0][0]  # Extract the numeric value
 
#            new_conection8=entry+result2


#            mycur.execute("SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
#            result3 = mycur.fetchall()[0][0]  # Extract the numeric value
#            new_conection9=entry+result3

           values = [newload_avg4, mn4, mx4]
           labels = ["Average", "Minimum", "Maximum"]
        # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric with new conection")
           plt.ylabel("Total HYdro Consumption with new conection (EJ)")
           plt.title("Hydro Consumption Metrics with new conection")
           plt.show()
       else:
         print("No data found in the database.")


     


    elif num == 5:
       mycur.execute("SELECT yr, min(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn GROUP BY yr")
       result = mycur.fetchall()

       if result:
           years = [row[0] for row in result]
           consumptions = [row[1] for row in result]
           years = np.array(years)
           consumptions = np.array(consumptions)

           # Plotting
           fig = plt.figure(figsize=(10, 5))
           plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
           plt.xlabel("Year")
           plt.ylabel("Total nuclear Consumption (EJ)")
           plt.title("Yearly nuclar Consumption")
           plt.show()
           mycur.execute(
           "SELECT AVG(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Nuclear_Consumption_EJ NOT IN (SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Nuclear_Consumption_EJ NOT IN (SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn)"
           )


           result = mycur.fetchall()[0][0]  # Extract the numeric value
            # Query for the minimum value
           mycur.execute("SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
           result2 = mycur.fetchall()[0][0]  # Extract the numeric value

          # Query for the maximum value
           mycur.execute("SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
           result3 = mycur.fetchall()[0][0]  # Extract the numeric value
        # Prepare data for the plot
           values = [result, result2, result3]
           labels = ["Average", "Minimum", "Maximum"]

            # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric")
           plt.ylabel("total_Nuclear_Consumption_EJ")
           plt.title("Nuclear Consumption")
           plt.show()
           table_name = "electricity_consptionsssssn"  # Replace with the correct name

# Fetch all data at once
           mycur.execute(f"SELECT total_Nuclear_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()

# Ensure sufficient data is available
           if len(results) < 10:
              print("Not enough data in the table.")
           else:
    # Extract the first 10 results
              dt2 = [row[0] for row in results[:10]]

    # Calculate differences (dt3)
              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
              s = sum(dt3) / len(dt3)
              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
              mx5=max(dt4)
              mn5=min(dt4)

              newload_avg5=sum(dt4)/len(dt4)
#            entry=int(input("after 2019 load_capacity="))
#            mycur.execute(
#            "SELECT AVG(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Nuclear_Consumption_EJ NOT IN (SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Nuclear_Consumption_EJ NOT IN (SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn)"
#            )
#            result = mycur.fetchall()[0][0] 
#            new_conection10=entry+result

#            mycur.execute("SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
#            result2 = mycur.fetchall()[0][0]  # Extract the numeric value

#            new_conection11=entry+result2


#            mycur.execute("SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
#            result3 = mycur.fetchall()[0][0]  # Extract the numeric value
#            new_conection12=entry+result3

           values = [newload_avg5, mn5, mx5]
           labels = ["Average", "Minimum", "Maximum"]

        # Plot the data
           fig = plt.figure(figsize=(10, 5))
           plt.bar(labels, values, color=['r','y','g'], width=0.4)
           plt.xlabel("Metric with new conection")
           plt.ylabel("Total Nucler Consumption with new conection (EJ)")
           plt.title("Nucler Consumption Metrics with new conection")
           plt.show()

        
       else:
           print("No data found in the database.")

    elif num == 6:
        mycur.execute("SELECT yr, min(total_Coconj) FROM electricity_consptionsssssn GROUP BY yr")
        result = mycur.fetchall()
        if result:
            years = [row[0] for row in result]
            consumptions = [row[1] for row in result]
            years = np.array(years)
            consumptions = np.array(consumptions)

        # Plotting
            fig = plt.figure(figsize=(10, 5))
            plt.bar(years, consumptions, color=['r','b','m','y'], width=0.4)
            plt.xlabel("Year")
            plt.ylabel("Total Co2 Consumption (EJ)")
            plt.title("Yearly Co2 Consumption")
            plt.show()
            mycur.execute(
            "SELECT AVG(total_Coconj) FROM electricity_consptionsssssn WHERE total_Coconj NOT IN (SELECT MAX(total_Coconj) FROM electricity_consptionsssssn) AND total_Coconj NOT IN (SELECT MIN(total_Coconj) FROM electricity_consptionsssssn)"
            )


            result = mycur.fetchall()[0][0]  # Extract the numeric value
       #     Query for the minimum value
            mycur.execute("SELECT MIN(total_Coconj) FROM electricity_consptionsssssn")
            result2 = mycur.fetchall()[0][0]  # Extract the numeric value

        # Query for the maximum value
            mycur.execute("SELECT MAX(total_Coconj) FROM electricity_consptionsssssn")
            result3 = mycur.fetchall()[0][0]  # Extract the numeric value
            # Prepare data for the plot
            values = [result, result2, result3]
            labels = ["Average", "Minimum", "Maximum"]

         # Plot the data
            fig = plt.figure(figsize=(10, 5))
            plt.bar(labels, values, color=['r','y','g'], width=0.4)
            plt.xlabel("Metric")
            plt.ylabel("total_Coconj")
            plt.title("CO2 Consumption")
            plt.show()
            table_name = "electricity_consptionsssssn"  # Replace with the correct name

# Fetch all data at once
            mycur.execute(f"SELECT total_Coconj FROM {table_name}")
            results = mycur.fetchall()

# Ensure sufficient data is available
            if len(results) < 10:
                print("Not enough data in the table.")
            else:
    # Extract the first 10 results
                dt2 = [row[0] for row in results[:10]]

    # Print the fetched resu

    # Calculate differences (dt3)
                dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]

                s = sum(dt3) / len(dt3)

                dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]

                mx6=max(dt4)

                mn6=min(dt4)

                newload_avg6=sum(dt4)/len(dt4)
#             entry=int(input("after 2019 load_capacity="))
#             mycur.execute(
#             "SELECT AVG(total_Coconj) FROM electricity_consptionsssssn WHERE total_Coconj NOT IN (SELECT MAX(total_Coconj) FROM electricity_consptionsssssn) AND total_Coconj NOT IN (SELECT MIN(total_Coconj) FROM electricity_consptionsssssn)"
#             )
#             result = mycur.fetchall()[0][0] 
#             new_conection13=entry+result

#             mycur.execute("SELECT MIN(total_Coconj) FROM electricity_consptionsssssn")
#             result2 = mycur.fetchall()[0][0]  # Extract the numeric value

#             new_conection14=entry+result2
#             print("new conection2=",new_conection14)


#             mycur.execute("SELECT MAX(total_Coconj) FROM electricity_consptionsssssn")
#             result3 = mycur.fetchall()[0][0]  # Extract the numeric value
#             new_conection15=entry+result3
    
            values = [ newload_avg6, mn6, mx6]
            labels = ["Average", "Minimum", "Maximum"]

            # Plot the data
            fig = plt.figure(figsize=(10, 5))
            plt.bar(labels, values, color=['r','y','g'], width=0.4)
            plt.xlabel("Metric with new conection")
            plt.ylabel("Total CO2 Consumption with new conection (EJ)")
            plt.title("CO2 Consumption Metrics with new conection")
            plt.show()
    elif num==7:
           table= "electricity_consptionsssssn"
           mycur.execute(f"SELECT total_Oil_Consumption_EJ FROM {table}")
           results = mycur.fetchall()
           if len(results) < 10:
                print("Not enough data in the table.")
           else:
               dt2 = [row[0] for row in results[:10]]
               dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
               s = sum(dt3) / len(dt3)
               dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
               mx1=max(dt4)
               mn1=min(dt4)
               newload_avg1=sum(dt4)/len(dt4)
               


           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Gas_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()
           if len(results) < 10:
                print("Not enough data in the table.")
           else:
                dt2 = [row[0] for row in results[:10]]
                dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
                s = sum(dt3) / len(dt3)
                dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
                mx2=max(dt4)
                mn2=min(dt4)
                newload_avg2=sum(dt4)/len(dt4)


           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Coal_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()
           if len(results) < 10:
             print("Not enough data in the table.")
           else:
             dt2 = [row[0] for row in results[:10]]
             dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
             s = sum(dt3) / len(dt3)
             dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
             mx3=max(dt4)
             mn3=min(dt4)
             newload_avg3=sum(dt4)/len(dt4) 
           table_name = "electricity_consptionsssssn"  # Replace with the correct name

# Fetch all data at once
           mycur.execute(f"SELECT total_Hydro_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()
           if len(results) < 10:
              print("Not enough data in the table.")
           else:
              dt2 = [row[0] for row in results[:10]]
            #   print("dt2:", dt2)
              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
            #   print("dt3:", dt3)
              s = sum(dt3) / len(dt3)
            #   print("Average difference (s):", s)
              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
              mx4=max(dt4)
              mn4=min(dt4)
              newload_avg4=sum(dt4)/len(dt4)   
           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Nuclear_Consumption_EJ FROM {table_name}")
           results = mycur.fetchall()
           if len(results) < 10:
              print("Not enough data in the table.")
           else:
              dt2 = [row[0] for row in results[:10]]
              print("dt2:", dt2)
              dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
              s = sum(dt3) / len(dt3)
              dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
              mx5=max(dt4)
              mn5=min(dt4)
              newload_avg5=sum(dt4)/len(dt4)
           table_name = "electricity_consptionsssssn"  # Replace with the correct name
           mycur.execute(f"SELECT total_Coconj FROM {table_name}")
           results = mycur.fetchall()
           if len(results) < 10:
               print("Not enough data in the table.")
           else:
            dt2 = [row[0] for row in results[:10]]
            dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
            s = sum(dt3) / len(dt3)
            dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
            mx6=max(dt4)
            mn6=min(dt4)
            newload_avg6=sum(dt4)/len(dt4)


#             entry=int(input("after 2019 load_capacity(oil)="))
#             mycur.execute(
#             "SELECT AVG(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Oil_Consumption_EJ NOT IN (SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Oil_Consumption_EJ NOT IN (SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn)"
#             )
#             result = mycur.fetchall()[0][0] 
#             new_conection22=entry+result
#             entry=int(input("after 2019 load_capacity(gas)="))
#             mycur.execute(
#             "SELECT AVG(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Gas_Consumption_EJ NOT IN (SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Gas_Consumption_EJ NOT IN (SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn)"
#              )
#             result = mycur.fetchall()[0][0] 
#             new_conection1=entry+result
#             entry=int(input("after 2019 load_capacity(coal)="))
#             mycur.execute(
#             "SELECT AVG(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Coal_Consumption_EJ NOT IN (SELECT MAX(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Coal_Consumption_EJ NOT IN (SELECT MIN(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn)"
#             )
#             result = mycur.fetchall()[0][0] 
#             new_conection4=entry+result
#             entry=int(input("after 2019 load_capacity(hydro)="))
#             mycur.execute(
#             "SELECT AVG(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Hydro_Consumption_EJ NOT IN (SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Hydro_Consumption_EJ NOT IN (SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn)"
#             ) 
#             result = mycur.fetchall()[0][0] 
#             new_conection7=entry+result
#             entry=int(input("after 2019 load_capacity(nuclyer)="))
#             mycur.execute(
#             "SELECT AVG(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Nuclear_Consumption_EJ NOT IN (SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Nuclear_Consumption_EJ NOT IN (SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn)"
#             )
#             result = mycur.fetchall()[0][0] 
#             new_conection10=entry+result
#             entry=int(input("after 2019 load_capacity(CO2)="))
#             mycur.execute(
#             "SELECT AVG(total_Coconj) FROM electricity_consptionsssssn WHERE total_Coconj NOT IN (SELECT MAX(total_Coconj) FROM electricity_consptionsssssn) AND total_Coconj NOT IN (SELECT MIN(total_Coconj) FROM electricity_consptionsssssn)"
#              )
#             result = mycur.fetchall()[0][0] 
#             new_conection13=entry+result
            values = [newload_avg1,newload_avg2,newload_avg3,newload_avg4,newload_avg5,newload_avg6]
            labels = ["Average(oil)", "Average(gas)", "Average(coal)","Average(Hydro)","Average(Nucelyer)","Average(CO2)"]
            fig = plt.figure(figsize=(10, 5))
            plt.bar(labels, values, color=['r','y','g'], width=0.4)
            plt.xlabel("Metric with new conection")
            plt.ylabel("Total Avrage of [oil,gas,coil,hydro,nuclyer,CO2] Consumption with new conection (EJ)")
            plt.title("[oil,gas,coil,hydro,nuclyer,CO2] Consumption Metrics with new conection")
            plt.show()
    elif num==8:
        break
   
else:
    print("No data found in the database.")



# # Query for the average oil consumption excluding max and min
# mycur.execute(
#     """
#     SELECT AVG(total_Oil_Consumption_EJ) 
#     FROM electricity_consptionsssssn 
#     WHERE total_Oil_Consumption_EJ NOT IN (
#         SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn
#     ) AND total_Oil_Consumption_EJ NOT IN (
#         SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn
#     )
#     """
# )
# result = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the minimum oil consumption
# mycur.execute("SELECT MIN(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
# result2 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the maximum oil consumption
# mycur.execute("SELECT MAX(total_Oil_Consumption_EJ) FROM electricity_consptionsssssn")
# result3 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the average gas consumption excluding max and min
# mycur.execute(
#     """
#     SELECT AVG(total_Gas_Consumption_EJ) 
#     FROM electricity_consptionsssssn 
#     WHERE total_Gas_Consumption_EJ NOT IN (
#         SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn
#     ) AND total_Gas_Consumption_EJ NOT IN (
#         SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn
#     )
#     """
# )
# result4 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the minimum gas consumption
# mycur.execute("SELECT MIN(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
# result5 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the maximum gas consumption
# mycur.execute("SELECT MAX(total_Gas_Consumption_EJ) FROM electricity_consptionsssssn")
# result6 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the average coal consumption excluding max and min
# mycur.execute(
#     """
#     SELECT AVG(total_Coal_Consumption_EJ) 
#     FROM electricity_consptionsssssn 
#     WHERE total_Coal_Consumption_EJ NOT IN (
#         SELECT MAX(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn
#     ) AND total_Coal_Consumption_EJ NOT IN (
#         SELECT MIN(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn
#     )
#     """
# )
# result7 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the minimum coal consumption
# mycur.execute("SELECT MIN(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn")
# result8 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the maximum coal consumption
# mycur.execute("SELECT MAX(total_Coal_Consumption_EJ) FROM electricity_consptionsssssn")
# result9 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the average hydro consumption excluding max and min
# mycur.execute(
#     """
#     SELECT AVG(total_Hydro_Consumption_EJ) 
#     FROM electricity_consptionsssssn 
#     WHERE total_Hydro_Consumption_EJ NOT IN (
#         SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn
#     ) AND total_Hydro_Consumption_EJ NOT IN (
#         SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn
#     )
#     """
# )
# result10 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the minimum hydro consumption
# mycur.execute("SELECT MIN(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
# result11 = mycur.fetchall()[0][0]  # Extract the numeric value

# # Query for the maximum hydro consumption
# mycur.execute("SELECT MAX(total_Hydro_Consumption_EJ) FROM electricity_consptionsssssn")
# result12 = mycur.fetchall()[0][0]  # Extract the numeric value



# mycur.execute(
# "SELECT AVG(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn WHERE total_Nuclear_Consumption_EJ NOT IN (SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn) AND total_Nuclear_Consumption_EJ NOT IN (SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn)"
# )


# result13 = mycur.fetchall()[0][0]  # Extract the numeric value
#             # Query for the minimum value
# mycur.execute("SELECT MIN(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
# result14 = mycur.fetchall()[0][0]  # Extract the numeric value

#           # Query for the maximum value
# mycur.execute("SELECT MAX(total_Nuclear_Consumption_EJ) FROM electricity_consptionsssssn")
# result15 = mycur.fetchall()[0][0]  # Extract the numeric value



# mycur.execute(
# "SELECT AVG(total_Coconj) FROM electricity_consptionsssssn WHERE total_Coconj NOT IN (SELECT MAX(total_Coconj) FROM electricity_consptionsssssn) AND total_Coconj NOT IN (SELECT MIN(total_Coconj) FROM electricity_consptionsssssn)"
# )


# result16 = mycur.fetchall()[0][0]  # Extract the numeric value
#        #     Query for the minimum value
# mycur.execute("SELECT MIN(total_Coconj) FROM electricity_consptionsssssn")
# result17 = mycur.fetchall()[0][0]  # Extract the numeric value

#         # Query for the maximum value
# mycur.execute("SELECT MAX(total_Coconj) FROM electricity_consptionsssssn")
# result18 = mycur.fetchall()[0][0]  # Extract the numeric value


# table= "electricity_consptionsssssn"  # Replace with the correct name:

# # Fetch all data at once
# mycur.execute(f"SELECT total_Oil_Consumption_EJ FROM {table}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)

#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx1=max(dt4)
# print("maximum=",mx1)
# mn1=min(dt4)
# print("minimum=",mn1)
# print(dt4)

# newload_avg1=sum(dt4)/len(dt4)
# print(newload_avg1)





# table_name = "electricity_consptionsssssn"  # Replace with the correct name

# # Fetch all data at once
# mycur.execute(f"SELECT total_Gas_Consumption_EJ FROM {table_name}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)

#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx2=max(dt4)
# print("maximum=",mx2)
# mn2=min(dt4)
# print("minimum=",mn2)
# print(dt4)

# newload_avg2=sum(dt4)/len(dt4)
# print(newload_avg2)

# table_name = "electricity_consptionsssssn"  # Replace with the correct name

# # Fetch all data at once
# mycur.execute(f"SELECT total_Coal_Consumption_EJ FROM {table_name}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)


#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx3=max(dt4)
# print("maximum=",mx3)
# mn3=min(dt4)
# print("minimum=",mn3)
# print(dt4)

# newload_avg3=sum(dt4)/len(dt4)
# print(newload_avg3)



# table_name = "electricity_consptionsssssn"  # Replace with the correct name

# # Fetch all data at once
# mycur.execute(f"SELECT total_Hydro_Consumption_EJ FROM {table_name}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)


#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx4=max(dt4)
# print("maximum=",mx4)
# mn4=min(dt4)
# print("minimum=",mn4)
# print(dt4)

# newload_avg4=sum(dt4)/len(dt4)
# print(newload_avg4)


# table_name = "electricity_consptionsssssn"  # Replace with the correct name

# # Fetch all data at once
# mycur.execute(f"SELECT total_Nuclear_Consumption_EJ FROM {table_name}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)


#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx5=max(dt4)
# print("maximum=",mx5)
# mn5=min(dt4)
# print("minimum=",mn5)
# print(dt4)

# newload_avg5=sum(dt4)/len(dt4)
# print(newload_avg5)


# table_name = "electricity_consptionsssssn"  # Replace with the correct name

# # Fetch all data at once
# mycur.execute(f"SELECT total_Coconj FROM {table_name}")
# results = mycur.fetchall()

# # Ensure sufficient data is available
# if len(results) < 10:
#     print("Not enough data in the table.")
# else:
#     # Extract the first 10 results
#     dt2 = [row[0] for row in results[:10]]

#     # Print the fetched results
#     print("dt2:", dt2)

#     # Calculate differences (dt3)
#     dt3 = [dt2[i + 1] - dt2[i] for i in range(len(dt2) - 1)]
    
#     # Print the differences
#     print("dt3:", dt3)


#     # Calculate the average of the differences
#     s = sum(dt3) / len(dt3)
#     print("Average difference (s):", s)
# dt4 = [dt2[i] + s for i in range(len(dt2) - 1)]
# print(dt4)
# mx6=max(dt4)
# print("maximum=",mx6)
# mn6=min(dt4)
# print("minimum=",mn6)
# print(dt4)

# newload_avg6=sum(dt4)/len(dt4)
# print(newload_avg6)


# # mycur.execute("create table elect_consuption(avrage_oil varchar(50),min_oil varchar(50),Max_oil varchar(50),avrage_oil_values float,min_oil_values float,max_oil_values float,avrage_gas_values float,min_gas_values float,max_gas_values float,avrage_coal_values float,min_coal_values float,max_coal_values float,avrage_hydro_values float,min_hydro_values float,max_hydro_values float,avrage_Nuc_values float,min_Nuc_values float,max_Nuc_values float,avrage_co2_values float,min_co2_values float,max_co2_values float,load_avrage_oil_values float,load_min_oil_values float,load_max_oil_values float,load_avrage_gas_values float,load_min_gas_values float,load_max_gas_values float,load_avrage_coal_values float,load_min_coal_values float,load_max_coal_values float,load_avrage_hydro_values float,load_min_hydro_values float,load_max_hydro_values float,load_avrage_Nuc_values float,load_min_Nuc_values float,load_max_Nuc_values float,load_avrage_co2_values float,load_min_co2_values float,load_max_co2_values float)")
# # mycur.execute("create table elect(avrage_oil varchar(50),min_oil varchar(50),Max_oil varchar(50),avrage_oil_values float,min_oil_values float,max_oil_values float,avrage_gas_values float,min_gas_values float,max_gas_values float,avrage_coal_values float,min_coal_values float,max_coal_values float,avrage_hydro_values float,min_hydro_values float,max_hydro_values float,avrage_Nuc_values float,min_Nuc_values float,max_Nuc_values float,avrage_co2_values float,min_co2_values float,max_co2_values float)")
# # Insert data into demo2 table
# sql = """
# INSERT INTO elect_consuption(avrage_oil, min_oil, Max_oil, avrage_oil_values, min_oil_values, max_oil_values,avrage_gas_values,min_gas_values,max_gas_values,avrage_coal_values ,min_coal_values,max_coal_values,avrage_hydro_values ,min_hydro_values,max_hydro_values ,avrage_Nuc_values,min_Nuc_values,max_Nuc_values,avrage_co2_values,min_co2_values,max_co2_values,load_avrage_oil_values ,load_min_oil_values ,load_max_oil_values ,load_avrage_gas_values ,load_min_gas_values ,load_max_gas_values ,load_avrage_coal_values ,load_min_coal_values ,load_max_coal_values ,load_avrage_hydro_values,load_min_hydro_values ,load_max_hydro_values ,load_avrage_Nuc_values,load_min_Nuc_values ,load_max_Nuc_values,load_avrage_co2_values,load_min_co2_values ,load_max_co2_values) 
# VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s)
# """
# dr = []
# d1, d2, d3 = "Avrage", "Min", "Max"
# dr.extend([d1, d2, d3, result, result2, result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16,result17,result18,newload_avg1,mn1,mx1,newload_avg2,mn1,mx1,newload_avg3,mn3,mx3,newload_avg4,mn4,mx4,newload_avg5,mn5,mx5,newload_avg6,mn6,mx6])

# # Correctly format data for executemany
# mycur.execute(sql, dr)

# # Commit changes to the database
# mydb.commit()

# # Print the number of inserted records
# print(mycur.rowcount, "records inserted.")

# # Retrieve and display data from the table
# mycur.execute("SELECT * FROM elect_consuption")
# result = mycur.fetchall()
# print("Data in the table:", result)







