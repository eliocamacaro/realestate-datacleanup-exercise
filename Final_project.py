# %% [markdown]
# # Real Estate Clean up
# 
# This is a real dataset and it was downloaded using web scraping techniques. The data contains registers from fotocasa which is one of the most popular websites of real estate in Spain. Please, do not do this (web scraping) unless it is for academic purposes.
# 
# The dataset was downloaded a few years ago by Henry Navarro and In no case were economic returns obtained from it.
# 
# It contains thousands of data from real houses published on the web www.fotocasa.com. Your goal is to extract as much information as possible with the knowledge you have so far about data science, for example what is the most expensive house in the entire dataset?
# 
# Let's start with precisely that question... Good luck!

# %% [markdown]
# #### Exercise 00. Read the dataset assets/real_estate.csv and try to visualize the table (★☆☆)

# %%
import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')
ds

# %% [markdown]
# #### Exercise 01. Which is the most expensive house in the dataset? (★☆☆)
# 
# Print the address and the price of the selected house. For example:
# 
# `The house with address General Street Nº5 is the most expensive and its price is 5000000 USD`

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Highest_Value = np.nanmax(ds.price) #Valor de la casa mas cara
Location1 = ds.loc[ds.price == Highest_Value].index[0] # Obtener el numero de fila
address1 = ds._get_value(Location1, 'address') #Nombre de la direccion
print("The house with address "+ str(address1)+ " is the most expensive and its price is "+ str(Highest_Value) + " EUR")

# %% [markdown]
# #### Exercise 02. Which is cheapest house in the dataset? (★☆☆)
# 
# Print the address and the price of the selected house. For example:
# 
# `The house with address Concrete Street Nº1 is the cheapest and its price is 12000 USD`

# %%
clean = np.array(ds.price) # Se convierte en un array la columna 'price'
clean2 = clean[np.nonzero(clean)] # Se eliminan los valores del array que son igual a 0
Lowest_Value = np.nanmin(clean2) # Una vez eliminados los 0, se obtiene el valor minimo
Location2 = ds.loc[ds.price == Lowest_Value].index[0] # Obtener el numero de fila
address2 = ds._get_value(Location2, 'address') #Nombre de la direccion
print("The house with address "+ str(address2)+ " is the cheapest and its price is "+ str(Lowest_Value) + " EUR")

# %% [markdown]
# #### Exercise 03. Which is the biggest and the smallest house in the dataset? (★☆☆)
# 
# Print both the address and the surface of the selected houses. For example:
# 
# `The bigger house is located on Yukka Street Nº10 and its surface is 5000 meters`
# 
# `The smaller house is located on County Road 1 N and its surface is 200 meters`

# %%
Highest_Surface = np.nanmax(ds.surface) #Superficie de la casa mas grande
Location31 = ds.loc[ds.surface == Highest_Surface].index[0]
address31 = ds._get_value(Location31, 'address')
print("The bigger house is located on "+ str(address31)+ " and its surface is "+ str(Highest_Surface) + " meters")

Lowest_Surface = np.nanmin(ds.surface) #Superficie de la casa mas pequeña
Location32 = ds.loc[ds.surface == Lowest_Surface].index[0]
address32 = ds._get_value(Location32, 'address')
print("The smaller house is located on "+ str(address32)+ " and its surface is "+ str(Lowest_Surface) + " meters")

# %% [markdown]
# #### Exercise 04. How many populations (level5 column) the dataset contains? (★☆☆)
# 
# Print the name of the populations with comma as separator. For example:
# 
# `> print(populations)`
# 
# `population1, population2, population3,...`

# %%
pop = pd.Series(ds.level5)
population = pd.Series.to_list(pop)
print(population)

# %% [markdown]
# #### Exercise 05. Does the dataset contain NAs? (★☆☆)
# 
# Print a boolean value (`true` or `fase`) followed by the rows/cols that contains NAs.

# %%
print("***DOES THE ROW/COLUMNS CONTAIS NAs?***")
print(ds.isnull()) #Aparecen todas las filas porque las columnas 'zipCode' y 'customZone' estan totalmente vacias

# %% [markdown]
# #### Exercise 06. Delete the NAs of the dataset, if applicable (★★☆)
# 
# Print a comparison between the dimensions of the original DataFrame versus the DataFrame after the deletions

# %%
No_nan_ds = ds.dropna(how= 'all',axis=1) #No hay ninguna fila donde todos sus valores sean NAs, por eso solo se borran las columnas
print( "The original file has " + str(ds.shape[0]) +" rows x "+ str(ds.shape[1]) + " columns")
print( "The no NAs file has " + str(No_nan_ds.shape[0]) +" rows x "+ str(No_nan_ds.shape[1]) + " columns")

# %% [markdown]
# #### Exercise 07. Which is the mean of prices in the population (level5 column) of "Arroyomolinos (Madrid)"? (★★☆)
# 
# Print the obtained value

# %%
Arroyomolinos = ds.loc[ds.level5 == "Arroyomolinos (Madrid)"]
prices_arroyomolinos= np.array(Arroyomolinos.price)
R_prices_arroyomolinos =prices_arroyomolinos[np.nonzero(prices_arroyomolinos)]
mean_prices = np.mean(R_prices_arroyomolinos)
print("The mean of prices in Arroyomolinos is " + str(round(mean_prices)) +" EUR")

# %% [markdown]
# #### Exercise 08. Plot the histogram of prices for the population (level5 column) of "Arroyomolinos (Madrid)" and explain what you observe (★★☆)
# 
# Print the histogram of the prices and write in the Markdown cell a brief analysis about the plot.

# %%
plt.title("Prices in Arroyomolinos")
plt.hist(R_prices_arroyomolinos, bins= 30, alpha= 0.7)
plt.figure( figsize=(10, 5))
plt.show()

# %% [markdown]
# La mayoria de las viviendas tienen un precio de entre los 20k-40k EUR, solo unas pocas superan los 40k, por lo que la media de precios en esta zona seria un poco inexacta (En mi opinion)

# %% [markdown]
# #### Exercise 09. Is the average of "Valdemorillo" and "Galapagar" prices the same? (★★☆)
# 
# Print the both average prices and then write a conclusion about them

# %%
Valdemorillo = ds.loc[ds.level5 == "Valdemorillo"]
Galapagar = ds.loc[ds.level5 == "Galapagar"]

prices_valdemorillo= np.array(Valdemorillo.price)
R_prices_valdemorillo =prices_valdemorillo[np.nonzero(prices_valdemorillo)]
mean_prices_v = np.mean(R_prices_valdemorillo)
print("The mean of prices in valdemorillo is " + str(round(mean_prices_v)) +" EUR")

prices_galapagar= np.array(Galapagar.price)
R_prices_galapagar =prices_galapagar[np.nonzero(prices_galapagar)]
mean_prices_g = np.mean(R_prices_galapagar)
print("The mean of prices in galapagar is " + str(round(mean_prices_g)) +" EUR")

if mean_prices_v == mean_prices_g :
    print("The average prices are the same")
else:
    print("The average prices are not the same")



# %% [markdown]
# #### Exercise 10. Is the average of "Valdemorillo" and "Galapagar" price per square meter (price/m2) the same? (★★☆)
# 
# Print the both average prices and then write a conclusion about
# 
# Hint: Create a new column called `pps` (price per square) and then analyse the values

# %%
houses_v = pd.Series(Valdemorillo.surface)
r_houses_v = houses_v.dropna(how= 'all')
total_m2_v =sum(r_houses_v)
total_pr_v = sum(R_prices_valdemorillo)
avg_v = total_pr_v / total_m2_v
print("The price/m2 in valdemorillo is " + str(round(avg_v)) +" EUR")

houses_g = pd.Series(Galapagar.surface)
r_houses_g = houses_g.dropna(how= 'all')
total_m2_g =sum(r_houses_g)
total_pr_g = sum(R_prices_galapagar)
avg_g = total_pr_g / total_m2_g
print("The price/m2 in galapagar is " + str(round(avg_g)) +" EUR")

if avg_v == avg_g :
    print("The average prices/m2 are the same")
else:
    print("The average prices/m2 are not the same")






# %% [markdown]
# #### Exercise 11. Analyse the relation between the surface and the price of the houses (★★☆)
# 
# Hint: You can make a `scatter plot` and then write a conclusion about it

# %%
plt.figure(figsize = (10, 5))

plt.scatter(ds.surface, ds.price, label = "House")

plt.title("Relation Surface/Price")
plt.legend()
plt.show()


# %% [markdown]
# **TODO: Markdown**. To write here, double click to this cell and just remove this content and place the text you want to write. Then, execute the cell.

# %%
"There are three houses that are bigger than usual and that doesn't allow us to see the real relation"

# %% [markdown]
# #### Exercise 12. How many real estate agencies the dataset contains? (★★☆)
# 
# Print the obtained value

# %%
re_agencies = ds.pivot_table(index = ['realEstate_name'], aggfunc ='size')
print(len(re_agencies))

# %% [markdown]
# #### Exercise 13. Which is the population (level5 column) that contains the most houses? (★★☆)
# 
# Print both the population and the number of houses

# %%
re_populations = ds.pivot_table(index = ['level5'], aggfunc ='size')
most_houses = np.sort(re_populations)[-1]
big_pop = re_populations.loc[re_populations == most_houses].index[0]
print("The population of " + str(big_pop) + " has the most houses, with " + str(most_houses) +" houses")




# %% [markdown]
# #### Exercise 14. Now let's work with the "south belt" of madrid. Make a subset of the original DataFrame that contains the following populations (level5 column): "Fuenlabrada","Leganés","Getafe","Alcorcón" (★★☆)
# 
# Hint: Filter the original DataFrame using the column `level5` and the function `isin`

# %%
ds_south_sb = ds.isin(["Fuenlabrada", "Leganés", "Getafe", "Alcorcón" ])
ds_south = ds.loc[ds_south_sb.level5 == True]
print(ds_south)

# %% [markdown]
# #### Exercise 15. Make a bar plot of the median of the prices and explain what you observe (you must use the subset obtained in the question 14) (★★★)
# 
# Print the bar of the median of the prices and write in the Markdown cell a brief analysis about the plot

# %%

ds_south
ds_south_array = np.array(ds_south.price)
ds_south_prices = ds_south_array[np.nonzero(ds_south_array)]

ds_Fuenlabrada = ds_south.loc[ds_south.level5 == "Fuenlabrada"]
prices_Fuenlabrada= np.array(ds_Fuenlabrada.price)
R_prices_Fuenlabrada =prices_Fuenlabrada[np.nonzero(prices_Fuenlabrada)]
mean_prices_fu = np.mean(R_prices_Fuenlabrada)


ds_Leganes = ds_south.loc[ds_south.level5 == "Leganés"]
prices_Leganes= np.array(ds_Leganes.price)
R_prices_Leganes =prices_Leganes[np.nonzero(prices_Leganes)]
mean_prices_le = np.mean(R_prices_Leganes)

ds_Getafe = ds_south.loc[ds_south.level5 == "Getafe"]
prices_Getafe= np.array(ds_Getafe.price)
R_prices_Getafe =prices_Getafe[np.nonzero(prices_Getafe)]
mean_prices_ge = np.mean(R_prices_Getafe)


ds_Alcorcon = ds_south.loc[ds_south.level5 == "Alcorcón"]
prices_Alcorcon= np.array(ds_Alcorcon.price)
R_prices_Alcorcon =prices_Alcorcon[np.nonzero(prices_Alcorcon)]
mean_prices_al = np.mean(R_prices_Alcorcon)

labels = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]
values = [mean_prices_fu, mean_prices_le, mean_prices_ge, mean_prices_al]

plt.figure(figsize = (10, 5))

plt.bar(labels, values)

plt.title("Median of prices in the south")
plt.show()



# %% [markdown]
# Getafe is the population with the most expensive houses in the south belt, while Fuenlabrada is the cheapest one. Leganés and Alcorcón have a similar mean of prices

# %% [markdown]
# #### Exercise 16. Calculate the sample mean and variance of the variables: price, rooms, surface area and bathrooms (you must use the subset obtained in the question 14) (★★★)
# 
# Print both values for each variable

# %%
ds_south
ds_south_array = np.array(ds_south.price)
ds_south_prices = ds_south_array[np.nonzero(ds_south_array)]
mean_price_south = np.mean(ds_south_prices)
var_prices_south = np.var(ds_south_prices)
print( "mean prices in the south are "+ str(round(mean_price_south))+ " and the variance is " + str(var_prices_south) )

ds_rooms_series = pd.Series(ds_south.rooms)
ds_south_rooms = ds_rooms_series.dropna(how= "all")
mean_rooms_south = np.mean(ds_south_rooms)
var_rooms_south = np.var(ds_south_rooms)
print( "mean rooms in the south are "+ str(round(mean_rooms_south))+ " and the variance is " + str(var_rooms_south) )

ds_surface_series = pd.Series(ds_south.surface)
ds_south_surface = ds_surface_series.dropna(how= "all")
mean_surface_south = np.mean(ds_south_surface)
var_surface_south = np.var(ds_south_surface)
print( "mean surface in the south are "+ str(round(mean_surface_south))+ " and the variance is " + str(var_surface_south) )

ds_bathrooms_series = pd.Series(ds_south.bathrooms)
ds_south_bathrooms = ds_bathrooms_series.dropna(how= "all")
mean_bathrooms_south = np.mean(ds_south_bathrooms)
var_bathrooms_south = np.var(ds_south_bathrooms)
print( "mean bathrooms in the south are "+ str(round(mean_bathrooms_south))+ " and the variance is " + str(var_bathrooms_south) )




# %% [markdown]
# #### Exercise 17. What is the most expensive house of each population? You must use the subset obtained in the question 14 (★★☆)
# 
# Print both the address and the price of the selected house of each population. You can print a DataFrame or a single line for each population

# %%
Highest_Value_fu = np.nanmax(ds_Fuenlabrada.price) 
Location_fu = ds_Fuenlabrada.loc[ds_Fuenlabrada.price == Highest_Value_fu].index[0]
address_fu = ds_south._get_value(Location_fu, 'address')
print("The house with address "+ str(address_fu)+ " is the most expensive in Fuenlabrada and its price is "+ str(Highest_Value_fu) + " EUR")

Highest_Value_le = np.nanmax(ds_Leganes.price)
Location_le = ds_Leganes.loc[ds_Leganes.price == Highest_Value_le].index[0]
address_le = ds_south._get_value(Location_le, 'address') 
print("The house with address "+ str(address_le)+ " is the most expensive in Leganés and its price is "+ str(Highest_Value_le) + " EUR")

Highest_Value_ge = np.nanmax(ds_Getafe.price) 
Location_ge = ds_Getafe.loc[ds_Getafe.price == Highest_Value_ge].index[0] 
address_ge = ds_south._get_value(Location_ge, 'address')
print("The house with address "+ str(address_ge)+ " is the most expensive in Getafe and its price is "+ str(Highest_Value_ge) + " EUR")

Highest_Value_al = np.nanmax(ds_Alcorcon.price) 
Location_al = ds_Alcorcon.loc[ds_Alcorcon.price == Highest_Value_al].index[0] 
address_al = ds_south._get_value(Location_al, 'address')
print("The house with address "+ str(address_al)+ " is the most expensive in Alcorcón and its price is "+ str(Highest_Value_al) + " EUR")

print("The exact addresses for the most expesive houses in Getafe and Alcorcón are not specified in the document")

# %% [markdown]
# #### Exercise 18. Normalize the variable of prices for each population and plot the 4 histograms in the same plot (you must use the subset obtained in the question 14) (★★★)
# 
# For the normalization method you can use the one you consider to, there is not a single correct answer to this question. Print the plot and write in the Markdown cell a brief analysis about the plot
# 
# Hint: You can help yourself reviewing the multihist demo of Matplotlib

# %%
#I will take the arrays I created in question 15 (Those arrays were created using the subset from question 14)
from sklearn import preprocessing #Lib para calcular la varianza de precios

nv_prices_fu = preprocessing.normalize([prices_Fuenlabrada])
nv_prices_le = preprocessing.normalize([prices_Leganes])
nv_prices_ge = preprocessing.normalize([prices_Getafe])
nv_prices_al = preprocessing.normalize([prices_Alcorcon])

hist_prices_fu = pd.DataFrame(nv_prices_fu)
hist_prices_le = pd.DataFrame(nv_prices_le)
hist_prices_ge = pd.DataFrame(nv_prices_ge)
hist_prices_al = pd.DataFrame(nv_prices_al)

fig, axis = plt.subplots(2, 2, figsize = (20, 20))

axis[0, 0].hist(hist_prices_fu, bins = 30, alpha = 0.7)
axis[0 ,0].set_title("Fuenlabrada")
axis[0, 1].hist(hist_prices_le, bins = 30, alpha= 0.7)
axis[0 ,1].set_title("Leganés")
axis[1, 0].hist(hist_prices_ge, bins = 15, alpha = 0.7)
axis[1, 0].set_title("Getafe")
axis[1, 1].hist(hist_prices_al, bins= 15, alpha= 0.7)
axis[1, 1].set_title("Alcorcón")


plt.show()

# %% [markdown]
# En Fuenlabrada y Leganes es donde hay mas varianza entre los precios, mientas que en Getafe y Alcorcón no varian demasiado (Especialmente en Getafe)

# %% [markdown]
# #### Exercise 19. What can you say about the price per square meter (price/m2) between the towns of "Getafe" and "Alcorcón"? You must use the subset obtained in the question 14 (★★☆)
# 
# Hint: Create a new column called `pps` (price per square) and then analyse the values

# %%
ds_Getafe = ds_south.loc[ds_south.level5 == "Getafe"]
houses_ge = pd.Series(ds_Getafe.surface)
r_houses_ge = houses_ge.dropna(how= 'all')
total_m2_ge =sum(r_houses_ge)
total_pr_ge = sum(R_prices_Getafe)
avg_ge = total_pr_ge / total_m2_ge
print("The price/m2 in Getafe is " + str(round(avg_ge)) +" EUR")

ds_Alcorcon = ds_south.loc[ds_south.level5 == "Alcorcón"]
houses_al = pd.Series(ds_Alcorcon.surface)
r_houses_al = houses_al.dropna(how= 'all')
total_m2_al =sum(r_houses_al)
total_pr_al = sum(R_prices_Alcorcon)
avg_al = total_pr_al / total_m2_al
print("The price/m2 in Alcorcón is " + str(round(avg_al)) +" EUR")

print("The prices are similar, but Getafe is a bit more expensive")

# %% [markdown]
# #### Exercise 20. Make the same plot for 4 different populations (level5 column) and rearrange them on the same graph? You must use the subset obtained in the question 14 (★★☆) 
# Hint: make a scatter plot of each population using subplots.

# %%
ds_Fuenlabrada = ds_south.loc[ds_south.level5 == "Fuenlabrada"]
ds_Leganes = ds_south.loc[ds_south.level5 == "Leganés"]
ds_Getafe = ds_south.loc[ds_south.level5 == "Getafe"]
ds_Alcorcon = ds_south.loc[ds_south.level5 == "Alcorcón"]

# Fuenlabrada
pop_fuenlabrada = len(ds_Fuenlabrada.level5)
x1 = [pop_fuenlabrada]
y1 = [pop_fuenlabrada]

#Leganés
pop_leganes = len(ds_Leganes.level5)
x2 = [pop_leganes]
y2 = [pop_leganes]

#Getafe
pop_getafe = len(ds_Getafe.level5)
x3 = [pop_getafe]
y3 = [pop_getafe]

#Alcorcón
pop_alcorcon = len(ds_Alcorcon.level5)
x4 = [pop_alcorcon]
y4 = [pop_alcorcon]

plt.scatter(x1, y1, c= "green", label= "Fuenlabrada")
plt.scatter(x2, y2, c= "blue", label= "Leganés")
plt.scatter(x3, y3, c= "red", label= "Getafe")
plt.scatter(x2, y4, c= "purple", label= "Alcorcón")


plt.legend() 
plt.show()

# %% [markdown]
# #### Exercise 21. Make a plot of the coordinates (latitude and longitude columns) of the south belt of Madrid by color of each population (you must use the subset obtained in the question 14) (★★★★)
# 
# Execute the following cell and then start coding in the next one. You must implement a simple code that transform the coordinates columns in a Python dictionary (add more information if needed) and then add it to the map

# %%
from ipyleaflet import Map, basemaps

# Map centred on (60 degrees latitude et -2.2 degrees longitude)
# Latitude, longitude
map = Map(center = (60, -2.2), zoom = 2, min_zoom = 1, max_zoom = 20, 
    basemap=basemaps.Esri.DeLorme)
map

# %%
dict_south_lat = {"fuenlabrada":[ds_Fuenlabrada.latitude], "leganes":[ds_Leganes.latitude], "getafe":[ds_Getafe.latitude], "alcorcon":[ds_Alcorcon.latitude]} 
dict_south_lon = {"fuenlabrada":[ds_Fuenlabrada.longitude], "leganes":[ds_Leganes.longitude], "getafe":[ds_Getafe.longitude], "alcorcon":[ds_Alcorcon.longitude]}

ds_lon = pd.DataFrame(dict_south_lon)
ds_lat = pd.DataFrame(dict_south_lat)

#No he sido capaz, he buscado y he visto ejemplos online, pero todos usan librerias a las que todavia no tenemos acceso, es lo mas que puedo hacer



