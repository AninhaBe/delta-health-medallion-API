## 🏗️ Arquitetura e Decisões Técnicas

### 1. Por que um Data Lakehouse e não um Banco Relacional (Postgres)?
Em vez de um banco de dados tradicional, este projeto implementa um **Data Lakehouse**. Esta escolha reflete os padrões de grandes empresas (como o Santander) por permitir o desacoplamento total entre **armazenamento** e **processamento**:
* **Escalabilidade:** O armazenamento em disco (simulando S3/Azure Blob) é virtualmente infinito e mais barato.
* **Flexibilidade:** Conseguimos manipular dados brutos (JSON) e estruturados no mesmo ecossistema.
* **Cloud Ready:** A lógica aplicada aqui é 100% transferível para ambientes de nuvem pública.

### 2. O papel do dbt no Lakehouse
Embora o **dbt** tenha nascido no contexto de Data Warehouses, aqui ele é utilizado como o motor de transformação sobre o **Apache Spark**.
* **Lógica Modular:** O dbt organiza as camadas Medallion (Staging, Silver, Gold) através de modelos SQL.
* **Governança no Lake:** O dbt traz para os arquivos "soltos" no disco a mesma robustez de documentação, testes e linhagem de dados que antes só existia em bancos de dados caros.

### 3. Delta Lake: O Coração da Consistência
Para garantir que o nosso Data Lake não se torne um "Data Swamp" (Pântano de Dados), utilizamos o formato **Delta Lake**:
* **Transações ACID:** Garante que, se um processo de ingestão falhar, os dados não fiquem corrompidos.
* **Time Travel:** Permite consultar versões anteriores dos dados e auditar alterações.
* **Performance:** Utiliza arquivos Parquet otimizados, superando a performance de bancos relacionais para grandes volumes analíticos.

### 5. Escalabilidade Horizontal e Desacoplamento
A arquitetura foi desenhada para suportar o crescimento exponencial de dados (Petabytes) através da escalabilidade horizontal:
* **Computação (Spark):** Permite adicionar nós de processamento conforme a complexidade analítica aumenta, sem impactar o armazenamento.
* **Armazenamento (Delta Lake):** Permite a expansão do Data Lake de forma independente, garantindo que o custo de armazenamento não seja inflado por necessidades de CPU.
* **Resiliência:** O desacoplamento garante que falhas na camada de computação não resultem em perda de dados, uma vez que o estado do Lakehouse é persistido de forma independente.