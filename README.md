# Advanced computing using Minecraft
Make customized assembly structure and translate it to Minecraft functions.

# Requirements
- Minecraft Java Edition 1.13+
    - Future version might be unstable because recent Minecraft command architecture
    is changing so fast
- Python 3.7+

# Low level instruction sets
The basic instructions to make computing architecture.

## Data types
Base type is int(word) since it's expensive to access and decode bits in shorter size.

## Conditions
- Not implemented

## Register and memory architecture
- There is no big I/O difference between register and memory!
    - Static access: Cost = O(1), Just use raw name
    - Dynamic access: Cost = O(log(n)), Use binary search to find data by changeable value.
    - There is no reason to separate register and memory. 
        - But, there is a special register to store special flag values or temporary loading values.
- There are several kinds of memory:
    - Instruction memory: Minecraft is not optimized to divide instruction into several parts
    and we assume that we have almost infinite size for memory.
    So in this architecture we are going to use multibyte to decode instruction easily.
    - Stack memory: Used for procedural recursive call. This stores temporary values.
    - Output memory: Used to out values.
- Also there are some special registers:
    - $Lmain : Temporary registers to save value loaded from main memory
    - $Lstack : Temporary registers to save value loaded from stack memory
    - $FlagExc : Flag value to recognize exceptions.

## .mcfunction structure
All files below are in *[WORLD_NAME]/datapacks/[DATA_PACK_NAME]/data/[NAMESPACE]/functions*
```
CPU/ : Whole architecture are in this folder
    init.mcfunction : Initialize all basic things(Memory, Stack, etc)
    InstructionMemory/ : Instruction memory related
        ... (Dynamic memory access)
    MainMemory/ : Main memory related; Supports load and store
        ... (Dynamic memory access)
    StackMemory/ : Stack memory related; Supports push and pop
        push.mcfunction : Pop and load value from stack memory to main memory
        pop.mcfunction: Push value from main memory to stack memory
    FloatingPoint/ : Floating point number operations
        ... (Arithmetic operations supported)
    MCIO/ : Supports Minecraft I/O
        ...
```

## Assembly file structure
- Recommended file extension: **.mcfasm** (Minecraft Function Assembly)
- Syntax: ``<Memory address> <Instruction name> [d] [s..] [i..]``
    - ``d``: Destination address.
    - ``s``: Source address. There can be multiple sources.
    - ``i``: Immediate value. There can be multiple immediate values.

Example:
```
// This is the comment
// <Address> <Instruction name> <arguments..>

0       SET     d=0     i=1
1       SET     d=1     i=2
2       ADD     d=2     s1=1    s2=1
3       SUB     
```

## Arithmetic instructions
1. **MOV d s** : Copy value
    ```
    Mem[d] = Mem[s]
    ```
2. **SET d i** : Set with immediate value
    ```
    Mem[d] = i
    ```
3. **ADD d s** : Integer addition 
    ```
    Mem[d] += Mem[s]
    ```
4. **ADDI d i** : Integer addition with immediate value
    ```
    Mem[d] += i
    ```
5. **SUB d s** : Integer subtraction 
    ```
    Mem[d] -= Mem[s]
    ```
6. **SUBI d i** : Integer subtraction with immediate value
    ```
    Mem[d] -= i
    ```
7. **MUL d s** : Integer multiplication
    ```
    Mem[d] *= Mem[s]
    ```
8. **MULI d i** : Integer multiplication with immediate value
    ```
    Mem[d] *= i
    ```
9. **DIV d s** : Integer division
    ```
    Mem[d] /= Mem[s]
    ```
10. **DIVI d i** : Integer division with immediate value
    ```
    Mem[d] /= i
    ```
11. **REM d s** : Integer division remainder
    ```
    Mem[d] %= Mem[s2]
    ```
12. **REMI d i** : Integer division remainder with immediate value
    ```
    Mem[d] %= i
    ```

## Set/Load instructions
1. **LOAD d s i** : Load value with variable based access
    ```
    $Lmain = Mem[Mem[s]+i]
    Mem[d] = $Lmain
    ```
2. **STORE d s i** : Store value with variable based access
    ```
    $Lmain = Mem[s]
    Mem[Mem[d]+i] = $Lmain
    ```
3. **STKPUSH s** : Push new value to stack memory
    ```
    StackMem.push(Mem[s])
    ```
4. **STKPOP d** : Pop top value from stack memory
    ```
    Mem[d] = StackMem.pop()
    ```

## Branch instructions
1. **BU i** : Unconditional branch.
    ```
    PC += i
    ```
2. **BEQ s1 s2 i** : Branch if two values are equal.
    ```
    if Mem[s1] == Mem[s2]:
        PC += i
    ```
3. **BEQI s1 i1 i2** : Branch if two values(with immediate value) are equal.
    ```
    if Mem[s1] == i1:
        PC += i2
    ```
4. **BNE s1 s2 i** : Branch if two values are not equal.
    ```
    if Mem[s1] != Mem[s2]:
        PC += i
    ```
5. **BNEI s1 i1 i2** : Branch if two values(with immediate value) are not equal.
    ```
    if Mem[s1] != i1:
        PC += i2 
    ```
    
## Jump instructions
1. **J i** : Jump to specific address
    ```
    PC = i
    ```
2. **JM s** : Jump to specific address
    ```
    PC = Mem[s]
    ```

## I/O instructions
These instructions are used to display value to end user. 
There are several ways to print result below:
- tellraw: Base chat interaction; This is the first priority
- title: Base screen interaction
    - title title: Big one
    - title subtitle: Small one
- book: Print result by minecraft:book, this feature is delayed for future due to complexity.

1. **PBUFSTR str**       : Push "str" in I/O entity stack buffer
2. **PBUFREG s**         : Push str(Mem[s]) in I/O entity stack buffer
3. **PBUFINT i**         : Push str(i) in I/O entity stack buffer
4. **TELLRAW i**         : Print on Minecraft console(tellraw) for BUF[0:i]
5. **TITLE i**           : Print on Minecraft console(title title) for BUF[0:i]
6. **SUBTITLE i**        : Print on Minecraft console(title subtitle) for BUF[0:i]
 
# High level instruction sets
The reason why I made this:
- To use multibyte data types like floating point number
- Make high-level development easier

## High level arithmetic instructions
1. **ADDF d s1 s2**: Add two floating point numbers
    ```
    // Float at x -> Mem[x] * 10^Mem[x+1]
    ADD 
    ```
2. 