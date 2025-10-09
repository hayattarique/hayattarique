<h1 align="center">👋 Hey, I'm <a href="https://github.com/TariqueHayat">Tarique Hayat</a></h1>
<h3 align="center">🚀 Backend Developer | Java | Spring Boot | Microservices | DevOps | AWS</h3>

---

### 👨‍💻 About Me
- 💼 3+ years of professional experience as a **Java Developer** at **eSparksIT**
- 🧠 Currently mastering **Spring Boot**, **Microservices**, and **Kubernetes**
- 🌱 Learning **Angular** (1.5 hrs/day) & improving **Cloud + DevOps** skills
- 💬 Ask me about: `Spring Cloud`, `Kafka`, `Docker`, `AWS`, `System Design`
- 🎯 2025 Goal: Build enterprise-grade SaaS solutions using Spring Cloud + Angular
- 📫 Reach me at: **hayattarique3@gmail.com**
- 📍 Preferred locations: Hyderabad | Kolkata | Delhi

---

### 🛠️ Tech Arsenal

#### 💻 Backend
`Java` • `Spring Boot` • `Spring Cloud` • `Hibernate` • `JPA` • `Microservices`

#### ☁️ Cloud & DevOps
`Docker` • `Jenkins` • `AWS (EC2, S3, RDS)` • `SonarQube` • `Kafka` • `Kubernetes (Learning)`

#### 🧠 Tools & Others
`Postman` • `Swagger` • `Maven` • `GitHub Actions` • `JUnit5` • `Mockito`

#### 🌐 Frontend
`Angular` • `TypeScript` (Learning Phase)

---

### 📊 GitHub Analytics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=TariqueHayat&show_icons=true&theme=radical" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=TariqueHayat&layout=compact&theme=radical" height="165" />
</p>

---

### 🧩 Featured Projects

| Project | Description | Tech Stack |
|----------|--------------|------------|
| 🏗️ [Real Estate ERP](https://github.com/TariqueHayat/real-estate-erp) | Full-stack ERP system for real estate management | Spring Boot, Spring Cloud, React/Angular |
| 📬 [Mailing System](https://github.com/TariqueHayat/springboot-mailer) | Dynamic email service using FreeMarker templates | Spring Boot, SMTP, Docker |
| ⚙️ [Kafka Microservice](https://github.com/TariqueHayat/kafka-integration) | Event-driven producer-consumer communication | Spring Boot, Kafka, Docker |
| ☁️ [AWS Deployer](https://github.com/TariqueHayat/aws-deployment) | CI/CD setup for cloud deployment | Jenkins, Docker, AWS EC2 |

---

### 🧠 Tech Badges

<p align="center">
  <img src="https://img.shields.io/badge/Java-17-blue?logo=java&logoColor=white">
  <img src="https://img.shields.io/badge/Spring_Boot-Expert-green?logo=springboot">
  <img src="https://img.shields.io/badge/Microservices-Architecture-important">
  <img src="https://img.shields.io/badge/Kafka-Enabled-red?logo=apachekafka">
  <img src="https://img.shields.io/badge/Docker-Containerization-blue?logo=docker">
  <img src="https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws">
  <img src="https://img.shields.io/badge/Angular-Learning-red?logo=angular">
</p>

---

### ⚙️ CI/CD Pipeline Showcase
Here’s my sample **GitHub Action** to build Java projects automatically:

```yaml
name: Java CI with Maven
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build with Maven
        run: mvn clean install -DskipTests
