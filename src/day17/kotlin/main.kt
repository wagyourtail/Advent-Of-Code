import xyz.wagyourtail.commonskt.utils.repeat
import java.util.stream.IntStream
import java.util.stream.LongStream
import kotlin.jvm.Throws
import kotlin.math.exp
import kotlin.system.exitProcess

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

enum class Opcodes {
    ADV,
    BXL,
    BST,
    JNZ,
    BXC,
    OUT,
    BDV,
    CDV
    ;
}

class Computer(val program: List<Int>) {
    var regA: Long = 0
    var regB: Long = 0
    var regC: Long = 0

    var pc: Int = 0

    val output = mutableListOf<Long>()

    fun setReg(reg: Char, value: Long) {
        when (reg) {
            'A' -> regA = value
            'B' -> regB = value
            'C' -> regC = value
            else -> throw IllegalArgumentException()
        }
    }

    fun copyFrom(other: Computer) {
        regA = other.regA
        regB = other.regB
        regC = other.regC
    }

    fun run() {
        try {
            while (true) {
                runOp()
            }
        } catch (e: IndexOutOfBoundsException) {
        }
    }

    fun getComboValue(value: Int): Long {
        return when (value) {
            0, 1, 2, 3 -> value.toLong()
            4 -> regA
            5 -> regB
            6 -> regC
            else -> throw IllegalArgumentException()
        }
    }

    fun runOp() {
        val (op, arg1) = program.subList(pc, pc + 2)
        when (Opcodes.entries[op]) {
            Opcodes.ADV -> {
                regA = regA shr getComboValue(arg1).toInt()
                pc += 2
            }
            Opcodes.BXL -> {
                regB = regB xor arg1.toLong()
                pc += 2
            }
            Opcodes.BST -> {
                regB = getComboValue(arg1).mod(8L)
                pc += 2
            }
            Opcodes.JNZ -> {
                if (regA != 0L) {
                    pc = arg1
                } else {
                    pc += 2
                }
            }
            Opcodes.BXC -> {
                regB = regB xor regC
                pc += 2
            }
            Opcodes.OUT -> {
                output.add(getComboValue(arg1).mod(8).toLong())
                pc += 2
            }
            Opcodes.BDV -> {
                regB = regA shr getComboValue(arg1).toInt()
                pc += 2
            }
            Opcodes.CDV -> {
                regC = regA shr getComboValue(arg1).toInt()
                pc += 2
            }
        }
    }

}

val registryKey = Regex("([A-C]): (-?\\d+)")

fun part1(src: String) {
    val (reg, prog) = src.split("\n\n")
    val computer = Computer(prog.substringAfter(":").trimStart().split(",").map { it.toInt() })
    for (s in reg.split("\n")) {
        val m = registryKey.find(s) ?: continue
        computer.setReg(m.groups[1]!!.value[0], m.groups[2]!!.value.toLong())
    }
    computer.run()
    println(computer.output.joinToString(","))
}

fun part2(src: String) {
    val (reg, prog) = src.split("\n\n")
    val computer = Computer(prog.substringAfter(":").trimStart().split(",").map { it.toInt() })
    for (s in reg.split("\n")) {
        val m = registryKey.find(s) ?: continue
        computer.setReg(m.groups[1]!!.value[0], m.groups[2]!!.value.toLong())
    }
    val m = reverse(computer.program.reversed(), 0L).min()
    println(m)
    println(runProgram(m))
}


fun runProgram(regA: Long): List<Int> {
    var regA = regA
    var regB = 0L
    var regC = 0L

    val output = mutableListOf<Int>()

    do {
        regB = regA and 0b111 // 2, 4
        regB = regB xor 0b111 // 1, 7
        regC = regA shr regB.toInt() // 7, 5
        regB = regB xor regC // 4, 1
        regB = regB xor 4 // 1, 4
        output.add((regB and 0b111).toInt()) // 5, 5
        regA = regA shr 3 // 0, 3
    } while (regA != 0L) // 3, 0

    return output
}

val xorTable = buildMap<Int, MutableList<Pair<Int, Int>>> {
    for (i in 0..7) {
        for (j in 0..7) {
            val xor = i xor j
            if (xor !in this) put(xor, mutableListOf())
            getValue(xor).add(i to j)
        }
    }
}

fun reverse(output: List<Int>, current: Long): List<Long> {
    if (output.isEmpty()) return listOf(current)
    val regB = output[0] xor 4
    val list = mutableListOf<Long>()
    for ((b, c) in xorTable[regB]!!) {
        val bb = b xor 0b111
        val d = (current shl 3) or bb.toLong()
        if ((d shr b) and 0b111 != c.toLong()) continue
        list.addAll(reverse(output.drop(1), current shl 3 or bb.toLong()))
    }
    return list
}