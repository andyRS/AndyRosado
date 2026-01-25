# Guía para Capturas de Pantalla del Portafolio

Este documento proporciona instrucciones detalladas para capturar screenshots de alta calidad para los proyectos del portafolio.

## Estado Actual

Actualmente se están utilizando **imágenes placeholder** temporales para los siguientes proyectos:
- FreisiWeb
- Angular Blog
- CoopDinamic
- Proy Eli

## URLs a Capturar

### 1. FreisiWeb (Proyecto Reemplazado - Posición 6)
- **URL:** https://andyrs.github.io/FreisiWeb/
- **Nombre del archivo:** `image/freisiweb-screenshot.jpg`
- **Descripción:** Sitio web de trading y mentoría financiera

### 2. Angular Blog (Proyecto Reemplazado - Posición 7)
- **URL:** https://andyrs.github.io/project_angularWebApp/
- **Nombre del archivo:** `image/angular-blog-screenshot.jpg`
- **Descripción:** Blog interactivo con Angular

### 3. CoopDinamic (Proyecto Nuevo - Posición 8)
- **URL:** https://github.com/andyRS/CoopDinamic
- **Nombre del archivo:** `image/coopdinamic-screenshot.jpg`
- **Descripción:** Página del repositorio en GitHub (no tiene GitHub Pages activo)
- **Nota:** Capturar la página principal del repositorio

### 4. Proy Eli (Proyecto Nuevo - Posición 9)
- **URL:** https://andyrs.github.io/proy_eli/
- **Nombre del archivo:** `image/proy-eli-screenshot.jpg`
- **Descripción:** Proyecto PHP

## Especificaciones Técnicas

### Dimensiones
- **Resolución recomendada:** 1920x1080px (16:9) o 1200x800px
- **Viewport para captura:** 1920x1080px (desktop)
- **Orientación:** Horizontal (landscape)

### Formato y Calidad
- **Formato:** JPG (preferido) o PNG
- **Calidad JPG:** 80-85%
- **Peso máximo:** 300KB por imagen
- **Optimización:** Usar herramientas de compresión después de capturar

### Atributos HTML
Todas las imágenes ya tienen configurados:
- Atributos `alt` descriptivos
- `loading="lazy"` para carga diferida
- `decoding="async"` para decodificación asíncrona

## Métodos de Captura

### Opción A: Extensión de Navegador (Recomendado)

#### Chrome/Edge
1. Instalar extensión "Full Page Screen Capture" o "GoFullPage"
2. Abrir la URL del proyecto
3. Esperar a que cargue completamente
4. Hacer clic en el icono de la extensión
5. Guardar la imagen con el nombre correspondiente

#### Firefox
1. Presionar `Ctrl+Shift+I` (Windows) o `Cmd+Opt+I` (Mac) para abrir DevTools
2. Presionar `Ctrl+Shift+P` o `Cmd+Shift+P`
3. Escribir "screenshot" y seleccionar "Take a screenshot of the entire page"
4. Guardar con el nombre correspondiente

### Opción B: DevTools de Chrome
1. Abrir la página del proyecto
2. Presionar `F12` para abrir DevTools
3. Presionar `Ctrl+Shift+P` (Windows) o `Cmd+Shift+P` (Mac)
4. Escribir "screenshot" y seleccionar "Capture full size screenshot"
5. La imagen se descargará automáticamente
6. Renombrar según corresponda

### Opción C: Servicios Online

#### Screenshot Machine
```
https://api.screenshotmachine.com/?key=YOUR_KEY&url=URL_DEL_PROYECTO&dimension=1920x1080
```

#### Screenshotlayer
```
http://api.screenshotlayer.com/api/capture?access_key=YOUR_KEY&url=URL_DEL_PROYECTO&viewport=1920x1080
```

### Opción D: Línea de Comandos (Avanzado)

#### Con Chromium/Chrome Headless
```bash
# Para FreisiWeb
chromium --headless --disable-gpu --screenshot=/tmp/freisiweb.png \
  --window-size=1920,1080 https://andyrs.github.io/FreisiWeb/

# Para Angular Blog
chromium --headless --disable-gpu --screenshot=/tmp/angular-blog.png \
  --window-size=1920,1080 https://andyrs.github.io/project_angularWebApp/

# Para CoopDinamic
chromium --headless --disable-gpu --screenshot=/tmp/coopdinamic.png \
  --window-size=1920,1080 https://github.com/andyRS/CoopDinamic

# Para Proy Eli
chromium --headless --disable-gpu --screenshot=/tmp/proy-eli.png \
  --window-size=1920,1080 https://andyrs.github.io/proy_eli/
```

#### Con Firefox Headless
```bash
firefox --headless --screenshot /tmp/screenshot.png --window-size=1920,1080 URL
```

## Proceso de Optimización

### 1. Conversión a JPG (si es PNG)
```bash
convert screenshot.png -quality 85 screenshot.jpg
```

### 2. Optimización con ImageMagick
```bash
convert screenshot.jpg -strip -interlace Plane -quality 85 optimized.jpg
```

### 3. Optimización con JPEGoptim
```bash
jpegoptim --max=85 --strip-all screenshot.jpg
```

### 4. Verificar tamaño
```bash
du -h screenshot.jpg
```

Si el archivo es mayor a 300KB, reducir la calidad:
```bash
convert screenshot.jpg -quality 75 screenshot-optimized.jpg
```

## Instrucciones Paso a Paso (Método Manual)

### Paso 1: Preparación
1. Abrir un navegador en modo incógnito (para evitar extensiones que modifiquen el aspecto)
2. Ajustar la ventana del navegador a 1920x1080px o maximizar en pantalla Full HD

### Paso 2: Captura
Para cada URL:

1. **FreisiWeb**
   ```
   URL: https://andyrs.github.io/FreisiWeb/
   Archivo: image/freisiweb-screenshot.jpg
   ```
   - Abrir la URL
   - Esperar 3-5 segundos a que cargue completamente
   - Tomar captura de pantalla completa
   - Guardar como `freisiweb-screenshot.jpg`

2. **Angular Blog**
   ```
   URL: https://andyrs.github.io/project_angularWebApp/
   Archivo: image/angular-blog-screenshot.jpg
   ```
   - Abrir la URL
   - Esperar a que cargue completamente
   - Tomar captura de pantalla completa
   - Guardar como `angular-blog-screenshot.jpg`

3. **CoopDinamic**
   ```
   URL: https://github.com/andyRS/CoopDinamic
   Archivo: image/coopdinamic-screenshot.jpg
   ```
   - Abrir la URL del repositorio
   - Esperar a que cargue la página de GitHub
   - Tomar captura de la parte superior (README visible)
   - Guardar como `coopdinamic-screenshot.jpg`

4. **Proy Eli**
   ```
   URL: https://andyrs.github.io/proy_eli/
   Archivo: image/proy-eli-screenshot.jpg
   ```
   - Abrir la URL
   - Esperar a que cargue completamente
   - Tomar captura de pantalla completa
   - Guardar como `proy-eli-screenshot.jpg`

### Paso 3: Optimización
1. Abrir cada imagen en un editor (GIMP, Photoshop, o herramienta online)
2. Si es necesario, recortar para mostrar la mejor parte del sitio
3. Redimensionar a 1200x800px si el tamaño del archivo es muy grande
4. Exportar como JPG con calidad 80-85%
5. Verificar que el peso sea menor a 300KB

### Paso 4: Reemplazo
1. Guardar las imágenes en la carpeta `image/` del proyecto
2. Sobrescribir los archivos placeholder existentes:
   - `image/freisiweb-screenshot.jpg`
   - `image/angular-blog-screenshot.jpg`
   - `image/coopdinamic-screenshot.jpg`
   - `image/proy-eli-screenshot.jpg`

## Verificación

Después de reemplazar las imágenes:

1. Abrir `index.html` en un navegador
2. Navegar a la sección de Portafolio
3. Verificar que las 4 nuevas imágenes se muestren correctamente
4. Verificar que los enlaces funcionan correctamente
5. Probar la responsividad en diferentes tamaños de pantalla

## Checklist Final

- [ ] Captura de FreisiWeb tomada
- [ ] Captura de Angular Blog tomada
- [ ] Captura de CoopDinamic tomada
- [ ] Captura de Proy Eli tomada
- [ ] Todas las imágenes optimizadas (<300KB)
- [ ] Todas las imágenes guardadas en `image/`
- [ ] Imágenes verificadas en el navegador
- [ ] Enlaces externos verificados
- [ ] Responsividad verificada

## Notas Adicionales

- Las imágenes deben capturar la esencia y funcionalidad principal de cada proyecto
- Preferir capturas que muestren contenido real en lugar de páginas de carga
- Para CoopDinamic (GitHub), asegurarse de que el README sea visible
- Mantener consistencia visual con las otras imágenes del portafolio

## Recursos Útiles

- **Herramientas de captura:** [Awesome Screenshot](https://www.awesomescreenshot.com/)
- **Optimización online:** [TinyJPG](https://tinyjpg.com/), [Squoosh](https://squoosh.app/)
- **Verificar tamaño:** [Image Size Tool](https://www.imgonline.com.ua/eng/get-info.php)

---

**Última actualización:** 2026-01-25
**Estado:** Placeholders activos, pendiente reemplazo con screenshots reales
