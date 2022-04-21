"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
from operator import itemgetter
from numpy import sort
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return tbl0.shape[0]


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    return tbl0.shape[1]


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    # tbl0._c1.value_counts().sort_index(axis=0,ascending=True)
    return  tbl0.groupby('_c1')['_c1'].count()


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return tbl0.groupby('_c1')['_c2'].mean() 


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    q6 = []
    q6 =sorted( [ i.upper() for i in tbl1['_c4'].unique().tolist() ], key=itemgetter(0), reverse=False )

    return q6


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return tbl0.groupby('_c1')['_c2'].sum()


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    # tbl0['year'] = pd.to_datetime( tbl0['_c3'], errors='ignore' ).to_string().split('-')
    tbl0['year'] = tbl0['_c3'].astype(str).apply( lambda x: list(str(x).split('-'))[0] )

    tbl0 = pd.DataFrame( { '_c0':tbl0['_c0'], '_c1':tbl0['_c1'], '_c2':tbl0['_c2'], '_c3':tbl0['_c3'], 'year':tbl0['year']} )
    # print( tbl0.shape )
    
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

    # step:1 obtain a subset of the DataFrame’s columns
    tbl0 = tbl0[['_c1','_c2']]
    # print(tbl0)

    # step:2 group by first column
    tbl0 = tbl0.groupby('_c1')['_c2'].apply(list).apply( lambda x: sort(x)).astype(str).apply(lambda x: x.replace(' ',':')).apply(lambda x: x.replace('[','')).apply(lambda x: x.replace(']',''))
    # print( type(tbl0) )
    # print( tbl0 )

    # step:3 convert to df 
    tbl0 = pd.DataFrame( {'_c2':tbl0.values} , index=pd.Series(tbl0.index, name='_c1' ),  )

    return tbl0


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    group_c0_tbl1 = tbl1.groupby('_c0')['_c4'].apply(list).apply( lambda x: sort(x) ).apply( lambda x: ','.join(x) )
    # print ( type(group_c0_tbl1) )

    group_c0_tbl1 = pd.DataFrame( {'_c0':group_c0_tbl1.index, '_c4':group_c0_tbl1.values } )
    # print ( type(group_c0_tbl1) )
    # print ( group_c0_tbl1.columns )

    return group_c0_tbl1


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """

    tbl2['_c5ab'] = tbl2['_c5a']+":"+tbl2['_c5b'].astype(str)
    # print ( tbl2 )
    
    gc0_tbl2 = tbl2.groupby('_c0')['_c5ab'].apply(list)
    # print ( gc0_tbl2 )

    gc0_tbl2 = pd.DataFrame({'_c0':gc0_tbl2.index, '_c5':gc0_tbl2.values })
    # print ( gc0_tbl2 )

    gc0_tbl2['_c5'] = gc0_tbl2['_c5'].apply( lambda x: sort(x)  ).apply( lambda x: ','.join(x) )
    # print ( gc0_tbl2 )
 
    return gc0_tbl2


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """

    mergeTable = pd.merge(tbl0,tbl2, sort=True) 
    # print ( mergeTable.head(n=20) )

    g_mergeTable = mergeTable.groupby('_c1')['_c5b'].sum()
    # print ( g_mergeTable )

    return g_mergeTable
"""
print('* * * * * * * * * * ** * * * * Result pregunta_01')
print(pregunta_01())
print('* * * * * * * * * * ** * * * * Result pregunta_02')
print(pregunta_02())
print('* * * * * * * * * * ** * * * * Result pregunta_03')
print(pregunta_03())
print('* * * * * * * * * * ** * * * * Result pregunta_04')
print(pregunta_04())
print('* * * * * * * * * * ** * * * * Result pregunta_05')
print(pregunta_05())
print('* * * * * * * * * * ** * * * * Result pregunta_06')
print(pregunta_06())
print('* * * * * * * * * * ** * * * * Result pregunta_07')
print(pregunta_07())
print('* * * * * * * * * * ** * * * * Result pregunta_08')
print(pregunta_08())
print('* * * * * * * * * * ** * * * * Result pregunta_09')
print(pregunta_09())
print('* * * * * * * * * * ** * * * * Result pregunta_10')
print(pregunta_10())
print('* * * * * * * * * * ** * * * * Result pregunta_11')
print(pregunta_11())
print('* * * * * * * * * * ** * * * * Result pregunta_12')
print(pregunta_12())
print('* * * * * * * * * * ** * * * * Result pregunta_13')
print(pregunta_13())
"""