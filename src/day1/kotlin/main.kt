import java.util.*
import kotlin.math.abs

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText())
    part2(obj.javaClass.getResource("input1.txt").readText())
}

fun part1(src: String) {
    val l1 = mutableListOf<Int>()
    val l2 = mutableListOf<Int>()
    src.lines().filter { it.isNotEmpty() }.forEach {
        val (a, b) = it.split(" ").filter { it.isNotEmpty() }
        l1.add(a.toInt())
        l2.add(b.toInt())
    }
    l1.sort()
    l2.sort()
    println(l1.zip(l2).sumOf { (a, b) -> abs(b - a) })
}

fun part2(src: String) {
    val l1 = mutableListOf<Int>()
    val l2 = mutableListOf<Int>()
    src.lines().filter { it.isNotEmpty() }.forEach {
        val (a, b) = it.split(" ").filter { it.isNotEmpty() }
        l1.add(a.toInt())
        l2.add(b.toInt())
    }
    println(l1.map { e -> e * l2.count { e == it } }.sum())
}