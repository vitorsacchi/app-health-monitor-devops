# 🚀 API Python com Deploy Automatizado na AWS (DevOps Project)

Projeto completo de DevOps que implementa uma API em Python com:

- Containerização com Docker
- Infraestrutura como código com Terraform
- Deploy automático com GitHub Actions
- Monitoramento com Prometheus e Grafana
- Execução em instância EC2 na AWS

---

## 🧠 Arquitetura

Fluxo:

1. Desenvolvedor faz push no GitHub
2. GitHub Actions executa pipeline
3. Conecta via SSH na EC2
4. Atualiza código
5. Rebuild da imagem Docker
6. Reinicia container automaticamente
7. Prometheus coleta métricas
8. Grafana exibe dashboards

---

## 🛠 Tecnologias Utilizadas

- Python (Flask)
- Docker
- Terraform
- AWS EC2
- GitHub Actions (CI/CD)
- Prometheus
- Grafana
- Git

---

## 📦 Aplicação

Endpoints:

- `/` → API principal
- `/health` → Health check
- `/metrics` → Métricas Prometheus

Métrica customizada:

app_requests_total


---

## ☁️ Infraestrutura (Terraform)

- Região: us-east-1
- EC2 t2.micro
- Security Group:
  - 22 (SSH)
  - 5000 (API)
  - 3000 (Grafana)
  - 9090 (Prometheus)

---

## 🔄 CI/CD

Pipeline executado a cada push na branch `main`.

Etapas:
- Checkout do código
- Conexão via SSH
- Pull do repositório
- Stop container antigo
- Build Docker
- Run container atualizado

---

## 📊 Monitoramento

### Prometheus
Coleta métricas da API a cada 15s.

### Grafana
Dashboard exibindo:
- Total de requisições
- Evolução ao longo do tempo

---

## 📍 Acesso (quando ativo)

- API: http://EC2-IP:5000
- Prometheus: http://EC2-IP:9090
- Grafana: http://EC2-IP:3000

---

## 📚 Objetivo

Projeto criado para prática de:

- Cloud (AWS)
- DevOps
- Observabilidade
- Automação de deploy
- Infraestrutura como código

---

## 👨‍💻 Autor

**Vitor Sacchi Sanches**

Focado em Cloud | DevOps | AWS
