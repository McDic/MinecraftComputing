# Advanced computing using Minecraft
Make customized assembly structure and translate it to Minecraft functions.

# Requirements
- Minecraft Java Edition 1.13+
    - Future version might be unstable because recent Minecraft command architecture
    is changing so fast
- Python 3.7+

# Basic introduction

## Data types
Base type is int(word) since it's expensive to access and decode bits in shorter size.

## Register and memory architecture
- There is no big I/O difference between register and memory!
    - // Static access: Cost = O(1), Just use raw name
    - // Dynamic access: Cost = O(log(n)), Use binary search to find data by changeable value.
    - There is no reason to separate register and memory. 
    But, there is a special register to store special flag values or temporary loading values.
- There are several kinds of memory:
    - Main memory(*MCF-MAIN*) :
    Minecraft is not optimized to divide instruction into several parts 
    and we assume that we have almost infinite size for memory.
    So, in this architecture we are going to use multi-byte to decode instruction easily.
    - Stack memory(*MCF-STACK*) :
    Used for procedural recursive call. This stores temporary values.
    - Output memory(*MCF-OUT*) :
    Used to print values. 
- Also there are some special registers(*MCF-REG*) :
    - *$MCF-REG-temp* : General temporary value.
    - *$MCF-REG-flag-exception* : Flag value to recognize exceptions.
    - *$MCF-REG-flag-compare* : Flag value to store result of compare operation.
    - *$MCF-REG-return-address* : Store return address for procedural call.

# Whole functions structure overview
All files below are in *[WORLD_NAME]/datapacks/[DATA_PACK_NAME]/data/[NAMESPACE]/functions*
```
CPU/ : Whole architecture are in this folder
    init.mcfunction : Initialize all basic things(Memory, Stack, etc)
    MainMemory/ : Main/Instruction memory related; Supports load and store
        ... (Dynamic memory access)
    StackMemory/ : Stack memory related; Supports push and pop
        push.mcfunction : Pop and load value from stack memory to main memory
        pop.mcfunction: Push value from main memory to stack memory
    MCIO/ : Supports Minecraft I/O
        ...
```
