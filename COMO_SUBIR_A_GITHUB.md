# Cómo subir el proyecto a GitHub

**Iris Giselle Balderas Arreola · A01752895**

1. Se debe crear un repositorio vacío en GitHub. Puede llamarse `deteccion-spam-cnn`. No agregar README, licencia ni .gitignore al crearlo, ya que el proyecto incluye sus archivos.
2. Se debe descomprimir el ZIP y abrir una terminal dentro de la carpeta `proyecto_spam`, donde se encuentra `README.md`.
3. Se debe reemplazar `URL_DEL_REPOSITORIO` por el enlace real del repositorio y ejecutar:

```bash
git init
git add .
git commit -m "Se implementó una CNN para detectar SMS spam"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

GitHub puede solicitar autenticación con el navegador o un token. No se debe colocar un token en archivos, comandos compartidos ni en el notebook.

Si Git solicita configurar identidad, ejecutar lo siguiente con el correo que se quiera asociar al commit y repetir el commit:

```bash
git config user.name "Iris Giselle Balderas Arreola"
git config user.email "TU_CORREO_ASOCIADO_A_GITHUB"
```

Para subir correcciones posteriores:

```bash
git add .
git commit -m "Se incorporaron correcciones del proyecto"
git push
```

Si el repositorio ya contiene archivos o `origin` ya existe, se deben adaptar los pasos a ese estado. No se debe usar `push --force` como solución automática.

El archivo que se entrega en Canvas es el enlace del repositorio. Antes de entregar, comprobar que se vean `reporte_spam.ipynb`, sus resultados y `modelos/modelo_final.keras`. El modelo es pequeño y no necesita Git LFS.
