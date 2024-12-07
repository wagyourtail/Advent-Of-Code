
val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun testAdd(current: Long, nums: List<Long>, nextFun: (Long, List<Long>) -> Boolean): Boolean {
    val next = current - nums[0]
    if (nums.size == 1) return next == 0L
    return nextFun(next, nums.drop(1))
}

fun testMul(current: Long, nums: List<Long>, nextFun: (Long, List<Long>) -> Boolean): Boolean {
    if (current % nums[0] != 0L) return false
    val next = current / nums[0]
    if (nums.size == 1) return next == 1L
    return nextFun(next, nums.drop(1))
}

fun p1NextFun(current: Long, nums: List<Long>): Boolean {
    return testAdd(current, nums, ::p1NextFun) || testMul(current, nums, ::p1NextFun)
}

fun part1(src: String) {
    var c = 0L
    for (line in src.lines()) {
        val values = line.replace(":", "").split(" ").map { it.toLong() }
        val target = values[0]
        val operands = values.subList(1, values.size).reversed()
        if (p1NextFun(target, operands)) {
            c += target
        }
    }
    println(c)
}

fun testConcat(current: Long, nums: List<Long>, nextFun: (Long, List<Long>) -> Boolean): Boolean {
    val currStr = current.toString()
    val operandStr = nums[0].toString()
    if (!currStr.endsWith(operandStr)) return false
    val nextStr = currStr.removeSuffix(nums[0].toString())
    if (nextStr.isEmpty() || nextStr == "-") return false
    val next = nextStr.toLong()
    if (nums.size == 2) return next == nums[1]
    return nextFun(next, nums.drop(1))
}

fun p2NextFun(current: Long, nums: List<Long>): Boolean {
    val c = if (nums.size > 1) testConcat(current, nums, ::p2NextFun) else false
    return c || testAdd(current, nums, ::p2NextFun) || testMul(current, nums, ::p2NextFun)
}

fun part2(src: String) {
    var c = 0L
    for (line in src.lines()) {
        val values = line.replace(":", "").split(" ").map { it.toLong() }
        val target = values[0]
        val operands = values.subList(1, values.size).reversed()
        if (p2NextFun(target, operands)) {
            c += target
        }
    }
    println(c)
}