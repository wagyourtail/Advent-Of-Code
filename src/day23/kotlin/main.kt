import xyz.wagyourtail.commonskt.utils.mutliAssociate
import xyz.wagyourtail.commonskt.utils.permutations
import java.util.stream.Collectors.toList
import java.util.stream.Collectors.toSet

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun part1(src: String) {
    val graph = src.split("\n").map { it.split("-") }.flatMap { listOf(it.first() to it.last(), it.last() to it.first()) }.mutliAssociate { it }
    val perms = graph.keys.flatMap { f -> graph[f]!!.permutations(2).filter { graph[it[0]]!!.contains(it[1]) }.map { (it + f).toSet() }.toSet() }.toSet()
    println(perms.filter { it.any { it.startsWith("t") } }.size)
}

fun cycles(graph: Map<String, Set<String>>, current: Set<String>, found: MutableSet<Set<String>> = mutableSetOf()): Set<String> {
    return sequence {
        yield(current)
        found.add(current)
        outer@for ((k, v) in graph) {
            if (k in current) continue
            for (c in current) {
                if (k !in graph.getValue(c)) {
                    continue@outer
                }
            }
            val next = current + k
            if (found.any { it.containsAll(next) }) continue
            found.add(next)
            yield(cycles(graph, next, found))
        }
    }.maxBy { it.size }
}

fun part2(src: String) {
    val graph = src.split("\n").map { it.split("-") }.flatMap { listOf(it.first() to it.last(), it.last() to it.first()) }.mutliAssociate { it }.mapValues { it.value.toSet() }
    println(cycles(graph, setOf()).sorted().joinToString(","))
}