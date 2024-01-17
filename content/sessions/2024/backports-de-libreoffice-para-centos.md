---
title: "Backports de libreoffice para CentOS"
slug: backports-de-libreoffice-para-centos
speakers:
 - Sandino Araico 🇲🇽
time_start: 2024-02-24 10:10:00
time_end: 2024-02-24 13:00:00
track: Tools for open source development and collaboration
format: Workshop
---

El ejercicio de backport de Libreoffice para CentOS responde a la necesidad de ejecutarlo como servicio en un sistema operativo estable, ya sea en scripts de importación de formatos o (más importante) como servicio en línea "LibreOffice OnLine" para la edición colaborativa de documentos e integración con Nextcloud.
 
 Para hacer el backport se tuvieron que hacer modicicaciones al spec de Fedora, además del backport de los paquetes que se requieren como dependencia, en sus respectivos archivos spec.
 
 Además de las modificaciones a los specs se han tenido que habilitar repositorios propios y distintos ambientes de compilación con distintas características.