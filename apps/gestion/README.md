Sistema de Gestión de Horarios

Python 3 + Django | Arquitectura Hexagonal

Este proyecto es un sistema básico para la gestión de horarios, construido con Django y siguiendo el enfoque de arquitectura hexagonal (ports & adapters).
El objetivo es mantener una separación clara entre la lógica de negocio, la aplicación y las dependencias externas.



Dijiste:
Dame un readme de un sistema de gestión de horario algo básico esta con python + django y estructura hexagonal solo con domain, infraestructura, aplocatiom
ChatGPT dijo:
Aquí tienes un README.md básico, claro y listo para usar para un sistema de gestión de horarios desarrollado con Python + Django y una arquitectura hexagonal (domain, application, infrastructure).
Lo puedes copiar/pegar y adaptar según tu proyecto.

🕒 Sistema de Gestión de Horarios
Python 3 + Django | Arquitectura Hexagonal

Este proyecto es un sistema básico para la gestión de horarios, construido con Django y siguiendo el enfoque de arquitectura hexagonal (ports & adapters).
El objetivo es mantener una separación clara entre la lógica de negocio, la aplicación y las dependencias externas.

 Arquitectura Hexagonal 
El sistema sigue 3 capas principales:

1. Domain (Núcleo del negocio)
Contiene las entidades y lógica pura del dominio.

No depende de Django ni de ninguna tecnología.

Ejemplos:

Schedule: representa un horario.

ScheduleService: lógica para crear, actualizar o validar horarios.

2. Application (Casos de uso)
Orquesta el flujo entre el dominio y las dependencias externas.

Expone Commands y Queries.

Usa DTOs para intercambiar datos.

Ejemplo: ManageScheduleUseCase.

3. Infrastructure (Adaptadores)
Implementación concreta usando Django.

Contiene:

Modelos Django (ORM)

Serializadores

Vistas / API REST

Repositorios concretos para acceder a la base de datos

Instalación y Ejecución
1. Clonar el repositorio
git clone https://github.com/tu_usuario/gestion-horarios.git
cd gestion-horarios
