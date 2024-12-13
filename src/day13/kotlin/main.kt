import org.apache.commons.math3.fraction.BigFraction
import org.apache.commons.math3.linear.FieldLUDecomposition
import org.apache.commons.math3.linear.MatrixUtils
import java.math.BigInteger
import kotlin.math.abs

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

// this would've been so much easier in python
// or matlab...

fun solveMin(machine: String): Double {
    // a(X1) + b(X2) = prizeX
    // a(Y1) + b(Y2) = prizeY
    val lines = machine.split("\n").map { it.substringAfter(":").trim().split(" ").map { it.substring(1).replace(",", "").replace("=", "") } }

    val a = MatrixUtils.createFieldMatrix(arrayOf(
        arrayOf(BigFraction(lines[0][0].toBigInteger()), BigFraction(lines[1][0].toBigInteger())),
        arrayOf(BigFraction(lines[0][1].toBigInteger()), BigFraction(lines[1][1].toBigInteger()))
    ))

    val aInv = FieldLUDecomposition(a).solver.inverse


    val s = MatrixUtils.createFieldMatrix(arrayOf(
        arrayOf(BigFraction(lines[2][0].toBigInteger())),
        arrayOf(BigFraction(lines[2][1].toBigInteger()))
    ))

    val soln = aInv.multiply(s).data.flatMap { it.toList() }
    if (soln.all { it.toDouble() < 100 && (abs(it.toInt().toDouble() - it.toDouble()) == 0.0) }) {
        return soln[0].toDouble() * 3 + soln[1].toDouble()
    }
    return 0.0
}

fun solveMin2(machine: String): BigInteger {
    // a(X1) + b(X2) = prizeX
    // a(Y1) + b(Y2) = prizeY
    val lines = machine.split("\n").map { it.substringAfter(":").trim().split(" ").map { it.substring(1).replace(",", "").replace("=", "") } }

    val a = MatrixUtils.createFieldMatrix(arrayOf(
        arrayOf(BigFraction(lines[0][0].toBigInteger()), BigFraction(lines[1][0].toBigInteger())),
        arrayOf(BigFraction(lines[0][1].toBigInteger()), BigFraction(lines[1][1].toBigInteger()))
    ))

    val aInv = FieldLUDecomposition(a).solver.inverse


    val s = MatrixUtils.createFieldMatrix(arrayOf(
        arrayOf(BigFraction(lines[2][0].toBigInteger() + BigInteger("10000000000000"))),
        arrayOf(BigFraction(lines[2][1].toBigInteger() + BigInteger("10000000000000")))
    ))

    val soln = aInv.multiply(s).data.flatMap { it.toList() }
    if (soln.all { (abs(it.toLong().toDouble() - it.toDouble()) == 0.0) }) {
        return soln[0].bigDecimalValue().toBigInteger() * BigInteger("3") + soln[1].bigDecimalValue().toBigInteger()
    }
    return BigInteger("0")
}

fun part1(src: String) {
    val machines = src.split("\n\n")
    var c = 0.0
    for (machine in machines) {
        c += solveMin(machine)
    }
    println(c)
}

fun part2(src: String) {
    val machines = src.split("\n\n")
    var c = BigInteger("0")
    for (machine in machines) {
        c += solveMin2(machine)
    }
    println(c.toBigDecimal().toPlainString())
}