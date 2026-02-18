# 🚀 App Health Monitor - End-to-End DevOps Project

Este projeto demonstra um pipeline completo de CI/CD e Observabilidade, monitorando uma API Python (Flask) rodando em containers Docker dentro da AWS (EC2).

## 🛠️ Tecnologias Utilizadas
* **Cloud:** AWS (EC2, Security Groups, IAM)
* **Containers:** Docker & Docker Compose
* **CI/CD:** GitHub Actions (Deploy automatizado via SSH)
* **Monitoramento:** Prometheus (Coleta de métricas)
* **Visualização:** Grafana (Dashboards em tempo real)
* **Linguagem:** Python (Flask)

## 🏗️ Arquitetura
1.  **API Flask**: Expõe um endpoint `/metrics` com o `prometheus_client`.
2.  **GitHub Actions**: A cada `push` na `main`, o código é atualizado na EC2, o container sofre build e restart automático.
3.  **Prometheus**: Realiza o scrape dos dados da API a cada 15 segundos.
4.  **Grafana**: Conecta no Prometheus e exibe o volume de tráfego e saúde da aplicação.

## 📈 Dashboard
O dashboard no Grafana monitora o total de requisições HTTP (`app_requests_total`) em tempo real.
