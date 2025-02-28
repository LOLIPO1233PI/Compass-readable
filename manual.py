def manual():
  print("func\nbody: func name:body\n\nused for defining functions (if you couldn't understand already somehow)\n\n"+"="*50)
  print("print\nbody: print(content1,...,contentN)\n\nused for printing content that can be either a variable or a string")
def cpecm():
  print(f"Compass Pharsing and Execution Console Manual","="*55,
                                      "\"$help\" Print's the manual for Compass",
                                      "\"$clear\" Clears the memory (if any)",
                                      "\"$exec\" Executes the memory as code",
                                      "\"$exit\" End's the CPEC session",
                                      "\"$modify\" Modifies a line in the memory (if any)",
                                      "\"$list\" Prints the memory",
                                      "\"$cpec\" Prints the manual for CPEC",sep="\n")