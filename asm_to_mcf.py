"""
asm_to_mcf.py

Author: McDic

Description:
    This .py is used to convert assembly to minecraft functions.
"""

# File related
import os
import shutil

# Assembly related errors
class AssemblyBaseError(Exception): pass # Base exception
class AssemblySyntaxError(AssemblyBaseError, SyntaxError): # Syntax exception
    def __init__(self, address, instruction_line):
        message = "Assembly syntax error at address %d: [%s]" % (address, instruction_line)
        super().__init__(message)
class AssemblySourceDestinationSameError(AssemblyBaseError, ValueError): # Source and destination is same
    def __init__(self, address, instruction_line):
        message = "Assembly source and destination is same at address %d: [%s]" % (address, instruction_line)
        super().__init__(message)

# Convert assembly into minecraft functions
def makeFunction(assemblies, generatePath,
                 dataPackName = "McDicArchitecture", namespace = "main"):

    # Error handling
    if not os.path.isdir(generatePath):
        raise NotADirectoryError("Given path [%s] is not valid" % (generatePath,))
    if len(os.listdir(generatePath)):
        raise OSError("Given path [%s] is not empty" % (generatePath,))

    # Init file
    with open(generatePath + "/init.mcfunction", "w") as initMCF:
        pass

    for line in assemblies:
        pass

# Make functions from the file
def makeFunctionFromFile(filePath, generatePath):
    with open(filePath, "r") as ASMfile:
        raw = ASMfile.read().split("\n")
    return makeFunction(raw, generatePath)