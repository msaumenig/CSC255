CSC 255 — Python Project Ideas

Agentic / MCP-style project planning document

Why Python?

Using Python gives the group several advantages:

Faster development time
Easier GUI/game libraries
Excellent threading/multiprocessing support
Strong cryptography/compression libraries
Easier visualization and demos
Cleaner code for presentations

Recommended libraries:

pygame → games/graphics
tkinter or customtkinter → GUI apps
threading / multiprocessing
hashlib / cryptography
numpy
socket
matplotlib
networkx
Project Idea #1 — Parallel Password Cracking Simulator
Topics
Cryptography
Parallel Concurrency
Random Number Generation
Elevator Pitch

A cybersecurity simulator that demonstrates how password cracking works using:

brute force attacks
dictionary attacks
multithreaded parallel processing

This project visually demonstrates why weak passwords are dangerous.

Snazzy Features
Live cracking dashboard
Real-time guesses-per-second counter
Adjustable CPU thread count
Password complexity meter
Hash visualization
Benchmark graphs
Tech Stack
threading
multiprocessing
hashlib
tkinter/customtkinter
matplotlib
Core Algorithms
SHA-256 hashing
Brute-force search
Dictionary attack
Parallel workload distribution
Stretch Goals
GPU acceleration simulation
Rainbow tables
Network-distributed cracking
Difficulty

⭐⭐⭐⭐☆

Project Idea #2 — Procedural Dungeon Roguelike
Topics
Games
Random Number Generation
Parallel Concurrency
Elevator Pitch

A randomly generated dungeon crawler where:

every level is unique
enemy AI acts concurrently
loot and combat are randomized

Think:

classic roguelikes
Minecraft dungeon generation
retro pixel-art gameplay
Snazzy Features
Procedural dungeon generation
Animated combat
AI enemies running on separate threads
Fog of war
Inventory system
Boss battles
Tech Stack
pygame
threading
random
numpy
Core Algorithms
Cellular automata dungeon generation
Pathfinding (A*)
Enemy state machines
Collision detection
Stretch Goals
Online multiplayer
Save system
Procedural soundtrack generation
Difficulty

⭐⭐⭐⭐⭐

Project Idea #3 — Huffman Compression Studio
Topics
Compression
Visualization
Elevator Pitch

A visual compression application that:

compresses files using Huffman Coding
animates tree creation
shows binary encoding live

This is one of the strongest “academic” projects because it directly demonstrates algorithms.

Snazzy Features
Drag-and-drop file support
Animated Huffman tree
Binary stream viewer
Compression ratio dashboard
File comparison charts
Decompression playback
Tech Stack
tkinter/customtkinter
heapq
networkx
matplotlib
Core Algorithms
Priority queue construction
Binary tree traversal
Huffman encoding/decoding
Stretch Goals
Compare Huffman vs ZIP vs RLE
Real-time streaming compression
Difficulty

⭐⭐⭐☆☆

Project Idea #4 — Conway’s Game of Life Supercomputer
Topics
Parallel Concurrency
Games/Simulation
Elevator Pitch

A high-performance Conway’s Game of Life simulator capable of handling:

massive grids
thousands of generations
real-time multithreaded updates
Snazzy Features
Infinite zoom
GPU-like visual effects
Pattern presets
Speed benchmarking
Multi-core simulation
Heatmap visualization
Tech Stack
pygame
numpy
multiprocessing
matplotlib
Core Algorithms
Cellular automata
Grid partitioning
Parallel processing
Stretch Goals
Distributed computing mode
AI-discovered patterns
Difficulty

⭐⭐⭐⭐☆

Project Idea #5 — Secure Encrypted File Transfer System
Topics
Cryptography
Compression
Parallel Concurrency
Elevator Pitch

A secure file transfer app that:

Compresses files
Encrypts them
Transfers them across a network

Basically a mini secure cloud transfer platform.

Snazzy Features
AES encryption
Drag-and-drop UI
Real-time transfer statistics
Multi-threaded chunk transfers
Compression analysis
Secure chat/log panel
Tech Stack
socket
threading
cryptography
gzip
tkinter/customtkinter
Core Algorithms
AES encryption
File chunking
Compression
TCP socket networking
Stretch Goals
End-to-end encrypted chat
LAN discovery
QR-code pairing
Difficulty

⭐⭐⭐⭐⭐

BEST CHOICE RECOMMENDATIONS
Easiest to Finish
Huffman Compression Studio

Why:

Directly tied to coursework
Algorithms are manageable
Strong visualization potential
Lower debugging complexity
Best Presentation/Demo
Procedural Dungeon Roguelike

Why:

Very flashy
Easy to impress instructor/class
Fun to work on
Excellent screenshots/video potential
Most Technically Impressive
Secure Encrypted File Transfer System

Why:

Combines networking + crypto + compression
Feels like “real software”
Great resume project
Best Overall Balance
Parallel Password Cracking Simulator

Why:

Strong CS concepts
Easier than full game development
Excellent concurrency showcase
Clear measurable performance improvements
Suggested Group Roles
Role	Responsibilities
Backend Engineer	Core algorithms
Concurrency Engineer	Threads/processes
UI/Visualization Engineer	GUI and graphics
Documentation/Testing Lead	Reports and QA
Recommended Folder Structure
project/
│
├── src/
│   ├── main.py
│   ├── ui/
│   ├── algorithms/
│   ├── networking/
│   ├── assets/
│
├── docs/
│   ├── proposal.md
│   ├── report.md
│
├── tests/
│
├── requirements.txt
│
└── README.md
Suggested Demo Strategy

During presentation:

Explain the problem
Show architecture diagram
Explain algorithms briefly
Run live demo
Show performance metrics
Discuss lessons learned
Recommended Final Pick
If your group wants the safest A:
Huffman Compression Studio
If your group wants the coolest presentation:
Procedural Dungeon Roguelike
If your group wants maximum technical credibility:
Secure Encrypted File Transfer System
If your group wants the best balance:
Parallel Password Cracking Simulator
