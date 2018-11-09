# Assembly file structure
This project is translating assembly file to minecraft function files. 

- Only level 0 and level 1 instructions are allowed to write in assembly file.
- Recommended file extension: **.mcfasm** (Minecraft Function Assembly)
- Syntax: ``<Memory address> <Flag condition> <Instruction name> [Destination..] [Source..] [Intermediate..]``
    - ``Flag condition (f)``: The condition to decide to execute commands.
    - ``Destination (d)``: Destination address.
    - ``Source (s)``: Source address. There can be multiple sources.
    - ``Immediate (i)``: Immediate value to operate(usually arithmetic). 
                          There can be multiple immediate values.

## .mcfasm example
```
// This is the comment. Empty or comment line will be ignored.
// Instruction: \t <instruction name>, <arguments..>
// Label: <label name> ::

F1::
    SET, f=0, d=0, i=1
    SET, f=1, d=1, i=2
    ADD, f=0, d=2, s=1
    SUB, f=0, d=1
    CMP, 
    J,   f=
    
F2::
    
```

# Level 0 instructions
Level 0 instructions are the basic instructions to make computing architecture. 
These instructions are the smallest unit and indivisible.
Low level operations are performed.

## Arithmetic/Logical instructions
The instructions below are used to calculate the simplest arithmetic and logical operations.
For floating point number operation, see Level 1 or above.

1. **MOV d s** : Copy value
    ```
    // Abstraction
    Mem[d] = Mem[s]
    
    // Static
    scoreboard players operation McDic McDic$Reg
    
    // Dynamic
    scoreboard players 
    ```
2. **SET d i** : Set with immediate value
    ```
    // Abstraction
    Mem[d] = i
    
    // Static
    
    
    // Dynamic
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

## Dynamic memory access instructions
The instructions below are focused on accessing memory.
- Some of them are used to access memory with dynamically changing value.
- Some of them are used to interact between the main memory and the stack memory.

1. **PTRL d s** : Load value in main memory with variable based access
    ```
    $Lmain = Mem[Mem[s]]
    Mem[d] = $Lmain
    ```
2. **PTRS d s** : Store value in main memory with variable based access
    ```
    $Lmain = Mem[s]
    Mem[Mem[d]] = $Lmain
    ```
3. **STKPUSH s** : Push new value to stack memory
    ```
    &Lstack = Mem[s]
    StackMem.push() // Lstack is pushed
    ```
4. **STKPOP d** : Pop top value from stack memory
    ```
    StackMem.pop() // Poppped value is moved to Lstack
    Mem[d] = &Lstack
    ```

## Flag set instructions
The instructions below are used to set flag with some conditions.
All instructions are executed in some conditions, which are affected by these flags.

1. **CMP s1 s2** : Compare main memory values in address s1, s2.
    ```
    if Mem[s1] < Mem[s2]:
        $FlagCmp = -1
    elif Mem[s1] == Mem[s2]:
        $FlagCmp = 0
    else: // Mem[s1] > Mem[s2]
        $FlagCmp = 1
    ```
2. **CMPI s i** : Compare main memory value and immediate value.
    ```
    if Mem[s] < i:
        $FlagCmp = -1
    elif Mem[s] == i:
        $FlagCmp = 0
    else: // Mem[s] > i
        $FlagCmp = 1
    ```

## Branch and jump instructions
The instructions below are used to control flow of the program. 

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
6. **J i** : Jump to specific address
    ```
    PC = i
    ```
7. **JM s** : Jump to specific address
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

1. **PBUFSTR i**         : Push char(i) in I/O entity stack buffer
2. **PBUFREG s**         : Push char(Mem[s]) in I/O entity stack buffer
3. **PBUFINT i**         : Push str(i) in I/O entity stack buffer
4. **TELLRAW i**         : Print on Minecraft console(tellraw) for BUF[0:i]
5. **TITLE i**           : Print on Minecraft console(title title) for BUF[0:i]
6. **SUBTITLE i**        : Print on Minecraft console(title subtitle) for BUF[0:i]
 
## Time delay instructions

1. **SLEEP i**          : Sleep this process for i tick
 
# Level 1 instructions
Level 1 instructions is the instructions used to describe 
higher level of operations from multiple level 0 instructions.

Features:
- Floaing point nu

The reason why I made this:
- To use multibyte data types like floating point number
- Make high-level development easier

## Arithmetic instructions
1. **ADDF d s1 s2**: Add two floating point numbers
    ```
    // Float at x -> Mem[x] * 10^Mem[x+1]
    CMP  
    ```
2. 