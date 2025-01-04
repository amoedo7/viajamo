import subprocess

# Ejecutar cargador.py
print("Ejecutando cargador.py...")
subprocess.run(["python", "cargador.py"])

# Ejecutar gen1.py
print("Ejecutando gen1.py...")
subprocess.run(["python", "gen1.py"])

# Ejecutar a.sh
print("Ejecutando a.sh...")
subprocess.run(["./a.sh"])

print("Proceso completado con éxito.")
