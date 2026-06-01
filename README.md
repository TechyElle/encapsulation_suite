# Encapsulation Suite

**Programming exercises implementing OOP principles with emphasis on encapsulation.**

## Assignment Requirements

- Complete programming exercises from module 6, pages 18-20
- Upload code to GitHub repository  
- Each program in its own folder
- **Git commit on every milestone** (grading requirement)
- Code must follow OOP principles with encapsulation implementation
- Create a demo video
- Submit GitHub repo link and demo video link

---

## Coding Standards

### Style & Naming Conventions (PEP-8)

| Item | Convention | Example |
|------|-----------|---------|
| **Classes** | PascalCase | `AdditionOperation` |
| **Methods/Functions** | snake_case | `perform_operation()` |
| **Variables** | snake_case | `first_number` |
| **Files** | snake_case | `math_operation.py` |
| **Private Attributes** | Leading underscore | `_result` |

### Code Requirements

- Class-based (OOP integrated)
- Short, direct code
- No single-letter variables
- Lowercase variable names
- Minimal comments (only when WHY is non-obvious)
- Call `.close()` on file resources when applicable

---

## Architecture & OOP Principles

### Encapsulation Pattern

- Private attributes prefixed with `_` (e.g., `_result`, `_error_message`)
- Abstract base classes for operation contracts
- Specific exception classes for error handling

### Key Patterns

1. **Abstraction**: Base ABC with abstract methods
2. **Encapsulation**: Private attributes hidden from external access
3. **Inheritance**: Operations inherit from base class
4. **Polymorphism**: Different operations implement `calculate()` differently

### Exception Handling

- Use **specific exceptions** (e.g., `ZeroDivisionError`) over generic `Exception`
- Validate input with `try-except ValueError` when converting to floats
- Create **custom exceptions** for domain-specific errors
- Use `try-except-else-finally` blocks for resource management

---

## Git Workflow & Milestones

### Committing (Grading Requirement)

Commit after **each milestone** with small, descriptive commits (not one final commit).

**Suggested Workflow:**

1. Make one logical change (create one module/class or one method)
2. Verify it runs (quick manual check)
3. Stage relevant files: `git add <changed_files>`
4. Commit with descriptive message:
   - `docs: ...` | `feat: ...` | `fix: ...` | `refactor: ...` | `chore: ...`
5. Repeat until complete

**Result**: Milestone-focused commit history demonstrating incremental development.

---

## Project Structure

```
encapsulation_suite/
├── program_1/              # Each program in separate folder
│   ├── main.py
│   └── modules/
├── program_2/
│   ├── main.py
│   └── modules/
└── README.md               # This file
```

---

## Building & Running

1. **Analyze requirements** for each program
2. **Design classes** following OOP encapsulation principles  
3. **Implement operations** with proper exception handling
4. **Test thoroughly** with edge cases
5. **Create demo video** showing program execution

---

<div align="center">

⚠️ *For educational purposes only. Created for the PUP Object-Oriented Programming course.*

</div>
