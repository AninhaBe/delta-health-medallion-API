# Usando Python 3.11 para compatibilidade total com dbt e Spark modernos
FROM apache/airflow:2.10.2-python3.11

USER root
# Instala o Java 17 (mais moderno e performático para o Spark)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    apt-get clean

USER airflow

# Atualiza o pip e instala as dependências direto
# Sem compilação pesada aqui
COPY --chown=airflow:root requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt