
import streamlit as st
st.markdown(
    """
    # Clasificacionde de flores utilizando .tfrec en TPU
    Una comptencia donde debemos hacer el tipico ejemplo de clasificacion de flores pero en este caso sera usando TPU en lugar de GPU o CPU y solo e clasificaran 100 flores, naturalmente mas seria mas complicado.

    ## Herramientas a utilizar
    - DataLore
    - TensorFlow

    ## Carga de imagenes
    ### Carga de la ubicacion de la imagen
    Para cargar las imagenes primero necesitaremos la direccionde ubicacion de las imagenes, donde cargamos 3 carpetas que corresponden a los datos de: entrenamiento, validacion y prueba.
    ```
    GLOBAL_PATH = os.path.basename("KaggleDataset")

    # array para acceder a los path y sus valoers de forma ordenada

    ForDataset = [GLOBAL_PATH+"/tfrecords-jpeg-192x192", GLOBAL_PATH+"/tfrecords-jpeg-224x224", GLOBAL_PATH+"/tfrecords-jpeg-331x331", GLOBAL_PATH+"/tfrecords-jpeg-512x512"]

    TEST_FIELS = tf.io.gfile.glob(ForDataset[0]+"/test/*.tfrec")

    TRAIN_FIELS = tf.io.gfile.glob(ForDataset[0]+"/train/*.tfrec")

    VALIDATION_FIELS = tf.io.gfile.glob(ForDataset[0]+"/val/*.tfrec")

    print(len(TRAIN_FIELS))
    ```

    A diferencia de otros ejemplos nosotros usamos un array para guarda las variables de modo que solo cambiemos el indice y pasemos al siguien tamaño de entrenamiento.

    ### Decodificacion de la imagen
    #### Funciones
    ##### decodificacion
    Primero decodificaremos la imagen para trabajar con los datos y como son imagenes le especificaremos que el canal ah usar sera el 3 ya que es el canal que maneja datos RGB.
    ```
    def decode_imagen(imagen):
        imagen = tf.image.decode_jpeg(imagen, channels=3)
    ```

    A continuacion tomaremos los datos y nos a seguraremos de que los datos sean trabajado en formato float, el lo normal es un ==tf.float32== pero dependiendo de los datos que manejos puede cambiar a ==tf.float64==.
    ```
        imagen = tf.cast(imagen, tf.float32)
    ```

    ahora acomodaremos las imagen para que sean del mismo tamaño
    ```
        imagen = tf.reshape(imagen, [*Image_size, 3])
        return imagen
    ```

    ##### Funcion de union de datos 
    Los modelos por lo general utilizan (x,y) para evaluar y entrenar, acontinucacion lo que se hara es unir los datos a evaluar con las imagen ==.tfrec== objetivo.
    ```
    def read_tfrec(example, labeled):
        tfrecord_format = (
            {
            'imagen': tf.io.FixedLenFeature([], tf.string),
            'clase': tf.io.FixedLenFeature([], tf.int64)
            } if labeled else {'imagen': tf.io.FixedLenFeature([], tf.string)}
        )
    ```

    Luego tomarmemos la precaucion de evitar datos sin pareja
    ```
        example = tf.io.parse_single_example(example, tfrecord_format)
        imagen = decode_imagen(example['imagen'])
        if labeled:
            label = tf.cast(example['clase'], tf.int32)
            return imagen, label
            return imagen
    ```

    ##### Carga de datos
    Los datos estan por si mismo desordenados, por lo que lo que los mantendremos asi pra trabajar con los datos a medida vayan llegan para ajilizar la lectura de los mismo.
    ```
    def load_dataset(filenames, labeled=True):
        ignore_order = tf.data.Options()
        ignore_order.experimental_deterministic = False 
    ```

    Despues leeremos de multiples archivos al mismo tiempo.
    ```
        data_set = tf.data.TFRecordDataset(files_name)
    ```

    En la siguiente linea usaremos los datos tan pronto como el dato sea leido o interpretado, de forma que se ignore cualquier tipo de orden con  el objetivo de ir mas rapido.
    ```
        data_set = data_set.with_options(ignore_order)
    ```

    Ahora retornaremos un dataset en el formato (imagen, label) lo hara en pares si el labeled es true y solo pasara la imagen si el labeled es falso.
    ```
        data_set = data_set.map(
                partial(read_tfrec, labeled=labeled), num_parallel_calls=tf.data.AUTOTUNE
        )
    ```

    ##### obtener el dataset
    Esta parte es comun pero en nuestro caso esta funcion púede ser usada tanto para el dataset de entrenamiento, como para los de prueba, como para los datos valores, con solo cambiar el labeled a True o False la funcion deberia adaptarse a caulquiera de los dataset. Normalmente el dataset test sera el que lleve labeled=False.
    ```
    def get_dataset(filename, labeled=True):
            dataset = load_dataset(filename, labeled=labeled)
            dataset = dataset.shuffle(2048)
            dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
            dataset = dataset.batch(BATCH_SIZE)
            return dataset
    ```

    Ejemplo tomado de: https://keras.io/examples/keras_recipes/tfrecord/

    """
)