window.GLOSSARY_DATA = [
  {
    "term": "CPython",
    "category": "Runtime",
    "def": "The standard, reference C-based implementation of the Python programming language that compiles Python source code into bytecode and executes it via a stack-based virtual machine."
  },
  {
    "term": "PyObject",
    "category": "Memory",
    "def": "The foundational C struct in CPython from which all Python objects inherit, containing the reference count (ob_refcnt) and the object type pointer (ob_type)."
  },
  {
    "term": "Global Interpreter Lock (GIL)",
    "category": "Concurrency",
    "def": "A mutual-exclusion lock used by CPython to ensure only one OS thread executes Python bytecode at any given moment, preventing race conditions on memory reference counts."
  },
  {
    "term": "Method Resolution Order (MRO)",
    "category": "OOP",
    "def": "The deterministic algorithmic order (computed via C3 Linearization) in which Python searches for method implementations across complex multiple inheritance class hierarchies."
  },
  {
    "term": "Abstract Base Class (ABC)",
    "category": "OOP",
    "def": "A class defined via the abc module that enforces interface contracts by prohibiting instantiation of subclasses unless all @abstractmethod declarations are overridden."
  },
  {
    "term": "Dunder Methods",
    "category": "Data Model",
    "def": "Special 'double underscore' methods (e.g. __init__, __getitem__, __call__) that bind user-defined classes into Python's built-in syntax, operators, and protocols."
  },
  {
    "term": "Dynamic Array Over-Allocation",
    "category": "Algorithms",
    "def": "The growth strategy used by Python's list where extra capacity is pre-allocated proportionally during appends to achieve amortized O(1) insertion time."
  },
  {
    "term": "Hash Table Perturbation",
    "category": "Data Structures",
    "def": "The collision resolution algorithm in CPython dicts that incorporates high-order bits of the hash code to break cyclic probing patterns in open addressing."
  },
  {
    "term": "Call Stack Frame (PyFrameObject)",
    "category": "Runtime",
    "def": "The heap-allocated C struct representing a function execution scope, storing local variables, the evaluation value stack, instruction pointer, and globals dict."
  },
  {
    "term": "Asyncio Event Loop",
    "category": "Concurrency",
    "def": "A single-threaded reactive scheduler that manages and dispatches asynchronous tasks and I/O callbacks via non-blocking OS multiplexers (epoll/kqueue)."
  },
  {
    "term": "Descriptor Protocol",
    "category": "Metaprogramming",
    "def": "An object attribute protocol implementing __get__, __set__, or __delete__, providing the underlying engine for properties, classmethods, and ORM fields."
  },
  {
    "term": "Timsort",
    "category": "Algorithms",
    "def": "A hybrid adaptive sorting algorithm combining MergeSort and InsertionSort designed by Tim Peters, providing O(N) best-case and O(N log N) worst-case time complexity."
  },
  {
    "term": "Context Manager",
    "category": "Control Flow",
    "def": "An object adhering to the runtime context protocol (__enter__ and __exit__) utilized within 'with' statements to guarantee deterministic resource cleanup."
  },
  {
    "term": "Cyclomatic Complexity",
    "category": "Software Eng",
    "def": "A software metric indicating the number of linearly independent execution paths through source code, calculated as M = E - N + 2P."
  },
  {
    "term": "SIMD Vectorization",
    "category": "Performance",
    "def": "Single Instruction Multiple Data: hardware CPU instructions utilized by NumPy to perform parallel arithmetic operations across contiguous memory buffers in C."
  }
];