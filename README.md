# Flask and Dapr.io Integration Project

---

sample dockerized flask project that integrated with dapr.io

run the dapr with makefile

## Resource

---

* [dapr conv](https://www.youtube.com/watch?v=AAQSShtl9S0&t=640s)
* [Dapr .NET microservice books](https://dotnet.microsoft.com/en-us/download/e-book/dapr/pdf)
* [Dapr Introduction](https://www.youtube.com/watch?v=-HVWs_3mS6A)


## Documentation

this project will run in dapr.io make sure the dapr is installed

* [Getting Started with dapr](https://docs.dapr.io/getting-started/)
* [Install Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)

---
### How to run this project?

make sure `make` and `dapr CLI` is installed on your computer

```sh
dapr init
```

| **Command**           | **Description**                                                |
|-----------------------|----------------------------------------------------------------|
| `make dapr-run`       | run flask project then integrate with dapr.io run on port 5000 |
| `make dapr-dashboard` | running dapr.io dashboard on port 8080                         |

