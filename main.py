# main.py

# Importar el archivo que ignora las advertencias
import ignore_warnings

# Importar otras bibliotecas necesarias
import mkdocs  # Esto es solo un ejemplo; puedes importar lo que necesites

def main():
    # Aquí puedes incluir la lógica para iniciar tu aplicación o script
    print("Iniciando la aplicación...")

    # Si deseas ejecutar MkDocs desde aquí, puedes hacerlo
    # Esto es solo un ejemplo; ajusta según tus necesidades
    # Puedes usar subprocess para ejecutar comandos de MkDocs
    import subprocess
    subprocess.run(["mkdocs", "serve"])

if __name__ == "__main__":
    main()