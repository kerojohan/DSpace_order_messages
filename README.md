# DSpace_order_messages

#Eina per a la ordenació dels fitxers messages i detecció d'errors
Saltar al final de los metadatos
Creado por Joan Caparros, modificado por última vez hace 3 horas Ir al inicio de los metadatos
Per tal de controlar els fitxers de missatges s'ha creat una eina que donat un diccionari
- Elimina els comentaris
- Extreu tots els seus valors
- Ordena totes les etiquetes pel seu key
- Trimeja el seu valor, excepte si afegim espais al final de la frase, ja que a vegades interessa
- Analitza tan si l'xml d'entrada està ben format com si el xml de sortida és correcte.
- Identa tot el codi per a una correcta visualització

order&check_messages.py
 
mode d'ús:
```
# python order\&check_messages.py
usage: order&check_messages.py [-h] -i INPUT -o OUTPUT -l LANGUAGE
order&check_messages.py: error: argument -i/--input is required
``` 
Exemple
```
#python order\&check_messages.py -i originals/messages.xml -o messages.xml -l en
messages.xml
```
```
<?xml version="1.0"?>
<!--
    The contents of this file are subject to the license and copyright
    detailed in the LICENSE and NOTICE files at the root of the source
    tree and available online at
    http://www.dspace.org/license/
-->
<catalogue xml:lang="en" xmlns:i18n="http://apache.org/cocoon/i18n/2.1">
    <!--
        The format used by all keys is as follows
        xmlui.<Aspect>.<Java Class>.<name>
        There are a few exceptions to this naming format,
        1) Some general keys are in the xmlui.general namespace
           because they are used very frequently.
        2) Some general keys which are specific to a particular aspect
           may be found at xmlui.<Aspect> without specifying a
           particular java class.
        -->
    <!-- General keys -->
    <message key="xmlui.general.dspace_home">Home</message>
    <message key="xmlui.general.search">Search</message>
    <message key="xmlui.general.go">Go</message>
    <message key="xmlui.general.go_home">Go to home</message>
    <message key="xmlui.general.save">Save</message>
    <message key="xmlui.general.cancel">Cancel</message>
    <message key="xmlui.general.return">Return</message>
    <message key="xmlui.general.update">Update</message>
    <message key="xmlui.general.delete">Delete</message>
    <message key="xmlui.general.next">Next</message>
    <message key="xmlui.general.untitled">Untitled</message>
        <message key="xmlui.general.perform">Perform</message>
        <message key="xmlui.general.queue">Queue</message>
        <!-- Keys which are used by exception2dri.xsl on error pages -->
        <message key="xmlui.error.contact_msg">Please contact the site administrator if you wish to report this error. If possible, please  provide details about what you were doing at the time this error occurred.</message>
        <message key="xmlui.error.contact">Contact site administrator</message>
        <message key="xmlui.error.show_stack">Show underlying error stack</message>
     
</catalogue>
```

Resultat

``` 
<?xml version="1.0" ?>
<catalogue xml:lang="en" xmlns:i18n="http://apache.org/cocoon/i18n/2.1">
   <message key="xmlui.error.contact">Contact site administrator</message>
   <message key="xmlui.error.contact_msg">Please contact the site administrator if you wish to report this error. If possible, pleaseprovide details about what you were doing at the time this error occurred.</message>
   <message key="xmlui.error.show_stack">Show underlying error stack</message>
   <message key="xmlui.general.cancel">Cancel</message>
   <message key="xmlui.general.delete">Delete</message>
   <message key="xmlui.general.dspace_home">Home</message>
   <message key="xmlui.general.go">Go</message>
   <message key="xmlui.general.go_home">Go to home</message>
   <message key="xmlui.general.next">Next</message>
   <message key="xmlui.general.perform">Perform</message>
   <message key="xmlui.general.queue">Queue</message>
   <message key="xmlui.general.return">Return</message>
   <message key="xmlui.general.save">Save</message>
   <message key="xmlui.general.search">Search</message>
   <message key="xmlui.general.untitled">Untitled</message>
   <message key="xmlui.general.update">Update</message>
</catalogue>
```

juntament amb dspace-i10n-check2.py (modificació que dona les keys ordenanes) tenim ja totes les eines per fer bons diccionaris
