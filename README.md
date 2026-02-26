# Microservice 4 – Add / Edit / Remove Personal Information and Activity

## Overview

This microservice provides a **REST API** for adding, editing, and removing personal information and activity records for a user in the application.

Other services (such as the main Dashboard or other microservices) can call this microservice to:

- **ADD** new records 
- **EDIT** previously saved records
- **REMOVE** records that are no longer needed

All operations require a valid authenticated user and enforce that users can only modify their **own** records.

This README defines the **communication contract** for this microservice.  
Once defined, it should **not be changed**, so that all teammates can reliably call it.

---

## Technology

- Architecture style: **REST API**
- Transport: HTTP
- Data format: **JSON** for both requests and responses
- Example local base URL (for development):

```text
http://localhost:5004
