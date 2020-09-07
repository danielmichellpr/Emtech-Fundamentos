import lifestore_file as lf 					# Importamos los datos
import getpass, os 								# Para poner una contraseña y limpiar la pantalla

#Buscamos mayores ventas, creamos una lista vacía donde se guarden las mayores ventas 
#lifestore_searches = [id_search, id product]
#lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
#lifestore_products = [id_product, name, price, category, stock (en existencia)]

input('Escribe tu nombre de usuario: ')							#Ingresa el LOGIN
password = getpass.getpass('Contraseña: *********** ')
os.system ("cls")

#Mensaje de bienvenida
print('''Bienvenido a la base de datos de LifeStore, debido a un análisis de los productos hemos tenido que hacer un ajuste en nuestra configuración. \n
		A continuación se desplegarán 3 apartados:\n
		Primero se muestran los productos más vendidos y los productos rezagados, esto a través de un listado con las mayores ventas y mayores busquedas:
		Tambien se muestra por categoría
		Segundo se muestran los productos por reseña, los productos con mejores reseñas y con peores.
		Finalmente se muestran los ingresos totales y las ventas promedio mensual.
		¿Estás listo? 
		''')



input('Se mostrará a continuación el primer punto, los productos más vendidos y más buscados, presiona Enter:')

os.system ("cls")

							###########################################################################

greater_sales = []											#Lista vacía que almacenará las mayores ventas 
for i in range(1,len(lf.lifestore_products)+1): 			#Lo buscamos por su tamaño por qué nos devolverá el número de listas, más no los elementos de cada lista, se empieza en 1, por qué no tenemos índice 0
	contador_greater_sales = 0								#Un contador que añadiremos a nuestra lista
	for j in lf.lifestore_sales:							#Iteramos sobre la lista de ventas
		if i == j[1]:										#Si el producto en la lista de ventas es igual al producto en la lista de productos agregamos 1 al contador
			contador_greater_sales +=1
	greater_sales.append([i,contador_greater_sales])		#Gurdamos el producto y el contador


  							###########################################################################

#Realizamos lo mismo con las busquedas

greater_searches = []
for i in range(1,len(lf.lifestore_products)+1): 
	contador_greater_searches = 0		
	for j in lf.lifestore_searches:
		if i == j[1]:
			contador_greater_searches +=1
	greater_searches.append([i,contador_greater_searches])

#print(greater_sales) #Este es más de apoyo para mi para visualizar lo realizado
#print(greater_searches)

							###########################################################################


#Ahora vamos a acomodar en orden descendente las listas obtenidas, realizamos una pequeña función para hacerlo, sólo para acomodar el sort
def Sort_Sales(element):
	return element[1]

greater_sales.sort(key = Sort_Sales, reverse =True)			#La lista se acomoda en orden descendente
#print(greater_sales)
worst_sales = greater_sales.copy()							#Realizamos una copia para las peores ventas
worst_sales.sort(key = Sort_Sales)							#Acomodamos en orden ascendente

 							###########################################################################

 #Realizamos lo mismo con las busquedas				
def Sort_Searches(element):
	return element[1]
greater_searches.sort(key = Sort_Searches, reverse =True)
#print(greater_searches)
worst_searches = greater_searches.copy()
worst_searches.sort(key = Sort_Searches)
				

						##############################################################################

#Imprimimos los resultados obtenidos
#Vamos a cambiar esto: Mostramos los primeros 10 más vendidos, ya que se pierde detalle al mostrar tantos

input('Los 10 productos más vendidos son:  (presiona Enter) \n')
print('***************** LOS MÁS VENDIDOS *****************************\n \n')

for i in range(len(greater_sales[0:10])):								#Mostramos los 10 primeros
    print(lf.lifestore_products[greater_sales[i][0]][1] ,'\n')			#Para eso mandamos a llamar a la lista de productos 



### Realizamos lo mismo para los menos vendidos
input('Los menos vendidos son: (presiona Enter)  \n')
print('***************** LOS MENOS VENDIDOS ***************************** \n \n')
#print('Los menos vendidos son:')
for i in range(len(greater_sales[0:10])):
    print(lf.lifestore_products[worst_sales[i][0]][1] ,'\n')

						##############################################################################


input('Los más buscados son: (presiona Enter)  \n')
print('***************** LOS MÁS BUSCADOS *****************************\n \n')
for i in range(len(worst_searches[0:10])):
    print(lf.lifestore_products[greater_searches[i][0]][1] ,'\n')

input('Los menos buscados son: (presiona Enter)  \n')
print('***************** LOS MENOS BUSCADOS *****************************\n \n')
for i in range(len(worst_searches[0:10])):
    print(lf.lifestore_products[worst_searches[i][0]][1] ,'\n')

						##############################################################################




#Dado que no siempre nuestra base de datos será tan pequeña, es conveniente resivar cuantos tipos de categorías hay en lifestore_file
#Y con eso hacer una lista con los valores no repetidos de las categorías.
#Vamos a realizar una lista con todas las categorias y una más con las categorías sin repetición
category = []
category_unique = []

for i in range(1, len(lf.lifestore_products)):				#Hacemos un for sobre el tamaño d los productos para revisar a que categoría pertenece
	#print(lf.lifestore_products[i][3])
	category.append(lf.lifestore_products[i][3])			#Agregamos las categorías

for i in category:											#Nos quedamos con las categorías únicas
	if i not in category_unique:
		category_unique.append(i)

#print(category_unique)


						##############################################################################

#Identificamos los elementos que se encuentran en la misma categoria
category_same = []										#Creamos una lista donde guardaremos los elementos que se encuentran en la misma categoría
for i in range(len(category_unique)): 					#Recorremos las categorías únicas
	lista_category_same = []	 						#En vez de ir enumerando como anteriormente lo haciamos, vamos ir creando listas de listas 
	for j in lf.lifestore_products:						#Recorremos los productos
		if category_unique[i] == j[3]:					#Si nuestra categoría concuerda con el categoría del producto guardamos
			lista_category_same.append(j[0])
	category_same.append(lista_category_same)			#La guardamos en la lista category_same
#print(category_same)

						##############################################################################


#Vamos a ver cuantos ventas tuvo cada categoria

category_sales=[] 										#Vamos a ver cuantas ventas tuvo cada categoría				
for i in category_same : 								#Recorremos la lista anteriormente creada
    lista_category_sales =[] 							#Nuevamente crearemos una lista de listas
    for j in range(len(i)): 							#De igual forma se crea una lista vacia para cada ciclo
        for k in greater_sales:							#Recorremos la lista de las ventas
            if i[j]==k[0]:								#Si los indices concuerdan se guarda en ventas por categoría
                lista_category_sales.append(k)
    category_sales.append(lista_category_sales)  		#La guardamos en la lista category_sales


						##############################################################################


    
category_searches=[] 									#se hace la misma operacion para la seccion de busquedas 
for i in category_same: 
    lista_category_searches =[]
    for j in range(len(i)): 
        for k in greater_searches:
            if i[j]==k[0]:
                lista_category_searches.append(k)
    category_searches.append(lista_category_searches) 


						##############################################################################


input('Se mostrará a continuación los productos más vendidos por categoría, sus ventas y cuantas busquedas se realizaron, presiona Enter: \n')

os.system ("cls")


input('Listo para ver las ventas y busquedas por categoría? (Presiona Enter): \n')


						##############################################################################

#Hacemos una lista para cada categoría, mostraremos los productos más vendidos y menos vendidos por caterogoría 
procesadores_sales = category_sales[0]
#print(procesadores_sales)
tarjetas_de_video_sales  = category_sales[1]
tarjetas_madre_sales  = category_sales[2]
discos_duros_sales = category_sales[3]
memorias_usb_sales = category_sales[4]
pantallas_sales  = category_sales[5]
bocinas_sales = category_sales[6]
audifonos_sales = category_sales[7]

procesadores_searches = category_searches[0]
tarjetas_de_video_searches  = category_searches[1]
tarjetas_madre_searches  = category_searches[2]
discos_duros_searches = category_searches[3]
memorias_usb_searches = category_searches[4]
pantallas_searches  = category_searches[5]
bocinas_searches = category_searches[6]
audifonos_searches = category_searches[7]


						##############################################################################
#Realizamos una función sort, en la cual se acomoda de forma descentente cada categoría, además se crean copias
#para aplicarlas posteriormente en las peores ventas o busquedas

def Sort(element):
	return element[1]

procesadores_sales.sort(key = Sort, reverse =True)
procesadores_searches.sort(key = Sort, reverse =True)
procesadores_sales_worst = procesadores_sales.copy()
procesadores_sales_worst.sort(key = Sort)
procesadores_searches_worst = procesadores_searches.copy()
procesadores_searches_worst.sort(key = Sort)

tarjetas_de_video_sales.sort(key = Sort, reverse =True)
tarjetas_de_video_searches.sort(key = Sort, reverse =True)
tarjetas_de_video_sales_worst = tarjetas_de_video_sales.copy()
tarjetas_de_video_sales_worst.sort(key = Sort)
tarjetas_de_video_searches_worst = tarjetas_de_video_searches.copy()
tarjetas_de_video_searches_worst.sort(key = Sort)


tarjetas_madre_sales.sort(key = Sort, reverse =True)
tarjetas_madre_searches.sort(key = Sort, reverse =True)
tarjetas_madre_sales_worst = tarjetas_madre_sales.copy()
tarjetas_madre_sales_worst.sort(key = Sort)
tarjetas_madre_searches_worst = tarjetas_madre_searches.copy()
tarjetas_madre_searches_worst.sort(key = Sort)

discos_duros_sales.sort(key = Sort, reverse =True)
discos_duros_searches.sort(key = Sort, reverse =True)
discos_duros_sales_worst = discos_duros_sales.copy()
discos_duros_sales_worst.sort(key = Sort)
discos_duros_searches_worst = discos_duros_searches.copy()
discos_duros_searches_worst.sort(key = Sort)

memorias_usb_sales.sort(key = Sort, reverse =True)
memorias_usb_searches.sort(key = Sort, reverse =True)
memorias_usb_sales_worst = memorias_usb_sales.copy()
memorias_usb_sales_worst.sort(key = Sort)
memorias_usb_searches_worst = memorias_usb_searches.copy()
memorias_usb_searches_worst.sort(key = Sort)

pantallas_sales.sort(key = Sort, reverse =True)
pantallas_searches.sort(key = Sort, reverse =True)
pantallas_sales_worst = pantallas_sales.copy()
pantallas_sales_worst.sort(key = Sort)
pantallas_searches_worst = pantallas_searches.copy()
pantallas_searches_worst.sort(key = Sort)

bocinas_sales.sort(key = Sort, reverse =True)
bocinas_searches.sort(key = Sort, reverse =True)
bocinas_sales_worst = bocinas_sales.copy()
bocinas_sales_worst.sort(key = Sort)
bocinas_searches_worst = bocinas_searches.copy()
bocinas_searches_worst.sort(key = Sort)

audifonos_sales.sort(key = Sort, reverse =True)
audifonos_searches.sort(key = Sort, reverse =True)
audifonos_sales_worst = audifonos_sales.copy()
audifonos_sales_worst.sort(key = Sort)
audifonos_searches_worst = audifonos_searches.copy()
audifonos_searches_worst.sort(key = Sort)


						##############################################################################


#print(procesadores)
print('Procesadores, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en procesadores fueron: \n')
for i in range(len(procesadores_sales[0:2])):
	print('El producto ', lf.lifestore_products[procesadores_sales[i][0]-1][1],'tuvo',procesadores_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en procesadores fueron: \n')
for i in range(len(procesadores_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[procesadores_sales_worst[i][0]-1][1],'tuvo',procesadores_sales_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************ \n')

print('Tarjetas de vídeo, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en tarjetas de vídeo fueron: \n')
for i in range(len(tarjetas_de_video_sales[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_de_video_sales[i][0]-1][1],'tuvo',tarjetas_de_video_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en tarjetas de vídeo fueron: \n')
for i in range(len(tarjetas_de_video_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_de_video_sales_worst[i][0]-1][1],'tuvo',tarjetas_de_video_sales_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************ \n')

print('Tarjetas madre, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en tarjetas madre fueron: \n')
for i in range(len(tarjetas_madre_sales[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_madre_sales[i][0]-1][1],'tuvo',tarjetas_madre_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en tarjetas madre fueron: \n')
for i in range(len(tarjetas_madre_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_madre_sales_worst[i][0]-1][1],'tuvo',tarjetas_madre_sales_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************ \n')

print('Discos duros, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en discos duros fueron: \n')
for i in range(len(discos_duros_sales[0:2])):
	print('El producto ', lf.lifestore_products[discos_duros_sales[i][0]-1][1],'tuvo',discos_duros_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en discos duros fueron: \n')
for i in range(len(discos_duros_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[discos_duros_sales_worst[i][0]-1][1],'tuvo',discos_duros_sales_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************ \n')

print('Memorias USB, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en Memorias USB fueron: \n')
for i in range(len(memorias_usb_sales[0:2])):
	print('El producto ', lf.lifestore_products[memorias_usb_sales[i][0]-1][1],'tuvo',memorias_usb_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en Memorias USB fueron: \n')
for i in range(len(memorias_usb_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[memorias_usb_sales_worst[i][0]-1][1],'tuvo',memorias_usb_sales_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************\n')


print('Pantallas, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en Pantallas fueron: \n')
for i in range(len(pantallas_sales[0:2])):
	print('El producto ', lf.lifestore_products[pantallas_sales[i][0]-1][1],'tuvo',pantallas_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en Pantallas fueron: \n')
for i in range(len(pantallas_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[pantallas_sales_worst[i][0]-1][1],'tuvo',pantallas_sales_worst[i][1],'ventas \n')


input('******************** Presiona Enter para continuar ************************ \n')


print('Bocinas, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en bocinas fueron: \n')
for i in range(len(bocinas_sales[0:2])):
	print('El producto ', lf.lifestore_products[bocinas_sales[i][0]-1][1],'tuvo',bocinas_sales[i][1],'ventas \n')
print('Las peores ventas por categoria en Pantallas fueron: \n')
for i in range(len(bocinas_sales_worst[0:2])):
	print('El producto ', lf.lifestore_products[bocinas_sales_worst[i][0]-1][1],'tuvo',bocinas_sales_worst[i][1],'ventas \n')





#######################################################################################################################


input('Se mostrará a continuación los productos más buscados por categoría, presiona Enter: \n')

os.system ("cls")

input('Presiona Enter para contunuar y ver las busquedas por categoría: \n')


print('Procesadores, se muestran los 2 más buscados y los 2 menos buscados \n')
print('Los más buscados por categoria en procesadores fueron: \n')
for i in range(len(procesadores_searches[0:2])):
	print('El producto ', lf.lifestore_products[procesadores_searches[i][0]-1][1],'tuvo',procesadores_searches[i][1],'busquedas \n')
print('Los menos buscados por categoria en procesadores fueron: \n')
for i in range(len(procesadores_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[procesadores_sales_worst[i][0]-1][1],'tuvo',procesadores_searches_worst[i][1],'busquedas \n')

input('******************** Presiona Enter para continuar ************************ \n')

print('Tarjetas de vídeo, se muestran los 2 más buscados y los 2 menos buscados \n')
print('Los más buscados por categoria en tarjetas de vídeo fueron: \n')
for i in range(len(tarjetas_de_video_searches[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_de_video_searches[i][0]-1][1],'tuvo',tarjetas_de_video_searches[i][1],'busquedas \n')
print('Los menos buscados por categoria en tarjetas de vídeo fueron: \n')
for i in range(len(tarjetas_de_video_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_de_video_searches_worst[i][0]-1][1],'tuvo',tarjetas_de_video_searches_worst[i][1],'busquedas \n')

input('******************** Presiona Enter para continuar ************************ \n')


print('Tarjetas madre, se muestran los 2 más buscados y los 2 menos buscados \n')
print('Los más buscados por categoria en tarjetas madre fueron: \n')
for i in range(len(tarjetas_madre_searches[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_madre_searches[i][0]-1][1],'tuvo',tarjetas_madre_searches[i][1],'busquedas \n')
print('Los menos buscados por categoria en tarjetas madre fueron: \n')
for i in range(len(tarjetas_madre_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[tarjetas_madre_searches_worst[i][0]-1][1],'tuvo',tarjetas_madre_searches_worst[i][1],'busquedas \n')


input('******************** Presiona Enter para continuar ************************ \n')


print('Discos duros, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en discos duros fueron: \n')
for i in range(len(discos_duros_searches[0:2])):
	print('El producto ', lf.lifestore_products[discos_duros_searches[i][0]-1][1],'tuvo',discos_duros_searches[i][1],'ventas \n')
print('Las peores ventas por categoria en discos duros fueron: \n')
for i in range(len(discos_duros_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[discos_duros_searches_worst[i][0]-1][1],'tuvo',discos_duros_searches_worst[i][1],'ventas \n')



input('******************** Presiona Enter para continuar ************************ \n')


print('Memorias USB, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en Memorias USB fueron: \n')
for i in range(len(memorias_usb_searches[0:2])):
	print('El producto ', lf.lifestore_products[memorias_usb_searches[i][0]-1][1],'tuvo',memorias_usb_searches[i][1],'ventas \n')
print('Las peores ventas por categoria en Memorias USB fueron: \n')
for i in range(len(memorias_usb_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[memorias_usb_searches_worst[i][0]-1][1],'tuvo',memorias_usb_searches_worst[i][1],'ventas \n')



input('******************** Presiona Enter para continuar ************************ \n')


print('Pantallas, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en pantallas fueron: \n')
for i in range(len(pantallas_searches[0:2])):
	print('El producto ', lf.lifestore_products[pantallas_searches[i][0]-1][1],'tuvo',pantallas_searches[i][1],'ventas \n')
print('Las peores ventas por categoria en pantallas fueron: \n')
for i in range(len(pantallas_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[pantallas_searches_worst[i][0]-1][1],'tuvo',pantallas_searches_worst[i][1],'ventas \n')



input('******************** Presiona Enter para continuar ************************ \n')


print('Bocinas, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en bocinas fueron: \n')
for i in range(len(bocinas_searches[0:2])):
	print('El producto ', lf.lifestore_products[bocinas_searches[i][0]-1][1],'tuvo',bocinas_searches[i][1],'ventas \n')
print('Las peores ventas por categoria en bocinas fueron: \n')
for i in range(len(bocinas_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[bocinas_searches_worst[i][0]-1][1],'tuvo',bocinas_searches_worst[i][1],'ventas \n')



input('******************** Presiona Enter para continuar ************************ \n')


print('Audifonos, se muestran los 2 más vendidos y los 2 menos vendidos \n')
print('Las mejores ventas por categoria en audifonos fueron: \n')
for i in range(len(audifonos_searches[0:2])):
	print('El producto ', lf.lifestore_products[audifonos_searches[i][0]-1][1],'tuvo',audifonos_searches[i][1],'ventas \n')
print('Las peores ventas por categoria en audifonos fueron: \n')
for i in range(len(audifonos_searches_worst[0:2])):
	print('El producto ', lf.lifestore_products[audifonos_searches_worst[i][0]-1][1],'tuvo',audifonos_searches_worst[i][1],'ventas \n')

input('******************** Presiona Enter para continuar ************************ \n')
	

input('Se mostrará a continuación los productos por reseña, las mejores reseñas y las peores, presiona Enter: \n')

os.system ("cls")

input('Presiona Enter para contunuar y ver las mejores y peores reseñas: \n')
######################################################################################################################

#Realizamos una lista vacía donde se almacenarán las resenhas

review = []
for i in range(1, len(lf.lifestore_products)+1):		#De manera similar a lo realizado anteriormente se realiza con ciclo for
	review_score = []									#Lista para la puntuacíón de la resenha
	review_refund = []									#Lista para si fue devuelta o no
	for j in lf.lifestore_sales:						#Iteramos sobre las ventas 
		if i==j[1]:										#Si cumplen la igualdad
			review_score.append(j[2]) 				#Esta variable guarda las reseñas para cada producto
			review_refund.append(j[4]) 				#Gurdar si el producto fue regresado o no.
												#Si el producto no fue comprado, entonces no puede ser regresado

	#print(review_score)
	#print(reviw_refund)
	review.append([i, review_score,review_refund])


#Vamos a retirar los espacios vacíos, hay listas que no continen nada

flag =True 							#Damos un banderazo de salida verdadero
while flag:							#Mientras sea verdadero
    flag=False 						#Cambiamos la bandera a falso 
    for i in review:				#Iteramos sobre las resenhas
        if not i[1]: 				#Verificamos si la lista se encuentra vacía
            flag=True
            #print(i)
            review.remove(i)		#Removemos las listas vacías
#print(review)

#Vamos a calcular el promedio de cada reseña, para saber cual fue mejor y luego acomdarlo
for i in review:
    if len(i[1])!=0: 					
        i[1]=sum(i[1])/len(i[1])		#Función que promedia
    else:
        i[1]=0

#print(review)
def SortReview(element):
	return element[1]
review.sort(key = SortReview, reverse =True)		#Ordenamos del mejor al peor sacando el promedio de las resenhas
#print(review)


#Decidimos cuales son las mejores y peores resenhas, esto lo decidimos manualmente, si pasa de 4.6 es una buena resenha
#Guardamos en listas estos datos
best_review= []
worst_review = []
for i in review: 				 		#Iteramos sobre las reseñas 
    if i[1]>4.6: 						
        best_review.append(i)
    else:
        worst_review.append(i)



#Realizamos la impresión de las mejores y peores 

input('La mejor reseña: (presiona Enter)  \n')
print('***************** LA MEJOR RESEÑA ***************************** \n \n')
for i in range(len(best_review[0:10])):
    print(lf.lifestore_products[best_review[i][0]][1] ,'\n')

input('La peor reseña: (presiona Enter)  \n')
print('***************** LA PEOR RESEÑA  *****************************\n \n')
for i in range(len(worst_review[0:10])):
    print(lf.lifestore_products[worst_review[i][0]][1] ,'\n')

#print(best_review)
#print(worst_review)






#Realizamos una lista donde se almacenan los meses del anhos con string, igual con números 
#Dejamos dos espacios en ceros, donde se almancenará el número de ventas por mes y los ingresos percibidos
Meses = [['Enero',1,0,0],['Febrero',2,0,0],['Marzo',3,0,0], ['Abril',4,0,0],['Mayo',5,0,0],['Junio',6,0,0],
                ['Julio',7,0,0],['Agosto',8,0,0],['Septiembre',9,0,0], ['Octubre',10,0,0],['Noviembre',11,0,0],['Diciembre',12,0,0]]

for i in lf.lifestore_sales:						 			#Iteramos sobre las lista de ventas
    mes_indice = int(i[3][3:5])-1 								#Se obtiene el índice del mes
    producto_indice = i[1]-1 									#Se obtiene el índice del producto
    if i[4] == 0: 												#Si el producto fue regresado, no se almacena la venta 
        													
        price = lf.lifestore_products[producto_indice][2]	 	#Hacemos la variable precio la cual almacena los el precio, recogido de la lista de productos
        Meses[mes_indice][2] += 1 								#Si eso se cumple aumentamos una venta
        Meses[mes_indice][3] += price 							#Aumentamos el ingreso 



#Realizamos copias de la lista Meses
sales_months = Meses.copy()
takings_months = Meses.copy()


#Realizamos funciones sort, una donde se acomoda por número de ventas y otra por cantidad obtenida en el mes 
def Sales_months(element):
	return element[2]

def Takings_months(element):
	return element[3]


sales_months.sort(key=Sales_months, reverse = True)
takings_months.sort(key = Takings_months, reverse = True)
#print(sales_months)
#print(takings_months)
input('Finalmente se muestra los datos por meses : (presiona Enter)  \n')


print('***************** LAS VENTAS POR MESES Y LOS MESES CON MÁS VENTAS FUERON:  *****************************\n \n')


for i in range(0,len(sales_months)):
	print('En el mes de ', sales_months[i][0], ' hubo ', sales_months[i][2], ' ventas. \n')



print('***************** LOS INGRESOS POR MESES  Y LOS MESES CON MÁS INGRESOS FUERON:  *****************************\n \n')
for i in range(0,len(takings_months)):
	print('En el mes de ', takings_months[i][0], ' hubo ', takings_months[i][3], ' ingresos. \n')

print('***************** El total de ingresos totales es:  *****************************\n \n')

ingreso_total = 0

for i in takings_months:
    ingreso_total += i[3] #Aumentamos el numero de ingresos por mes para obtener el total
print('El total de ingresos ha sido:', ingreso_total) #Imprimos el ingreso total del año
