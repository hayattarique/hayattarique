<h1 align="center">👋 Hey, I'm <a href="https://github.com/TariqueHayat">Tarique Hayat</a></h1>
<h3 align="center">🚀 Backend Developer | Java | Spring Boot | Microservices | DevOps | AWS</h3>

---

### 👨‍💻 About Me

- 💼 3+ years of professional experience as a **Java Developer** with strong exposure to **DevOps** practices.
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

### 🧩 Featured Projects

| Project                                                                    | Description                                      | Tech Stack                               |
|----------------------------------------------------------------------------|--------------------------------------------------|------------------------------------------|
| 🏗️ [Real Estate ERP](https://github.com/TariqueHayat/real-estate-erp)     | Full-stack ERP system for real estate management | Spring Boot, Spring Cloud, React/Angular |
| 📬 [Mailing System](https://github.com/TariqueHayat/springboot-mailer)     | Dynamic email service using FreeMarker templates | Spring Boot, SMTP, Docker                |
| ⚙️ [Kafka Microservice](https://github.com/TariqueHayat/kafka-integration) | Event-driven producer-consumer communication     | Spring Boot, Kafka, Docker               |
| ☁️ [AWS Deployer](https://github.com/TariqueHayat/aws-deployment)          | CI/CD setup for cloud deployment                 | Jenkins, Docker, AWS EC2                 |

---

### 🧰 Skills & Tools

<p align="center">
  <!-- Backend -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="50" height="50" alt="Java"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg" width="50" height="50" alt="Spring Boot"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="50" height="50" alt="MySQL"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="50" height="50" alt="PostgreSQL"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="50" height="50" alt="MongoDB"/>

  <!-- DevOps -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="50" height="50" alt="Docker"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" width="50" height="50" alt="Kubernetes"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="50" height="50" alt="Jenkins"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="50" height="50" alt="Git"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="50" height="50" alt="GitHub"/>

  <!-- Cloud & Message Queue -->
  <img src="https://cdn.iconscout.com/icon/free/png-512/free-amazon-aws-icon-svg-download-png-3151644.png?f=webp&w=256" width="50" height="50" alt="AWS"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="50" height="50" alt="Redis"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rabbitmq/rabbitmq-original.svg" width="50" height="50" alt="RabbitMQ"/>
  <img src="https://img.icons8.com/?size=64&id=fOhLNqGJsUbJ&format=png" width="50" height="50" alt="Kafka"/>

  <!-- Frontend -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angular/angular-original.svg" width="50" height="50" alt="Angular"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="50" height="50" alt="JavaScript"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="50" height="50" alt="TypeScript"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="50" height="50" alt="HTML5"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="50" height="50" alt="CSS3"/>
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
