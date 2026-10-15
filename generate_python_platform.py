#!/usr/bin/env python3
"""
MS Applied Programming (Python) - Master Platform Generator
Generates the complete 15-week, 30-lesson interactive learning platform with:
- Master's-level CPython internals & systems programming prose (1,500-3,000+ words/lesson)
- Formal mathematical foundations & LaTeX proofs
- Mermaid.js runtime diagrams & mindmaps
- Production-grade Python implementations
- 4-Step Hands-On Engineering Labs & Benchmarks in every lesson
- Interactive Python playground, complexity visualizer, search index, and glossary
"""

import json
import os
import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\fayaz.hussain\.gemini\antigravity\scratch\applied-python-platform")

# Complete 15-Week Syllabus Matrix
WEEKS = [
    {
        "num": 1,
        "slug": "week-01",
        "title": "Foundations & Environment",
        "desc": "CPython runtime architecture, virtual environments, execution models, memory primitives, and basic operators.",
        "lessons": [
            {
                "num": "1.1",
                "slug": "course-intro-setup-and-python-basics",
                "title": "Course Intro, Setup, and Python Basics",
                "focus": "CPython virtual runtime, venv, REPL vs scripts, Jupyter kernel IPC, PyObject struct, reference counting, and PEP 8.",
                "duration": "90 min",
                "difficulty": "Foundational"
            },
            {
                "num": "1.2",
                "slug": "operators-io-and-type-conversion",
                "title": "Operators, I/O, and Type Conversion",
                "focus": "Arithmetic/logical/bitwise AST operators, operator precedence, standard I/O streams, explicit type casting, and f-string format specifiers.",
                "duration": "90 min",
                "difficulty": "Foundational"
            }
        ]
    },
    {
        "num": 2,
        "slug": "week-02",
        "title": "Control Flow",
        "desc": "Conditionals, branch prediction bytecode, boolean logic, iteration protocols, and loop optimization.",
        "lessons": [
            {
                "num": "2.1",
                "slug": "conditionals-and-boolean-logic",
                "title": "Conditionals & Boolean Logic",
                "focus": "Short-circuit evaluation, truthy/falsy dunder methods (__bool__, __len__), jump bytecode, and rule-based pattern matching.",
                "duration": "90 min",
                "difficulty": "Foundational"
            },
            {
                "num": "2.2",
                "slug": "loops-and-iteration-mechanics",
                "title": "Loops & Iteration Mechanics",
                "focus": "for/while bytecode mechanics, loop else semantics, iterator protocol (iter, next), loop unrolling, and prime sieves.",
                "duration": "105 min",
                "difficulty": "Foundational"
            }
        ]
    },
    {
        "num": 3,
        "slug": "week-03",
        "title": "Functions & Modular Design",
        "desc": "Execution frames, parameter binding, LEGB scope resolution, closures, recursion limits, and functional pipelines.",
        "lessons": [
            {
                "num": "3.1",
                "slug": "functions-and-execution-scopes",
                "title": "Functions & Execution Scopes",
                "focus": "Positional-only/keyword-only arguments, variadic unpacking (*args, **kwargs), PyFrameObject stack frames, closures, and docstrings.",
                "duration": "100 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "3.2",
                "slug": "recursion-and-functional-tools",
                "title": "Recursion & Functional Tools",
                "focus": "Call stack frames, recursion depth limits, memoization (lru_cache), lambda, map/filter/reduce, and lazy generators.",
                "duration": "110 min",
                "difficulty": "Intermediate"
            }
        ]
    },
    {
        "num": 4,
        "slug": "week-04",
        "title": "Data Structures I: Sequences",
        "desc": "Memory layouts of contiguous sequences, string interning, slicing mechanics, regex automata, and dynamic array resizing.",
        "lessons": [
            {
                "num": "4.1",
                "slug": "strings-and-text-processing",
                "title": "Strings & Text Processing",
                "focus": "Unicode representations (PyASCIIObject, PyCompactUnicodeObject), string interning, zero-copy slicing, and regex DFA/NFA engines.",
                "duration": "105 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "4.2",
                "slug": "lists-and-tuples",
                "title": "Lists & Tuples",
                "focus": "Dynamic array over-allocation growth formula, pointer arrays, tuple immutability optimizations, matrix linear algebra, and comprehension bytecode.",
                "duration": "105 min",
                "difficulty": "Intermediate"
            }
        ]
    },
    {
        "num": 5,
        "slug": "week-05",
        "title": "Data Structures II: Mappings & Sets",
        "desc": "Hash tables, compact dictionary memory layout, open addressing collision resolution, set algebra, and the collections module.",
        "lessons": [
            {
                "num": "5.1",
                "slug": "dictionaries-and-hash-tables",
                "title": "Dictionaries & Hash Tables",
                "focus": "CPython compact dict architecture (indices array + entries array), perturbation hash probe sequence, collision resolution, and dict comprehensions.",
                "duration": "110 min",
                "difficulty": "Advanced"
            },
            {
                "num": "5.2",
                "slug": "sets-and-collections-module",
                "title": "Sets & collections Module",
                "focus": "Set hash table mechanics, bitwise set algebra, Counter, defaultdict, namedtuple, deque double-ended ring buffers, and graph adjacency structures.",
                "duration": "100 min",
                "difficulty": "Intermediate"
            }
        ]
    },
    {
        "num": 6,
        "slug": "week-06",
        "title": "Object-Oriented Programming I",
        "desc": "Object models, instance vs class namespaces, method descriptor binding, encapsulation, and C3 Linearization MRO.",
        "lessons": [
            {
                "num": "6.1",
                "slug": "classes-and-objects-internals",
                "title": "Classes & Objects Internals",
                "focus": "PyTypeObject, __init__ vs __new__, instance dict vs __slots__, method binding, name mangling, and transactional encapsulation.",
                "duration": "110 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "6.2",
                "slug": "inheritance-mro-and-polymorphism",
                "title": "Inheritance, MRO, and Polymorphism",
                "focus": "Multiple inheritance, C3 Linearization algorithm, super() cooperative dispatch, Abstract Base Classes (abc.ABC), and polymorphic Shape hierarchies.",
                "duration": "115 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 7,
        "slug": "week-07",
        "title": "OOP II & Design Patterns",
        "desc": "Data model dunder protocols, operator overloading, composition, and Pythonic enterprise design patterns.",
        "lessons": [
            {
                "num": "7.1",
                "slug": "dunder-methods-and-composition",
                "title": "Dunder Methods & Composition",
                "focus": "Python Data Model protocols (__add__, __getitem__, __enter__, __repr__), custom numeric types (Vector/Matrix), and composition over inheritance.",
                "duration": "110 min",
                "difficulty": "Advanced"
            },
            {
                "num": "7.2",
                "slug": "design-patterns-in-python",
                "title": "Design Patterns in Python",
                "focus": "Pythonic Singleton, Factory, Strategy, Observer, and Decorator implementations; decoupling event buses and subscriber dispatchers.",
                "duration": "115 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 8,
        "slug": "week-08",
        "title": "Midterm Checkpoint",
        "desc": "Practical systems assessment, timed OOP architecture challenge, Cyclomatic complexity analysis, and peer code refactoring.",
        "lessons": [
            {
                "num": "8.1",
                "slug": "midterm-project-and-practical-assessment",
                "title": "Midterm Project & Practical Assessment",
                "focus": "Timed hands-on engineering exam: designing and implementing an end-to-end transactional OOP order fulfillment system under strict memory & SLA bounds.",
                "duration": "150 min",
                "difficulty": "Advanced"
            },
            {
                "num": "8.2",
                "slug": "peer-code-review-and-refactoring",
                "title": "Peer Code-Review & Refactoring",
                "focus": "Code review rubrics, Cyclomatic Complexity metrics, AST linting, PEP 8 enforcement, and architectural decoupling.",
                "duration": "90 min",
                "difficulty": "Intermediate"
            }
        ]
    },
    {
        "num": 9,
        "slug": "week-09",
        "title": "Error Handling, Testing & Debugging",
        "desc": "Exception unwinding, defensive programming, pytest test suites, fixtures, mocking, and debugging with pdb/logging.",
        "lessons": [
            {
                "num": "9.1",
                "slug": "exceptions-and-defensive-programming",
                "title": "Exceptions & Defensive Programming",
                "focus": "CPython exception stack unwinding, custom domain exceptions, exception chaining (from), context managers, and robust ETL parsers.",
                "duration": "100 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "9.2",
                "slug": "testing-and-debugging-ecosystem",
                "title": "Testing & Debugging Ecosystem",
                "focus": "pytest framework, parameterized fixtures, monkeypatching with unittest.mock, interactive pdb debugging, and structured logging.",
                "duration": "115 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 10,
        "slug": "week-10",
        "title": "File I/O, Data Formats & Persistence",
        "desc": "Operating system file descriptors, buffer streaming, CSV/JSON/XML parsing, SQLite persistence, and SQLAlchemy ORM.",
        "lessons": [
            {
                "num": "10.1",
                "slug": "file-io-and-structured-data",
                "title": "File I/O & Structured Data",
                "focus": "OS page cache, buffered I/O streams, streaming multi-gigabyte CSV/JSON payloads, XML DOM/SAX parsers, and schema validation.",
                "duration": "105 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "10.2",
                "slug": "databases-and-orm",
                "title": "Databases & ORM",
                "focus": "SQLite engine, parameterized queries against SQL injection, ACID transactions (commit/rollback), and SQLAlchemy ORM declarative models.",
                "duration": "120 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 11,
        "slug": "week-11",
        "title": "Algorithms & Data Structures",
        "desc": "Asymptotic Big-O proofs, sorting/searching benchmarks, custom linked lists, binary search trees, and hash tables from scratch.",
        "lessons": [
            {
                "num": "11.1",
                "slug": "complexity-and-sorting-searching",
                "title": "Complexity & Sorting/Searching",
                "focus": "Formal Big-O, Omega, and Theta asymptotic bounds, Binary Search, MergeSort, QuickSort, and empirical benchmarking against Timsort.",
                "duration": "120 min",
                "difficulty": "Advanced"
            },
            {
                "num": "11.2",
                "slug": "core-data-structures-from-scratch",
                "title": "Core Data Structures from Scratch",
                "focus": "Implementing Stacks, Queues, Doubly Linked Lists, Binary Search Trees with tree rotations, and Hash Tables with collision chaining.",
                "duration": "130 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 12,
        "slug": "week-12",
        "title": "Concurrency & Performance",
        "desc": "OS threading vs multiprocessing, Global Interpreter Lock (GIL) internals, asyncio event loops, and profiling with cProfile/NumPy.",
        "lessons": [
            {
                "num": "12.1",
                "slug": "concurrency-threading-multiprocessing-asyncio",
                "title": "Concurrency: Threads, Processes, Asyncio",
                "focus": "CPython GIL execution model, CPU-bound multiprocessing IPC, I/O-bound asyncio event loops, coroutines, and task groups.",
                "duration": "130 min",
                "difficulty": "Advanced"
            },
            {
                "num": "12.2",
                "slug": "performance-profiling-and-optimization",
                "title": "Performance Profiling & Optimization",
                "focus": "Deterministic profiling with cProfile/pstats, tracemalloc heap tracking, __slots__ memory reduction, and SIMD vectorization with NumPy.",
                "duration": "120 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 13,
        "slug": "week-13",
        "title": "Applied Python: Data & APIs",
        "desc": "NumPy arrays, Pandas DataFrames, exploratory data analysis, REST API consumption, and high-throughput FastAPI web services.",
        "lessons": [
            {
                "num": "13.1",
                "slug": "data-analysis-stack-numpy-pandas-matplotlib",
                "title": "Data Analysis Stack: NumPy, Pandas, Matplotlib",
                "focus": "N-dimensional array striding, Pandas columnar indexes, groupby aggregations, vector transformations, and statistical data visualization.",
                "duration": "120 min",
                "difficulty": "Advanced"
            },
            {
                "num": "13.2",
                "slug": "apis-and-web-services",
                "title": "APIs & Web Services",
                "focus": "Consuming REST APIs with httpx/requests, rate limiting, connection pooling, and building high-performance async REST services with FastAPI.",
                "duration": "120 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 14,
        "slug": "week-14",
        "title": "Professional Software Engineering Practices",
        "desc": "Git workflows, pyproject.toml packaging, static type checking (mypy/ruff), Docker containerization, and GitHub Actions CI/CD.",
        "lessons": [
            {
                "num": "14.1",
                "slug": "version-control-linters-and-packaging",
                "title": "Version Control, Linters & Packaging",
                "focus": "Git branching strategies, pyproject.toml builds (Hatch/Flit), PEP 517/518, static type checking with mypy, and linting with Ruff.",
                "duration": "110 min",
                "difficulty": "Intermediate"
            },
            {
                "num": "14.2",
                "slug": "ci-cd-and-containers",
                "title": "CI/CD & Containerization",
                "focus": "Automated testing pipelines with GitHub Actions, multi-stage Dockerfiles for Python apps, minimal runtime images, and health checks.",
                "duration": "115 min",
                "difficulty": "Advanced"
            }
        ]
    },
    {
        "num": 15,
        "slug": "week-15",
        "title": "Capstone Project & Wrap-Up",
        "desc": "End-to-end applied software architecture, peer review rubrics, capstone defense, and transition to systems programming & ML engineering.",
        "lessons": [
            {
                "num": "15.1",
                "slug": "capstone-build-session-and-architectural-review",
                "title": "Capstone Build Session & Architectural Review",
                "focus": "End-to-end integration of OOP, automated test coverage (90%+), persistent storage, and applied REST/Data pipeline components with architectural review.",
                "duration": "150 min",
                "difficulty": "Advanced"
            },
            {
                "num": "15.2",
                "slug": "final-capstone-defense-and-career-roadmap",
                "title": "Final Capstone Defense & Career Roadmap",
                "focus": "Engineering defense presentations, production readiness checklists, and bridging Python mastery to Distributed Systems, ML Engineering, and PyO3/Rust.",
                "duration": "120 min",
                "difficulty": "Advanced"
            }
        ]
    }
]

# Flatten all lessons
ALL_LESSONS = []
for w in WEEKS:
    for l in w["lessons"]:
        ALL_LESSONS.append({
            "week_num": w["num"],
            "week_title": w["title"],
            "week_slug": w["slug"],
            "num": l["num"],
            "slug": l["slug"],
            "title": l["title"],
            "focus": l["focus"],
            "duration": l["duration"],
            "difficulty": l["difficulty"]
        })

# Glossary Database
GLOSSARY = [
    {"term": "CPython", "category": "Runtime", "def": "The standard, reference C-based implementation of the Python programming language that compiles Python source code into bytecode and executes it via a stack-based virtual machine."},
    {"term": "PyObject", "category": "Memory", "def": "The foundational C struct in CPython from which all Python objects inherit, containing the reference count (ob_refcnt) and the object type pointer (ob_type)."},
    {"term": "Global Interpreter Lock (GIL)", "category": "Concurrency", "def": "A mutual-exclusion lock used by CPython to ensure only one OS thread executes Python bytecode at any given moment, preventing race conditions on memory reference counts."},
    {"term": "Method Resolution Order (MRO)", "category": "OOP", "def": "The deterministic algorithmic order (computed via C3 Linearization) in which Python searches for method implementations across complex multiple inheritance class hierarchies."},
    {"term": "Abstract Base Class (ABC)", "category": "OOP", "def": "A class defined via the abc module that enforces interface contracts by prohibiting instantiation of subclasses unless all @abstractmethod declarations are overridden."},
    {"term": "Dunder Methods", "category": "Data Model", "def": "Special 'double underscore' methods (e.g. __init__, __getitem__, __call__) that bind user-defined classes into Python's built-in syntax, operators, and protocols."},
    {"term": "Dynamic Array Over-Allocation", "category": "Algorithms", "def": "The growth strategy used by Python's list where extra capacity is pre-allocated proportionally during appends to achieve amortized O(1) insertion time."},
    {"term": "Hash Table Perturbation", "category": "Data Structures", "def": "The collision resolution algorithm in CPython dicts that incorporates high-order bits of the hash code to break cyclic probing patterns in open addressing."},
    {"term": "Call Stack Frame (PyFrameObject)", "category": "Runtime", "def": "The heap-allocated C struct representing a function execution scope, storing local variables, the evaluation value stack, instruction pointer, and globals dict."},
    {"term": "Asyncio Event Loop", "category": "Concurrency", "def": "A single-threaded reactive scheduler that manages and dispatches asynchronous tasks and I/O callbacks via non-blocking OS multiplexers (epoll/kqueue)."},
    {"term": "Descriptor Protocol", "category": "Metaprogramming", "def": "An object attribute protocol implementing __get__, __set__, or __delete__, providing the underlying engine for properties, classmethods, and ORM fields."},
    {"term": "Timsort", "category": "Algorithms", "def": "A hybrid adaptive sorting algorithm combining MergeSort and InsertionSort designed by Tim Peters, providing O(N) best-case and O(N log N) worst-case time complexity."},
    {"term": "Context Manager", "category": "Control Flow", "def": "An object adhering to the runtime context protocol (__enter__ and __exit__) utilized within 'with' statements to guarantee deterministic resource cleanup."},
    {"term": "Cyclomatic Complexity", "category": "Software Eng", "def": "A software metric indicating the number of linearly independent execution paths through source code, calculated as M = E - N + 2P."},
    {"term": "SIMD Vectorization", "category": "Performance", "def": "Single Instruction Multiple Data: hardware CPU instructions utilized by NumPy to perform parallel arithmetic operations across contiguous memory buffers in C."}
]


def get_graduate_python_content(lesson):
    """
    Returns deep graduate-level theoretical prose, formal mathematical derivations,
    production code implementations, and 4-step hands-on engineering lab drills.
    """
    w = lesson["week_num"]
    title = lesson["title"]
    num = lesson["num"]

    if w in (1, 2):
        sec4 = r"""
          <h3>4.1 CPython Virtual Machine Architecture & The PyObject Model</h3>
          <p>Python is an interpreted, bytecode-compiled, dynamically typed language. When a Python source file (<code>.py</code>) is invoked, the CPython interpreter executes a multi-stage compilation pipeline: Lexical Analysis $\to$ Abstract Syntax Tree (AST) Generation $\to$ Control Flow Graph Construction $\to$ Bytecode Generation (<code>.pyc</code> cache).</p>
          <p>At the C systems layer, every entity in Python—from small integers and booleans to complex classes and functions—is represented by a heap-allocated C struct known as <code>PyObject</code>:</p>
          <pre><code class="language-c">// CPython Include/object.h
typedef struct _object {{
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;          // 64-bit reference counter
    struct _typeobject *ob_type;   // Pointer to class type metadata
}} PyObject;</code></pre>
          <p>Because every variable binding is a pointer to a <code>PyObject</code>, integer arithmetic incurs pointer indirection overhead compared to native C integers ($32$ or $64$ bits directly in CPU registers). Variable assignment in Python does not duplicate memory; it increments the object's reference counter (<code>ob_refcnt</code>) and associates a symbol table name with the memory address.</p>

          <h3>4.2 Operator Bytecode Evaluation & Short-Circuit Branching</h3>
          <p>Python evaluates operators using a stack-based virtual machine. When expressions such as <code>a + b * c</code> or <code>x and y</code> are parsed, the compiler generates sequential evaluation opcodes (e.g. <code>BINARY_OP</code>, <code>COMPARE_OP</code>, <code>POP_JUMP_IF_FALSE</code>).</p>
          <p>Logical operators in Python (<code>and</code>, <code>or</code>) utilize <strong>short-circuit evaluation</strong>. Rather than returning pure boolean flags, they return the actual operand that satisfied or broke the evaluation condition, allowing concise idiomatic fallback patterns (e.g., <code>user_val or default_val</code>).</p>

          <h3>4.3 The Iterator Protocol & Memory Complexity</h3>
          <p>Looping in Python does not rely on index counters. Instead, the <code>for</code> statement consumes the <strong>Iterator Protocol</strong>: calling <code>iter(iterable)</code> to obtain an iterator object implementing <code>__next__()</code>. Iteration terminates cleanly when the object raises a <code>StopIteration</code> exception. This enables $\mathcal{{O}}(1)$ constant memory overhead during large dataset streams compared to $\mathcal{{O}}(N)$ memory consumption when loading full arrays into RAM.</p>
        """
        math_block = r"""
          <p><strong>Memory Footprint & Asymptotic Loop Iteration Complexity:</strong></p>
          <p>Let $N$ represent the number of numerical records processed in a stream. The memory allocation cost $M(N)$ for an eagerly evaluated list versus a lazy iterator is formulated as:</p>
          $$M_{\text{list}}(N) = \mathcal{O}(N) \cdot S_{\text{PyObject}} \quad \text{vs.} \quad M_{\text{iterator}}(N) = \mathcal{O}(1)$$
          <p>Where $S_{\text{PyObject}} \approx 28\text{ bytes}$ for a 64-bit integer object on CPython. For $N = 10{,}000{,}000$ records:</p>
          $$\text{List Allocation} = 10^7 \times 28\text{ bytes} \approx 280\text{ MB RAM}$$
          $$\text{Iterator Allocation} = 1 \times 28\text{ bytes} \approx 28\text{ bytes RAM}$$
          <p>Achieving a $10{,}000{,}000\times$ reduction in peak memory consumption.</p>
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
CPython Bytecode Disassembly & High-Precision Temperature Conversion Module:
Demonstrates AST evaluation, type annotations, and custom exception handling.
\"\"\"
import dis
import sys

class TemperatureConversionError(Exception):
    \"\"\"Custom domain exception for invalid physical temperatures.\"\"\"
    pass

def celsius_to_fahrenheit(celsius: float) -> float:
    \"\"\"
    Converts Celsius to Fahrenheit with thermodynamic absolute zero validation.
    Formula: F = (C * 9/5) + 32
    \"\"\"
    if celsius < -273.15:
        raise TemperatureConversionError(f"Temperature {celsius}C is below absolute zero (-273.15C).")
    return (celsius * 9.0 / 5.0) + 32.0

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    \"\"\"
    Converts Fahrenheit to Celsius with thermodynamic absolute zero validation.
    Formula: C = (F - 32) * 5/9
    \"\"\"
    if fahrenheit < -459.67:
        raise TemperatureConversionError(f"Temperature {fahrenheit}F is below absolute zero (-459.67F).")
    return (fahrenheit - 32.0) * 5.0 / 9.0

if __name__ == "__main__":
    test_temps_c = [0.0, 21.5, 100.0, -40.0]
    print("--- Temperature Conversion Suite ---")
    for c in test_temps_c:
        f = celsius_to_fahrenheit(c)
        c_back = fahrenheit_to_celsius(f)
        print(f"{c:6.2f}°C  -->  {f:6.2f}°F  -->  {c_back:6.2f}°C (Verified: {abs(c - c_back) < 1e-9})")
    
    print("\n--- Disassembled CPython Bytecode ---")
    dis.dis(celsius_to_fahrenheit)"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build a high-precision, interactive CLI financial splitting & BMI diagnostic engine in Python 3.13, enforcing defensive input validation, type casting, mathematical bounds checking, and formatted output reporting.</p>

          <h4>Step 1: Financial Split & BMI Diagnostic Implementation</h4>
          <pre><code class="language-python"># financial_and_health_cli.py
from typing import Tuple, List, Dict
import math

def calculate_bmi(weight_kg: float, height_m: float) -> Tuple[float, str]:
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be strictly positive numeric values.")
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal Weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

def split_bill_with_tip(subtotal: float, tip_percent: float, num_people: int) -> Dict[str, float]:
    if subtotal < 0 or tip_percent < 0 or num_people <= 0:
        raise ValueError("Invalid bill parameters. Ensure subtotal >= 0, tip >= 0, and people >= 1.")
    
    tip_amount = subtotal * (tip_percent / 100.0)
    total_bill = subtotal + tip_amount
    per_person = math.ceil((total_bill / num_people) * 100) / 100.0  # Round up to prevent penny deficit
    
    return {{
        "subtotal": round(subtotal, 2),
        "tip_amount": round(tip_amount, 2),
        "total_bill": round(total_bill, 2),
        "per_person": per_person,
        "num_people": num_people
    }}

if __name__ == "__main__":
    print("=== Health Diagnostic Run ===")
    bmi_val, cat = calculate_bmi(weight_kg=78.5, height_m=1.82)
    print(f"Computed BMI: {{bmi_val}} | Category: {{cat}}")

    print("\n=== Expense Split Run ===")
    summary = split_bill_with_tip(subtotal=245.50, tip_percent=18.0, num_people=4)
    for k, v in summary.items():
        print(f"  {{k.replace('_', ' ').capitalize():15}}: ${{v:,.2f}}" if isinstance(v, float) else f"  {{k:15}}: {{v}}")</code></pre>

          <h4>Step 2: Execution & Output Verification</h4>
          <pre><code class="language-bash">python financial_and_health_cli.py</code></pre>
          <p>Expected stdout output:</p>
          <pre><code>=== Health Diagnostic Run ===
Computed BMI: 23.7 | Category: Normal Weight

=== Expense Split Run ===
  Subtotal       : $245.50
  Tip amount     : $44.19
  Total bill     : $289.69
  Per person     : $72.43
  num_people     : 4</code></pre>

          <h4>Step 3: Edge Case & Exception Validation</h4>
          <pre><code class="language-python"># test_edge_cases.py
import pytest
from financial_and_health_cli import calculate_bmi, split_bill_with_tip

def test_invalid_bmi_inputs():
    with pytest.raises(ValueError):
        calculate_bmi(-50.0, 1.75)
    with pytest.raises(ValueError):
        calculate_bmi(70.0, 0.0)

def test_split_bill_math():
    res = split_bill_with_tip(100.0, 20.0, 3)
    assert res["total_bill"] == 120.0
    assert res["per_person"] * 3 >= 120.0  # Zero-deficit guarantee</code></pre>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement an algorithmic Sieve of Eratosthenes generator in Python that computes all prime numbers up to $N = 1{,}000{,}000$ in $\mathcal{{O}}(N \log \log N)$ time using a pre-allocated bytearray buffer.</p>
        """
        mermaid_diag = """flowchart TD
  Source[Python Source Code .py] --> Lex[Lexer & Tokenizer]
  Lex --> Parser[AST Abstract Syntax Tree]
  Parser --> CFG[Control Flow Graph Optimizer]
  CFG --> Bytecode[CPython Bytecode .pyc]
  Bytecode --> EvalLoop[Evaluation Loop: _PyEval_EvalFrameDefault]
  EvalLoop --> PyObj[(Heap: PyObject Structs & Memory Arena)]"""
    elif w in (3, 4):
        sec4 = r"""
          <h3>4.1 Call Stack Frames, Closures & LEGB Scope Resolution</h3>
          <p>In CPython, every function call dynamically allocates a <code>PyFrameObject</code> on the heap rather than using the native C machine stack. This execution frame encapsulates:</p>
          <ul>
            <li><code>f_localsplus</code>: Fast array of local variable pointers indexed by integer opcodes (<code>LOAD_FAST</code>, <code>STORE_FAST</code>).</li>
            <li><code>f_globals</code>: Dictionary reference to the module's global symbol table.</li>
            <li><code>f_builtins</code>: Reference to the standard built-in namespace.</li>
            <li><code>f_valuestack</code>: The internal evaluation operand stack.</li>
          </ul>
          <p>Symbol resolution follows the strict <strong>LEGB Rule</strong> (Local $\to$ Enclosing $\to$ Global $\to$ Builtin). When nested functions reference variables in outer scopes, Python constructs a <strong>Closure</strong> by packing the variable into a <code>cell</code> object (<code>PyCellObject</code>), allowing the inner function to maintain references even after the outer frame has terminated.</p>

          <h3>4.2 Sequence Internals: Dynamic Arrays & Compact Strings</h3>
          <p>Python's sequence types exhibit distinct physical memory layouts:</p>
          <ul>
            <li><strong>Lists (<code>PyListObject</code>):</strong> Implemented as dynamic arrays of pointers to <code>PyObject</code>. To avoid allocating memory on every single append, CPython uses an over-allocation growth formula:
            $$\text{New Capacity} = \text{size} + (\text{size} \gg 3) + (\text{size} < 9 \ ? \ 3 : 6)$$
            This guarantees amortized $\mathcal{{O}}(1)$ append complexity.</li>
            <li><strong>Tuples (<code>PyTupleObject</code>):</strong> Immutable fixed-size pointer arrays. CPython caches small freed tuples in a local free list to eliminate <code>malloc()</code> syscall overhead.</li>
            <li><strong>Strings (<code>PyUnicodeObject</code> - PEP 393):</strong> Implemented with compact UTF representations (1-byte Latin-1, 2-byte UCS-2, or 4-byte UCS-4 depending on the maximum character ordinal), drastically reducing memory consumption for ASCII corpora.</li>
          </ul>
        """
        math_block = r"""
          <p><strong>List Over-Allocation & Amortized Insertion Proof:</strong></p>
          <p>Let $N$ sequential elements be appended to an initially empty Python list. Although individual resize operations incur $\mathcal{O}(K)$ array copy overhead, the total cost over $N$ appends satisfies:</p>
          $$\sum_{i=1}^N \text{Cost}(i) \le N + \sum_{k=1}^{\lceil \log_{1.125} N \rceil} 1.125^k \le C \cdot N$$
          <p>Dividing by $N$ operations yields an amortized time complexity of:</p>
          $$\text{Amortized Cost per Append} = \frac{\mathcal{O}(N)}{N} = \mathcal{O}(1)$$
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
Functional Sequence Processing & Matrix Algebra Engine:
Demonstrates memoized recursion, higher-order functions, and list comprehensions.
\"\"\"
import functools
import time
from typing import List, Callable, TypeVar

T = TypeVar('T')
Matrix = List[List[float]]

@functools.lru_cache(maxsize=256)
def memoized_fibonacci(n: int) -> int:
    \"\"\"Computes the n-th Fibonacci number in O(N) time and space via memoization.\"\"\"
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def matrix_transpose(m: Matrix) -> Matrix:
    \"\"\"Computes matrix transpose using nested list comprehensions.\"\"\"
    if not m or not m[0]:
        return []
    return [[m[row][col] for row in range(len(m))] for col in range(len(m[0]))]

def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    \"\"\"Performs O(M * K * N) matrix multiplication.\"\"\"
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError(f"Incompatible dimensions: ({rows_a}x{cols_a}) and ({rows_b}x{cols_b})")
    
    return [
        [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(rows_a)
    ]

if __name__ == "__main__":
    print("--- Memoized Fibonacci Output ---")
    for i in range(1, 11):
        print(f"Fib({i:2d}) = {memoized_fibonacci(i)}")
    print(f"Cache Statistics: {memoized_fibonacci.cache_info()}")

    mat_1 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    mat_2 = [[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]]
    prod = matrix_multiply(mat_1, mat_2)
    print("\n--- Matrix Multiplication Result ---")
    print(f"Product (2x3 @ 3x2 -> 2x2): {prod}")"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build an end-to-end text corpus token analyzer and regular expression validation engine, extracting word frequencies, evaluating text metrics, and validating structured inputs with zero-copy string operations.</p>

          <h4>Step 1: Text Corpus & Regex Processing Engine</h4>
          <pre><code class="language-python"># text_analyzer_and_validator.py
import re
from collections import Counter
from typing import Dict, List, Any

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PHONE_REGEX = re.compile(r"^\+?[1-9]\d{{1,14}}$") # E.164 standard format

def analyze_corpus(text: str) -> Dict[str, Any]:
    tokens = re.findall(r"\b[a-zA-Z]{{2,}}\b", text.lower())
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = Counter(tokens)
    
    return {{
        "total_word_count": total_words,
        "unique_word_count": unique_words,
        "lexical_diversity": round(unique_words / total_words, 4) if total_words > 0 else 0.0,
        "top_5_frequent": freq.most_common(5)
    }}

def validate_contact_records(records: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    results = []
    for rec in records:
        email_valid = bool(EMAIL_REGEX.match(rec.get("email", "")))
        phone_valid = bool(PHONE_REGEX.match(rec.get("phone", "")))
        results.append({{
            "name": rec.get("name"),
            "email_valid": email_valid,
            "phone_valid": phone_valid,
            "all_valid": email_valid and phone_valid
        }})
    return results

if __name__ == "__main__":
    sample_text = \"\"\"
    Python is an interpreted high-level general-purpose programming language.
    Python dynamic typing and garbage collection manage memory automatically.
    Python design philosophy emphasizes code readability with significant indentation.
    \"\"\"
    print("=== Corpus Analysis Metrics ===")
    stats = analyze_corpus(sample_text)
    for k, v in stats.items():
        print(f"  {{k:20}}: {{v}}")

    test_contacts = [
        {{"name": "Alice Smith", "email": "alice@cs.stanford.edu", "phone": "+14155552671"}},
        {{"name": "Bob Jones", "email": "bob-invalid-email", "phone": "12345"}}
    ]
    print("\n=== Validation Results ===")
    for res in validate_contact_records(test_contacts):
        print(f"  {{res['name']:15}} -> Valid: {{res['all_valid']}} (Email: {{res['email_valid']}}, Phone: {{res['phone_valid']}})")</code></pre>

          <h4>Step 2: Verification Run</h4>
          <pre><code class="language-bash">python text_analyzer_and_validator.py</code></pre>

          <h4>Step 3: Unit Testing Validation</h4>
          <pre><code class="language-python"># test_text_engine.py
from text_analyzer_and_validator import analyze_corpus, EMAIL_REGEX

def test_corpus_frequency():
    out = analyze_corpus("apple banana apple orange apple")
    assert out["total_word_count"] == 5
    assert out["unique_word_count"] == 3
    assert out["top_5_frequent"][0] == ("apple", 3)

def test_email_regex():
    assert EMAIL_REGEX.match("valid.user+test@domain.co.uk")
    assert not EMAIL_REGEX.match("@missing-username.com")</code></pre>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement a Recursive Descent Parser in Python that parses and evaluates arithmetic string expressions containing addition, subtraction, multiplication, division, and parentheses (e.g. <code>"(12 + 4) * 3 - 8 / 2"</code>) without using <code>eval()</code>.</p>
        """
        mermaid_diag = """flowchart TD
  Caller[Caller Function] --> Alloc[Heap Frame Allocation: PyFrameObject]
  Alloc --> Scope[LEGB Scope Binding]
  Scope --> Locals[f_localsplus: Fast Local Array]
  Scope --> Globals[f_globals: Module Namespace Dict]
  Scope --> Cell[PyCellObject: Closure Enclosed Scope]
  Locals --> FastBytecode[LOAD_FAST / STORE_FAST O(1)]"""
    elif w in (5, 6):
        sec4 = r"""
          <h3>5.1 CPython Compact Dictionary & Open Addressing Hash Tables</h3>
          <p>Prior to Python 3.6, dictionaries stored a sparse array of 24-byte hash table entries, wasting up to $60\%$ of memory space in empty hash buckets. Modern CPython implements the <strong>Compact Dict Architecture</strong> (designed by Raymond Hettinger and Inada Naoki):</p>
          <pre><code class="language-text"># Compact Dictionary Memory Layout:
indices:  [ -1,  0, -1,  1, -1, -1,  2, -1 ]  # Compact 1-byte integer hash bucket index table
entries:  [
    {"hash": 0x12a4, "key": "name", "value": "Alice"},
    {"hash": 0x89b1, "key": "role", "value": "Admin"},
    {"hash": 0x4f2c, "key": "dept", "value": "Eng"}
] # Dense contiguous array storing entries in exact insertion order</code></pre>
          <p>Collision resolution is performed via <strong>Perturbation Probing</strong>:</p>
          $$i = (5 \times i + 1 + \text{perturb}) \pmod{\text{size}}$$
          <p>Where <code>perturb</code> starts as the object's 64-bit hash code and shifts right by 5 bits on each probe iteration (<code>perturb >>= 5</code>). This guarantees high entropy distribution across bucket indices and eliminates clustering.</p>

          <h3>6.1 The Object Model, Metaclasses & C3 Linearization MRO</h3>
          <p>Classes in Python are first-class runtime objects instances of <code>type</code> (<code>PyTypeObject</code>). When a class is defined, Python coordinates object construction through two distinct dunder methods:</p>
          <ol>
            <li><code>__new__(cls, *args, **kwargs)</code>: Static constructor method responsible for physical memory allocation and returning the raw <code>PyObject</code> instance.</li>
            <li><code>__init__(self, *args, **kwargs)</code>: Instance initializer that configures attributes on the instantiated object.</li>
          </ol>
          <p>In multiple inheritance hierarchies, attribute and method resolution is resolved via <strong>C3 Linearization (MRO)</strong>, satisfying three formal mathematical properties: local precedence order, monotonic inheritance, and consistency with the extended precedence graph.</p>
        """
        math_block = r"""
          <p><strong>C3 Linearization Merge Formula for Method Resolution Order:</strong></p>
          <p>Let $C$ be a class inheriting from parent base classes $B_1, B_2, \dots, B_n$. The linear MRO list $L(C)$ is defined recursively as:</p>
          $$L(C) = [C] + \text{merge}(L(B_1), L(B_2), \dots, L(B_n), [B_1, B_2, \dots, B_n])$$
          <p>The <code>merge</code> function selects the first head element $H$ that does not appear in the tail of any other remaining list in the merge sequence, removes $H$ from all lists, and appends it to the output until all lists are exhausted.</p>
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
High-Performance Object-Oriented Polymorphic Domain Model:
Demonstrates __slots__, Abstract Base Classes, and MRO resolution.
\"\"\"
import abc
import math
from typing import List

class Shape(abc.ABC):
    \"\"\"Abstract Base Class enforcing polymorphic geometric contracts.\"\"\"
    
    @abc.abstractmethod
    def area(self) -> float:
        \"\"\"Compute mathematical surface area.\"\"\"
        pass

    @abc.abstractmethod
    def perimeter(self) -> float:
        \"\"\"Compute geometric perimeter boundary length.\"\"\"
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} Area={self.area():.2f} Perim={self.perimeter():.2f}>"

class Circle(Shape):
    __slots__ = ('_radius',) # Eliminates __dict__ overhead, saving 64% RAM per instance

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = radius

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    def perimeter(self) -> float:
        return 2.0 * math.pi * self._radius

class Rectangle(Shape):
    __slots__ = ('_width', '_height')

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive.")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2.0 * (self._width + self._height)

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=5.0),
        Rectangle(width=4.0, height=7.0),
        Circle(radius=2.5)
    ]
    print("--- Polymorphic Shape Evaluation ---")
    total_area = sum(s.area() for s in shapes)
    for s in shapes:
        print(f"  {s}")
    print(f"\nTotal Surface Area: {total_area:.2f} sq units")"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build a complete transactional banking system and library catalog in Python using OOP principles, encapsulation, custom dunder methods, and atomic balance safeguards.</p>

          <h4>Step 1: Transactional Banking Domain Model</h4>
          <pre><code class="language-python"># banking_and_library_system.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

class InsufficientFundsError(Exception):
    pass

@dataclass(frozen=True)
class TransactionRecord:
    timestamp: datetime
    tx_type: str
    amount: float
    resulting_balance: float

class BankAccount:
    def __init__(self, account_id: str, owner: str, initial_deposit: float = 0.0):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        self.account_id = account_id
        self.owner = owner
        self._balance = initial_deposit
        self._ledger: List[TransactionRecord] = []
        
        if initial_deposit > 0:
            self._ledger.append(TransactionRecord(datetime.now(), "DEPOSIT", initial_deposit, self._balance))

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive.")
        self._balance += amount
        self._ledger.append(TransactionRecord(datetime.now(), "DEPOSIT", amount, self._balance))

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be strictly positive.")
        if amount > self._balance:
            raise InsufficientFundsError(f"Cannot withdraw ${{amount:.2f}}. Current balance: ${{self._balance:.2f}}")
        self._balance -= amount
        self._ledger.append(TransactionRecord(datetime.now(), "WITHDRAWAL", amount, self._balance))

    def get_statement(self) -> List[TransactionRecord]:
        return list(self._ledger) # Return defensive copy

    def __repr__(self) -> str:
        return f"<BankAccount ID={{self.account_id}} Owner='{{self.owner}}' Balance=${{self._balance:.2f}}>"

if __name__ == "__main__":
    acc = BankAccount("ACC-9042", "Dr. Jane Doe", initial_deposit=1000.0)
    acc.deposit(500.0)
    acc.withdraw(250.0)
    print(acc)
    print("\n--- Ledger Audit Trail ---")
    for tx in acc.get_statement():
        print(f"  [{{tx.timestamp.strftime('%H:%M:%S')}}] {{tx.tx_type:10}}: ${{tx.amount:7.2f}} | Balance: ${{tx.resulting_balance:7.2f}}")</code></pre>

          <h4>Step 2: Verification Run</h4>
          <pre><code class="language-bash">python banking_and_library_system.py</code></pre>

          <h4>Step 3: Boundary & Exception Test Harness</h4>
          <pre><code class="language-python"># test_bank_account.py
import pytest
from banking_and_library_system import BankAccount, InsufficientFundsError

def test_atomic_withdraw_guard():
    acc = BankAccount("ACC-1", "Alice", 100.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(150.0)
    assert acc.balance == 100.0  # Balance must remain unchanged on failure</code></pre>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement a thread-safe <code>AccountManager</code> using Python's <code>threading.Lock</code> context manager to handle concurrent deposit and withdrawal requests across 50 simulated worker threads without race condition anomalies.</p>
        """
        mermaid_diag = """flowchart TD
  subgraph Compact_Dict [CPython 3.13 Compact Dict Layout]
    Indices["Hash Indices Array: [-1, 0, -1, 1, -1, 2]"]
    Entries["Dense Entries Array: [{hash, key, val}, {hash, key, val}]"]
    Indices -->|Perturbation Probe Index| Entries
  end
  subgraph Class_Model [Object Metaclass Hierarchy]
    Type[type: PyTypeObject] --> Class[Custom Class]
    Class --> Inst1[Instance 1: __slots__ Pointers]
    Class --> Inst2[Instance 2: __slots__ Pointers]
  end"""
    elif w in (7, 8):
        sec4 = r"""
          <h3>7.1 The Python Data Model & Dunder Protocol Mechanics</h3>
          <p>Python achieves its expressive syntax through the <strong>Python Data Model</strong>. Rather than introducing language keywords for every operation, Python delegates language syntax to special double-underscore ("dunder") methods:</p>
          <ul>
            <li><strong>Emulating Numeric Types:</strong> <code>__add__</code>, <code>__sub__</code>, <code>__mul__</code>, <code>__matmul__</code>, <code>__truediv__</code>, <code>__neg__</code>. Supporting reflected operations (<code>__radd__</code>) and in-place assignment (<code>__iadd__</code>).</li>
            <li><strong>Emulating Container Sequences:</strong> <code>__len__</code>, <code>__getitem__</code>, <code>__setitem__</code>, <code>__delitem__</code>, <code>__contains__</code>.</li>
            <li><strong>Object String Representations:</strong> <code>__str__</code> (human-readable UI format) vs. <code>__repr__</code> (unambiguous developer representation, ideally executable Python code satisfying <code>eval(repr(obj)) == obj</code>).</li>
          </ul>

          <h3>7.2 Pythonic Enterprise Design Patterns</h3>
          <p>Design patterns in Python leverage first-class functions and duck typing:</p>
          <ul>
            <li><strong>Observer Pattern:</strong> Decouples event producers from consumer subscribers using callable callback registrations.</li>
            <li><strong>Strategy Pattern:</strong> Replaces heavy class hierarchies with higher-order functions passed as arguments.</li>
            <li><strong>Singleton Pattern:</strong> Implemented cleanly via module-level imports (Python modules are cached singletons in <code>sys.modules</code>) or class decorators.</li>
          </ul>
        """
        math_block = r"""
          <p><strong>Vector Inner Product & $L_2$ Euclidean Norm Metrics:</strong></p>
          <p>Let $\mathbf{u}, \mathbf{v} \in \mathbb{R}^N$ represent two mathematical vectors. Vector operations overloaded via dunder methods satisfy:</p>
          $$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_N + v_N \end{bmatrix}, \quad \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^N u_i v_i, \quad \|\mathbf{u}\|_2 = \sqrt{\sum_{i=1}^N u_i^2}$$
          <p>Cosine similarity between two vectorized representations is computed as:</p>
          $$\text{Sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
Mathematical Vector2D/3D Class with Overloaded Dunder Protocols:
Implements operator overloading (__add__, __mul__, __matmul__, __repr__).
\"\"\"
import math
from typing import Sequence, Union

class Vector:
    __slots__ = ('_coords',)

    def __init__(self, *coords: float):
        if not coords:
            raise ValueError("Vector must possess at least one dimension.")
        self._coords = tuple(float(c) for c in coords)

    def __len__(self) -> int:
        return len(self._coords)

    def __getitem__(self, index: int) -> float:
        return self._coords[index]

    def __add__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError(f"Cannot add vectors of mismatched dimensions {len(self)} and {len(other)}")
        return Vector(*(a + b for a, b in zip(self._coords, other._coords)))

    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(*(c * scalar for c in self._coords))

    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        return self.__mul__(scalar)

    def __matmul__(self, other: 'Vector') -> float:
        \"\"\"Implements @ matrix/dot product operator.\"\"\"
        if len(self) != len(other):
            raise ValueError(f"Cannot compute dot product of mismatched dimensions {len(self)} and {len(other)}")
        return sum(a * b for a, b in zip(self._coords, other._coords))

    def norm(self) -> float:
        \"\"\"Computes L2 Euclidean norm.\"\"\"
        return math.sqrt(sum(c ** 2 for c in self._coords))

    def __repr__(self) -> str:
        return f"Vector({', '.join(f'{c:.2f}' for c in self._coords)})"

if __name__ == "__main__":
    v1 = Vector(3.0, 4.0, 0.0)
    v2 = Vector(1.0, 2.0, 2.0)
    print(f"v1: {v1} (L2 Norm: {v1.norm():.2f})")
    print(f"v2: {v2} (L2 Norm: {v2.norm():.2f})")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 * 2.5: {v1 * 2.5}")
    print(f"v1 @ v2 (Dot Product): {v1 @ v2}")"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build a complete real-time Event Dispatcher and Stock Price Notification system using the Pythonic Observer pattern and custom subscriber callback protocols.</p>

          <h4>Step 1: Observer Event Dispatcher Implementation</h4>
          <pre><code class="language-python"># observer_event_system.py
from typing import Callable, Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class PriceAlertEvent:
    ticker: str
    old_price: float
    new_price: float
    percentage_change: float
    timestamp: datetime

ObserverCallback = Callable[[PriceAlertEvent], None]

class StockMarketFeed:
    def __init__(self):
        self._prices: Dict[str, float] = {{}}
        self._subscribers: Dict[str, List[ObserverCallback]] = {{}}

    def subscribe(self, ticker: str, callback: ObserverCallback) -> None:
        if ticker not in self._subscribers:
            self._subscribers[ticker] = []
        self._subscribers[ticker].append(callback)

    def set_price(self, ticker: str, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Price must be positive.")
        old_price = self._prices.get(ticker, new_price)
        self._prices[ticker] = new_price

        if old_price != new_price and ticker in self._subscribers:
            pct = ((new_price - old_price) / old_price) * 100.0
            evt = PriceAlertEvent(ticker, old_price, new_price, round(pct, 2), datetime.now())
            for sub in self._subscribers[ticker]:
                sub(evt)

if __name__ == "__main__":
    feed = StockMarketFeed()
    
    # Register subscribers
    feed.subscribe("NVDA", lambda e: print(f"[SMS ALERT] {{e.ticker}}: ${{e.old_price:.2f}} -> ${{e.new_price:.2f}} ({{e.percentage_change:+5.2f}}%)"))
    feed.subscribe("NVDA", lambda e: print(f"[AUDIT LOG] Recorded event at {{e.timestamp.strftime('%H:%M:%S')}}"))

    print("=== Simulating Market Updates ===")
    feed.set_price("NVDA", 120.00)
    feed.set_price("NVDA", 128.50)
    feed.set_price("NVDA", 124.00)</code></pre>

          <h4>Step 2: Verification Run</h4>
          <pre><code class="language-bash">python observer_event_system.py</code></pre>

          <h4>Step 3: Midterm OOP Practical Scenario</h4>
          <p>Design an Order Processing Pipeline adhering to Strategy Pattern, where payment strategies (CreditCard, Crypto, PayPal) and tax strategies (US, EU, Asia) are decoupled and injected into an <code>OrderCheckout</code> entity.</p>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement an asynchronous Event Bus in Python using <code>asyncio.Queue</code> that dispatches event notifications concurrently to multiple worker consumers without blocking the main event stream.</p>
        """
        mermaid_diag = """flowchart LR
  Publisher[StockMarketFeed Publisher] --> Dispatcher{Event Dispatch Engine}
  Dispatcher -->|PriceAlertEvent| Sub1[SMS Alert Subscriber]
  Dispatcher -->|PriceAlertEvent| Sub2[Audit Log Subscriber]
  Dispatcher -->|PriceAlertEvent| Sub3[Algorithmic Trading Bot]"""
    elif w in (9, 10):
        sec4 = r"""
          <h3>9.1 CPython Exception Unwinding & Defensive Programming</h3>
          <p>When an exception is raised via <code>raise</code>, CPython initiates <strong>Stack Unwinding</strong>. The interpreter traverses the active <code>PyFrameObject</code> call stack in reverse, searching for a matching <code>except</code> block. If found, the execution pointer jumps to the handler; if unhandled, the interpreter terminates and formats the traceback from frame metadata.</p>
          <p>Exception chaining with <code>raise NewException(...) from original_exc</code> sets the <code>__cause__</code> attribute, preserving the root-cause diagnosis across architectural layers without masking critical diagnostic stack traces.</p>

          <h3>10.1 Operating System Page Cache & File I/O Buffering</h3>
          <p>File I/O in Python utilizes the OS kernel page cache. Standard <code>open()</code> calls wrap C standard library <code>FILE*</code> streams or POSIX file descriptors. For large datasets, reading line-by-line via the generator protocol ensures that only the current buffer chunk ($8\text{{ KB}}$ to $64\text{{ KB}}$) resides in memory, rather than loading the entire file into memory.</p>

          <h3>10.2 Relational Persistence with SQLite & SQLAlchemy</h3>
          <p>The <code>sqlite3</code> module exposes an ACID-compliant embedded B-Tree database engine. All SQL operations must utilize <strong>parameterized queries</strong> (<code>?</code> placeholders) to prevent SQL Injection attacks. Modern applications layer SQLAlchemy ORM on top to map Python classes directly to relational schema tables with automated connection pooling.</p>
        """
        math_block = r"""
          <p><strong>Buffer Streaming Memory Sizing & I/O Latency:</strong></p>
          <p>Let $F$ represent total disk file size ($20\text{ GB}$) and $B$ represent the read buffer size ($64\text{ KB}$). Number of I/O operations $K$ and memory overhead $M$ are formulated as:</p>
          $$K = \frac{F}{B} = \frac{20 \times 10^9\text{ bytes}}{65{,}536\text{ bytes}} \approx 305{,}175\text{ read operations}$$
          $$M_{\text{stream}} = B = 64\text{ KB} \quad \ll \quad M_{\text{eager}} = 20\text{ GB}$$
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
Robust SQLite Relational Persistence Layer with Custom Exceptions & Transactions:
Demonstrates ACID transactional safety, parameterized queries, and context managers.
\"\"\"
import sqlite3
from dataclasses import dataclass
from typing import List, Optional

class DatabaseError(Exception):
    pass

@dataclass
class UserEntity:
    user_id: int
    username: str
    email: str
    tier: str

class UserDatabaseManager:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self._init_schema()

    def _init_schema(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(\"\"\"
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    tier TEXT CHECK(tier IN ('Gold', 'Silver', 'Bronze')) NOT NULL
                )
            \"\"\")

    def create_user(self, username: str, email: str, tier: str) -> int:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (username, email, tier) VALUES (?, ?, ?)",
                    (username, email, tier)
                )
                return cur.lastrowid
        except sqlite3.IntegrityError as e:
            raise DatabaseError(f"User with username '{username}' or email '{email}' already exists.") from e

    def get_users_by_tier(self, tier: str) -> List[UserEntity]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT user_id, username, email, tier FROM users WHERE tier = ?", (tier,))
            return [UserEntity(*row) for row in cur.fetchall()]

if __name__ == "__main__":
    db = UserDatabaseManager()
    uid1 = db.create_user("alice_dev", "alice@corp.com", "Gold")
    uid2 = db.create_user("bob_admin", "bob@corp.com", "Gold")
    print(f"Created Users: ID {uid1}, ID {uid2}")
    
    gold_users = db.get_users_by_tier("Gold")
    print("\n--- Gold Tier Users ---")
    for u in gold_users:
        print(f"  {u}")"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build a complete automated CSV-to-JSON analytics pipeline and SQLite database persistence service, incorporating full <code>pytest</code> test coverage, mocking, and structured exception handling.</p>

          <h4>Step 1: Data Pipeline & Persistence Service</h4>
          <pre><code class="language-python"># data_pipeline_and_db.py
import csv
import json
import sqlite3
import os
from typing import List, Dict, Any

def process_csv_to_json(csv_path: str, json_path: str) -> int:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Input CSV file not found: {{csv_path}}")
    
    rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            # Type casting and cleanup
            rows.append({{
                "product_id": int(r["product_id"]),
                "name": r["name"].strip(),
                "price": float(r["price"]),
                "quantity": int(r["quantity"])
            }})
            
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
        
    return len(rows)

if __name__ == "__main__":
    # Generate sample CSV
    with open("raw_products.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "name", "price", "quantity"])
        writer.writerow([101, "Mechanical Keyboard", 129.99, 45])
        writer.writerow([102, "UltraWide Monitor", 499.50, 18])
        
    count = process_csv_to_json("raw_products.csv", "processed_products.json")
    print(f"Successfully converted {{count}} records to JSON.")</code></pre>

          <h4>Step 2: PyTest Test Suite with Fixtures & Mocking</h4>
          <pre><code class="language-python"># test_data_pipeline.py
import pytest
import os
import json
from data_pipeline_and_db import process_csv_to_json

@pytest.fixture
def sample_csv(tmp_path):
    file_path = tmp_path / "test.csv"
    file_path.write_text("product_id,name,price,quantity\\n1,Laptop,999.99,10\\n", encoding="utf-8")
    return str(file_path)

def test_pipeline_transformation(sample_csv, tmp_path):
    json_out = tmp_path / "out.json"
    count = process_csv_to_json(sample_csv, str(json_out))
    assert count == 1
    
    with open(json_out) as f:
        data = json.load(f)
    assert data[0]["name"] == "Laptop"
    assert data[0]["price"] == 999.99</code></pre>

          <h4>Step 3: Test Execution & Coverage Audit</h4>
          <pre><code class="language-bash">pytest test_data_pipeline.py -v</code></pre>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement an automated database migration script that introspects an existing SQLite database schema, generates forward/rollback migration DDLs, and validates schema versioning against an internal <code>schema_migrations</code> metadata table.</p>
        """
        mermaid_diag = """flowchart LR
  CSV[Raw CSV File Stream] --> Parser[CSV DictReader Generator]
  Parser --> TypeClean[Schema Validation & Type Casting]
  TypeClean --> JSON[JSON Analytic Report]
  TypeClean --> DB[(SQLite ACID Database)]"""
    elif w in (11, 12):
        sec4 = r"""
          <h3>11.1 Algorithm Complexity & Empirical Sorting Bounds</h3>
          <p>Algorithm efficiency is measured by asymptotic notations: $\mathcal{{O}}$ (upper bound), $\Omega$ (lower bound), and $\Theta$ (tight bound). Python's default sorting engine is <strong>Timsort</strong> (adaptive hybrid MergeSort + InsertionSort). Timsort identifies naturally occurring contiguous ordered runs in dataset sequences, achieving $\mathcal{{O}}(N)$ best-case execution on partially ordered inputs while guaranteeing $\mathcal{{O}}(N \log N)$ worst-case performance.</p>

          <h3>12.1 CPython Concurrency Models: GIL, Threads, and Asyncio</h3>
          <p>CPython manages concurrency across three distinct paradigms:</p>
          <ul>
            <li><strong>The Global Interpreter Lock (GIL):</strong> A mutual-exclusion lock preventing multi-threaded bytecode execution on multiple CPU cores simultaneously. Consequently, the <code>threading</code> module provides concurrency for <em>I/O-bound tasks</em> (waiting on sockets or disk), but cannot scale <em>CPU-bound numerical computation</em>.</li>
            <li><strong>Multiprocessing:</strong> Spawns separate OS processes, each with its own CPython interpreter, address space, and independent GIL. Uses Inter-Process Communication (IPC via pipes, queues, or shared memory) for true CPU parallelism.</li>
            <li><strong>Asyncio & Coroutines:</strong> Single-threaded cooperative multitasking utilizing non-blocking I/O multiplexing (<code>epoll</code> on Linux, <code>kqueue</code> on macOS, <code>IOCP</code> on Windows). Coroutines yield control to the event loop via <code>await</code>, handling tens of thousands of concurrent connections with low memory overhead.</li>
          </ul>
        """
        math_block = r"""
          <p><strong>Amdahl's Law for Multiprocessing Scalability:</strong></p>
          <p>Let $P$ represent the parallelizable proportion of a computation, and $S$ represent the strictly serial portion ($S = 1 - P$). For a cluster or machine with $N$ CPU cores, theoretical speedup $S(N)$ is formulated as:</p>
          $$S(N) = \frac{1}{(1 - P) + \frac{P}{N}}$$
          <p>If $90\%$ of a numerical algorithm is parallelized ($P = 0.90$) across $16$ CPU cores:</p>
          $$S(16) = \frac{1}{(1 - 0.90) + \frac{0.90}{16}} = \frac{1}{0.10 + 0.05625} = \frac{1}{0.15625} \approx 6.4\times \text{ speedup}$$
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
Comparative Concurrency Benchmark: Multiprocessing vs. Asyncio:
Demonstrates CPU-bound parallelism vs. I/O-bound cooperative event loops.
\"\"\"
import asyncio
import time
import multiprocessing
from typing import List

# CPU-Bound Task
def compute_heavy_factorials(n: int) -> int:
    total = 1
    for i in range(1, n + 1):
        total = (total * i) % 1000000007
    return total

# I/O-Bound Asyncio Task
async def simulate_async_api_call(task_id: int, delay_sec: float) -> str:
    await asyncio.sleep(delay_sec)
    return f"Task {task_id} completed after {delay_sec:.2f}s"

async def run_async_io_tasks():
    print("\n--- Running 5 Concurrent Asyncio I/O Tasks ---")
    t0 = time.perf_counter()
    tasks = [simulate_async_api_call(i, 0.25) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - t0
    print(f"Completed {len(results)} I/O tasks in {elapsed:.3f}s (Sequential would take ~1.25s)")

if __name__ == "__main__":
    # Benchmark CPU-Bound with Multiprocessing
    print("--- Running CPU-Bound Multiprocessing Benchmark ---")
    inputs = [100000] * 8
    t0 = time.perf_counter()
    with multiprocessing.Pool(processes=4) as pool:
        cpu_results = pool.map(compute_heavy_factorials, inputs)
    elapsed = time.perf_counter() - t0
    print(f"Processed {len(inputs)} CPU-heavy tasks across 4 processes in {elapsed:.3f}s")

    # Run Asyncio
    asyncio.run(run_async_io_tasks())"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Implement a Binary Search Tree (BST) and custom Sorting Benchmark from scratch, profiling memory allocation and execution bottlenecks using <code>cProfile</code> and <code>tracemalloc</code>.</p>

          <h4>Step 1: Core Data Structures from Scratch (BST & QuickSort)</h4>
          <pre><code class="language-python"># bst_and_sorting_algorithms.py
from typing import Optional, List
import random
import time

class BSTNode:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int, value: str) -> None:
        self.root = self._insert_rec(self.root, key, value)

    def _insert_rec(self, node: Optional[BSTNode], key: int, value: str) -> BSTNode:
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = self._insert_rec(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key, value)
        else:
            node.value = value # Update existing key
        return node

    def search(self, key: int) -> Optional[str]:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.value
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def in_order_traversal(self) -> List[int]:
        res = []
        def _inorder(n: Optional[BSTNode]):
            if n:
                _inorder(n.left)
                res.append(n.key)
                _inorder(n.right)
        _inorder(self.root)
        return res

if __name__ == "__main__":
    bst = BinarySearchTree()
    for k, v in [(50, "Root"), (30, "L1"), (70, "R1"), (20, "L2"), (40, "L3")]:
        bst.insert(k, v)
    print("In-order sorted keys:", bst.in_order_traversal())
    print("Search key 40:", bst.search(40))</code></pre>

          <h4>Step 2: Profiling with cProfile & tracemalloc</h4>
          <pre><code class="language-python"># profile_benchmark.py
import cProfile
import tracemalloc
from bst_and_sorting_algorithms import BinarySearchTree
import random

def profile_run():
    tracemalloc.start()
    bst = BinarySearchTree()
    keys = random.sample(range(1, 100000), 5000)
    for k in keys:
        bst.insert(k, f"Val_{{k}}")
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Memory -> Current: {{current / 1024:.2f}} KB | Peak: {{peak / 1024:.2f}} KB")

cProfile.run("profile_run()", sort="cumtime")</code></pre>

          <h4>Step 3: Verification & Output Analysis</h4>
          <pre><code class="language-bash">python profile_benchmark.py</code></pre>

          <h4>Step 4: Graduate Extension Challenge</h4>
          <p>Implement an AVL self-balancing tree with Left and Right single/double rotations that maintains strict $\mathcal{{O}}(\log N)$ height balance bounds during random insertions and deletions.</p>
        """
        mermaid_diag = """flowchart TD
  App[Python Application] --> Choice{Workload Type}
  Choice -->|CPU-Bound Numerical| Multi[multiprocessing: Separate IPC Processes]
  Choice -->|I/O-Bound Network/Socket| Async[asyncio: Non-Blocking Epoll Event Loop]
  Multi --> Core1[CPU Core 1]
  Multi --> Core2[CPU Core 2]
  Async --> SocketPool[Non-Blocking Sockets]"""
    else:
        # Weeks 13, 14, 15
        sec4 = r"""
          <h3>13.1 High-Performance Data Analysis & SIMD Vectorization</h3>
          <p>Standard Python loops over collections incur dynamic type-checking and pointer dereferencing on every element. The <strong>Scientific Python Stack (NumPy & Pandas)</strong> overcomes this by storing homogeneous data in contiguous C memory buffers (<code>ndarray</code>). Operations on arrays trigger hardware SIMD (Single Instruction Multiple Data) vector execution in compiled C/Fortran routines, achieving $50\times$ to $200\times$ throughput speedups.</p>

          <h3>13.2 Modern Microservices: FastAPI & Asynchronous REST</h3>
          <p>Modern Python web applications utilize <strong>ASGI (Asynchronous Server Gateway Interface)</strong> frameworks such as <strong>FastAPI</strong> and <strong>Uvicorn</strong>. Features include:</p>
          <ul>
            <li><strong>Pydantic Type Validation:</strong> Automatic serialization and schema parsing based on standard Python type hints.</li>
            <li><strong>OpenAPI / Swagger Generation:</strong> Automatic generation of interactive REST API documentation.</li>
            <li><strong>Non-Blocking Endpoints:</strong> Native <code>async def</code> route handlers executing on the asyncio event loop.</li>
          </ul>

          <h3>14.1 Packaging Standards (PEP 517/518/621) & CI/CD Pipelines</h3>
          <p>Modern Python engineering standardizes on declarative <code>pyproject.toml</code> configuration files for builds (Hatch, Flit, Poetry), replacing legacy <code>setup.py</code> scripts. Continuous Integration (GitHub Actions) automates linting (Ruff), strict type validation (Mypy), and test execution across isolated Docker containers.</p>
        """
        math_block = r"""
          <p><strong>Vector Striding & Columnar Memory Access Mathematics:</strong></p>
          <p>Let an $N \times M$ 2D NumPy array of 64-bit floating point numbers be stored in C-contiguous row-major order. The byte offset for element $A[i, j]$ is computed in $\mathcal{O}(1)$ time as:</p>
          $$\text{Byte Offset}(i, j) = \text{Base Address} + (i \times M \times 8) + (j \times 8)$$
          <p>Enabling CPU cache prefetching and vectorized SIMD instruction pipelines.</p>
        """
        code_py = """#!/usr/bin/env python3
\"\"\"
FastAPI High-Throughput Asynchronous REST Microservice:
Demonstrates Pydantic validation, async route handlers, and in-memory analytics.
\"\"\"
from dataclasses import dataclass
from typing import List, Optional
import time

# Simulated FastAPI/Pydantic Microservice Skeleton
@dataclass
class TelemetryPayload:
    device_id: str
    temperature: float
    humidity: float
    voltage: float

class TelemetryAnalyticsService:
    def __init__(self):
        self._store: List[TelemetryPayload] = []

    def ingest(self, payload: TelemetryPayload) -> dict:
        self._store.append(payload)
        return {"status": "INGESTED", "total_records": len(self._store)}

    def compute_summary(self) -> dict:
        if not self._store:
            return {"count": 0, "avg_temperature": 0.0}
        temps = [p.temperature for p in self._store]
        return {
            "count": len(self._store),
            "avg_temperature": round(sum(temps) / len(temps), 2),
            "max_temperature": max(temps),
            "min_temperature": min(temps)
        }

if __name__ == "__main__":
    service = TelemetryAnalyticsService()
    service.ingest(TelemetryPayload("DEV-01", 24.5, 45.0, 3.3))
    service.ingest(TelemetryPayload("DEV-02", 28.2, 52.0, 3.2))
    service.ingest(TelemetryPayload("DEV-03", 22.1, 40.0, 3.4))
    
    print("--- Analytics API Response ---")
    print(service.compute_summary())"""
        lab_content = r"""
          <p><strong>Lab Objective:</strong> Build, test, containerize, and package an end-to-end applied Python microservice using <code>FastAPI</code>, <code>pyproject.toml</code>, and a multi-stage <code>Dockerfile</code>.</p>

          <h4>Step 1: Packaging Configuration (pyproject.toml)</h4>
          <pre><code class="language-toml"># pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "applied-telemetry-service"
version = "1.0.0"
description = "MS Applied Programming Python Microservice"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.110.0",
    "uvicorn>=0.28.0",
    "pydantic>=2.6.0",
    "pandas>=2.2.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.3.0",
    "mypy>=1.9.0"
]</code></pre>

          <h4>Step 2: Multi-Stage Dockerfile Containerization</h4>
          <pre><code class="language-dockerfile"># Dockerfile
# Stage 1: Build & Dependency Resolution
FROM python:3.13-slim AS builder
WORKDIR /app
RUN pip install --no-cache-dir hatchling
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Stage 2: Minimal Distroless/Slim Production Runtime
FROM python:3.13-slim AS runtime
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY . /app

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]</code></pre>

          <h4>Step 3: Verification & Execution Drill</h4>
          <pre><code class="language-bash"># Run static linting and type checking
ruff check .
mypy .
# Build and run Docker container
docker build -t telemetry-service:1.0 .
docker run -p 8000:8000 telemetry-service:1.0</code></pre>

          <h4>Step 4: Graduate Capstone Challenge</h4>
          <p>Complete your end-to-end Applied Python Capstone project, integrating an OOP domain core, automated pytest test coverage ($90\%+$), persistent SQLite/SQLAlchemy storage, and a FastAPI REST interface.</p>
        """
        mermaid_diag = """flowchart LR
  Dev[Developer Workspace] --> Git[Git Feature Branch]
  Git --> PR[Pull Request]
  PR --> CI[GitHub Actions CI: Ruff + Mypy + PyTest]
  CI --> DockerBuild[Multi-Stage Docker Build]
  DockerBuild --> Registry[Container Registry & Production Deploy]"""

    return sec4, math_block, code_py, lab_content, mermaid_diag


def render_lesson_page(lesson, idx, all_lessons):
    title = lesson["title"]
    num = lesson["num"]
    w_num = lesson["week_num"]
    w_title = lesson["week_title"]
    w_slug = lesson["week_slug"]
    slug = lesson["slug"]
    dur = lesson["duration"]
    diff = lesson["difficulty"]
    focus = lesson["focus"]

    sec4, math_block, code_py, lab_content, mermaid_diag = get_graduate_python_content(lesson)

    prev_l = all_lessons[idx - 1] if idx > 0 else None
    next_l = all_lessons[idx + 1] if idx < len(all_lessons) - 1 else None

    prev_html = f'<a class="btn" href="../../weeks/{prev_l["week_slug"]}/{prev_l["slug"]}.html">← Previous: {prev_l["num"]} {prev_l["title"]}</a>' if prev_l else '<span></span>'
    next_html = f'<a class="btn btn-primary" href="../../weeks/{next_l["week_slug"]}/{next_l["slug"]}.html">Next: {next_l["num"]} {next_l["title"]} →</a>' if next_l else '<span></span>'

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lesson {num}: {title} | MS Applied Programming (Python)</title>
  <meta name="description" content="Master's-level study of {title}. Comprehensive theory, CPython internals, math foundations, and hands-on engineering lab.">
  <link rel="stylesheet" href="../../assets/css/styles.css">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body data-root="../../" data-page-id="week-{w_num:02d}/lesson-{num.replace('.', '-')}">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="../../index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>

      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>

      <nav class="course-nav" id="courseNav"></nav>

      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span class="separator">/</span>
          <a href="../../weeks/{w_slug}/index.html">Week {w_num}: {w_title}</a>
          <span class="separator">/</span>
          <span>Lesson {num}</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Week {w_num} · Lesson {num}</div>
          <h1>{title}</h1>
          <p class="lead">{focus}</p>

          <div class="meta-grid">
            <div class="meta-item">
              <strong>Estimated Time</strong>
              <span>{dur}</span>
            </div>
            <div class="meta-item">
              <strong>Academic Level</strong>
              <span>{diff} · MS Level</span>
            </div>
            <div class="meta-item">
              <strong>Runtime Stack</strong>
              <span>CPython 3.13 / POSIX</span>
            </div>
            <div class="meta-item">
              <strong>Verification</strong>
              <span>PyTest + Typing</span>
            </div>
          </div>

          <div class="toolbar">
            <button class="btn btn-primary" id="completeBtn" type="button">Mark Complete</button>
            <button class="btn" id="bookmarkBtn" type="button">☆ Bookmark</button>
            <button class="btn" id="quizModeBtn" type="button">Toggle Quiz Mode</button>
            <button class="btn print-page" type="button">🖨️ Export PDF</button>
          </div>
        </header>

        <div class="layout-article">
          <article class="article">
            <!-- 1. Introduction -->
            <section id="section-1">
              <h2>1. Introduction & Systems Intuition</h2>
              <p>In modern computer science and enterprise software engineering, <strong>{title}</strong> represents a cornerstone discipline. While introductory programming treats code as abstract scripts, graduate-level software engineering requires understanding the physical machine mechanics: memory layouts, CPython virtual machine bytecode evaluation, instruction pointer dispatching, and operating system system calls.</p>
              <p>This module deconstructs <strong>{title}</strong> from first principles: analyzing memory allocation hierarchies, execution invariants, computational complexity, and production software patterns.</p>
            </section>

            <!-- 2. Graduate Learning Outcomes -->
            <section id="section-2">
              <h2>2. Graduate Learning Outcomes</h2>
              <ul>
                <li><strong>Theoretical Mastery:</strong> Rigorously analyze the operational semantics, data structures, and algorithms underlying {title}.</li>
                <li><strong>CPython Systems Internals:</strong> Trace C-level struct representations (<code>PyObject</code>, pointer arrays, hash buckets) and memory lifecycle events.</li>
                <li><strong>Asymptotic Complexity:</strong> Formulate formal mathematical proofs ($\mathcal{{O}}$, $\Omega$, $\Theta$) for time and space scaling.</li>
                <li><strong>Production Engineering:</strong> Implement defensive, typed, PEP 8 compliant Python solutions with automated test verification.</li>
              </ul>
            </section>

            <!-- 3. Prerequisites -->
            <section id="section-3">
              <h2>3. Prerequisites & Boundary Conditions</h2>
              <p>Students are expected to possess proficiency in foundational computer architecture (RAM, CPU cache, pointers), standard terminal commands, and basic Python syntax. Boundary invariants enforced across this module:</p>
              <ul>
                <li><strong>Deterministic Execution:</strong> Zero undefined behavior; proper exception propagation across stack boundaries.</li>
                <li><strong>Resource Safety:</strong> Strict context manager bounds preventing memory leaks, socket starvation, and unclosed file descriptors.</li>
              </ul>
            </section>

            <!-- 4. Core Concepts & CPython Systems Internals -->
            <section id="section-4">
              <h2>4. Core Concepts & CPython Systems Internals</h2>
              {sec4}
            </section>

            <!-- 5. Visual Architecture & Flow Diagrams -->
            <section id="section-5">
              <h2>5. Visual Architecture & Flow Diagrams</h2>
              <div class="diagram">
                <div class="mermaid">
{mermaid_diag}
                </div>
              </div>
            </section>

            <!-- 6. Mind Maps & Taxonomies -->
            <section id="section-6">
              <h2>6. Mind Maps & Taxonomy</h2>
              <p>The structural taxonomy below categorizes the computational components of {title}:</p>
              <div class="diagram">
                <div class="mermaid">
mindmap
  root(({title}))
    Runtime Engine
      CPython Virtual Machine
      Bytecode Disassembly
      Stack Frame Allocator
    Memory Management
      PyObject Reference Count
      Cyclic Garbage Collector
      Arena Allocator
    Software Quality
      Static Type Checking mypy
      PyTest Automated Tests
      PEP 8 Compliance
    Performance
      Asymptotic Big-O Scaling
      SIMD Vectorization
      Zero-Copy Slicing
                </div>
              </div>
            </section>

            <!-- 7. Mathematical & Asymptotic Foundations -->
            <section id="section-7">
              <h2>7. Mathematical & Asymptotic Foundations</h2>
              {math_block}
            </section>

            <!-- 8. Industry Engineering Scenarios -->
            <section id="section-8">
              <h2>8. Practical Industry Engineering Scenarios</h2>
              <p>In high-scale enterprise platforms (e.g. Instagram, Dropbox, Stripe), {title} directly dictates infrastructure efficiency:</p>
              <ul>
                <li><strong>Low-Latency Microservices:</strong> Minimizing object allocation rates and GIL lock contention in API backends to achieve sub-10ms $p99$ response times.</li>
                <li><strong>Data Processing Pipelines:</strong> Leveraging streaming generators and columnar memory layouts to process multi-terabyte feeds without out-of-memory (OOM) crashes.</li>
              </ul>
            </section>

            <!-- 9. Production-Grade Python Implementations -->
            <section id="section-9">
              <h2>9. Production-Grade Python Implementations</h2>
              <pre><code class="language-python">{code_py}</code></pre>
            </section>

            <!-- 10. Security & Defensive Programming -->
            <section id="section-10">
              <h2>10. Security, Defensive Programming & Threat Modeling</h2>
              <div class="callout warning">
                <summary>Security Advisory: Defensive Invariants</summary>
                <p>Always enforce explicit type validation, input sanitization, and parameterized database queries. Avoid using <code>eval()</code> or deserializing untrusted payloads with <code>pickle</code> (which allows arbitrary remote code execution via <code>__reduce__</code> exploits). Use <code>json</code> or <code>pydantic</code> for safe data interchange.</p>
              </div>
            </section>

            <!-- 11. Industry Software Engineering Practices -->
            <section id="section-11">
              <h2>11. Industry Software Engineering Practices</h2>
              <ul>
                <li><strong>Static Type Typing:</strong> Enforce strict annotations validated via <code>mypy --strict</code>.</li>
                <li><strong>Formatting & Linting:</strong> Standardize on <code>ruff</code> and <code>black</code> in pre-commit Git hooks.</li>
                <li><strong>Dependency Hygiene:</strong> Pin dependencies deterministically via <code>pyproject.toml</code> lockfiles.</li>
              </ul>
            </section>

            <!-- 12. Academic Citations -->
            <section id="section-12">
              <h2>12. Academic & Computer Science Citations</h2>
              <ul>
                <li>Van Rossum, G., & Drake, F. L. (2009). <em>The Python Language Reference Manual</em>. Network Theory Ltd.</li>
                <li>Hettinger, R. (2012). <em>Modern Python Dictionaries: A Confluence of A Beautiful Idea</em>. PyCon US.</li>
                <li>Peters, T. (2002). <em>Timsort: An Adaptive, Stable, Natural Mergesort</em>. Python Software Foundation.</li>
              </ul>
            </section>

            <!-- 13. Case Studies -->
            <section id="section-13">
              <h2>13. Real-World Case Studies</h2>
              <p><strong>Instagram CPython Scale:</strong> Instagram serves billions of daily requests on a monolithic Django/CPython cluster. By disabling cyclic garbage collection on web worker processes and relying purely on reference counting and memory copy-on-write sharing across preforked master processes, Instagram saved over $10\%$ of server cluster memory overhead.</p>
            </section>

            <!-- 14. Common Misconceptions -->
            <section id="section-14">
              <h2>14. Common Misconceptions & Anti-Patterns</h2>
              <ul>
                <li><em>Misconception:</em> Python passes arguments by value or by reference.<br>
                <strong>Reality:</strong> Python uses <em>Pass-by-Object-Reference</em> (or Call-by-Sharing). The function receives a reference to the bound object, but reassigning the local parameter name does not rebind the caller's variable.</li>
                <li><em>Misconception:</em> The GIL makes multi-threaded Python programs thread-safe.<br>
                <strong>Reality:</strong> The GIL only protects CPython internal struct invariants. User-level operations across multiple bytecode instructions still require explicit mutex locks (<code>threading.Lock</code>) to prevent race conditions.</li>
              </ul>
            </section>

            <!-- 15. Executive Summary -->
            <section id="section-15">
              <h2>15. Executive & Engineering Summary</h2>
              <p>Mastering <strong>{title}</strong> bridges the gap between surface-level scripting and high-performance software engineering. Understanding CPython's execution model empowers engineers to architect memory-efficient, robust, and horizontally scalable backend systems.</p>
            </section>

            <!-- 16. Module Glossary -->
            <section id="section-16">
              <h2>16. Module Glossary Terms</h2>
              <table>
                <thead>
                  <tr><th>Term</th><th>Category</th><th>Definition</th></tr>
                </thead>
                <tbody>
                  <tr><td><code>PyObject</code></td><td>Memory</td><td>Foundational C struct encapsulating reference count and type metadata pointer.</td></tr>
                  <tr><td><code>GIL</code></td><td>Concurrency</td><td>Global Interpreter Lock synchronizing CPython bytecode execution.</td></tr>
                  <tr><td><code>MRO</code></td><td>OOP</td><td>Method Resolution Order computed via the C3 Linearization algorithm.</td></tr>
                </tbody>
              </table>
            </section>

            <!-- 17. Self-Assessment Quiz -->
            <section id="section-17">
              <h2>17. Interactive Self-Assessment Quiz</h2>
              <ul class="quiz-list">
                <li data-answer="CPython objects are allocated on the heap inside a PyObject struct containing an 8-byte reference counter (ob_refcnt) and an 8-byte type descriptor pointer (ob_type), introducing pointer indirection overhead compared to unboxed C scalars.">Why does an integer in Python consume ~28 bytes of memory whereas an integer in C consumes only 4 or 8 bytes?</li>
                <li data-answer="The GIL protects CPython interpreter memory invariants, but thread switching occurs between bytecode instructions. If a shared state operation requires multiple bytecodes (e.g. read-modify-write on an integer), race conditions will corrupt application state without a threading.Lock.">Why does Python's GIL not guarantee application-level thread safety for shared mutable variables?</li>
                <li data-answer="C3 Linearization guarantees local precedence order (a class comes before its parents) and monotonicity (parent precedence order is preserved across all descendants).">What formal properties does the C3 Linearization algorithm preserve during Python multiple inheritance MRO resolution?</li>
              </ul>
            </section>

            <!-- 18. Hands-On Practice Lab & Engineering Drill -->
            <section id="section-18">
              <h2>18. Expanded Hands-On Practice Lab & Engineering Drill</h2>
              <div class="interactive-widget-box">
                <div class="widget-header">
                  <div class="widget-title">⚡ Hands-On Lab: {title}</div>
                  <span class="widget-badge">4-Step Engineering Lab</span>
                </div>
                {lab_content}
              </div>
            </section>

            <!-- 19. Further Reading -->
            <section id="section-19">
              <h2>19. Curated Further Reading & PEP Citations</h2>
              <ul>
                <li><a href="https://peps.python.org/pep-0008/" target="_blank" rel="noopener">PEP 8 – Style Guide for Python Code</a></li>
                <li><a href="https://peps.python.org/pep-0393/" target="_blank" rel="noopener">PEP 393 – Flexible String Representation</a></li>
                <li><a href="https://peps.python.org/pep-0703/" target="_blank" rel="noopener">PEP 703 – Making the Global Interpreter Lock Optional in CPython</a></li>
              </ul>
            </section>
          </article>

          <!-- Sticky TOC -->
          <aside class="toc">
            <h2>On This Page</h2>
            <ol id="tocList"></ol>
          </aside>
        </div>

        <div class="prev-next">
          {prev_html}
          {next_html}
        </div>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="../../assets/js/site.js"></script>
</body>
</html>
"""
    return html


def render_week_index(week):
    w_num = week["num"]
    w_title = week["title"]
    w_slug = week["slug"]
    w_desc = week["desc"]
    lessons = week["lessons"]

    lesson_cards = ""
    for l in lessons:
        lesson_cards += f"""
        <div class="card week-card">
          <span class="week-num">Lesson {l['num']} · {l['duration']}</span>
          <h3>{l['title']}</h3>
          <p>{l['focus']}</p>
          <a class="btn btn-primary" href="{l['slug']}.html">Enter Lesson {l['num']} →</a>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Week {w_num}: {w_title} | MS Applied Programming (Python)</title>
  <link rel="stylesheet" href="../../assets/css/styles.css">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body data-root="../../" data-page-id="week-{w_num:02d}/index">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="../../index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span class="separator">/</span>
          <span>Week {w_num}: {w_title}</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Module Overview · Week {w_num}</div>
          <h1>{w_title}</h1>
          <p class="lead">{w_desc}</p>
        </header>

        <h2>Curriculum Lessons for Week {w_num}</h2>
        <div class="grid">
          {lesson_cards}
        </div>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="../../assets/js/site.js"></script>
</body>
</html>
"""
    return html


def render_home_page():
    week_cards = ""
    for w in WEEKS:
        lesson_links = "".join([f'<li><a href="weeks/{w["slug"]}/{l["slug"]}.html"><strong>{l["num"]}</strong> {l["title"]}</a></li>' for l in w["lessons"]])
        week_cards += f"""
        <div class="card week-card">
          <span class="week-num">Week {w['num']} · 2 Graduate Lessons</span>
          <h3>{w['title']}</h3>
          <p>{w['desc']}</p>
          <ul style="list-style:none; padding:0; margin-bottom:1.5rem; font-size:0.85rem;">
            {lesson_links}
          </ul>
          <a class="btn" href="weeks/{w['slug']}/index.html">Explore Week {w['num']} Overview →</a>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MS Applied Programming (Python) | Graduate Learning Platform</title>
  <meta name="description" content="Master's-level interactive learning platform for Applied Programming in Python. 15 Weeks, 30 Lessons, CPython internals, algorithms, concurrency, and 4-step engineering labs.">
  <link rel="stylesheet" href="assets/css/styles.css">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body data-root="" data-page-id="home">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum (Ctrl+K)...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <header class="hero">
          <div class="eyebrow">Graduate Computer Science · MS Level</div>
          <h1>Applied Programming in Python</h1>
          <p class="lead">A rigorous, systems-oriented Master's-level curriculum covering CPython runtime internals, asymptotic algorithms, OOP design patterns, asynchronous concurrency, and production software engineering practices.</p>

          <div class="meta-grid">
            <div class="meta-item">
              <strong>Curriculum Scope</strong>
              <span>15 Weeks · 30 Lessons</span>
            </div>
            <div class="meta-item">
              <strong>Engineering Labs</strong>
              <span>30 4-Step Practical Drills</span>
            </div>
            <div class="meta-item">
              <strong>Interactive Tools</strong>
              <span>In-Browser Python Sandbox</span>
            </div>
            <div class="meta-item">
              <strong>Architecture</strong>
              <span>CPython 3.13 & POSIX</span>
            </div>
          </div>

          <div class="toolbar">
            <a class="btn btn-primary" href="weeks/week-01/course-intro-setup-and-python-basics.html">Start Week 1, Lesson 1.1 →</a>
            <a class="btn" href="interactive-lab.html">⚡ Interactive Python Lab</a>
            <a class="btn" href="architecture.html">📐 Course Architecture</a>
            <a class="btn" href="glossary.html">📖 Python Glossary</a>
          </div>
        </header>

        <h2>Curriculum Weeks (1 — 15)</h2>
        <div class="grid">
          {week_cards}
        </div>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="assets/js/site.js"></script>
</body>
</html>
"""
    return html


def render_interactive_lab_page():
    html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Python Lab & Algorithm Workbench | MS Applied Python</title>
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body data-root="" data-page-id="interactive-lab">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Interactive Python Lab</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Interactive Workbench</div>
          <h1>Interactive Python Lab & Algorithm Workbench</h1>
          <p class="lead">Experiment with Python scripts, simulate Big-O complexity scaling, and inspect interactive data structures client-side in real-time.</p>
        </header>

        <!-- Tool 1: Interactive Python Playground -->
        <section class="interactive-widget-box">
          <div class="widget-header">
            <div class="widget-title">🐍 Tool 1: In-Browser Python Code Playground</div>
            <span class="widget-badge">Interactive Simulator</span>
          </div>
          <p style="margin-bottom:1rem; font-size:0.9rem; color:var(--text-secondary);">Select a preset algorithm or type your own Python 3.13 script below to execute and inspect runtime output:</p>
          
          <div style="margin-bottom:1rem; display:flex; gap:1rem; align-items:center;">
            <label style="font-weight:600; font-size:0.85rem;">Preset Algorithm:</label>
            <select id="pyPresetSelect" style="padding:0.4rem 0.8rem; background:var(--bg-surface-elevated); color:var(--text-primary); border:1px solid var(--border-color); border-radius:var(--radius-sm);">
              <option value="fib">Memoized Recursive Fibonacci</option>
              <option value="matrix">Matrix Transposition & Comprehensions</option>
              <option value="oop">Observer Pattern Event Dispatcher</option>
              <option value="quicksort">QuickSort Algorithm</option>
            </select>
          </div>

          <div class="py-editor-container">
            <textarea id="pyCodeInput" class="py-textarea"># Memoized Recursive Fibonacci in Python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Computing Fibonacci Sequence (n=1 to 12):")
results = [fibonacci(i) for i in range(1, 13)]
print("Results:", results)
print("Cache Info:", fibonacci.cache_info())</textarea>

            <div style="display:flex; gap:0.75rem;">
              <button class="btn btn-primary" id="runPythonBtn" type="button">▶ Execute Script</button>
              <button class="btn" id="resetPythonBtn" type="button">Reset</button>
            </div>

            <div style="font-size:0.8rem; font-weight:700; text-transform:uppercase; letter-spacing:0.8px; color:var(--text-muted); margin-top:0.5rem;">Console Execution Output:</div>
            <div id="pyConsoleOutput" class="py-console-output">>>> Ready for execution. Click "Execute Script".</div>
          </div>
        </section>

        <!-- Tool 2: Big-O Complexity Graph -->
        <section class="interactive-widget-box">
          <div class="widget-header">
            <div class="widget-title">📈 Tool 2: Big-O Algorithm Complexity Simulator</div>
            <span class="widget-badge">Asymptotic Analysis</span>
          </div>
          <p style="margin-bottom:1rem; font-size:0.9rem; color:var(--text-secondary);">Drag the input scale slider to evaluate theoretical CPU operation counts across asymptotic complexity classes:</p>
          
          <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1rem;">
            <input type="range" id="bigONSlider" min="10" max="10000" step="10" value="1000" style="flex:1;">
            <span id="bigONDisplay" style="font-weight:800; font-family:var(--font-mono); font-size:1.1rem; color:var(--accent-blue);">N = 1,000</span>
          </div>

          <div id="complexityChartBox"></div>
        </section>

        <!-- Tool 3: Data Structure Inspector -->
        <section class="interactive-widget-box">
          <div class="widget-header">
            <div class="widget-title">🌳 Tool 3: Interactive Data Structure Inspector</div>
            <span class="widget-badge">LIFO / FIFO Visualizer</span>
          </div>
          <p style="margin-bottom:1rem; font-size:0.9rem; color:var(--text-secondary);">Push and pop elements into a Stack (LIFO) or Queue (FIFO) to observe pointer manipulations:</p>

          <div style="display:flex; gap:1rem; align-items:center; margin-bottom:1rem; flex-wrap:wrap;">
            <select id="dsModeSelect" style="padding:0.4rem 0.8rem; background:var(--bg-surface-elevated); color:var(--text-primary); border:1px solid var(--border-color); border-radius:var(--radius-sm);">
              <option value="stack">Stack (LIFO - Last In First Out)</option>
              <option value="queue">Queue (FIFO - First In First Out)</option>
            </select>
            <input type="text" id="dsInputVal" placeholder="Enter node value (e.g. Node_X)" style="padding:0.4rem 0.8rem; background:var(--bg-surface-elevated); color:var(--text-primary); border:1px solid var(--border-color); border-radius:var(--radius-sm);">
            <button class="btn btn-primary btn-sm" id="dsPushBtn" type="button">Push / Enqueue</button>
            <button class="btn btn-sm" id="dsPopBtn" type="button">Pop / Dequeue</button>
          </div>

          <div id="dsVisualStack" style="padding:1rem; background:var(--code-bg); border:1px solid var(--code-border); border-radius:var(--radius-md); min-height:120px;"></div>
        </section>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="assets/js/site.js"></script>
  <script src="assets/js/interactive-tools.js"></script>
</body>
</html>
"""
    return html


def render_architecture_page():
    html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Architecture & Specifications | MS Applied Python</title>
  <link rel="stylesheet" href="assets/css/styles.css">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body data-root="" data-page-id="architecture">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Course Architecture & Specifications</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Academic Architecture</div>
          <h1>Course Architecture & Specifications</h1>
          <p class="lead">Pedagogical design system, 19-section graduate blueprint, and CPython systems execution model.</p>
        </header>

        <article class="article">
          <section>
            <h2>1. Pedagogical Architecture & Graduate Principles</h2>
            <p>The MS Applied Programming in Python curriculum is engineered to bridge foundational software syntax with enterprise systems architecture. Every module is structured around four pillars:</p>
            <ul>
              <li><strong>Systems Rigor:</strong> Deconstructing CPython runtime internals, memory allocations, and POSIX system call interfaces.</li>
              <li><strong>Formal Complexity:</strong> Mathematically proving asymptotic bounds and identifying algorithmic optimizations.</li>
              <li><strong>Defensive Engineering:</strong> Enforcing automated pytest test suites, strict typing with Mypy, and zero-defect exception handling.</li>
              <li><strong>Real-World Applicability:</strong> Multi-step practical engineering drills reflecting modern cloud, API, and data engineering environments.</li>
            </ul>
          </section>

          <section>
            <h2>2. 19-Section Lesson Blueprint</h2>
            <div class="diagram">
              <div class="mermaid">
flowchart TD
  S1[1. Intuition] --> S2[2. Learning Outcomes]
  S2 --> S3[3. Prerequisites]
  S3 --> S4[4. CPython Systems Internals]
  S4 --> S5[5. Mermaid Architecture]
  S5 --> S6[6. Mind Map]
  S6 --> S7[7. Asymptotic Math Proofs]
  S7 --> S8[8. Industry Scenarios]
  S8 --> S9[9. Production Code]
  S9 --> S10[10. Defensive Security]
  S10 --> S11[11. SWE Best Practices]
  S11 --> S12[12. Academic Citations]
  S12 --> S13[13. Case Studies]
  S13 --> S14[14. Anti-Patterns]
  S14 --> S15[15. Exec Summary]
  S15 --> S16[16. Glossary]
  S16 --> S17[17. Quiz Engine]
  S17 --> S18[18. 4-Step Hands-On Lab]
  S18 --> S19[19. PEP Citations]
              </div>
            </div>
          </section>

          <section>
            <h2>3. Capstone Project Requirements (Week 15)</h2>
            <p>Students must architect and defend an end-to-end applied Python software system fulfilling:</p>
            <ol>
              <li><strong>Object-Oriented Domain Core:</strong> Encapsulated domain entities utilizing custom dunder methods, ABC contracts, and Design Patterns.</li>
              <li><strong>Automated Test Coverage:</strong> Comprehensive pytest suite achieving $\ge 90\%$ line and branch coverage with mock isolation.</li>
              <li><strong>Data Persistence / Streaming:</strong> SQLite database integration via parameterized SQL/SQLAlchemy or streaming file parser.</li>
              <li><strong>Applied Interface Component:</strong> High-throughput FastAPI REST web service or exploratory Pandas/NumPy analytics pipeline.</li>
              <li><strong>DevOps / Packaging:</strong> Declarative <code>pyproject.toml</code> configuration and multi-stage <code>Dockerfile</code> containerization.</li>
            </ol>
          </section>
        </article>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="assets/js/site.js"></script>
</body>
</html>
"""
    return html


def render_glossary_page():
    rows = ""
    for g in GLOSSARY:
        rows += f"""
        <tr class="glossary-row" data-term="{g['term'].lower()}" data-cat="{g['category'].lower()}">
          <td style="font-weight:700; color:var(--accent-blue); font-family:var(--font-mono);">{g['term']}</td>
          <td><span class="widget-badge">{g['category']}</span></td>
          <td style="font-size:0.92rem; color:var(--text-secondary);">{g['def']}</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python & CS Terminology Glossary | MS Applied Python</title>
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body data-root="" data-page-id="glossary">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Python Terminology Glossary</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Reference Dictionary</div>
          <h1>Python & Computer Science Terminology Glossary</h1>
          <p class="lead">Searchable dictionary of fundamental CPython, algorithms, concurrency, and OOP systems concepts.</p>
        </header>

        <div style="margin-bottom:1.5rem; display:flex; gap:1rem; align-items:center;">
          <input type="text" id="glossaryFilterInput" placeholder="Filter terms (e.g. GIL, PyObject, MRO)..." class="site-search-input" style="max-width:400px;">
        </div>

        <table>
          <thead>
            <tr>
              <th style="width:25%;">Term</th>
              <th style="width:20%;">Category</th>
              <th>Definition & Technical Context</th>
            </tr>
          </thead>
          <tbody id="glossaryTableBody">
            {rows}
          </tbody>
        </table>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="assets/js/site.js"></script>
  <script>
    document.getElementById('glossaryFilterInput').addEventListener('input', function(e) {{
      const q = e.target.value.toLowerCase();
      document.querySelectorAll('.glossary-row').forEach(row => {{
        const term = row.getAttribute('data-term');
        const cat = row.getAttribute('data-cat');
        const text = row.innerText.toLowerCase();
        row.style.display = (term.includes(q) || cat.includes(q) || text.includes(q)) ? '' : 'none';
      }});
    }});
  </script>
</body>
</html>
"""
    return html


def render_search_page():
    html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Curriculum Search Engine | MS Applied Python</title>
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body data-root="" data-page-id="search">
  <div class="progress" id="readingProgress"></div>

  <div class="mobile-topbar">
    <button class="btn btn-sm" id="openSidebar">☰ Menu</button>
    <div class="brand-text">MS Applied Python</div>
    <button class="theme-toggle-btn btn-sm">🌓</button>
  </div>

  <div class="site-shell">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <a class="brand" href="index.html">
          <div class="brand-mark">Py</div>
          <div>
            <h1>Applied Python</h1>
            <small>MS CS Graduate Portal</small>
          </div>
        </a>
      </div>
      <div class="nav-search">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="site-search-input" id="navSearch" placeholder="Search curriculum...">
          <span class="search-shortcut">⌘K</span>
        </div>
      </div>
      <nav class="course-nav" id="courseNav"></nav>
      <div class="sidebar-footer">
        <button class="theme-toggle-btn" type="button">🌓 Theme</button>
        <span style="font-size:0.75rem; color:var(--text-muted);">Python 3.13 Ready</span>
      </div>
    </aside>

    <main class="main">
      <div class="page-wrap">
        <nav class="breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Course Search</span>
        </nav>

        <header class="hero">
          <div class="eyebrow">Search Index</div>
          <h1>Curriculum Full-Text Search Engine</h1>
          <p class="lead">Search across all 15 weeks, 30 lessons, CPython internals, algorithms, and hands-on engineering lab drills.</p>
        </header>

        <div style="margin-bottom:2rem;">
          <input type="text" id="fullSearchInput" placeholder="Search lessons, concepts, modules (e.g. PyObject, asyncio, MRO, pytest)..." class="site-search-input" style="padding:0.9rem 1.2rem; font-size:1.05rem;">
        </div>

        <div id="fullSearchResultsList" style="display:flex; flex-direction:column; gap:1rem;">
          <div style="padding:2rem; text-align:center; color:var(--text-muted);">Type your search query above to inspect matching curriculum topics.</div>
        </div>

        <footer class="footer">
          <p>MS Applied Programming (Python) · Master's Curriculum Portal · Built with Python 3.13</p>
        </footer>
      </div>
    </main>
  </div>

  <script src="assets/js/site.js"></script>
  <script src="assets/js/search-index.js"></script>
  <script>
    const fullInput = document.getElementById('fullSearchInput');
    const fullResults = document.getElementById('fullSearchResultsList');

    fullInput.addEventListener('input', () => {
      const q = fullInput.value.trim().toLowerCase();
      if (!q || typeof window.SEARCH_INDEX === 'undefined') {
        fullResults.innerHTML = '<div style="padding:2rem; text-align:center; color:var(--text-muted);">Type your search query above to inspect matching curriculum topics.</div>';
        return;
      }

      const matches = window.SEARCH_INDEX.filter(item => {
        return item.title.toLowerCase().includes(q) ||
               (item.summary && item.summary.toLowerCase().includes(q)) ||
               (item.keywords && item.keywords.toLowerCase().includes(q));
      });

      if (matches.length === 0) {
        fullResults.innerHTML = `<div style="padding:2rem; text-align:center; color:var(--text-muted);">No matching topics found for "<strong>${q}</strong>".</div>`;
        return;
      }

      fullResults.innerHTML = matches.map(m => `
        <div class="card" style="padding:1.25rem;">
          <span style="font-size:0.75rem; font-weight:700; color:var(--accent-blue); text-transform:uppercase;">${m.week || 'Applied Python'} · ${m.difficulty || 'Intermediate'}</span>
          <h3 style="margin:0.4rem 0;"><a href="${m.url}" style="color:var(--text-primary); text-decoration:none;">${m.title}</a></h3>
          <p style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:0.75rem;">${m.summary}</p>
          <a class="btn btn-sm btn-primary" href="${m.url}">Read Lesson →</a>
        </div>
      `).join('');
    });
  </script>
</body>
</html>
"""
    return html


def generate_metadata_js_files():
    # 1. nav-data.js
    nav_data = []
    for w in WEEKS:
        nav_data.append({
            "num": w["num"],
            "slug": w["slug"],
            "title": w["title"],
            "lessons": [{"num": l["num"], "slug": l["slug"], "title": l["title"]} for l in w["lessons"]]
        })

    nav_js = f"window.COURSE_NAV_DATA = {json.dumps(nav_data, indent=2)};"
    (BASE_DIR / "assets" / "js" / "nav-data.js").write_text(nav_js, encoding="utf-8")

    # 2. search-index.js
    search_data = []
    for l in ALL_LESSONS:
        search_data.append({
            "title": f"Lesson {l['num']}: {l['title']}",
            "week": f"Week {l['week_num']}: {l['week_title']}",
            "url": f"weeks/{l['week_slug']}/{l['slug']}.html",
            "summary": l["focus"],
            "difficulty": l["difficulty"],
            "keywords": f"{l['title']} {l['focus']} Python CPython algorithm OOP pytest concurrency asyncio"
        })

    search_js = f"window.SEARCH_INDEX = {json.dumps(search_data, indent=2)};"
    (BASE_DIR / "assets" / "js" / "search-index.js").write_text(search_js, encoding="utf-8")

    # 3. glossary-data.js
    glossary_js = f"window.GLOSSARY_DATA = {json.dumps(GLOSSARY, indent=2)};"
    (BASE_DIR / "assets" / "js" / "glossary-data.js").write_text(glossary_js, encoding="utf-8")


def generate_serve_script():
    serve_py = """#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8081
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    # Try port 8081, fallback to 8082 if occupied
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"============================================================")
            print(f"  MS Applied Programming (Python) Live Server Running!")
            print(f"  URL: http://localhost:{PORT}")
            print(f"  Root: {DIRECTORY}")
            print(f"  Press Ctrl+C to terminate.")
            print(f"============================================================")
            httpd.serve_forever()
    except OSError:
        PORT = 8082
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"============================================================")
            print(f"  MS Applied Programming (Python) Live Server Running!")
            print(f"  URL: http://localhost:{PORT}")
            print(f"  Root: {DIRECTORY}")
            print(f"  Press Ctrl+C to terminate.")
            print(f"============================================================")
            httpd.serve_forever()
"""
    (BASE_DIR / "serve.py").write_text(serve_py, encoding="utf-8")


def main():
    print("Generating MS Applied Programming (Python) Platform...")
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    (BASE_DIR / "assets" / "css").mkdir(parents=True, exist_ok=True)
    (BASE_DIR / "assets" / "js").mkdir(parents=True, exist_ok=True)
    (BASE_DIR / "weeks").mkdir(parents=True, exist_ok=True)

    # 1. Generate Metadata JS Files
    generate_metadata_js_files()

    # 2. Generate Portal Pages
    (BASE_DIR / "index.html").write_text(render_home_page(), encoding="utf-8")
    (BASE_DIR / "interactive-lab.html").write_text(render_interactive_lab_page(), encoding="utf-8")
    (BASE_DIR / "architecture.html").write_text(render_architecture_page(), encoding="utf-8")
    (BASE_DIR / "glossary.html").write_text(render_glossary_page(), encoding="utf-8")
    (BASE_DIR / "search.html").write_text(render_search_page(), encoding="utf-8")

    # 3. Generate Week Folders & Lessons
    for w in WEEKS:
        week_dir = BASE_DIR / "weeks" / w["slug"]
        week_dir.mkdir(parents=True, exist_ok=True)
        (week_dir / "index.html").write_text(render_week_index(w), encoding="utf-8")

    for i, lesson in enumerate(ALL_LESSONS):
        week_dir = BASE_DIR / "weeks" / lesson["week_slug"]
        lesson_html = render_lesson_page(lesson, i, ALL_LESSONS)
        (week_dir / f"{lesson['slug']}.html").write_text(lesson_html, encoding="utf-8")

    # 4. Generate Local Serve Script
    generate_serve_script()

    print(f"Successfully generated all 30 MS Applied Python lessons across 15 weeks at: {BASE_DIR}")


if __name__ == "__main__":
    main()
