class ALU:
    def __init__(self):
        # Operation code selector
        self.__operation = 0

        # Intermediate pipeline values
        self.result_z = 0
        self.result_y = 0
        self.pass_through = 0

        # Selectors for inputs and output stages
        self.sel_op2 = 0    # 0 → rs2, 1 → imm
        self.sel_op1 = 0    # 0 → rs1, 1 → pc
        self.sel_output = 0 # 0 → RZ, 1 → MDR, 2 → return address

        # ALU operation mode (0: basic, 1: LUI, etc.)
        self.alu_mode = 0

    def execute(self, rs1, rs2, rz, ry, imm, funct3, funct7, pc):
        operand1 = [rs1, pc, rz, ry][self.sel_op1]
        operand2 = [rs2, imm, rz, ry][self.sel_op2]

        print(f"\tALU Operand1: 0x{operand1:08x}")
        print(f"\tALU Operand2: 0x{operand2:08x}")

        if self.alu_mode == 3:
            print("\t[ALU] No operation specified.")
            self.result_z = 0
            return

        # Determine which operation to execute
        self._control_unit(funct3, funct7)

        if self.__operation == 1:      # ADD
            self.result_z = operand1 + operand2
        elif self.__operation == 2:    # SUB
            self.result_z = operand1 - operand2
        elif self.__operation == 3:    # MUL
            self.result_z = operand1 * operand2
        elif self.__operation == 4:    # DIV
            self.result_z = operand1 // operand2
        elif self.__operation == 5:    # REM
            self.result_z = operand1 % operand2
        elif self.__operation == 6:    # AND
            self.result_z = operand1 & operand2
        elif self.__operation == 7:    # OR
            self.result_z = operand1 | operand2
        elif self.__operation == 8:    # XOR
            self.result_z = operand1 ^ operand2
        elif self.__operation == 9:    # SLL
            self.result_z = operand1 << operand2
        elif self.__operation == 10:   # SRL (logical shift)
            self.result_z = (operand1 % (1 << 32)) >> operand2
        elif self.__operation == 11:   # SRA (arithmetic shift)
            self.result_z = operand1 >> operand2
        elif self.__operation == 12:   # SLT (set on less than)
            self.result_z = int(operand1 < operand2)
        elif self.__operation == 13:   # LUI
            if operand1 < 0:
                operand1 += 1 << 32
            self.result_z = ((operand1 << 20) >> 20) + operand2

        if self.result_z < 0:
            self.result_z += 1 << 32
        
        print(f"\tALU Result RZ: 0x{self.result_z:08x}")

    def _control_unit(self, funct3, funct7):
        """ Determines the ALU operation based on control signals. """
        if self.alu_mode == 0:
            self.__operation = 1  # Basic ADD (e.g., for load/store)
        elif self.alu_mode & 1:
            self.__operation = 13  # LUI-type operation
        else:
            if funct3 == 0:
                if self.sel_op2 == 1 or funct7 == 0:
                    self.__operation = 1  # ADD immediate or normal
                elif funct7 == 1:
                    self.__operation = 3  # MUL
                elif funct7 == 32:
                    self.__operation = 2  # SUB
            elif funct3 == 7:
                self.__operation = 6  # AND
            elif funct3 == 6:
                self.__operation = 7 if (self.sel_op2 == 1 or funct7 == 0) else 5  # OR or REM
            elif funct3 == 4:
                self.__operation = 8 if (self.sel_op2 == 1 or funct7 == 0) else 4  # XOR or DIV
            elif funct3 == 1:
                self.__operation = 9  # SLL
            elif funct3 == 101:
                self.__operation = 10 + ((funct7 & 32) >> 5)  # SRL or SRA
            elif funct3 == 2:
                self.__operation = 12  # SLT

    def process_output(self, memory_data, ret_addr):
        """ Choose final value for writing back to register file """
        if self.sel_output == 0:
            self.result_y = self.result_z
        elif self.sel_output == 1:
            self.result_y = memory_data
        elif self.sel_output == 2:
            self.result_y = ret_addr

        print(f"\tALU Final Output RY: 0x{self.result_y:08x}")
