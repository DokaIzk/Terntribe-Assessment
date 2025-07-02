# 📦 Social Causes API

This is a RESTful API built with Django and Django REST Framework to manage social causes and user contributions. The API supports full CRUD operations for causes and allows users to contribute to a specific cause by submitting their name, email, and amount.

---

## 🚀 Features

- **CRUD operations for causes**
- **Contribute to a specific cause**
- **Nested cause details in contribution responses**
- **Amount validation to ensure positive contributions**

---

## 🛠️ Models

The project uses two core models:

1. **Cause**
   - `title`: Title of the cause
   - `description`: Description of the cause
   - `image_url`: URL to the cause's image/banner

2. **Contribution**
   - `name`: Name of the contributor
   - `email`: Email of the contributor
   - `amount`: Amount contributed
   - `cause`: Foreign key linking the contribution to a specific cause

This relational structure provides a clear and scalable way to manage contributions linked to their respective causes.

---

## 📝 Serializers

- **CauseSerializer** exposes all fields of the Cause model using `ModelSerializer`.
  
- **ContributionSerializer** includes:
  - A nested read-only `CauseSerializer` to provide full cause details in responses.
  - An overridden `create()` method to associate the contribution with the correct cause ID from the URL context.
  - A `validate_amount()` method to ensure contribution amounts are greater than zero.

All business logic related to contributions is handled within the serializer, maintaining clean views and focused responsibilities.

---

## 👨‍💻 Views

Both **CauseViewSet** and **ContributionViewSet** inherit from `ModelViewSet` for full CRUD functionality. 

In `ContributionViewSet`, `get_serializer_context()` is overridden to pass the `cause_id` from the URL to the serializer. This ensures contributions are created for the correct cause without requiring the client to pass the cause ID in the request body.

---

## 🌐 URLs

The API endpoints are structured as follows:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET, POST | `/causes/` | List and create causes |
| GET, PATCH, DELETE | `/causes/<id>/` | Retrieve, update, or delete a specific cause |
| POST | `/causes/<id>/contribute/` | Create a contribution for a specific cause |

Manual URL paths were used instead of DRF routers to maintain fine-grained control and clarity.

---

## 🎯 Design Decisions

- **Nested serialization** for contributions to provide detailed cause information in responses.
- **Serializer-based creation logic**, keeping views clean and responsibilities separated.
- **Validation** to ensure contribution amounts are positive.
- **Manual URL configuration** for clear, RESTful route definitions.

---

## ✅ Summary

This API implementation is clean, maintainable, and production-ready for managing social causes and their contributions. It ensures data integrity, delivers meaningful responses, and is structured for easy extension in real-world applications.

---

### 💡 Author

Designed and implemented by [Your Name].

---
