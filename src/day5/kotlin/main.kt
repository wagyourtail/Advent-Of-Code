
val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText())
    part2(obj.javaClass.getResource("input1.txt").readText())
}

fun part1(src: String) {
    val (rules, updates) = src.split("\n\n", limit = 2).map { it.split('\n') }
    val parsedRules = buildMap<Int, MutableSet<Int>> {
        for (rule in rules) {
            val (a, b) = rule.split("|").map { it.toInt() }
            if (a !in this) put(a, mutableSetOf())
            getValue(a).add(b)
        }
    }
    var c = 0
    outer@for (update in updates) {
        val updateNums = update.split(",").map { it.toInt() }
        val indexes = buildMap {
            for ((i, j) in updateNums.withIndex()) {
                put(j, i)
            }
        }
        for ((r1, r2) in parsedRules) {
            if (r1 !in indexes) continue
            for (r in r2) {
                if (r !in indexes) continue
                if (indexes[r1]!! >= indexes[r]!!) continue@outer
            }
        }
        c += updateNums[updateNums.size / 2]
    }
    println(c)
}

fun part2(src: String) {
    val (rules, updates) = src.split("\n\n", limit = 2).map { it.split('\n') }
    val parsedRules = buildMap<Int, MutableSet<Int>> {
        for (rule in rules) {
            val (a, b) = rule.split("|").map { it.toInt() }
            if (a !in this) put(a, mutableSetOf())
            getValue(a).add(b)
        }
    }
    var c = 0
    outer@for (update in updates) {
        val updateNums = update.split(",").map { it.toInt() }
        val indexes = buildMap {
            for ((i, j) in updateNums.withIndex()) {
                put(j, i)
            }
        }
        var incorrect = false
        rfor@for ((r1, r2) in parsedRules) {
            if (r1 !in indexes) continue
            for (r in r2) {
                if (r !in indexes) continue
                if (indexes[r1]!! >= indexes[r]!!) {
                    incorrect = true
                    break@rfor
                }
            }
        }
        if (!incorrect) continue@outer
        val fixed = mutableListOf<Int>()
        for (a in updateNums) {
            val j: Int = fixed.indexOfFirst { parsedRules[it]?.contains(a) ?: false }
            if (j == -1) {
                fixed.add(a)
            } else {
                fixed.add(j, a)
            }
        }
        c += fixed[updateNums.size / 2]
    }
    println(c)
}