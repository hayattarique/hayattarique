<!-- ============================================================ -->
<!--   TARIQUE HAYAT · GITHUB PROFILE README                     -->
<!-- ============================================================ -->

<p align="center">
  <img src="https://raw.githubusercontent.com/hayattarique/hayattarique/main/assets/hero.svg" width="100%" alt="Tarique Hayat — Java Backend and Cloud Engineer" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=19&duration=3000&pause=1000&color=A78BFA&background=00000000&center=true&vCenter=true&width=820&height=44&lines=Java+17+%2F+21+%C2%B7+Spring+Boot+3+%2F+4+%C2%B7+Microservices+at+scale;Event-driven+systems+on+Kafka+%C2%B7+Saga+%C2%B7+Resilience4j;Cloud-native+delivery+on+AWS+%C2%B7+Docker+%C2%B7+Kubernetes+%C2%B7+Jenkins" alt="Java 17 and 21, Spring Boot 3 and 4, microservices, Kafka, AWS" />
</p>

<p align="center">
  <a href="mailto:hayattarique3@gmail.com">
    <img src="https://img.shields.io/badge/%F0%9F%9F%A2%20OPEN%20TO%20WORK-Senior%20Java%20Backend%20%26%20Cloud%20Engineer-22C55E?style=for-the-badge&labelColor=064e3b" alt="Open to work: Senior Java Backend and Cloud Engineer" />
  </a>
</p>

<p align="center">
  <a href="mailto:hayattarique3@gmail.com"><img src="https://img.shields.io/badge/Email-hayattarique3%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email" /></a>&nbsp;
  <img src="https://img.shields.io/badge/Focus-Distributed%20Systems%20%C2%B7%20Cloud%20Native-A78BFA?style=flat-square&labelColor=0d1117" alt="Focus: distributed systems, cloud native" />&nbsp;
  <img src="https://img.shields.io/badge/Based%20in-Hyderabad%20%C2%B7%20Kolkata%20%C2%B7%20Delhi%20%C2%B7%20Remote-7C3AED?style=flat-square&labelColor=0d1117" alt="Location" />&nbsp;
  <img src="https://komarev.com/ghpvc/?username=hayattarique&style=flat-square&color=7C3AED&label=Profile+views&abbreviated=true" alt="Profile views" />
</p>

---

## About

I build backend systems that stay up. Shipping Java services into production has made me
opinionated about a short list of things: clear service boundaries, failure handled at the edge
before it cascades, and enough telemetry to answer "what broke?" in minutes rather than hours.

```java
public final class TariqueHayat implements BackendEngineer {

    static final String ROLE  = "Java Backend & Cloud Engineer";
    static final String FOCUS = "Resilient, observable, event-driven systems";
    static final String BASE  = "Hyderabad · Kolkata · Delhi · Remote";

    @Override
    public Stack primaryStack() {
        return Stack.of(
            Language.JAVA_17, Language.JAVA_21,
            Framework.SPRING_BOOT_3, Framework.SPRING_BOOT_4,
            Framework.SPRING_CLOUD, Framework.SPRING_SECURITY_6,
            Messaging.KAFKA, Persistence.POSTGRES, Persistence.REDIS,
            Cloud.AWS, Platform.DOCKER, Platform.KUBERNETES
        );
    }

    @Override
    public String currentlyBuilding() {
        return "High-throughput FinTech microservices — resilient, observable, event-driven";
    }

    @Override
    public List<String> learningNext() {
        return List.of("Helm & K8s operators", "CQRS + event sourcing", "OpenTelemetry");
    }

    @Override
    public boolean openToOpportunities() {
        return true;   // Senior Backend & Cloud Engineer
    }
}
```

---

## Impact

<table width="100%">
  <tr>
    <td width="33%" align="center">
      <h3>11</h3>
      <b>Spring Boot microservices</b><br/>
      <sub>Independently deployable services powering a live FinTech platform</sub>
      <br/><br/>
    </td>
    <td width="33%" align="center">
      <h3>~30%</h3>
      <b>Faster inter-service calls</b><br/>
      <sub>Netflix Eureka + Spring Cloud Gateway replacing hardcoded service routing</sub>
      <br/><br/>
    </td>
    <td width="33%" align="center">
      <h3>50+</h3>
      <b>REST APIs designed</b><br/>
      <sub>Versioned, documented with OpenAPI, secured with JWT and role-based access</sub>
      <br/><br/>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <h3>Zero</h3>
      <b>Downtime deployments</b><br/>
      <sub>Rolling releases on AWS after re-architecting legacy modules — ~30% less release effort</sub>
      <br/><br/>
    </td>
    <td width="33%" align="center">
      <h3>10+</h3>
      <b>CI/CD pipelines automated</b><br/>
      <sub>Build, test, SonarQube quality gate, image push and deploy — no manual steps</sub>
      <br/><br/>
    </td>
    <td width="33%" align="center">
      <h3>TDD</h3>
      <b>JUnit 5 · Mockito · JaCoCo</b><br/>
      <sub>Coverage gates enforced in the pipeline, cutting regression risk across services</sub>
      <br/><br/>
    </td>
  </tr>
</table>

**What that looked like in practice:** Resilience4j circuit breakers and bulkheads to stop
cascading failure, configuration and credentials pulled from AWS Secrets Manager instead of
committed properties, and distributed tracing plus centralised logging so production incidents
get diagnosed from evidence rather than guesswork.

---

## System Architecture

The reference architecture I build and operate in production. The flagship project below implements
the edge, discovery and security layers today; the event and observability tiers are its roadmap.

<p align="center">
  <img src="https://raw.githubusercontent.com/hayattarique/hayattarique/main/assets/architecture.svg" width="100%" alt="Cloud-native microservices architecture: edge clients, Spring Cloud Gateway with Eureka discovery and Config Server, six domain services, Kafka event backbone, polyglot persistence, and the platform and observability layer" />
</p>

---

## Featured Work

### 🛒 [Enterprise E-Commerce Microservices](https://github.com/hayattarique/ecommerce-microservice) &nbsp;·&nbsp; flagship

<p>
  <img src="https://img.shields.io/badge/Java-21-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java 21" />
  <img src="https://img.shields.io/badge/Spring_Boot-4.1.0-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot 4.1.0" />
  <img src="https://img.shields.io/badge/Spring_Cloud-2025.1.2-6DB33F?style=flat-square&logo=spring&logoColor=white" alt="Spring Cloud 2025.1.2" />
  <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL 16" />
  <img src="https://img.shields.io/badge/Flyway-12.4.0-CC0200?style=flat-square&logo=flyway&logoColor=white" alt="Flyway" />
  <img src="https://img.shields.io/badge/MapStruct-1.6.3-E37B4A?style=flat-square&logo=java&logoColor=white" alt="MapStruct" />
</p>

A distributed e-commerce backend on **Java 21 and Spring Boot 4**, built sprint by sprint with
review and refactoring between each. Seven Maven modules — `gateway`, `auth-service`,
`user-service`, `discovery-server`, `utility-service`, `config-server`, under an
`ecommerce-parent` reactor.

| | |
|---|---|
| **A security starter, not a copied filter** | `utility-service` ships a real Spring Boot **auto-configuration** — a new service adds one dependency and inherits JWT validation, claim extraction and the auth entry point. Every bean is `@ConditionalOnMissingBean`, so a service overrides one without forking the library. |
| **Full token lifecycle** | HS256 access tokens (1 h) plus persisted refresh tokens (7 d) with **rotation, revocation and token-type separation** — a refresh token is rejected anywhere an access token is expected. |
| **Authorization with no network hop** | `users → roles → permissions` flattened into token claims, so every service authorizes locally. Refresh tokens deliberately omit them, so a permission change lands within one token lifetime instead of needing re-login. |
| **Defence in depth** | JWT verified at the gateway *and* again inside each service — a request that bypasses the edge is still fully protected. |
| **Separate service-to-service channel** | Internal API on its own filter chain, guarded by `X-Internal-Api-Key` compared in **constant time** — never touches the JWT path. |
| **Migrations own the schema** | Flyway-versioned SQL with `ddl-auto=none`, so entity/schema drift fails at startup instead of silently mutating a database. |
| **Stable error contract** | An `ErrorCode` interface and per-service enums produce machine-readable codes (`AUTH_101`, `SEC-002`) that clients branch on, instead of parsing prose. |
| **Database per service** | No shared tables, no cross-service foreign keys — services linked by identifier only, exactly as if deployed independently. |

Also: JPA auditing with `@CreatedBy`/`@LastModifiedBy` off the security context, `@Version`
optimistic locking on every table, MapStruct mapping, a uniform `ApiResponse<T>` / `PageResponse<T>`
envelope, and springdoc OpenAPI on both business services.

**Shipping model.** A promotion workflow — `main ← stage ← qa ← dev ← feature/*`, one branch per
ticket, merged by PR after review. All four environment branches plus live `feature/*` branches
exist in the repo — the process is real, not just documented.

**In flight.** Authentication is near complete; next are Testcontainers integration tests,
Resilience4j, gateway rate limiting, Docker Compose and GitHub Actions — then the product, cart and
order services, Kafka with a transactional outbox, and observability. The project README marks every
item as shipped or planned rather than blurring the two.

---

### More work

<table width="100%">
<tr>
<td width="33%" valign="top">

### ☁️ [spring-cloud](https://github.com/hayattarique/spring-cloud)

`Java` · `Spring Cloud Config` · `Jenkins` · ⭐ 2

Centralised configuration management across a microservices estate — **configserver** serving
**distributornetwork** and **inventorymanagement**, with a committed **Jenkinsfile** driving the
build.

Shows the part most tutorials skip: how config actually propagates across services and
environments without redeploying every one of them.

</td>
<td width="33%" valign="top">

### ⚡ [saga-choreography](https://github.com/hayattarique/saga-choreography)

`Java` · `Apache Kafka` · `Event-Driven`

Distributed transactions with no central orchestrator. **order-service** and **payment-service**
exchange domain events over Kafka through a shared **common-dtos** contract module.

Covers the hard half of the pattern — eventual consistency, fault isolation, and compensating
transactions that unwind a failed flow cleanly.

</td>
<td width="33%" valign="top">

### 🚪 [cloud-gateway](https://github.com/hayattarique/cloud-gateway)

`Java` · `Spring Cloud Gateway` · `Eureka`

API gateway with **Spring Cloud Load Balancer** and **Netflix Eureka** for dynamic discovery,
intelligent routing and client-side load distribution.

Route configuration, filter chains and resilience wiring in a production-shaped setup rather than
a single-file example.

</td>
</tr>
</table>

### Deeper dives

Focused repositories, each isolating one production concern so the pattern is readable on its own.

| Repository | Concern it isolates |
|---|---|
| [circuitbreaker3.3.x](https://github.com/hayattarique/circuitbreaker3.3.x) | Spring Cloud Circuit Breaker against slow and unresponsive downstreams |
| [spring-security-jwt-h2-swagger](https://github.com/hayattarique/spring-security-jwt-h2-swagger) | Spring Security 6, stateless JWT, RBAC, documented end-to-end with OpenAPI |
| [spring-security-6.2.x](https://github.com/hayattarique/spring-security-6.2.x) | Spring Security 6.2 filter chain internals, built with Gradle |
| [feign-client](https://github.com/hayattarique/feign-client) | Declarative HTTP clients for typed inter-service calls |
| [spring-webflux](https://github.com/hayattarique/spring-webflux) | Reactive, non-blocking APIs with Project Reactor |
| [spring-batch](https://github.com/hayattarique/spring-batch) | Chunked batch processing, job orchestration and restartability |
| [junit-demo](https://github.com/hayattarique/junit-demo) | JUnit 5 and Mockito patterns underpinning the TDD workflow |
| [spring-boot-mutiple-db](https://github.com/hayattarique/spring-boot-mutiple-db) | Multiple datasources and transaction managers in one application |
| [voting-api](https://github.com/hayattarique/voting-api) | REST API built on the Gradle toolchain |
| [data-rest](https://github.com/hayattarique/data-rest) | Spring Data REST repository exposure and HAL responses |

---

## Tech Stack

<table width="100%">
  <tr>
    <td width="20%" valign="middle"><b>Language &amp; Core</b></td>
    <td valign="middle">
      <img src="https://img.shields.io/badge/Java_17_%2F_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java 17 and 21" />
      <img src="https://img.shields.io/badge/Spring_Boot_3_%2F_4-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot 3 and 4" />
      <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white" alt="Spring Cloud" />
      <img src="https://img.shields.io/badge/Spring_Security_6-6DB33F?style=flat-square&logo=springsecurity&logoColor=white" alt="Spring Security 6" />
      <img src="https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=flat-square&logo=spring&logoColor=white" alt="Spring Data JPA" />
      <img src="https://img.shields.io/badge/Hibernate-59666C?style=flat-square&logo=hibernate&logoColor=white" alt="Hibernate" />
      <img src="https://img.shields.io/badge/Flyway-CC0200?style=flat-square&logo=flyway&logoColor=white" alt="Flyway" />
      <img src="https://img.shields.io/badge/MapStruct-E37B4A?style=flat-square&logo=java&logoColor=white" alt="MapStruct" />
      <img src="https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white" alt="Maven" />
    </td>
  </tr>
  <tr>
    <td valign="middle"><b>Distributed Systems</b></td>
    <td valign="middle">
      <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" alt="Apache Kafka" />
      <img src="https://img.shields.io/badge/Netflix_Eureka-E50914?style=flat-square&logo=netflix&logoColor=white" alt="Netflix Eureka" />
      <img src="https://img.shields.io/badge/Resilience4j-FF6B35?style=flat-square&logo=spring&logoColor=white" alt="Resilience4j" />
      <img src="https://img.shields.io/badge/Feign_Client-00C7B7?style=flat-square&logo=spring&logoColor=white" alt="Feign Client" />
      <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
      <img src="https://img.shields.io/badge/JWT_%2F_OAuth2-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT and OAuth2" />
      <img src="https://img.shields.io/badge/OpenAPI_%2F_Swagger-85EA2D?style=flat-square&logo=swagger&logoColor=black" alt="OpenAPI and Swagger" />
    </td>
  </tr>
  <tr>
    <td valign="middle"><b>Cloud &amp; Delivery</b></td>
    <td valign="middle">
      <img src="https://img.shields.io/badge/AWS_EC2_%C2%B7_S3_%C2%B7_RDS-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS EC2, S3, RDS" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
      <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes" />
      <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white" alt="Jenkins" />
      <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white" alt="SonarQube" />
    </td>
  </tr>
  <tr>
    <td valign="middle"><b>Data</b></td>
    <td valign="middle">
      <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/MySQL_8-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL 8" />
      <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
    </td>
  </tr>
  <tr>
    <td valign="middle"><b>Testing &amp; Observability</b></td>
    <td valign="middle">
      <img src="https://img.shields.io/badge/JUnit_5-25A162?style=flat-square&logo=junit5&logoColor=white" alt="JUnit 5" />
      <img src="https://img.shields.io/badge/Mockito-C5D9F1?style=flat-square&logo=java&logoColor=black" alt="Mockito" />
      <img src="https://img.shields.io/badge/JaCoCo-E05C27?style=flat-square&logo=java&logoColor=white" alt="JaCoCo" />
      <img src="https://img.shields.io/badge/Zipkin-FF6C37?style=flat-square&logo=zipkin&logoColor=white" alt="Zipkin" />
      <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus" />
      <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana" />
      <img src="https://img.shields.io/badge/ELK_Stack-005571?style=flat-square&logo=elasticstack&logoColor=white" alt="ELK Stack" />
    </td>
  </tr>
</table>

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,hibernate,kafka,aws,docker,kubernetes,jenkins,githubactions,postgres,mysql,mongodb,redis,git,maven,postman&perline=16&theme=dark" alt="Technology icons" />
</p>

---

## Delivery Pipeline

A trimmed version of the pipeline shape I run for Java services — quality gate before image build,
image before deploy, and a rolling swap so the service never goes dark.

```yaml
name: Java CI/CD Pipeline
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: maven

      - name: Build, test and enforce coverage
        run: mvn clean verify -Dspring.profiles.active=test

      - name: SonarQube quality gate
        run: mvn sonar:sonar -Dsonar.host.url=${{ secrets.SONAR_URL }}

      - name: Build and push image
        run: |
          docker build -t hayattarique/app:${{ github.sha }} .
          docker push hayattarique/app:${{ github.sha }}

      - name: Rolling deploy to AWS EC2
        run: |
          ssh ${{ secrets.EC2_HOST }} \
            "docker pull hayattarique/app:${{ github.sha }} && \
             docker compose up -d --no-deps --scale app=2 app"
```

---

## GitHub Activity

<p align="center">
  <img height="180em" src="https://github-stats-extended.vercel.app/api/top-langs/?username=hayattarique&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=a78bfa&text_color=c9d1d9&langs_count=6&hide=html,css" alt="Most used languages by code volume" />
  &nbsp;
  <img height="180em" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=hayattarique&theme=github_dark" alt="Top languages by commit" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=hayattarique&theme=tokyo-night&hide_border=true&area=true&area_color=7c3aed&color=a78bfa&line=7c3aed&point=f59e0b&bg_color=0d1117&custom_title=Contribution%20Graph" width="98%" alt="Contribution graph" />
</p>

---

## How I Work

**Design for failure.** Every distributed system fails eventually. Circuit breakers, bulkheads,
timeouts and graceful degradation go in on day one, not after the first incident.

**Observability is part of done.** A service you cannot see inside is unfinished. Structured logs,
distributed traces and health metrics ship with the feature.

**Automate the second time.** CI/CD, provisioning and coverage gates. Manual steps are technical
debt wearing a process costume.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:050510,25:0b2548,55:1a0845,80:0f0030,100:050510&height=140&section=footer&animation=twinkling" width="100%" alt="" />
</p>

<h3 align="center">Let's build something that stays up</h3>

<p align="center">
  Open to <b>Senior Java Backend &amp; Cloud Engineer</b> roles — Hyderabad · Kolkata · Delhi · Remote
</p>

<p align="center">
  <a href="mailto:hayattarique3@gmail.com">
    <img src="https://img.shields.io/badge/%F0%9F%93%A9%20Get%20in%20touch-hayattarique3%40gmail.com-EA4335?style=for-the-badge&labelColor=0d1117" alt="Email hayattarique3@gmail.com" />
  </a>
</p>
