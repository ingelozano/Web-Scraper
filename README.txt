---------IMPORTANTE----------
TODO ESTO SE HACE CON FINES EDUCATIVOS Y ETICOS (NO ME HAGO RESPONSABLE DE SU MAL USO)
-
Para que puedas correr el codigo debes tener instalada las librerias "REQUESTS y BEAUTIFULSOUP4"
------------------------------------------------------------------------------------------------
************************************************************************************************
--------- INSTALAR LIBRERIAS--------

Para instalarlas sigue estos pasos:

1- abre el CMD en modo administrador

2- Coloca este comando: pip install requests y presiona enter (espera a que termine)

3- Coloca este otro comando para instalar la otra libreria: pip install beautifulsoup4 y presiona enter (espera a que termine)

4- coloca exit o simplemente cierra el CMD

------------------------------------------------------------------------------------------------------------------------------
******************************************************************************************************************************
---------¿QUÉ TIPO DE PAGINAS PUEDO HACERLE UN WEB SCRAPER?----------
Puedes aplicar un web scraper a una amplia variedad de páginas web, pero es importante tener en cuenta algunas consideraciones
éticas y legales al hacerlo. Aquí hay algunos ejemplos de tipos de páginas que podrías abordar con un web scraper:

1. **Sitios de noticias:** Extraer titulares, resúmenes o artículos de noticias de diversos sitios de noticias.

2. **Blogs y sitios de contenido:** Recopilar contenido de blogs y otros sitios web que compartan información interesante.

3. **Sitios de precios y comparación de productos:** Obtener información de precios, características y reseñas de productos en tiendas en línea.

4. **Redes sociales:** Analizar datos públicos de perfiles y publicaciones en plataformas como Twitter, Instagram o Facebook.

5. **Foros:** Recopilar información o comentarios de foros en línea sobre temas específicos.

6. **Sitios gubernamentales y de datos abiertos:** Extraer datos gubernamentales, como información del censo o datos meteorológicos.

7. **Sitios de clasificados:** Obtener información sobre artículos a la venta en sitios de clasificados en línea.

8. **Sitios de reseñas y calificaciones:** Analizar reseñas y calificaciones de productos, restaurantes, hoteles, etc.

Es importante destacar que, aunque muchas páginas web permiten el acceso y el web scraping de su contenido público, 
algunos sitios pueden tener restricciones, políticas de uso o incluso bloquear el acceso de web scrapers. Antes de hacer web scraping en un sitio web, 
siempre debes revisar sus términos de servicio y respetar las políticas establecidas por el sitio. Es recomendable verificar si el sitio ofrece una API 
o una fuente de datos específica para acceder a la información de forma más estructurada y legal.

Además, ten en cuenta que un web scraper ético debe respetar la privacidad de los usuarios y no intentar acceder a datos privados o protegidos sin permiso. 
El web scraping debe realizarse de manera responsable y consciente de las implicaciones legales y éticas que pueda tener.

************************************************************************************************************************************************************
---------¿POR QUÉ ESAS BIBLIOTECAS?--------
Las bibliotecas `requests` y `BeautifulSoup` son ampliamente utilizadas en Python para realizar web scraping debido 
a su facilidad de uso, flexibilidad y capacidad para manejar solicitudes HTTP y analizar HTML de manera eficiente. 
Aquí hay una breve explicación de cada una de ellas:

1. `requests`:
   - `requests` es una biblioteca de Python que facilita realizar solicitudes HTTP a través de Internet. 
      Es una biblioteca muy popular y fácil de usar para obtener el contenido de páginas web y trabajar con APIs REST.
   - Permite realizar solicitudes GET, POST, PUT, DELETE y otras operaciones HTTP de manera sencilla.
   - Proporciona una interfaz simple para trabajar con cabeceras, cookies y otros parámetros de solicitud.
   - Es muy útil para obtener el contenido HTML de una página web, lo cual es el primer paso necesario para el web scraping.

2. `BeautifulSoup`:
   - `BeautifulSoup` es una biblioteca de Python que se utiliza para analizar y extraer datos de documentos HTML y XML.
   - Facilita la navegación y búsqueda en la estructura del árbol DOM del HTML, lo que permite acceder y extraer fácilmente 
     los datos que se desean.
   - Proporciona métodos y selectores para encontrar elementos y atributos específicos en el código HTML.
   - Ayuda a manejar el HTML mal formateado y realizar el análisis de manera robusta.
   - Es ampliamente utilizado en web scraping porque simplifica enormemente el proceso de extracción de datos estructurados de páginas web.

En resumen, la combinación de `requests` y `BeautifulSoup` ofrece una forma poderosa y efectiva de realizar web 
scraping en Python. La biblioteca `requests` se encarga de obtener el contenido de la página web, mientras que 
`BeautifulSoup` se encarga de analizar y extraer los datos específicos que necesitas.
*****************************************************************************************************************************************