
## Configuración de Jupyter Notebook

### Localizacón de los ficheros de configuracion:

Jpyter usa **perfiles** para la cofiguraciñon, y estos perfiles
se almacenan en un directorio determinado por el siguinte
algoritmo:

 - El especificado en la línea de comamdo si se a usado la opcion `--config-dir`

 - Si no se especifica nada, se usará el valor retornado por 
   la función `IPython.paths.get_ipython_dir()`. Está función mira
   primero si está definida la variable de entorno `IPYTHONDIR`, usando
   en ese caso tal valor. Si no está definida la variable, usará el 
   valor predefinido `~/.ipython`. (El uso de la variable de entorno
   está desaconsejado porque se dejará de dar soporte en futuras 
   versiones)

Esto significa, en la práctica, que en la mayoría de los casos el
directorio  será `~/.ipython`

Una vez que tenemos claro el directorio ¿Qué perfíl estamos usando? En el caso
de que no hayamos creado ningún perfíl, habrá uno con el nombre `default`, y de
nuevo, el ma mayoría de los casos, la ruta será `~/.ipython/profile_default`.

¿En qué consiste este profile? La idea básica es que cada aplicación mantiene
su propio fichero de configuración. En el caso del propio iPython, el fichero
es `ipython_config.py`. El kernel de python usa su propio ficheo llamado
`ipython_kernel_config.py`. Este último fichero se ejecutará
cada vez que se cargue el kernel.

Para crear este fichero podemos usar la orden:

    ipython profile create

que nos creara los dos ficheros mencionados

## Definiendo comandos custom propios

Hay dos maneras de definir nuestras propias funciones mágicas, usando
funciones simples o escribiendo una clase propia que derive de una
especial definida en IPython: `IPython.core.magic.Magics`. Podemos
usar el fichero de configuración del kernel que vimos
en el apartado anterior para cargar estas funciones o clases
en el arranque.

### Usando solo funciones

Esta sería la forma más sencilla. El siguiente código implementa una serie
de ordenes mágicas muy sencilla, una que solo funciona en modo línea, una que
solo funciona en modo celda, y una que es capaz de funcionar en ambos 
modos:

    from IPython.core.magic import (
        register_line_magic,
        register_cell_magic,
        register_line_cell_magic
        )

    @register_line_magic
    def lmagic(line):
        "my line magic"
        return line

    @register_cell_magic
    def cmagic(line, cell):
        "my cell magic"
        return line, cell

    @register_line_cell_magic
    def lcmagic(line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            return line
        else:
            print("Called as cell magic")
            return line, cell

    # We delete these to avoid name conflicts for automagic to work
    del lmagic, lcmagic

Para que el kernel de Python carge este código, solo tenemos que salvarlo en la
carpeta `startup` deltro del perfil. Todos los scripts con extensiones `.py`
o `.ipy` que se encuentren en
esta carpeta son cargados cuando se arranca el kernel y antes de ejecutar
cualquier fichero especificado mediente las opciones `exec_lines` o exec_files.

Los ficheros se ejecutan ordenados por nombre, de forma que podemos controlar
el orden de ejecucion usando, por ejemplo, prefijos:

    - 00-primero.py
    - 50-intermedio.py
    - 99-ultimo.py

