class InstructionAddressGenerator:
    def __init__(self, initial_pc):
        self.program_counter = initial_pc
        # PC source: 0 = PC + 4 (sequential), 1 = branch/jump, 2 = register (e.g., jalr)
        self.pc_source = -1

    def update_pc(self, immediate_target, reg_target):
        print("\n[PC Update]")
        if self.pc_source == 0:
            print("→ Proceeding to next instruction (PC + 4).")
            return False
        elif self.pc_source == 1:
            self.program_counter = immediate_target
            print(f"→ Jump to immediate offset: PC ← {hex(self.program_counter)}")
            return True
        elif self.pc_source == 2:
            self.program_counter = reg_target
            print(f"→ Jump to register-based address: PC ← {hex(self.program_counter)}")
            return True

        # Fallback if pc_source is undefined
        print(f"→ Current PC unchanged: {hex(self.program_counter)}")
        return False
