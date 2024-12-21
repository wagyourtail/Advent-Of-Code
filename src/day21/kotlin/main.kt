import xyz.wagyourtail.commonskt.collection.DefaultMap
import xyz.wagyourtail.commonskt.collection.defaultedMapOf
import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.utils.repeat

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

val keypad = """
    789
    456
    123
    .0A
""".trimIndent().lines().withIndex().flatMap { (y, line) ->
    line.withIndex().map { (x, c) ->
        c to Pos2(x, y)
    }
}.associate { it }

val arrowPad = """
    .^A
    <v>
""".trimIndent().lines().withIndex().flatMap { (y, line) ->
    line.withIndex().map { (x, c) ->
        c to Pos2(x, y)
    }
}.associate { it }

fun part1(src: String) {
    val keypads = listOf(keypad) + listOf(arrowPad).repeat(2)
    val keypadsInv = keypads.map { it.map { it.value to it.key }.toMap() }

    val padSteps = run {
        lateinit var padSteps: DefaultMap<Triple<Char, Char, Int>, String>

        padSteps = defaultedMapOf { key ->
            if (key.first == key.second) return@defaultedMapOf "A"
            val (c, n, depth) = key
            val pad = keypads[depth]
            val padInv = keypadsInv[depth]
            val cp = pad[c]!!
            val np = pad[n]!!
            val steps: String = if (cp.x == np.x) {
                if (cp.y < np.y) "v".repeat(np.y - cp.y) + "A"
                else "^".repeat(cp.y - np.y) + "A"
            } else if (cp.y == np.y) {
                if (cp.x < np.x) ">".repeat(np.x - cp.x) + "A"
                else "<".repeat(cp.x - np.x) + "A"
            } else {
                if (cp.y < np.y) {
                    if (cp.x < np.x) {
                        val a = "v".repeat(np.y - cp.y)
                        val b = ">".repeat(np.x - cp.x)
                        if (Pos2(cp.x, np.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    } else {
                        val a = "<".repeat(cp.x - np.x)
                        val b = "v".repeat(np.y - cp.y)
                        if (Pos2(np.x, cp.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    }
                } else {
                    if (cp.x < np.x) {
                        val a = "^".repeat(cp.y - np.y)
                        val b = ">".repeat(np.x - cp.x)
                        if (Pos2(cp.x, np.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    } else {
                        val a = "<".repeat(cp.x - np.x)
                        val b = "^".repeat(cp.y - np.y)
                        if (Pos2(np.x, cp.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    }
                }
            }
            if (depth == keypads.size - 1) {
                steps
            } else {
                buildString {
                    for ((c, n) in "A$steps".zipWithNext()) {
                        append(padSteps[Triple(c, n, depth + 1)])
                    }
                }
            }

        }

        padSteps
    }

    var s = 0
    for (line in src.lines()) {
        var permutations = ""
        for ((c, n) in "A$line".zipWithNext()) {
            permutations = permutations + padSteps[Triple(c, n, 0)]
        }
        s += permutations.length * line.removeSuffix("A").toInt()
    }
    println(s)
}

fun part2(src: String) {
    val keypads = listOf(keypad) + listOf(arrowPad).repeat(25)
    val keypadsInv = keypads.map { it.map { it.value to it.key }.toMap() }

    val padSteps = run {
        lateinit var padSteps: DefaultMap<Triple<Char, Char, Int>, Long>

        padSteps = defaultedMapOf { key ->
            if (key.first == key.second) return@defaultedMapOf 1L
            val (c, n, depth) = key
            val pad = keypads[depth]
            val padInv = keypadsInv[depth]
            val cp = pad[c]!!
            val np = pad[n]!!
            val steps: String = if (cp.x == np.x) {
                if (cp.y < np.y) "v".repeat(np.y - cp.y) + "A"
                else "^".repeat(cp.y - np.y) + "A"
            } else if (cp.y == np.y) {
                if (cp.x < np.x) ">".repeat(np.x - cp.x) + "A"
                else "<".repeat(cp.x - np.x) + "A"
            } else {
                if (cp.y < np.y) {
                    if (cp.x < np.x) {
                        val a = "v".repeat(np.y - cp.y)
                        val b = ">".repeat(np.x - cp.x)
                        if (Pos2(cp.x, np.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    } else {
                        val a = "<".repeat(cp.x - np.x)
                        val b = "v".repeat(np.y - cp.y)
                        if (Pos2(np.x, cp.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    }
                } else {
                    if (cp.x < np.x) {
                        val a = "^".repeat(cp.y - np.y)
                        val b = ">".repeat(np.x - cp.x)
                        if (Pos2(cp.x, np.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    } else {
                        val a = "<".repeat(cp.x - np.x)
                        val b = "^".repeat(cp.y - np.y)
                        if (Pos2(np.x, cp.y) == pad['.']) {
                            b + a + "A"
                        } else {
                            a + b + "A"
                        }
                    }
                }
            }
            if (depth == keypads.size - 1) {
                steps.length.toLong()
            } else {
                var s = 0L
                for ((c, n) in "A$steps".zipWithNext()) {
                     s += padSteps[Triple(c, n, depth + 1)]
                }
                s
            }

        }

        padSteps
    }

    var s = 0L
    for (line in src.lines()) {
        var permutations = 0L
        for ((c, n) in "A$line".zipWithNext()) {
            permutations += padSteps[Triple(c, n, 0)]
        }
        s += permutations * line.removeSuffix("A").toInt()
    }
    println(s)
}