import capstone
from binaryninja import *
from capstone.arm64 import *
from pprint import pprint
def pp_print(str):
    pprint(str)

def get_targte_reg_name(bv,cs,address):
    # address = 0x9cc7c
    inst_bytes = bv.read(address, bv.get_instruction_length(address))
    for inst in cs.disasm(inst_bytes, address):
        inst: capstone.CsInsn = inst
        for operand in inst.operands:
            operand: capstone.arm64.Arm64Op = operand
            return inst.reg_name(operand.value.reg)


def find_operation(llil :LowLevelILFunction,llil_operation: LowLevelILOperation) -> List[Optional[LowLevelILInstruction]]:
    def find_(llil_inst: LowLevelILInstruction):
        if llil_inst.operation == llil_operation:
            return llil_inst
    return list(llil.traverse(find_))


# 找到所有设置 flag的地方 并返回 operation(怎么比较的) raw_operands 比较的寄存器
def find_all_flag_def_info(llil :LowLevelILFunction):
    fag_defs_il = find_operation(llil,LowLevelILOperation.LLIL_SET_FLAG)
    info = {

    }
    for flag in llil.flags:
        for index,il in enumerate(fag_defs_il):
            il : LowLevelILSetFlag
            if il.operands[0].name == flag.name:
                info[flag.name] = {
                    "operation": il.operands[1].operation,
                    "raw_operands": il.operands[1].raw_operands,
                    "size": il.operands[1].size
                }
                fag_defs_il.pop(index)
                break
    return info

# 只获取只有一个值的寄存器的值
def get_reg_const_value_after(il,reg):
    reg_value = il.get_possible_reg_values_after(reg)
    # 只需要 只可能是一个值的
    # 多个值的是 InSetOfValues 未知的是 UndeterminedValue
    if not reg_value.type == RegisterValueType.ConstantValue:
        return None
    return reg_value

# 判断是否是操作自己 sp = sp - 0x70
#   x20 = x20 + 0xc80
def is_operate_self(il:LowLevelILInstruction):

    if not hasattr(il,"src") or not hasattr(il,"dest"):
        return False



