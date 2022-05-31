\## YTVSerie

Este sitio se trata de una web tipo catalogo sobre Series de TV en esencia, va a contener lista de [Bingers](https://www.chilango.com/cine/como-saber-si-eres-un-binger/#:~:text=B%C3%A1sicamente%20se%20aplica%20a%20aquellas,los%2012%20pasos%20de%20recuperaci%C3%B3n.)  afiliados, así como también Críticos especializados.

Para el acceso va a tener dos tipos de usuarios, el admin con permisos de Lectura, Escritura y Actualización en el sitio web. El otro es un usuario con solo permiso de lectura.

La Base de datos está conformada por:

# Tabla de **Serie**

|     |     |
| --- | --- |
| codserie | codigo o alias referente a la serie |
| nombre | nombre publicado |
| tipo | podría considerarse tambien como el genero |
| plataforma | Servicio de Streaming donde se encuentra la serie |
| fecha | fecha de emision de la temporada |
| episodios | cantidad de episodios de la temporada |
| temporada | numero de temporada |
| terminada | Si está o no terminada. |
| sinopsis | Esto es un pequeño resumen de la serie o temporada |
| imagen | Campo para agregar una imagen referencial |

# Tabla de **Critico**

|     |     |
| --- | --- |
| nombre | nombre del critico |
| apellido | apellido |
| email | email |
| alias | alias o seudónimo |
| experiencia | experiencia o estudios |

# Tabla de **Bringer**

|     |     |
| --- | --- |
| nombre | nombre |
| apellido | apellido |
| email | email |
| alias | alias o seudónimo |


Para los accesos está registrado únicamente un admin y puede registrar tantos usuarios (solo lectura) que desee.

|     |     |
| --- | --- |
| **admin** | YTVS.123 |
| **usuario1** | YTVS.user1 |
| **usuario2** | YTVS.user2 |

# Para la administracion:
http://127.0.0.1:8000/admin/